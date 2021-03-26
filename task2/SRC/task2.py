import math

def parser(str_):
    return str_['sphere']['center'], str_['sphere']['radius'], str_['line'][0], str_['line'][1]


if __name__ == '__main__':
    # a = {
    #     'sphere':
    #         {'center': [0, 0, 0], 'radius': 10.67},
    #     'line':
    #         [[1, 0.5, 15], [43, -14.6, 0.04]]
    #     }

    a = {
        'sphere':
            {'center': [0, 0, 0], 'radius': 100},
        'line':
            [[0,0,0], [1,0,0]]
        }
    C, R, M0, M1 = parser(a)


    b = sum([(-2*M0[i]**2 + 2*M0[i]*M1[i] + 2*M0[i]*C[i] - 2*C[i]*M1[i]) for i in range(3)])
    a = sum([(M0[i] ** 2 - 2*M1[i]*M0[i] + M1[i] ** 2) for i in range(3)])
    c = -R**2 + sum([(M0[i] ** 2 - 2*C[i]*M0[i] + C[i] ** 2) for i in range(3)])

    D = b**2-4*a*c
    k = []
    if D < 0:
        print("нет решений")
    elif D == 0:
        print("одно решение")
        k.append(-b/(2*a))
    elif D > 0:
        print("два решения")
        k.append(-b + math.sqrt(D)/ (2 * a))
        k.append(-b - math.sqrt(D) / (2 * a))

    for t in k:
        point = [(M0[i]*(1-t) + t*M1[i]) for i in range(3)]
        print(point)


