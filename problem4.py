# 1. Matrix Multiplication
def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        return "Error: Matrices cannot be multiplied due to dimension mismatch."
    
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

# Example Usage:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Matrix Multiplication Result:")
print(matrix_multiplication(A, B))


# 2. Palindrome Checker for Sentences
import string

def is_palindrome(sentence):
    cleaned = ''.join(c.lower() for c in sentence if c.isalnum())
    return cleaned == cleaned[::-1]

# Example Usage:
sentence = "A man, a plan, a canal: Panama"
print(f"Is the sentence a palindrome? {is_palindrome(sentence)}")


# 3. File Search Utility
def search_in_file(filename, word):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                if word in line:
                    print(f"Line {idx}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")


# Create a sample file
with open("bishal.txt", "w") as file:
    file.write("This is a test file.\nIt contains multiple lines.\nSome lines mention Python.")

search_in_file("sample.txt", "lines")
