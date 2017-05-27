def run():
    storage = []
    for x in range(0, 1000):
        if x % 3 == 0 or x % 5 == 0:
            storage.append(x)

    sum = 0
    for item in storage:
        sum += item

    return sum

if __name__ == '__main__':
    print(run())
