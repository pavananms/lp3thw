def largest_num(input_list):
    biggest = input_list[0]
    for i in range(len(input_list)):
        if(input_list[i] > biggest):
            biggest = input_list[i]
    return biggest

def smallest_num(input_list):
    smallest = input_list[0]
    for i in range(len(input_list)):
        if(input_list[i] < smallest):
            smallest = input_list[i]
    return smallest

print("largest : " + str(largest_num([1,2,-5,3,10,6,8])))
print("smallest : " +  str(smallest_num([1,2,5,3,10,6,8])))
