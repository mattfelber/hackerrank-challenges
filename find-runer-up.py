N = int(input(''))

A = input('').split(' ')      # the 'A' List
#print(A)

as_int = list(map(int, A))      #converting the 'A' list to integers list
#print(as_int)

unique_set = set(as_int)        #removing repeated values
#print(unique_set)

R = sorted(list(unique_set))    #set by increasing order
#print(R)

print(R[-2])                    #print second largest number