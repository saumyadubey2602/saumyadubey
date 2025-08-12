def add(num1,num2):
    result=num1+num2
    def square():
        return result*result

    return square()
print(add(10,20))
