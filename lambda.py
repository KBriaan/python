people = [
    {'name':'Harry', 'house':'13B'},
    {'name':'Chebet', 'house':'12B'},
    {'name':'kipkirui', 'house':'11B'}

]

# def f(person):
#     return person['house']


# people.sort(key=f)

# or
people.sort(key=lambda person:person['name'])

print(people)