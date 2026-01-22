#cli/menu
def show_menu():
    print("\n*** College Companion ***")
    print("1] Add tasks")
    print("2] List tasks")
    print("3] Complete tasks")
    print("0] Exit Menu")

def main():
    while True:
        show_menu()
        choice=input("Enter your Choice: ").strip()

        if choice=="1":
            print("Add tasks:(not implemented yet)")
        elif choice=="2":
            print("List tasks:(not implemented yet)")
        elif choice=="3":
            print("Complete tasks:(not implemented yet)")
        elif choice=="0":
            print("Thank you for using this programe.\n")
            break
        else:
            print("Invalid Choice, Try again (1/2/3/0).")

if __name__=="__main__":
    main()