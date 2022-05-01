my_list = [1, 2, 3]

double = [item * 2 for item in my_list]
#double = []
# for item in my_list:
#     double.append(item * 2)
print(double) 

users = [{'name' : 'Amit', 'age' : 26}, {'name' : 'Vishal', 'age' : 27}, {'name' : 'Pankaj', 'age' : 36}]
user_name = [user['name'] for user in users]
print(user_name)

user_name_old = [user['name'] for user in users if user['age'] > 30]
print(user_name_old)

user_groups = [
    [
        {'name' : 'Amit', 'age' : 26},
        {'name' : 'Vishal', 'age' : 27}
    ],
    [
        {'name' : 'sarah', 'age' : 27},
        {'name' : 'maria', 'age' : 37}
    ]
]

user_name_new = [person['name'] for group in user_groups for person in group ]
print(user_name_new)
user_name_new_old = [person['name'] for group in user_groups for person in group if person['age'] > 30]
print(user_name_new_old)