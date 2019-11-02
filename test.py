
#test after

# a= 30
# b= 20
# c= 10
# d= 10

# assert a<b,"a is not smaller than b"
# assert c==d,"{} and {} are not equal".format(c,d)

#test after 2
# def add_num(a,b):
#     return 7

# assert add_num(2,5) == 7,"the result of the add function is not correct"
# assert add_num(2,5) == 10,"the result of the add function is not correct"


# #test 3 the challenege 
# def count_upper_case(message):
#     return sum([1 for c in message if c.isupper()])
    
# # assert count_upper_case("thIS") == 2,"the result is not equal to true neither"
# assert count_upper_case("FOUNDydf") == 5,"the result is not equal to true either"
# # assert count_upper_case("12345") == 0,"the result is not equal to true at all"
# # assert count_upper_case(5) == 0,"the result is not equal to true at all"


# #example teacher

# def find_even_num(list_of_num):
#     if type(list_of_num) == list:
#         count = 0
#         for num in list_of_num:
#             if type(num) == int or type(num) == float:
#                 if num % 2 == 0:
#                     count += 1
#         return count
#     else:
#         return 0

# assert find_even_num([2,3,4,5,6,7,8]) == 4, "The even number count is incorrect"
# assert find_even_num([2,3,4,5,6,7,8, 10, 12]) == 6, "The even number count is incorrect"
# assert find_even_num([2,3,4,5,6,7,8, 10, 12, 14, 16, 18]) == 9, "The even number count is incorrect"
# assert find_even_num([]) == 0, "The even number count is incorrect"
# assert find_even_num(["a","b",2,4]) == 2, "The even number count is incorrect"
# assert find_even_num("ha ha ha") == 0, "The type of argument is not list"
# assert find_even_num(123) == 0, "The type of argument is not list"

# print("All test passed")


#test challenge
# def even_number_of_evens(word):
#     if (len(word)) != 0:
#         counter = 0
#         for e in word:
#             if e % 2 == 0:  
#                 counter +=1
#         if counter % 2 == 0 and counter != 0:
#             return True
#         else:
#             return False
#     else:
#         return False
        
            
# assert even_number_of_evens([]) == False, "No numbers"
# assert even_number_of_evens([2]) == False, "One even number"
# assert even_number_of_evens([2, 4]) == True, "Two even numbers"
# assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
# assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"


    

