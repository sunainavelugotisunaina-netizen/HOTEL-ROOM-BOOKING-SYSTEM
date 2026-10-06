🏨 Family Hotel Room Booking System

📌 Project Overview

The Family Hotel Room Booking System is a Python-based console application developed to simplify the basic process of managing hotel room bookings.

The system allows users to view available rooms, enter customer details, select a suitable room based on the number of members, calculate the total booking bill, view booking details, and cancel a booking.

This project demonstrates the practical application of fundamental Python programming concepts to a real-world hotel booking scenario.

---

🎯 Project Objective

The main objective of this project is to develop a simple and user-friendly hotel room booking system using Python.

The system is designed to:

- Display available hotel rooms.
- Suggest a suitable room type based on the number of members.
- Collect and validate customer information.
- Book an available room.
- Calculate the total bill based on room price and number of days.
- Display booking details.
- Cancel an existing booking.
- Update room availability after booking or cancellation.

---

🛠️ Technologies and Concepts Used

Technology

- Python 3
- Visual Studio Code
- GitHub

Python Concepts

- Variables
- Dictionaries
- Lists
- "if-elif-else" statements
- "for" loops
- "while" loops
- "input()" and "print()"
- Type conversion using "int()"
- String functions such as "len()" and "isdigit()"
- Comparison operators
- Logical operators
- Arithmetic operations
- Input validation
- Dictionary and list indexing
- Dictionary methods such as ".items()" and ".clear()"
- "break" statement

---

🔄 System Workflow

The complete process of the application is:

Start
  ↓
Display Main Menu
  ↓
Select an Option
  ↓
 ┌─────────────────────┐
 │ 1. View Rooms       │
 │ 2. Book Room        │
 │ 3. View Booking     │
 │ 4. Cancel Booking   │
 │ 5. Exit             │
 └─────────────────────┘
  ↓
Perform Selected Operation
  ↓
Return to Main Menu
  ↓
Exit

---

1️⃣ Room Management

The system first stores the available rooms using a dictionary.

Code

rooms = {
    101: ["Single", 1500, "Available"],
    102: ["Single", 1500, "Available"],
    201: ["Double", 2500, "Available"],
    202: ["Double", 2500, "Available"],
    301: ["Deluxe", 3500, "Available"],
    302: ["Double", 2500, "Available"],
    303: ["Deluxe", 4500, "Available"],
}

Explanation

The room number is used as the dictionary key.

Each room contains three details:

Room Type → Price → Availability Status

For example:

101 → Single → ₹1500 → Available

This makes it easy to access and update room information.

---

2️⃣ Booking Storage

An empty dictionary is created to store the current booking details.

Code

booking = {}

Explanation

Initially, there is no booking, so the dictionary is empty.

After a successful booking, it stores:

- Customer name
- Phone number
- Number of members
- Room number
- Room type
- Number of days
- Total bill

---

3️⃣ Main Menu

The application uses a "while" loop to continuously display the menu.

Code

while True:

    print("\n===== FAMILY HOTEL ROOM BOOKING =====")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. View Booking")
    print("4. Cancel Booking")
    print("5. Exit")

Explanation

The "while True" loop keeps the application running so that the user can perform multiple operations.

The program stops when the user selects 5. Exit.

---

4️⃣ View Rooms

When the user selects Option 1, the system displays all rooms.

Code

for room, details in rooms.items():
    print(room, "   ", details[0], "   ₹", details[1], "   ", details[2])

Explanation

The "for" loop goes through each room in the dictionary.

The program displays:

- Room number
- Room type
- Price
- Availability status

Example Output

Room No   Type      Price      Status

101       Single    ₹1500      Available
102       Single    ₹1500      Available
201       Double    ₹2500      Available

---

5️⃣ Customer Information

When the user selects Option 2 – Book Room, the system asks for customer information.

Code

name = input("Enter customer name: ")
phone = input("Enter phone number: ")
members = int(input("Number of members for check-in: "))

Explanation

The system collects:

- Customer name
- Mobile number
- Number of members

The "int()" function converts numerical input into an integer.

---

6️⃣ Phone Number Validation

The system validates the customer's phone number before continuing.

Code

while True:
    phone = input("Enter phone number: ")

    if len(phone) == 10 and phone.isdigit():
        break
    else:
        print("Invalid phone number! Please enter 10 digit Mobile number.")

Explanation

Two conditions are checked:

- The phone number must contain exactly 10 digits.
- The input must contain only numbers.

If the input is invalid, the system asks the user to enter it again.

---

7️⃣ Room Type Suggestion

The system automatically suggests a room based on the number of members.

Code

if members <= 2:
    suggested_type = "Single"
elif members <= 5:
    suggested_type = "Double"
else:
    suggested_type = "Deluxe"

Room Selection Logic

