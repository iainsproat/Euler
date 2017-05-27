def largest_palindrome(num_digits):
    max_input = 10 ** num_digits
    min_input = 10 ** (num_digits - 1)
    inputs = range(min_input, max_input)
    products = []

    print('Debug: max_input: {0}'.format(max_input))
    print('Debug: min_input: {0}'.format(min_input))
    for input1 in inputs:
        for input2 in inputs: #TODO this doubles up items and could be optimised
            products.append(input1 * input2)

    largest_candidate = 0

    for candidate in products:
        if not candidate > largest_candidate:
            continue #move to the next candidate
        s = str(candidate)
        length = len(s)
        completed = True
        for i in range(0, int(length/2)):
            if s[i] != s[length - 1 - i]:
                completed = False
                break

        if completed:
            largest_candidate = candidate

    return largest_candidate

if __name__ == "__main__":
    print(largest_palindrome(3))
