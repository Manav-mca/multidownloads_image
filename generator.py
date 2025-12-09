# # # def my_generator():
# # #     for i in range(8):
# # #         yield i 


# # # gen = my_generator()
# # # # print(next(gen))
# # # print(next(gen))
# # # print(next(gen))
# # # print(next(gen))
# # # print(next(gen))
# # # print(next(gen))
# # # print(next(gen))
# # # print(next(gen))
# # # print(next(gen))
# # # print(next(gen))

# # # for g in gen:
# # #     print(g)


# # Basic Generator function:
# # def count_up_to(max):
# #     count = 1
# #     while count <= max:
# #         yield count
# #         count += 1

# # for num in count_up_to(3):
# #     print(num)

# # Generator EXpression:
# squares = (x**2 for x in range(6))
# print(list(squares))

# infinite Generator:
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a 
#         a, b = b, a + b

# fib = fibonacci()

# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# for k in fib:
#     print(k)

# file reading Generator:
def read_lines(filename):
    with open(filename) as f:
        for line in f :
            yield line.strip()


            