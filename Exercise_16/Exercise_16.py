
def magic_tuples(total_sum, max_number):
    return ((i, j) for i in range(1, max_number)
            for j in range(1, max_number) if (i+j) == total_sum)


if __name__ == "__main__":
    for t in magic_tuples(10, 10):
        print(t)
