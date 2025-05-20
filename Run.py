from SparseM import SparseMatrix
#for this file its pretty self explanatory, it loads the SparceMatrix function from our file then creates criteria to run the code and saves the results to our file results.
def main():
    try:
        matrix1 = SparseMatrix(file_path='matrixfile1.txt')
        matrix2 = SparseMatrix(file_path='matrixfile3.txt')

        print("sparse mtrix operations")
        print("Choose 1. Addition")
        print("Choose 2. Subtraction")
        print("Choose 3. Multiplication")
        choice = input("pick your character: ")

        if choice == '1':
            result = matrix1.add(matrix2)
        elif choice == '2':
            result = matrix1.subtract(matrix2)
        elif choice == '3':
            result = matrix1.multiply(matrix2)
        else:
            print("wrong choice bro.")
            return
#i would have loved to create a conditional statement here that creates an output file based on the expression chose however i had to save time and was on a tight schedule lol
        with open("result.txt", "w") as f:
            f.write(str(result))

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
