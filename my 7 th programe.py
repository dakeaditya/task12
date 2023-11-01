#call function
k[1,3,4,6]
print(all(k))

#call value false
k=[0,false]
print(all(k))

#one false value
k=[1,2,7,0]
print(all(k))

#one true value
k=[0,false,5]
print(all(k))

#empty iterable
k=[]
print(all(k))
