array=[10,20,30,40,50,1,3,6,9,2,6,3,3,3,3]

print(all(array))
print('')

print(bool(array))
print('')

o=enumerate(array)
print(o)
print('')

print(array)
print('')

print(sorted(array))
print('')

print(array.sort()) #?? Why None?
print('')

print(set(array))
print('')

print(list(array))
print('')

bick=slice(4,8)
print(array[bick])
print('')

print(array[slice(4,7)])
#print(slice.array(4,7))