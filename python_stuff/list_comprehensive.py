double_list = []
my_list = [1, 2, 3]
# using normal operation
print("Using normal operataion")
for item in my_list:
    double_list.append(item * 2)
print(double_list)

# using list comprehensive
print("List comprenensive")
double_list = [item * 3 for item in my_list]
print(double_list)

# accessing elements of list using list comprehension
users = [{'name': 'Tilak', 'age': 23}, {'name': 'Hari', 'age': 21}]
user_name = [user['name'] for user in users]
print(user_name)

# flterdata user

filter_user_name = [user['name']
                    for user in users if user['age'] > 22 and user['name'] == 'Tilak']
print(filter_user_name)

# nested loop in list comprehension
user_groups = [
    [
        {'name': 'Harke', 'age': 35},
        {'name': 'Haribahadur', 'age': 25}
    ],
    [
        {'name': 'chameli', 'age': 33},
        {'name': 'mina', 'age': 21}
    ]
]
user_name = [person['name']
             for group in user_groups for person in group if person['age'] < 30]
print(user_name)
