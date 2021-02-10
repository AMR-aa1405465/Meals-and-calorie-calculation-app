"""
The Purpose of this file , is to has the functions , that can be used with our main functions to
keep our code reusable as dr hind mentioned

"""


from PIL import Image
import requests
import matplotlib.pyplot as plt
import datetime  # to get date and time
import os
import random
from dateutil.relativedelta import relativedelta

HEADER = "joining_date ; name ; height ; weight ; dob ; age ; gender ; bmi ; bmi_range ; activity_level_choice ; bmr ; tee;  alergy_string;  edit_date"


# print the header to a file
def print_header(file_name):
    f = open(file_name, 'w')
    f.write(f"{HEADER}\n")
    f.close()


# Given the info of the user , print it
def view_user_profile(users_info, index):
    print("\n\n")  # keeping a space to look beautiful =)
    joining_date, name, height, weight, dob, age, gender, bmi, bmi_range, activity_level_choice, bmr, tee, alergy_string, edit_date = \
        users_info[index]
    print(f'User name: {name}')
    print(f'Join date: {joining_date}')
    if (edit_date.strip() != "NA"):
        print(f'Edit date: {joining_date}')
    print(f"Date of birth: {dob}")
    print(f'Age : {age} year old')
    print(f'Height : {float(height) / 100} m')
    print(f'Weight : {weight} Kg')
    print(f'Gender : {gender} ')
    print(f'Body Mass Index (BMI) : {bmi} ')
    print(f'BMI range : {bmi_range} ')
    print(f'Basal Metabolic Rate (BMR): {bmr} ')
    print(f'Total Energy Expenditure (TEE) : {tee} ')


# did it as a function to reuse it
def take_receipe_amount():
    number_of_receipes = 0
    while ( (number_of_receipes < 4) or (number_of_receipes > 6) ):
        number_of_receipes = int(input("Please enter how many receipes to generate 4-6 ").strip())

    return number_of_receipes




# Using Pillow library to display image , got from the internet
def display_image(url):
    response = requests.get(url, stream=True)
    img = Image.open(response.raw)
    plt.imshow(img)
    plt.show()


# Takes a food ingredient string and return its index from the file oat -> 2
def get_ingredient_index(ingredient_name):
    f = open("ingredients.csv")
    lines = f.readlines()
    for index, line in enumerate(lines):
        line = line.split(";")
        if (line[0] == ingredient_name):
            return index


def display_write_receipes_to_file(receipes, name):
    receipes_names = []
    total_calories = 0.0
    for one_receipe in receipes:
        total_calories += float(one_receipe[9])
        receipes_names.append(one_receipe[1])
    average_calories = total_calories / int(len(receipes_names))

    new_file = open(f"{name}-receipes.txt", "a")
    now = datetime.datetime.now()
    session_time = now.strftime("%d/%m/%Y,%H:%M:%S")
    all_meals_string = ",".join(receipes_names)
    # new_file.write(f"Session-time:{session_time}\nMeals Receipes:{all_meals_string}\nTotal-Calories:{total_calories}\nAverage_calories:{average_calories}\n")
    new_file.write(f"{session_time};{all_meals_string};{total_calories};{average_calories}\n")
    new_file.close()


# Given a user name , search for him and delete him from the file
def delete_user(name):
    #1 load info to a list  []
    all_users = load_userInformation_from_file()
    found = False
    index = 0
    #2. search for user index
    for user_info in all_users:
        if (user_info[1] == name):
            found = True  # found the person
            break
        index += 1

    if (found):
        # 3. delete him and return true
        all_users.remove(all_users[index])
        write_content_to_file(all_users, "temp.txt")
        os.remove("userInformation.txt")
        os.rename("temp.txt", "userInformation.txt")
        print(f"{name} record was Removed successfully ")
        if (len(all_users) == 0):
            # number of userInformation is 0 , then let's remove the file
            os.remove("userInformation.txt")
            print("The file userInformation.txt was removed successfully")

        return all_users

    return None  # did not find him , so did not delete


# Given User name , find him and return his information and index in the users_list loaded from file
def find_person(given_name):
    index = 0
    users_info = load_userInformation_from_file()
    for user_info in users_info:
        if (user_info[1].strip() == given_name):
            return users_info, index
        index += 1
    return [], -1


