# chechs if the values is repeated anywhere in the values entered
# [1,3,4,1] should return true

#after running this code in leetcode i see that method1 is not efficent and method 2 is more efficient


raw_input = input()
values = raw_input.strip().split(",")

#method 1
def contain_nums(values):
    dict_values = {}

    for index, values in  enumerate(values):
        if values in dict_values.values():
            return True
        else:
            dict_values[int(index)] = values
    return False




#method 2 I AM SORTING THE ARRAY AND THEN CHECKING
def cotains_num_2(values):
    values = sorted(values)
    for i in range(len(values)-1):
        if values[i] == values[i+1]:
            return True
    return False


#method 3  Using the hashset
def contains_num3(values):
    hashset = set()
    for i in values:
        if i in hashset:
            return True
        else:
            hashset.add(i)
    return False

print(contain_nums(values))
print(cotains_num_2(values))
print(contains_num3(values))