#How to swap all uppercase characters to lowercase and vice versa?
#string=input('enter string')
#a=string.swapcase()
#print(a)

def swap(s_string):
    return s_string.swapcase()

string = input("Enter String")
swap_string = swap(string)
print(swap_string)