# Given list of user information , write them to file , writting in the csv formate but with ; instead of ,
def write_content_to_file(list_userInformation, file_name):
    print_header(file_name)
    f = open(file_name, "a")  # append because we already wrote header with w,so everything shall be wiped

    for user in list_userInformation:
        last_char = 1
        for user_info in user:
            if (last_char == len(user)):
                f.write(f"{user_info}")  # last item in row dont add ;
            else:
                f.write(f"{user_info};")  # not last item , then add ;
            last_char += 1
        f.write("\n")
    f.close()


# Loads users information from the file and returning as a list of users info
def load_userInformation_from_file():
    user_file = open('userInformation.txt', 'r')  # Open the food file in read mode
    data = []
    next(user_file)  # This statement will skip the first line (header) in the CSV file

    # reading line by line from the file , then adding it in a list , so we have list of user info
    for line in user_file:
        joining_date, name, height, weight, dob, age, gender, bmi, bmi_range, activity_level_choice, bmr, tee, alergy_string, edit_date = line.strip().split(
            ";")
        data.append(
            [joining_date, name, height, weight, dob, age, gender, bmi, bmi_range, activity_level_choice, bmr, tee,
             alergy_string, edit_date])

    return data  # return list of userInformation


# Getting bmi_state (range) based on his bmi
def get_bmi_state(bmi):
    if (bmi < 18.5):
        return "Underweight"
    if (18.5 <= bmi < 24.9):
        return "Normal"
    if (25.0 <= bmi <= 29.9):
        return "Overweight"
    else:
        return "Obese"


# calculate the user real age based on his DOB
def calculate_date(current_date):
    # Taking child date of birth and getting the calculating the Age
    dob = input("Please enter the date of birth in the form dd/mm/yyyy example: 13/12/2002")
    day = int(dob.split('/')[0])  # getting the day and converting to integer
    month = int(dob.split('/')[1])
    year = int(dob.split('/')[2])
    child_dob = datetime.date(year, month, day)
    today_date = current_date.strftime("%d/%m/%Y")
    day2 = int(today_date.split('/')[0])
    month2 = int(today_date.split('/')[1])
    year2 = int(today_date.split('/')[2])
    today_date = datetime.date(year2, month2, day2)
    difference_in_years = relativedelta(today_date, child_dob).years
    return [difference_in_years, dob]


# Get the TEE value given both bmr and activity level
def get_tee(bmr, activity_level_choice):
    tee = 0
    if (activity_level_choice == 1):
        tee = bmr * 1.2
    if (activity_level_choice == 2):
        tee = bmr * 1.375
    if (activity_level_choice == 3):
        tee = bmr * 1.55
    if (activity_level_choice == 4):
        tee = bmr * 1.725
    if (activity_level_choice == 5):
        tee = bmr * 1.9
    return tee


# Gets the alergy number from user and returns a string concatention of his choices
def get_alergy_string():
    ingredints_list = []  # storing the food of allergies in list

    print("\nPlease choose the food number that you are alergic to:\nNumber Ingredient\n")
    with open("ingredients.csv", 'r') as file:
        for line in file:
            ingredient = line.split(';')[0]
            ingredints_list.append(ingredient)  # adding to list

    for (index, con) in enumerate(ingredints_list):  # Loop over the list of allergy and their indexs
        if (index != 0):
            print(f"{index}\t{con}")

    person_allergy_list = []  # store list of number of person alergy
    alergy_string = ""  # to store the person alergy as string
    alergy_number = 0
    while (alergy_number != "-1"):
        alergy_number = input("enter number of food or -1 to finish: ")
        if (alergy_number == "-1"):
            break
        if(int(alergy_number)>30 or int(alergy_number)<1):
            print("Invalid option... choose 1-30 only")
            continue
        person_allergy_list.append(alergy_number)

    # Creating a string from the list of allergies to put in the file
    if (len(person_allergy_list) == 0):
        alergy_string = "-"
    else:
        alergy_string = "-".join(person_allergy_list)

    return alergy_string

# Plots the calories per session as pie-chart , some code got from the searching online
def plot_the_calories_per_session(name_and_new_calories_per_meal):
    names = []
    calories = []
    for record in name_and_new_calories_per_meal:
        name = record[0]
        new_calories = record[1]
        names.append(name)
        calories.append(new_calories)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    fig1, ax1 = plt.subplots()
    ax1.pie(calories, labels=names, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


# Using Pillow library to display image , got from the internet
def display_image(url):
    response = requests.get(url, stream=True)
    img = Image.open(response.raw)
    plt.imshow(img)
    plt.show()
