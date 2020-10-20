# class Parent(object):
#     x = 1
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# print(Parent.x,Child1.x,Child2.x)
# Child1.x = 2
# print(Parent.x,Child1.x,Child2.x)
# Parent.x = 3
# print(Parent.x,Child1.x,Child2.x)

# def merge_list(arr1,arr2):
#     ans = arr1.copy()
#     print(ans)
#     ind = 0
#     for i in range(len(arr2)):
#         while ind < len(arr1):
#             if arr2[i] <= arr1[ind]:
#                 ans.insert(ind + i,arr2[i])
#                 break
#             else:
#                 ind = ind + 1
#         else:
#             ans = ans + arr2[i:]
#             break
#     return ans
# print(merge_list([1,3,4],[0,1,2,5,6]))

def merge_list(arr1,arr2):
    index1 = 0
    index2 = 0
    res = []
    while(index1<len(arr1) and index2<len(arr2)):
        if arr1[index1]<arr2[index2]:
            res.append(arr1[index1])
            index1 += 1
        else:
            res.append(arr2[index2])
            index2 += 1
    if index1==len(arr1):
        res += arr2[index2:]
    else:
        res += arr1[index1:]
    return res
print(merge_list([1,3,4],[0,1,2,5,6]))