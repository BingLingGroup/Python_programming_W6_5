import os

HERE = os.path.abspath(os.path.dirname(__file__))


def readValues(filename):
    value_list = []
    with open(filename, encoding="utf-8", mode="r") as input_file:
        line = input_file.readline()
        while line != "":
            if line != "\n":
                value_list.append(int(line))
            line = input_file.readline()
    return value_list


def analyseValues(value_list):
    sum = 0
    greatest = 0
    count = len(value_list)
    for value in value_list:
        sum = sum + value
        if value > greatest:
            greatest = value
    return "Count;Sum;Greatest;Average\n{count};{sum};{greatest};{average:.2f}\n".format(
        count=count, sum=sum, greatest=greatest, average=sum/count)


def print_numbers(results):
    print("")
    print("{count};{sum};{greatest};{average:.2f}".format(
        count=results[0], sum=results[1], greatest=results[2], average=results[3]))
    return None


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    print("File \"{filename}\" results:".format(filename=filename))
    filename = os.path.join(HERE, filename)
    print(analyseValues(readValues(filename=filename)))
    print("#### Number analysis - END ####")
    print("Program ending.")
    return None


main()
