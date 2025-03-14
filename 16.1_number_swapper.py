# without using temporary variable
def number_swapper(a,b):
    a = a + b # first add the numbers
    b = a - b   #then subtract it with one number and assign it to same number
    a = a - b   #for the other number do the same
    return (a,b)

print(number_swapper(1,3))

# can also use XOR 
