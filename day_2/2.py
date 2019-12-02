#Intcode programs

#You are given a list of integers in a list
#This integers correspond to opcodes, and positions that are used are zero indexed.
#1: Read the next three integers in the list.
#   The first two of the three correspond to positions in the list
#   where you should read values, and the third indicates the position
#   to put their values' sums.

#2: Same as 1, except multiply.

def sum(position):
    first_value=integers[integers[position+1]]
    second_value=integers[integers[position+2]]
    sum_position=integers[position+3]
    integers[sum_position]=first_value+second_value
    return 4

def product(position):
    first_value=integers[integers[position+1]]
    second_value=integers[integers[position+2]]
    product_position=integers[position+3]
    integers[product_position]=first_value*second_value
    return 4

def abort(position):
    return -1

integers_copy=[]
integers=[]
new_integers=[]
opcode_dict = {
    1: [sum, 3],
    2: [product, 3],
    99: [abort, 0]
}

with open('input_1.txt') as fp:
    line = fp.readline()
    for i in line.split(","):
        integers.append(int(i))
    integers_copy=list(integers)

def handle_opcode(position):
    opcode=integers[position]
    if opcode in opcode_dict.keys():
        if len(integers) >= position+opcode_dict[opcode][1]:
            return opcode_dict[opcode][0](position)
        else:
            return -1
    else:
        raise AssertionError()

def execute():
    position=0
    for i in integers:
        if position < len(integers):
            return_value=handle_opcode(position)
            
            if return_value >= 0:
                position+=return_value
            else:
                break
        else:
            break
stop_at=19690720

for noun in range(99):
    for verb in range(99):
        integers[1]=noun
        integers[2]=verb
        execute()
        if integers[0] == stop_at:
            print([noun, verb])
        integers=list(integers_copy)

print(integers)
