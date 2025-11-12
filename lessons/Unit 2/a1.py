import random

# Shifts the items in a list by a given amount
def shift_list(lst, amt):
    new_lst = [0] * len(lst)
    for i in range(len(lst)):
        new_lst[(i + amt) % len(lst)] = lst[i]
    return new_lst

# Adds two square matrices together (same size)
def add_matrices(A, B):
    if len(A) != len(B):
        return -1
    result = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

# Checks if a number (5–19) is prime
def is_prime(num):
    return (num == 5) or (num % 2 != 0 and num % 3 != 0 and num % 5 != 0)

# Prints a matrix neatly
def print_matrix(M):
    largest = 0
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] > largest:
                largest = M[i][j]
    width = len(str(largest))
    for i in range(len(M)):
        for j in range(len(M)):
            print("%*d " % (width, M[i][j]), end="")
        print()

# Finds the magic sum for a square of size N
def magic_sum(N):
    total = 0
    for i in range(1, N * N + 1):
        total += i
    return total // N

# Checks if a square is a magic square
def is_magic(M):
    size = len(M)
    target = magic_sum(size)

    # Check rows and columns together
    for i in range(size):
        row_sum = sum(M[i])
        col_sum = sum(M[j][i] for j in range(size))
        if row_sum != target or col_sum != target:
            return False

    # Check both diagonals
    diag1 = sum(M[i][i] for i in range(size))
    diag2 = sum(M[i][size - 1 - i] for i in range(size))

    if diag1 != target or diag2 != target:
        return False
    return True


# Ask user for valid input
valid = False
matrix_size = 0
while not valid:
    num = input("Enter a prime number between 5 and 19: ")
    if num.isdigit():
        num = int(num)
        if 5 <= num <= 19 and is_prime(num):
            valid = True
            matrix_size = num
        else:
            print("Must be an odd prime between 5 and 19.")
    else:
        print("Please enter a number.")

# Create first matrix (M1)
M1 = []
row = list(range(1, matrix_size + 1))
random.shuffle(row)

for i in range(0, matrix_size * 2 + 1, 2):
    M1.append(shift_list(row, i))

# Create second matrix (M2)
M2 = []
row = [matrix_size * i for i in range(matrix_size)]
random.shuffle(row)

for i in range(0, matrix_size * 3 + 1, 3):
    M2.append(shift_list(row, i))

# Combine matrices
M3 = add_matrices(M1, M2)

# Display the results
print(f"\nMagic Square {matrix_size}x{matrix_size}")
print("-" * 30)
print_matrix(M3)

magic_val = magic_sum(matrix_size)
print(f"\nMagic Sum: {magic_val}")

print("It’s magic!" if is_magic(M3) else "Not magic.")
