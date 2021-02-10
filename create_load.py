from help_functions import print_header, find_person, calculate_date, get_bmi_state, get_tee, get_alergy_string
import os
import datetime  # to get date and time

# the main function to create and load the profile , create or load profile and return list of user data + index in
# the list , so that we can use it in the other functions
#from help_functions import calculate_date


def create_load_profile():
    users = []
    if (not os.path.exists('userInformation.txt')):  # File does not exist , then create it
        # Writting header to the file since it is first use
        print_header("userInformation.txt")
        return take_user_input(users), 0  # take user input and return his data
    else:
        created_account = input("Have you created a profile? (n,y)  ")
        if (created_account.lower() == 'n'):
            return take_user_input(users), 0  # create new user and return it
        elif (created_account.lower() == 'y'):
            found = False
            while (not found):
                name = input("Please enter your name registered:  ")
                users_info, index = find_person(name)

                # User info exists
                if (index != -1):
                    # found the person
                    found = True
                    print("Your profile was loaded successfully\n")
                    # print(f"Found! {name}")
                    return users_info, index

        else:
            print("Invalid input....")


# Takes user input and write them to file
def take_user_input(users):
    now = datetime.datetime.now()
    joining_date = now.strftime("%d/%m/%Y,%H:%M:%S ")  # day/month/year,hour/min/second
    name = input("Please enter your name ")
    height = float(input("Please enter your height "))
    weight = float(input("Please enter your weight "))
    age, dob = calculate_date(now)  # getting the child Age
    bmi = weight / ((height / 100) ** 2)
    bmi_range = get_bmi_state(bmi)
    gender = ""
    while (gender != "male" and gender != "female"):
        gender = input("Please enter your gender (male or female) Only ")

    bmr = 0  # initalize the value for bmr
    if (gender.lower() == "female"):
        bmr = 655.1 + (9.563 * weight) + (1.85 * height * 100) - (4.676 * age)
    if (gender.lower() == "male"):
        bmr = 66.47 + (13.75 * weight) + (5.003 * height * 100) - (6.755 * age)

    activity_level_choice = int(input(
        "Please choose the number corresponding to your activity type\n1 Little/No exercise\n2 Light exercise\n3 "
        "Moderate exercise (3-5 days/week)\n4 Very active (6-7 days/week)\n5 Extra active (very active & physical "
        "job) "))

    tee = get_tee(bmr, activity_level_choice)  # Getting the tee giving the bmr

    alergy_string = get_alergy_string()  # getting the alergy string from user

    # specfiying only 2 decimal point since numbers is big 12.33
    bmi = float("{:.2f}".format(bmi))
    bmr = float("{:.2f}".format(bmr))
    tee = float("{:.2f}".format(tee))

    f = open("userInformation.txt", "a")
    f.write(
        f"{joining_date}; {name}; {height}; {weight}; {dob}; {age}; {gender}; {bmi}; {bmi_range}; {activity_level_choice}; {bmr}; {tee}; {alergy_string}; NA \n")
    f.close()
    users.append([joining_date, name, height, weight, dob, age, gender, bmi, bmi_range, activity_level_choice, bmr, tee,
                  alergy_string, joining_date])
    return users
