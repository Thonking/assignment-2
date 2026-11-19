import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]: #load data from file and return a tuple of a list of number and the total count of values in the column
    numbers = []
    count = 0
    with open(filepath, 'r') as file: #open file and read each line, split by tab, and convert to float if possible, otherwise skip
        for line in file:
            try: #try to access specified column, if not found, print error and exit
                num = line.split('\t')[column]
            except IndexError:
                print(f'Error: Column {column} not found in data file. Please try again.')
                sys.exit()
            try: #try to convert to float
                float_num = float(num)
                if math.isnan(float_num): #checks if number is NaN 
                    count += 1
                    continue
                numbers.append(float_num)
            except:
                pass
            count += 1
        if len(numbers) == 0:
            print(f'Error: There were no valid number(s) in column {column}')
            sys.exit()
    return (numbers, count)

def calculate_average(numbers:list)->float:
    return sum(numbers)/len(numbers)

def get_max_and_min(numbers:list)->tuple[float, float]:
    return (max(numbers), min(numbers))

def calculate_variance(numbers:list)->float:
    length = len(numbers)
    if length < 2:
        return 0.0
    avg = calculate_average(numbers)
    var_sum = 0
    for num in numbers:
        var_sum += (num - avg) ** 2
    var = (1/(length - 1)) * var_sum 
    return var

def calculate_std_dev(numbers:list)->float:
    return math.sqrt(calculate_variance(numbers))

def calculate_median(numbers:list)->float:
    length = len(numbers)
    numbers.sort()

    if length % 2 == 0: #average of two middle numbers if even length
        mid1 = length // 2
        mid2 = mid1 - 1
        median = (numbers[mid1] + numbers[mid2]) / 2
    else: #return middle number if odd length
        mid = length // 2 
        median = numbers[mid]
    return float(median)


