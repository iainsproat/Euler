def fibonacci(value_limit):
    oldresult = 1
    yield oldresult
    currentresult = 2
    yield currentresult
    while currentresult <= value_limit:
        newresult = oldresult + currentresult
        oldresult = currentresult
        currentresult = newresult
        yield newresult



def even_valued_fibonacci():
    for number in fibonacci(4000000):
        if number % 2 == 0:
            yield number

def sum_of_even_valued_fibonacci():
    return sum(even_valued_fibonacci())

if __name__ == "__main__":
        print(sum_of_even_valued_fibonacci())
