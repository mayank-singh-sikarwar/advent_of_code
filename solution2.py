class ReadInput:

    def __init__(self, path = "/Users/mayanksinghsikarwar/Elements/advent_of_code/Data/day3_input.txt"):
        print("Input object created")
        print("Reading directory",path)
        self.path = path

    def file_to_list(self):

        with open(self.path, "r") as file:
            input = [ x.strip() for x in file.readlines()]
        print("length of the list created =", len(input))
        return input


input_object = ReadInput("/Users/mayanksinghsikarwar/Elements/advent_of_code/Data/day2_input.txt")

input_list = input_object.file_to_list()





        