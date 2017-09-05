students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_students(arr):
    for student in arr:
        print student['first_name'], student['last_name']
print_students(students)

print

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_users(dict):
    for type in users:
        print type
        for idx in range(len(users[type])):
            record = users[type][idx]
            name = record['first_name'].upper() + ' ' + record['last_name'].upper()
            print '{} - {} - {}'.format(idx + 1, name, len(name))
print_users(users)
