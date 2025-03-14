def max_two_number(a,b):
    k = 1 - ((a-b)>>31 & 1) # Get 1 if a>b , else 0
    return a * k + b * (1-k)

# (a-b)>>31 
# if (a-b) is negative, bit 31 is 1
# if (a-b) is positive, bit 31 is 0
# &1 ensures we only get 0 if (a>=b) or 1 if (a<b)

def check_LSB(a,b):
    return (a-b)>>31

def get_0_or_1(a,b):
    return (a-b)>>31 & 1 

def flip(a,b):
    return 1-((a-b)>>31 & 1)



print("(bigger - smaller)>>31 : ",check_LSB(3,1), " (positive)")
print("(smaller - bigger)>>31 : ",check_LSB(1,3)," (negative)")

print("(bigger - smaller)>>31 & 1 : ",get_0_or_1(3,1), "(positive)" )
print("(smaller - bigger)>>31 & 1: ",get_0_or_1(1,3)," (negative)")

print("FLIP (1- (bigger - smaller)>>31 & 1) : ",flip(3,1), "(positive)" )
print("FLIP (1- (smaller - bigger)>>31 & 1) : ",flip(1,3)," (negative)")

print("The Bigger - Smaller is 1 ")

print("The k = 1 for (bigger-smaller i.e [a-b]) so returning a * k + b * (k-1) :",max_two_number(1,3))