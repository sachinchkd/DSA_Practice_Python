# without using temporary variable
def number_swapper(a,b):
    a = a + b
    b = a - b
    a = a - b
    return (a,b)

print(number_swapper(1,3))

# can also use XOR 
