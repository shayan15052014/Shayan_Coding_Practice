student_marks = {"Shayan": 100, "usman": 100}
def show_menu():
    print("\n============== what to do ===================")
    print("1. add item")
    print("2. read values")
    print("33. read keys & values")
    print("3. read keys")
    print("4. update value of kyes")
    print("5. deleate item")
    print("6. stop loop")


while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        adding_key = input("enter key: ")
        adding_value = input("enter value: ")
        student_marks[adding_key] = adding_value
        print(student_marks)
        print("Adding Successful")

    if choice == 2:
        print("\n======= Values =====")
        print(student_marks.values())

    if choice == 33:
        print("values: ", student_marks.values())
        print("keys: ", student_marks.keys())

    if choice == 3:
        print(student_marks.keys())

    if choice == 4:
        print(student_marks)
        user_key = input("enter the key from dictionary: ")
        user_value = input(f"enter the changing value of {user_key}: ")
        student_marks[user_key] = user_value
        print(student_marks)
        print("DONE")

    if choice == 5:
        print(student_marks)
        deleater = input("enter the key to deleate: ")
        del student_marks[deleater]
        print(student_marks)

    if choice == 6:
        break
