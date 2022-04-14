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