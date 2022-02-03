path  = "/Users/mayanksinghsikarwar/Elements/advent_of_code/Data/day1_input_data.txt"
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





