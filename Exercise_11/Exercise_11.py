# -*- coding: utf-8 -*-
import sys


class Tee():

    def __init__(self, *files):
        self.files = files

    def write(self, text):
        for one_file in self.files:
            one_file.write(text)

    def writelines(self, lines):
        for one_file in self.files:
            one_file.writelines(lines)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for one_file in self.files:
            one_file.close()


if __name__ == '__main__':
    f1 = open('/tmp/tee1.txt', 'w')
    f2 = open('/tmp/tee2.txt', 'w')
    t = Tee(sys.stdout, f1, f2)

    t.write('abc\n')
    t.write('def\n')
    t.write('ghi\n')

    f3 = open('/tmp/tee3.txt', 'w')
    f4 = open('/tmp/tee4.txt', 'w')

    with Tee(f3, f4) as t2:
        t2.write('!!!xyz\n')
        t2.write('???xyz\n')
