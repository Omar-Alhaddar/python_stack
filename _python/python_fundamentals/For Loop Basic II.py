# 1_Biggie Size
# def biggie_size(list):
#     for i in range (0, len(list), 1):
#         if list[i] >0:
#             list[i] = "big"
#     return list
# print(biggie_size([-1, 3, 5, -5]))

# 2_Count Positives
# def count_positives(list):
#     count=0
#     for i in list:
#         if i >0:
#             count += 1
#     list[-1]=count
#     print (count)
#     return list
# print(count_positives([1,6,-4,-2,-7,-2]))

# 3_Sum Total
# def sum_total(list):
#     sum=0
#     for i in range(len(list)):
#         sum +=list[i]
#     return sum
# print(sum_total([1,2,3,4]))

# 4_Average
# def average(list):
#     sum=0
#     avg=0
#     for i in range(len(list)):
#         sum +=list[i]
#         avg = sum/len(list)
#     return avg
# print(average([1,2,3,4]))

# 5_Length
# def length(list):
#     return len(list)
# print(length([37,2,1,-9]))

# 6_Minimum 
# def minimum(list):
#     if len(list)==0:
#         return False
#     else:
#         min=list[0]
#         for i in range(len(list)):
#             if min > list[i]:
#                 min = list[i]
#     return min
# print(minimum([37,2,1,-9]))

# 7_Maximum 
# def maximum(list):
#     if len(list)==0:
#         return False
#     else:
#         max=list[0]
#         for i in range(len(list)):
#             if max < list[i]:
#                 max = list[i]
#     return max
# print(maximum([37,2,1,-9]))

# 8_Ultimate Analysis
# def ultimate_analysis(list):
#     dictionary ={
#         "sumTotal": sum(list),
#         "average": sum(list) / len(list),
#         "minimum": min(list),
#         "maximum": max(list),
#         "length": len(list)
#     }
#     return dictionary
# print(ultimate_analysis([37,2,1,-9]))
########## another solution without using built-in:
# def ultimate_analysis(list):
#     dict={}
#     sum=0
#     avg=0
#     max =min = list[0]
#     count=0
#     for value in list:
#         sum+= value
#         count +=1
#         if max < value:
#             max = value
#         if min > value:
#             min =value
#     dict["sumTotal"] =sum
#     dict["average"] =sum/count
#     dict["minimum"] =min
#     dict["maximum"] =max
#     dict["length"] =len(list)
#     return dict
# print(ultimate_analysis([37,2,1,-9]))

# 9_Reverse List
# def reverse_list(list):
#     for i in range(int(len(list) / 2)):
#         list[i], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
#     return list
# print(reverse_list([37,2,1,-9]))