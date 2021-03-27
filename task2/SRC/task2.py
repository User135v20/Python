import json
import math
import sys


def pre_parsing(str_: str) -> dict:
    ind_ = str_.find('line:')
    j = str_.find('}', ind_)
    str_ = str_[:j] + ']' + str_[j + 1:]
    j = str_.find('{', ind_)
    str_ = str_[:j] + '[' + str_[j + 1:]
    for i in ["sphere", "center", "radius", "line"]:
        str_ = str_.replace(i, "\"" + i + "\"")
    return json.loads(str_)


def parse(points_data: dict):
    return points_data['sphere']['center'], points_data['sphere']['radius'], points_data['line'][0], \
           points_data['line'][1]


def calculations(C: list, R: int, M0: list, M1: list):
    b = sum([(-2 * M0[i] ** 2 + 2 * M0[i] * M1[i] + 2 * M0[i] * C[i] - 2 * C[i] * M1[i]) for i in range(3)])
    a = sum([(M0[i] ** 2 - 2 * M1[i] * M0[i] + M1[i] ** 2) for i in range(3)])
    c = -R ** 2 + sum([(M0[i] ** 2 - 2 * C[i] * M0[i] + C[i] ** 2) for i in range(3)])

    D = b ** 2 - 4 * a * c
    k = []
    if D < 0:
        return "Коллизий не найдено"
    elif D == 0:
        k.append(-b / (2 * a))
    elif D > 0:
        k.append(-b + math.sqrt(D) / (2 * a))
        k.append(-b - math.sqrt(D) / (2 * a))

    return [[(M0[i] * (1 - t) + t * M1[i]) for i in range(3)] for t in k]


def main(filepath: str):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    for line in lines:
        data = pre_parsing(line)
        result = calculations(*parse(data))
        if isinstance(result, str):
            print(result)
        else:
            print(json.dumps(result)[1:-1])


if __name__ == '__main__':
    args = sys.argv
    main(args[1])
    # ex: python task2.py task2.txt
