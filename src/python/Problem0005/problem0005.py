def smallest_positive_multiple(min_range, max_range):
    i = 1
    limit = 1000000000 #prevent infinite loops!
    candidate = 0
    while i < limit:
        candidate = i * max_range
        #print("testing candidate {0}".format(candidate))
        success = True
        for j in range(max_range - 1, min_range, -1):
            #print("testing candidate against {0}".format(j))
            if candidate % j != 0:
                success = False
                i += 1 #next candidate
                break

        if success:
            return candidate

    return candidate

if __name__ == "__main__":
    print(smallest_positive_multiple(1, 20))
