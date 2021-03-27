from datetime import datetime
from random import randint, choice
from time import sleep


class Barrel:
    def __init__(self):
        self.volume = randint(100, 1000)
        self.current_water_volume = randint(0, self.volume)
        with open('task3.log', 'w') as f:
            f.write('META DATA:\n')
            f.write(f'{self.volume} (объем бочки)\n')
            f.write(f'{self.current_water_volume} (текущий объем воды в бочке))\n')
        self.template = "{time} – [{username}] - wanna {action} {volume}l ({successfulness})\n"

    def action(self, type_action, username, volume, f):
        if type_action == 'top up':
            if volume + self.current_water_volume > self.volume:
                successfulness = 'фейл'
            else:
                successfulness = 'успех'
                self.current_water_volume += volume
        else:
            if - volume + self.current_water_volume < 0:
                successfulness = 'фейл'
            else:
                successfulness = 'успех'
                self.current_water_volume -= volume

        f.write(self.template.format(time=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z', username=username,
                                           action=type_action, volume=volume, successfulness=successfulness))


def generate_records():
    users = ['user1', 'user2', 'user3']
    barrel = Barrel()
    with open('task3.log', 'a') as f:
        for i in range(100000):
            sleep(0.0005)
            barrel.action(choice(['top up', 'scoop']), choice(users), randint(0, 100), f)
            if i%10000:
                f.flush()


if __name__ == '__main__':
    generate_records()
