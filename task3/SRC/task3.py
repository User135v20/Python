import csv
import sys
from datetime import datetime


def parse_log(filename: str = 'task3.log'):
    with open(filename, 'r') as f:
        lines = f.readlines()
    volume = int(lines[1].split(' ')[0])
    current = int(lines[2].split(' ')[0])

    log_data = []
    for line in lines[3:]:
        try:
            str_time = line.split('Z')[0]
            action_volumes = line.split(' ')[-2][:-1]
            log_data.append(
                {
                    'time': datetime.strptime(str_time+'000', '%Y-%m-%dT%H:%M:%S.%f'),
                    'action': 'top up' if line.find('top up') != -1 else 'scoop',
                    'success': 'фейл' if line.find('фейл') != -1 else 'успех',
                    'volume': int(action_volumes)
                }
            )
        finally:
            pass
    return volume, current, log_data


def find_index(time_: datetime, log_data: list, is_start: bool = True):
    if time_ < log_data[0]['time'] or time_ > log_data[-1]['time']:
        return None

    d = len(log_data)
    i = 0
    while d//2 != 0:
        i += d//2 * (1 if time_ > log_data[i]['time'] else -1)
        d = d//2
    if is_start:
        while time_ < log_data[i]['time']:
            i -= 1
        i += 1
    else:
        while time_ > log_data[i]['time']:
            i += 1
        i -= 1
    return i


def calculations(start_index: int, finish_index: int, log_data: list, current_volume: int):
    n = finish_index - start_index + 1
    if n == 0:
        return 'usage'
    mistakes = 0
    additional_volume = 0
    failed_additional_volume = 0
    scoop_volume = 0
    failed_scoop_volume = 0
    for i in range(start_index, finish_index + 1):
        if log_data[i]['success'] == 'фейл':
            mistakes += 1
            if log_data[i]['action'] == 'top up':
                failed_additional_volume += log_data[i]['volume']
            else:
                failed_scoop_volume += log_data[i]['volume']
        elif log_data[i]['success'] == 'успех':
            if log_data[i]['action'] == 'top up':
                additional_volume += log_data[i]['volume']
            else:
                scoop_volume += log_data[i]['volume']
    start_volume = current_volume + sum([log_data[i]['volume'] for i in range(start_index) if log_data[i]['success'] == 'успех' and log_data[i]['action'] == 'top up']) - \
    sum([log_data[i]['volume'] for i in range(start_index) if log_data[i]['success'] == 'успех' and log_data[i]['action'] == 'scoop'])
    return {
        'количество попыток': n,
        'процент ошибок': mistakes * 100 // n,
        'объем воды налитый в бочку за указанный период': additional_volume,
        'объем воды не налитый в бочку за указанный период': failed_additional_volume,
        'объем воды изъятый из бочки за указанный период': scoop_volume,
        'объем воды не изъятый из бочки за указанный период': failed_scoop_volume,
        'начальный объем': start_volume,
        'конечный объем': start_volume + additional_volume - scoop_volume
    }


def get_info_from_log(time1: datetime, time2: datetime, filename: str):
    max_volume, current_volume, log_data = parse_log(filename)
    start_index = find_index(time1, log_data)
    end_index = find_index(time2, log_data, is_start=False)
    if start_index is None or end_index is None:
        return 'usage'
    return calculations(start_index, end_index, log_data, current_volume)


def write_result(result: dict):
    with open("task3.csv", mode="w+", encoding='cp1251') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Наименование", "Значение"])
        for name, k in result.items():
            file_writer.writerow([name, str(k)])


def main(log_filepath: str, str_time1: str, str_time2: str):
    times = [datetime.strptime(str_time1, '%Y-%m-%dT%H:%M:%S'), datetime.strptime(str_time2, '%Y-%m-%dT%H:%M:%S')]
    time1 = min(times)
    time2 = max(times)
    res = get_info_from_log(time1, time2, log_filepath)
    if isinstance(res, str):
        print(res)
    else:
        write_result(res)


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        main(args[1], args[2], args[3])
    else:
        print('usage')
    # ex log: python task3.py task3.log 2021-03-27T02:14:03 2021-03-27T02:14:04
    # ex2 log v2: python task3.py task3.log 2021-03-27T16:47:50 2021-03-27T16:47:51