import re

# Custom Exceptions
class NameErrorException(Exception):
    pass

class EmailErrorException(Exception):
    pass

class PhoneErrorException(Exception):
    pass


# Function to add student
def add_student():
    try:
        name = input("Enter Student Name: ")

        if not name.replace(" ", "").isalpha():
            raise NameErrorException(
                "Name should contain only alphabets."
            )

        age = int(input("Enter Age: "))

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        email = input("Enter Email: ")

        email_pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'

        if not re.match(email_pattern, email):
            raise EmailErrorException(
                "Email must be in the format example@gmail.com"
            )

        phone = input("Enter Phone Number: ")

        if not phone.isdigit() or len(phone) != 10:
            raise PhoneErrorException(
                "Phone number must contain exactly 10 digits."
            )

        # Save to file
        with open("students.txt", "a") as file:
            file.write(f"Name : {name}\n")
            file.write(f"Age  : {age}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Phone: {phone}\n")
            file.write("-" * 30 + "\n")

        print("\nStudent record saved successfully!\n")

    except NameErrorException as e:
        print("Name Error:", e)

    except EmailErrorException as e:
        print("Email Error:", e)

    except PhoneErrorException as e:
        print("Phone Error:", e)

    except ValueError as e:
        print("Invalid Input:", e)

    except Exception as e:
        print("Unexpected Error:", e)


# Function to display records
def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.read()

            if data:
                print("\n===== STUDENT RECORDS =====")
                print(data)
            else:
                print("No records found.")

    except FileNotFoundError:
        print("No student records available.")


# Main Menu
while True:
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
