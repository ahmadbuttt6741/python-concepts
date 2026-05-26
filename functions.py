def functionsum(a, b):
    """Print the sum of two numbers."""
    print(a + b)


# Examples
functionsum(1, 2)
functionsum(1, 523)
functionsum(1123, 2)
functionsum(1234, 3422)
functionsum(1, 24343)


# Correct lambda example
sum_lambda = lambda a, b: a + b
print(sum_lambda(1, 2))


def fact(x):
    fac = 1
    for i in range (1,x+1):
     fac *=i
    return fac


print(fact(5))



def convert_usd(x):
    return x*280

print(convert_usd(100))


def check_number(x):
    if x%2==0:
        print("number is even")
    else:
        print ("number is odd")



check_number(12)
check_number(13)
check_number(2132)



def factorial(x):
    print(fact(x))
    if (x==0):
        return
    print(x)
    factorial(x-1)



factorial(5)


def factorials(n):
    if (n ==0 or n ==1):
        return 1
    else :
        return n*factorials(n-1)


print(factorials(6))


def calculate_sum(n):
    if n==0:
        return 0
    return n+calculate_sum(n-1)

print(calculate_sum(5))

list1 = [1,2,3,"Ahmad"]


def printlist(list, idx ):
    if idx ==len(list):
        return
    print( list[idx])
    printlist(list,idx+1)

printlist(list1,0)
