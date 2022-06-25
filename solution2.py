class ReadInput:

    def __init__(self, path = "/Users/mayanksinghsikarwar/Elements/advent_of_code/Data/day3_input.txt"):
        print("Reading directory",path)
        print("Input object created")
        self.path = path

    def file_to_list(self):

        with open(self.path, "r") as file:
            input = [ x.strip() for x in file.readlines()]
        print("length of the list created =", len(input))
        return input


input_object = ReadInput()
input_list = input_object.file_to_list()


def element_len_check(lst):
    first_length = len(lst[0])
    counter = 0
    for i in range(len(lst)):
        if len(lst[i]) != first_length:
            return i

        else:
            counter += 1
    return counter

def get_binary(lst):
    zero_count = {}
    one_count = {}
    first_length = len(lst[0])
    digit_gamma = []
    digit_epsilon = []
    for i in range(0,first_length):
        zero_counter = 0
        one_counter = 0
        for j in range(0,len(lst)):
            if lst[j][i] == '1':
                one_counter += 1
            else:
                zero_counter += 1
        zero_count[i+1] = zero_counter
        one_count[i+1] = one_counter
        #gamma digit
        if zero_count[i+1] < one_count[i+1]:
            digit_gamma.append('1')
        else:
            digit_gamma.append('0')
        #epsilon digit
        if zero_count[i+1] > one_count[i+1]:
            digit_epsilon.append('1')
        else:
            digit_epsilon.append('0')
    print("counts for one in each position = ",one_count)
    print("counts for zero in each position = ",zero_count)
    print(digit_epsilon, digit_gamma)
    gamma_rate  = int("".join(digit_gamma),2)
    print(gamma_rate)
    epsilon_rate = int("".join(digit_epsilon),2)
    print(epsilon_rate)
    power_consumption = gamma_rate*epsilon_rate
    return power_consumption
    # return power_consumption


def power_consumption(lst):
    check_counter = element_len_check(lst)

    if len(lst) == check_counter:
        print("All good")
        num = get_binary(input_list)
    else:
        print("unmatch found at = ", check_counter)
    return num

power_consumption(input_list)



