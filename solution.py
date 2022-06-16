#file_path
path  = "/Users/mayanksinghsikarwar/Elements/advent_of_code/Data/day1_input_data.txt"
#part 1##
with open(path, "r") as file:
    data = [x.strip('\n') for x in file.readlines()]
print(len(data))
increased = 1
decreased = 0
for i in range(len(data)-1):
    if data[i + 1] > data[i]:
        increased += 1
    else:
        decreased += 1

print(i)
print(increased)
print(decreased)

##part 2##
print(data)
sum_list = []
for i in range(len(data)-2):
    sum = int(data[i]) + int(data[i+1]) + int(data[i+2])
    sum_list.append(sum)
print(len(sum_list))
increased = 0
decreased = 0
for i in range(len(sum_list)-1):
    if sum_list[i + 1] > sum_list[i]:
        increased += 1
    else:
        decreased += 1
print(i)
print(sum_list)
print(increased)
print(decreased)



###############################################################################
path = "/Users/mayanksinghsikarwar/Elements/advent_of_code/Data/day2_input.txt"

with open(path, "r") as file:
    input = [x.strip('\n') for x in file.readlines()]

print(input)

input[0][0] + input[3][-1]

x = 0
y = 0
coordinate = -1
depth = 0

for i in range(len(input)):
    if input[i][0] == 'f':
        x = x + int(input[i][coordinate])
        depth = depth + y*int(input[i][coordinate])
    elif input[i][0] == 'd':
        y = y + int(input[i][coordinate])
    else:
        y = y - int(input[i][coordinate])

print(x)
print(depth)
print(depth*x)

#################################################################
#problem 3 part 1
#################################################################
path = "/Users/mayanksinghsikarwar/Elements/advent_of_code/Data/day3_input.txt"
#reading file and storing input data into a list

with open(path, "r") as file:
    input = [ x.strip() for x in file.readlines()]
print(input[0])
print(len(input))

print(input[0][0])

def gamma_rate(input):
    digit

