import random

boys_file = './boys.txt'
girls_file = './girls.txt'

boys_data = []
girls_data = []

with open(boys_file, 'r') as bp:
    lines = bp.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line + ', 0'
        boys_data.append(line)

with open(girls_file, 'r') as gp:
    lines = gp.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line + ', 1'
        girls_data.append(line)

random.shuffle(boys_data)
random.shuffle(girls_data)

print(f"Total boys data: {len(boys_data)}")
print(f"Total girl data: {len(girls_data)}")

data = boys_data + girls_data

random.shuffle(data)

print(f"Total data: {len(data)}")

ds = 'Name, Gender\n'

for d in data:
    ds += (d + '\n')

with open('bengli-boys-vs-girls-names-2k.csv', 'w') as fp:
    fp.write(ds)