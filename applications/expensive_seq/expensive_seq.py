# Your code here


def expensive_seq(x, y, z):
    # Your code here
    cache = {}

    def inner_expensive_seq(x, y, z):
        if x <= 0:
            cache[(x, y, z)] = y + z
            return cache[(x, y, z)]

        elif (x, y, z) in cache:
            return cache[(x, y, z)]

        else:
            cache[(x - 1, y + 1, z)] = inner_expensive_seq(x - 1, y + 1, z)
            cache[(x - 2, y + 2, z * 2)] = inner_expensive_seq(x - 2, y + 2, z * 2)
            cache[(x - 3, y + 3, z * 3)] = inner_expensive_seq(x - 3, y + 3, z * 3)

            # return cache[(x - 1, y + 1, z)] + cache[(x - 2, y + 2, z * 2)] + cache[(x - 2, y + 2, z * 2)]

            return inner_expensive_seq(x - 1, y + 1, z) + inner_expensive_seq(x - 2, y + 2, z * 2) + inner_expensive_seq(x - 3, y + 3, z * 3)

    return inner_expensive_seq(x, y, z)
    
# print(expensive_seq(2, 2, 2))

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
