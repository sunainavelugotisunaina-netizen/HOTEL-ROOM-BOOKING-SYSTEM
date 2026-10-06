rooms = {
    101: ["Single", 1500, "Available"],
    102: ["Single", 1500, "Available"],
    201: ["Double", 2500, "Available"],
    202: ["Double", 2500, "Available"],
    203: ["Double", 2500, "Available"],
    301: ["Deluxe", 3500, "Available"],
    303: ["Deluxe", 4500, "Available"],
}

booking = {}

while True:

    print("\n===== FAMILY HOTEL ROOM BOOKING =====")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. View Booking")
    print("4. Cancel Booking")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    # 1. View Rooms
    if choice == 1:

        print("\nRoom No   Type      Price      Status")

        for room, details in rooms.items():
            print(room, "   ", details[0], "   ₹", details[1], "   ", details[2])

    # 2. Book Room
    elif choice == 2:

        name = input("\nEnter customer name: ")

        # Phone number validation
        while True:
            phone = input("Enter phone number: ")

            if len(phone) == 10 and phone.isdigit():
                break
            else:
                print("Invalid phone number! Please enter 10 digit Mobile number.")

        members = int(input("Number of members for check-in: "))

        # Suggest room based on members
        if members <= 2:
            suggested_type = "Single"
        elif members <= 5:
            suggested_type = "Double"
        else:
            suggested_type = "Deluxe"

        print("\nSuggested Room Type:", suggested_type)
        print("\nAvailable", suggested_type, "Rooms:")

        for room, details in rooms.items():
            if details[0] == suggested_type and details[2] == "Available":
                print(room, "- ₹", details[1])

        room_no = int(input("Enter room number: "))

        if room_no in rooms:

            if rooms[room_no][0] == suggested_type:

                if rooms[room_no][2] == "Available":

                    # Number of days validation
                    while True:
                        days = int(input("Enter number of days : "))

                        if 1 <= days <= 15:
                            break
                        else:
                            print("Invalid number of days! HOTEL cannot do our service not more than 15 days!.")

                    price = rooms[room_no][1]
                    total = price * days

                    rooms[room_no][2] = "Booked"

                    booking["name"] = name
                    booking["phone"] = phone
                    booking["members"] = members
                    booking["room"] = room_no
                    booking["room_type"] = suggested_type
                    booking["days"] = days
                    booking["total"] = total

                    print("\nRoom booked successfully!")
                    print("Room Type:", suggested_type)
                    print("Total Bill: ₹", total)

                else:
                    print("\nRoom is already booked!.")

            else:
                print("Please select a", suggested_type, "room.")

        else:
            print("Invalid room number.")

    # 3. View Booking
    elif choice == 3:

        if booking:

            print("\n===== BOOKING DETAILS =====")
            print("Customer Name:", booking["name"])
            print("Phone:", booking["phone"])
            print("Number of Members:", booking["members"])
            print("Room Number:", booking["room"])
            print("Room Type:", booking["room_type"])
            print("Number of Days:", booking["days"])
            print("Total Bill: ₹", booking["total"])

        else:
            print("No booking found.")

    # 4. Cancel Booking
    elif choice == 4:

        if booking:

            room_no = int(input("Enter the room number to cancel: "))

            if room_no == booking["room"]:

                print("\n===== CANCELLATION DETAILS =====")
                print("Customer Name:", booking["name"])
                print("Mobile Number:", booking["phone"])
                print("Room Number:", booking["room"])

                rooms[room_no][2] = "Available"
                booking.clear()

                print("\nRoom cancelled successfully.")
                print("Room", room_no, "is now available.")

            else:
                print("Invalid room number! Please enter your assigned room number.")

        else:
            print("No booking found.")

    # 5. Exit
    elif choice == 5:

        print("THANK YOU for using FAMILY HOTEL ROOM BOOKING!")
        break

    else:
        print("Invalid choice")
        