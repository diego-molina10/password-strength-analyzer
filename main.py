import os

def run_script(filename):
    # Runs the given Python file
    os.system(f'python {filename}')

def main():
    while True:
        print("\n=== Password Strength Analyzer Menu ===")
        print("1. Run Dataset Processor 1")
        print("2. Run Dataset Processor 2")
        print("3. Run Dataset Processor 3")
        print("4. Run Dataset Processor 4")
        print("5. Run Dataset Processor 5")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            run_script("dataset1.py")
        elif choice == "2":
            run_script("dataset2.py")
        elif choice == "3":
            run_script("dataset3.py")
        elif choice == "4":
            run_script("dataset4.py")
        elif choice == "5":
            run_script("dataset5.py")
        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