Number of Members| Suggested Room
1–2| Single
3–5| Double
6 or more| Deluxe

Explanation

This feature helps the user choose a room suitable for the group size.

---

8️⃣ Display Available Rooms

After suggesting the room type, the system searches for available rooms of that type.

Code

for room, details in rooms.items():
    if details[0] == suggested_type and details[2] == "Available":
        print(room, "- ₹", details[1])

Explanation

The system checks two conditions:

1. The room type must match the suggested room type.
2. The room status must be ""Available"".

Only suitable available rooms are displayed.

---

9️⃣ Room Validation

After the user selects a room, the system checks whether the room can be booked.

Code

if room_no in rooms:

    if rooms[room_no][0] == suggested_type:

        if rooms[room_no][2] == "Available":

Explanation

The system verifies:

Does the room exist?
       ↓
Is it the correct room type?
       ↓
Is it available?
       ↓
Yes → Continue Booking

This prevents incorrect room selection.

---

🔟 Number of Days Validation

The system asks how many days the customer wants to stay.

Code

while True:
    days = int(input("Enter number of days : "))

    if 1 <= days <= 15:
        break
    else:
        print("Invalid number of days!")

Explanation

The system accepts a stay duration between 1 and 15 days.

If the user enters an invalid value, the program asks again.

---

1️⃣1️⃣ Bill Calculation

The total bill is calculated using the room price and number of days.

Code

price = rooms[room_no][1]
total = price * days

Formula

Total Bill = Room Price × Number of Days

Example

Room Price = ₹2500
Days = 3

Total Bill = ₹2500 × 3
           = ₹7500

---

1️⃣2️⃣ Confirming the Booking

After successful validation, the room status is changed to ""Booked"".

Code

rooms[room_no][2] = "Booked"

The customer details are then stored.

Code

booking["name"] = name
booking["phone"] = phone
booking["members"] = members
booking["room"] = room_no
booking["room_type"] = suggested_type
booking["days"] = days
booking["total"] = total

Explanation

The room is marked as booked and the customer's complete booking information is saved.

---

1️⃣3️⃣ View Booking Details

When the user selects Option 3, the system displays the current booking.

Information Displayed

Customer Name
Phone
Number of Members
Room Number
Room Type
Number of Days
Total Bill

Explanation

The system checks whether a booking exists.

If a booking exists, all stored details are displayed.

If there is no booking, the system displays:

No booking found.

---

1️⃣4️⃣ Cancel Booking

The user can cancel the current booking using Option 4.

The system asks for the booked room number.

Code

if room_no == booking["room"]:

    rooms[room_no][2] = "Available"
    booking.clear()

Explanation

When the correct room number is entered:

1. The room status changes from Booked to Available.
2. The booking information is cleared.
3. The room can be booked again.

---

1️⃣5️⃣ Exit the Program

When the user selects Option 5, the program displays a thank-you message and stops.

Code

print("THANK YOU for using FAMILY HOTEL ROOM BOOKING!")
break

Explanation

The "break" statement terminates the main "while" loop and ends the program.

---

🧪 Testing

The project was tested using different scenarios to verify that the system works correctly.

Normal Cases

- Viewing available rooms
- Booking a room
- Viewing booking details
- Calculating the total bill
- Cancelling a booking
- Exiting the program

Validation Cases

- Invalid phone number
- Invalid room number
- Selecting an unavailable room
- Selecting an incorrect room type
- Invalid number of days

Testing these cases helps ensure that the system responds correctly to both valid and invalid inputs.

---

📁 Project Structure

Family-Hotel-Room-Booking/
│
├── hotel_booking.py
│
└── README.md

"hotel_booking.py"

Contains the complete Python source code for the hotel room booking system.

"README.md"

Contains the project description, system workflow, important code explanations, testing details, and documentation.

---

▶️ How to Run the Project

Step 1

Install Python 3 on your computer.

Step 2

Open the project in Visual Studio Code.

Step 3

Open the file:

hotel_booking.py

Step 4

Run the program using the VS Code Run button or terminal:

python hotel_booking.py

Step 5

Select an option from the displayed menu and follow the instructions.

---

🚀 Future Enhancements

The current project is designed as a simple console-based application. It can be further improved by adding:

- Multiple customer bookings
- Customer booking history
- Database connectivity
- Login and authentication
- Online payment
- Check-in and check-out dates
- Room search by price
- Graphical User Interface (GUI)
- Automatic receipt generation

---

📌 Conclusion

The Family Hotel Room Booking System demonstrates how Python programming concepts can be used to solve a practical real-world problem.

Through this project, fundamental concepts such as dictionaries, lists, loops, conditional statements, input validation, calculations, and data management were applied to create a functional hotel booking application.

The project provides a simple approach to managing room availability, customer bookings, billing, and cancellation through a console-based interface.
