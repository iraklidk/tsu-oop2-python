from random import randint as ri
import os


def matr_gen(v_low=20, v_hight=30, n_low=20000, n_hight=22000):
    sz = ri(n_low, n_hight)
    def gen_row(vnum, count=sz):
        arr = []

        for _ in range(sz):
            num = str(ri(1, vnum + 1))
            a = f"x{num}" if ri(0, 1) else f"-x{num}"
            if num == str(vnum + 1):
                a = "-b" if a[0] == '-' else "b"
            arr.append(a)
        return arr
    row_num = ri(v_low, v_hight)
    return '\n'.join(' '.join(gen_row(row_num)) for _ in range(row_num))

for i in range(ri(20,30)):
    st = matr_gen()
    path = f"/mnt/data/file_{i}.in"
    with open(os.path.join(os.path.dirname(__file__), f'file_{i}.in'), 'w') as fd:

        fd.write(st)
        



