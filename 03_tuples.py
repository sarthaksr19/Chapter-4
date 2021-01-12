# the main differnce between tuples and list is in tuples we can't update the value of a particular element
t = (1,2,3,4)
t[0] = 44 # it throws error cause tuples are immutable
print(t)