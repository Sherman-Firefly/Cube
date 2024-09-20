def cube(num):
    return num*num*num
def dthree(num):
    if num %3==0:
        return cube(num)
    else:
        return False

print(dthree(12))
print(dthree(18))
print(dthree(2))