def even_num(num):
    for i in range(num):
        if i % 2 ==0:
            yield i

even_gen = even_num(10)
print(next(even_gen))
print(next(even_gen))
for num in even_gen:
    print(num)

def even_num(a,b):
    for i in range(a,b):
        if i % 2 == 0:
            yield i

even_gen = even_num(20,30)

# Use next() to retrieve and print the first three even numbers
print(next(even_gen))  # 0
print(next(even_gen))  # 2
print(next(even_gen))  # 4

sum = lambda x : print(x+1)
sum(5)







