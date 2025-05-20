from SparseM import SparseMatrix #import from our sparce file
#this is where we shall store our output
def write_to_file(content):
    with open("results.txt", "w") as f:
        f.write(content)

def main():
    # Automatically load default matrix files
    matrix1 = SparseMatrix("matrixfile1.txt")
    matrix2 = SparseMatrix("matrixfile3.txt")

    print("Sparse Matrix Operations")
    print("choose 1. Add")
    print("choose 2. Subtract")
    print("choose 3. Multiply")

    choice = input("Select an operation from 1-3: ")

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
        print("Ops Worng choice.")
        return

    # Print and save the result
    result_text = header + str(result)
    print(result_text)
    write_to_file(result_text)

if __name__ == "__main__":
    main()
