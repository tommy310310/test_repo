import random


def sgrk():
    goal = 30
    p1 = 0
    p2 = 0
    pp = 0
    n1 = input('最初にサイコロを振る人の名前は？＞')
    n2 = input('あとにサイコロを振る人の名前は？＞')
    while pp < goal:
        print(n1 + 'さんはサイコロを振ってください。')
        s1 = random.randint(1, 6)
        p1 += s1
        print('サイコロの目は　'+str(s1)+'　です。　　'+n1 +
              'さんのポイントは　'+str(p1)+'　です。'+'次は'+n2+'さんの番です。')
        if p1 >= 30:
            break
        else:
            print(n2 + 'さんはサイコロを振ってください。')
            s2 = random.randint(1, 6)
            p2 += s2
            print('サイコロの目は　'+str(s2)+'　です。　　'+n2+'さんのポイントは　'+str(p2)+'　です。')
            pp = p2


def nisinsuu():
    n = int(input('255以下の自然数を入力してください＞'))
    sinl = []
    for i in range(8):
        sinl.append(str(n % 2))
        n = n // 2
    sinl.reverse()
    print(''.join(sinl))


def futari_sugoroku(goal=20):
    fp = 0
    sp = 0
    while True:
        fs = random.randint(1, 6)
        fp += fs
        # print(str(fp))
        if fp >= goal:
            # print('fの勝ち')
            return 'f'
            break
        else:
            ss = random.randint(1, 6)
            sp += ss
            # print('　　　'+str(sp))
            if sp >= goal:
                # print('　　　'+'sの勝ち')
                return 's'
                break


def fs_matches(kaisuu=2000, goal=50):
    f_counter = 0
    s_counter = 0
    for i in range(kaisuu):
        if futari_sugoroku(goal) == 'f':
            f_counter += 1
        else:
            s_counter += 1
    f_syouritu = str(round(f_counter/kaisuu, 2))
    s_syouritu = str(round(s_counter/kaisuu, 2))
    return f_syouritu


def fs_ms_list(goal):
    kekka_list = []
    for i in range(goal):
        kekka_list.append([str(i), fs_matches(goal=i)])
    return kekka_list


def fs_test():
    for u in fs_ms_list(100):
        print(u)


def kojin_atari_kaisuu(tama=1000):
    atari_counter = 0
    for i in range(tama):
        kuji = random.randint(1, tama)
        if kuji == 1:
            atari_counter += 1
    return atari_counter


def atari_kaisuu_list(ninzuu=100):
    kekka_list = []
    for i in range(ninzuu):
        kekka_list.append(kojin_atari_kaisuu())
    return kekka_list


def kaisuu_ninzuu_list(list):
    kl = []
    mx = max(list)
    for i in range(0, mx):
        counter = 0
        for u in list:
            if u == i:
                counter += 1
        kl.append([i, counter])
    return kl


def test():
    print(kaisuu_ninzuu_list(atari_kaisuu_list))


def sikaku(kosuu=8):
    return '■'*kosuu


def sikaku_test():
    for i in range(20):
        print(str(i) + '：　' + sikaku(i))


def korattu_th(n=100):
    counter = 0
    while True:
        if n % 2 == 0:
            n = n // 2
            counter += 1
        elif n > 1:
            n = 3*n + 1
            counter += 1
        else:
            break
    return counter


def korattu_test(try_n=1000):
    kaisuu_list = []
    for n in range(1, try_n):
        kaisuu_list.append(korattu_th(n))
    return kaisuu_list


class Parent:
    def __init__(self, a, x):
        self.name = a
        self.nationality = x

    def parent_func(self):
        return 'hoge'


class Children(Parent):
    def __init__(self, p, q, b=1000):
        super().__init__(p, q)
        self.age = b


class Mago(Children):
    def __init__(self, *args, bl):
        super().__init__(*args)
        self.blood = bl


def cls_test():
    otona = Parent('トミー', 'ジャマイカ')
    kodomo = Children('syuhei', '日本', 15)
    kobito = Mago(1, 2, 3, bl='AB')
    print(kodomo.age)
    print(otona.name)
    print(kodomo.name)
    print(kodomo.nationality)
    print(kodomo.parent_func())
    print(kobito.blood)


if __name__ == '__main__':
    cls_test()
