#1_Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0]= 15
# print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]['last_name']='Bryant'
# print (students)

# In the sports_directory, change 'Messi' to 'Andres'
# sports_directory["soccer"][0] ="Andres"
# print(sports_directory)

# Change the value 20 in z to 30
# z[0]["y"]=30
# print(z)


#2_Iterate Through a List of Dictionaries
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# def iterateDictionary(list):
#     for i in list:
#         for j in i:
#             print("{} : {} ,".format(j,i[j]),end=" ")
#         print("")
# iterateDictionary(students)

#3_Get Values From a List of Dictionaries
# def iterateDictionary2(key,list):
#     for i in list:
#         print(i[key])
# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterateDictionary2("first_name",students) 
# iterateDictionary2("last_name",students) 

#4_Iterate Through a Dictionary with List Values
# def printInfo(dictionary):
#     for i in dictionary:
#         print(len(dictionary[i]),"",i.upper())
#         for j in dictionary[i]:
#             print(j)
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)