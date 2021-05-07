# 1_Countdown
# newlist = []
# def a(num):
#     for x in range (num,-1,-1):
#          newlist.append(x)
#     return newlist
# print(a(5))

# 2_Print and Return
# def PrintAndReturn(list):
#     print (list[0])
#     return list[1]
# PrintAndReturn([1,2])

# 3_First Plus Length
# def first_plus_length(list):
#     return list[0]+len(list)
# first_plus_length([1,2,3,4,5])

# 4_Values Greater than Second
# def values_greater_than_second(list):
#     count=0
#     if len(list) <2:
#         return False
#     else:
#         newlist =[]
#         for i in list:
#          if i > list[1]:
#                newlist.append(i)
#                count +=1
#     return newlist
# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([5]))

# 5_This Length, That Value
# def length_and_value(length,value):
#     list =[]
#     for i in range(0,length):
#        list.append(value)
#     return list
# print(length_and_value(4,7))