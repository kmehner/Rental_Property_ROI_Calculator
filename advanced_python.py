print("let's see if this saves")

lucklist = [1, 2, 2, 3, 4, 5, 5, 5, 5, 5]


def find_lucky(alist):
    max = -1
    for num in alist:
        if alist.count(num) == int(num):
            if num > max:
                max = num
    return max

# less pythonic
    # if max > 0:
    #     print (f"the lucky number is {max}")
    # else:
    #     return -1

find_lucky(lucklist)