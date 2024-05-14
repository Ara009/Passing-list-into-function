def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd

lst = [2,4,5,6,22,33,1,69,54,12]
even,odd = count(lst)

print(f'number of evens are {even},number of odds are {odd}')
