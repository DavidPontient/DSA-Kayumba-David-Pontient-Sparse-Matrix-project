from sparse_matrix import SparseMatrix

def write_to_file(content):
    with open("results.txt", "w") as f:
        f.write(content)

def main():
    # Automatically load default matrix files
    matrix1 = SparseMatrix("matrix1.txt")
    matrix2 = SparseMatrix("matrix2.txt")

    print("Sparse Matrix Operations")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")

    choice = input("Choose an operation (1/2/3): ").strip()

    if choice == "1":
        result = matrix1.add(matrix2)
        header = "Addition Result:\n"
    elif choice == "2":
        result = matrix1.subtract(matrix2)
        header = "Subtraction Result:\n"
    elif choice == "3":
        result = matrix1.multiply(matrix2)
        header = "Multiplication Result:\n"
    else:
        print("Invalid choice.")
        return

    # Print and save the result
    result_text = header + str(result)
    print(result_text)
    write_to_file(result_text)

if __name__ == "__main__":
    main()
