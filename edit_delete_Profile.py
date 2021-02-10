# import datetime

# For updating and deleteing here are the function that i have built , some of them to help me do the tasks
import datetime

from help_functions import get_tee, delete_user, calculate_date, get_bmi_state, get_alergy_string
import os


def edit_delete_profile(users_info, index):
    # [ [111,"aliya"] , [] ,[]]
    joining_date, name, height, weight, dob, age, gender, bmi, bmi_range, activity_level_choice, bmr, tee, alergy_string, edit_date = \
        users_info[index]
    print(f"Hello {name}")
    choice = "0"  # just initali value to enter the while loop
    while (choice != "1" and choice != "2"):
        choice = input(
            "You can perform one of the following operations only:\n1) Delete your profile\n2) Edit your user profile\n")

    if (choice == "1"):
        # person=find_person(name) #searching for the user
        #
        # if found ... delete him using his name
        # delete_user(person[1])
        return delete_user(name), -1  # l8tr
    if (choice == "2"):
        print(f"Hello {name}")
        return edit_record(users_info, index) , index


def edit_record(users_info, index):
    # [[],[],[],[,,,,,,,]]
    # joining_date, name, height, weight, dob, age, gender, bmi, bmi_range, activity_level_choice, bmr, tee, alergy_string, edit_date
    old_record = users_info[index].copy()
    height = float(users_info[index][2])
    weight = float(users_info[index][3])
    age = int(users_info[index][5])
    gender = users_info[index][6]
    activity_level_choice = int(users_info[index][9])
    bmr = float(users_info[index][10])

    edit_choice = input(
        "These are the fields that you can edit in your profile:\n1) Name\n2) Year of birth (or Date of Birth for "
        "bonus)\n3) Gender\n4) Height (m)\n5) Weight (Kg)\n6) Activity level\n7) Food allergies")
    if (edit_choice == "1"):
        new_name = input("Please enter a new Name")
        users_info[index][1] = new_name
        now = datetime.datetime.now()
        joining_date = now.strftime("%d/%m/%Y,%H:%M:%S")  # day/month/year,hour/min/second
        users_info[index][13] = joining_date

        update_record(old_record, users_info[index])
    elif (edit_choice == "2"):
        now = datetime.datetime.now()
        age, dob = calculate_date(now)  # getting the child Age
        bmr = 0  # initalize the value for bmr
        if (gender.lower() == "female"):
            bmr = 655.1 + (9.563 * weight) + (1.85 * height * 100) - (4.676 * age)
        if (gender.lower() == "male"):
            bmr = 66.47 + (13.75 * weight) + (5.003 * height * 100) - (6.755 * age)
        tee = get_tee(bmr, activity_level_choice)  # Getting the tee giving the bmr
        users_info[index][4] = dob
        users_info[index][5] = age
        users_info[index][10] = bmr
        users_info[index][11] = tee
        update_record(old_record, users_info[index])
    elif (edit_choice == "3"):
        new_gender = input("Please enter your gender (male or female)")
        bmr = 0  # initalize the value for bmr
        if (new_gender.lower() == "female"):
            bmr = 655.1 + (9.563 * weight) + (1.85 * height * 100) - (4.676 * age)
        if (new_gender.lower() == "male"):
            bmr = 66.47 + (13.75 * weight) + (5.003 * height * 100) - (6.755 * age)
        tee = get_tee(bmr, activity_level_choice)  # Getting the tee giving the bmr
        users_info[index][6] = new_gender
        users_info[index][10] = bmr
        users_info[index][11] = tee
        update_record(old_record, users_info[index])
    elif (edit_choice == "4"):
        new_height = float(input("Please enter your new height(cm)"))
        bmi = weight / ((new_height / 100) ** 2)
        bmi_range = get_bmi_state(bmi)
        bmr = 0  # initalize the value for bmr
        if (gender.lower() == "female"):
            bmr = 655.1 + (9.563 * weight) + (1.85 * height * 100) - (4.676 * age)
        if (gender.lower() == "male"):
            bmr = 66.47 + (13.75 * weight) + (5.003 * height * 100) - (6.755 * age)
        tee = get_tee(bmr, activity_level_choice)  # Getting the tee giving the bmr
        users_info[index][2] = new_height
        users_info[index][7] = bmi
        users_info[index][8] = bmi_range
        users_info[index][10] = bmr
        users_info[index][11] = tee
        update_record(old_record, users_info[index])
    elif (edit_choice == "5"):
        new_weight = float(input("Please enter your new height(cm)"))
        bmi = new_weight / ((height / 100) ** 2)
        bmi_range = get_bmi_state(bmi)
        bmr = 0  # initalize the value for bmr
        if (gender.lower() == "female"):
            bmr = 655.1 + (9.563 * new_weight) + (1.85 * height * 100) - (4.676 * age)
        if (gender.lower() == "male"):
            bmr = 66.47 + (13.75 * new_weight) + (5.003 * height * 100) - (6.755 * age)
        tee = get_tee(bmr, activity_level_choice)  # Getting the tee giving the bmr
        users_info[index][3] = new_weight
        users_info[index][7] = bmi
        users_info[index][8] = bmi_range
        users_info[index][10] = bmr
        users_info[index][11] = tee
        update_record(old_record, users_info[index])
    elif (edit_choice == "6"):
        activity_level_choice = int(input(
            "Please choose the number corresponding to your activity type\n1 Little/No exercise\n2 Light exercise\n3 Moderate exercise (3-5 days/week)\n4 Very active (6-7 days/week)\n5 Extra active (very active & physical job)"))
        tee = get_tee(bmr, activity_level_choice)  # Getting the tee giving the bmr
        users_info[index][9] = activity_level_choice
        users_info[index][11] = tee
        update_record(old_record, users_info[index])
    elif (edit_choice == "7"):
        alergy_string = get_alergy_string()  # getting the alergy string from user
        users_info[index][12] = alergy_string
        update_record(old_record, users_info[index])
    else:
        print("InValid Option...returning to menu")
    return users_info  # returned the Altered


#   Takes an old record and new record to replace it in the file
def update_record(old_record, new_record):
    found = False
    updated = False
    with open('userInformation.txt', 'r') as file:
        f = open('temp.txt', 'a')
        # Loop and copy line by line to put into the other file
        for line in file:
            stored_data = line.strip().split(";")
            # print(stored_data)
            # to check if the old record exist or not... check old record with the user_information data by data
            if (not found):

                for i in range(len(old_record)):
                    if stored_data[i].strip() == str(old_record[i]).strip():
                        found = True
                    else:
                        found = False  # if at least one info is incorrect, maybe he is another person not what we are looking for

            if (found and not updated):  # replacing with the new record
                last_char = 1  # to avoid having extra semi-colon at the end
                for user_info in new_record:
                    if (last_char == len(new_record)):
                        f.write(f"{user_info}")  # last item in row dont add ;
                    else:
                        f.write(f"{user_info};")  # not last item , then add ;
                    last_char += 1
                f.write("\n")
                updated = True  # so that other records doesnt get updated as well
            else:  # not the required record , just write it to the file directly
                f.write(line)

        f.close()
    os.remove("userInformation.txt")
    os.rename("temp.txt", "userInformation.txt")
    print("Successfully Updated... Thank You\n")
