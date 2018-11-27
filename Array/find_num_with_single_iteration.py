# find the number with single iteration in O(n)

def find_num(num_list):
    ans = num_list[0]
    for idx in range(1,len(num_list)):
        ans = ans^num_list[idx]
    return ans

print find_num([7,3,5,4,5,3,4])
