# input = [7,1,5,3,6,4]
# output = 5



def best_buy(values):
    profit = 0
    right_num = 1
    left_num = 0
    while right_num < len(values):
        if(values[left_num]<values[right_num]):
            temp_profit = int(values[right_num])-int(values[left_num])
            profit = max(profit,temp_profit)
        else:
            left_num = right_num
        right_num+=1
    return profit       
values_raw = input()
values_trim = values_raw.strip().split(",")
print(best_buy(values_trim))