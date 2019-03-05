import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--start', default=3, type=int)
parser.add_argument('-e', '--end', default=3, type=int)
parser.add_argument('-f', '--file', type=argparse.FileType('r'))

args = parser.parse_args()

print(vars(args))

# --start lines
for line_counter in range(args.start):
    print(args.file.readline().decode('utf-8').rstrip())

print('-'*60)

# --end lines
args.file.seek(-200 * args.end, 2)
print('\n'.join(args.file.read().decode('utf-8').split('\n')[-args.end-1:]))
