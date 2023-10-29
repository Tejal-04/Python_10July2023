numbers = [1,2,3,4,5,6,7,8,9]
even = []
for i in numbers:
    if i%2 == 0:
        even.append(i)
print(even)

# List Comprehension
print("List Comprehension")
even = [i for i in numbers if i%2 == 0]
print(even)

squ_numbers = [i*i for i in numbers]
print(squ_numbers)

print('----------------------------------------------------')

s = set([1,2,3,4,5,1,2,3])
print(s)

# Set Comprehension
print('Set Comprehension')
set_comp = {i for i in s}
print(set_comp)

print('----------------------------------------------------')

cities = ['Mumbai','New York','Paris']
countries = ['India','USA','France']
z = zip(cities,countries)
print(z)
for a in z:
    print(a)

# Dictionary Comprehension
print('Dictionary Comprehension')    
d = {city:country for city,country in zip(cities,countries)}
print(d)