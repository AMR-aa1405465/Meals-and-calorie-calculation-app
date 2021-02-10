
# Takes the users information list and the index of the current user. get his data and start generating recepipes
import random

from help_functions import take_receipe_amount, get_ingredient_index, display_image, display_write_receipes_to_file


def generate_recommended_receipes(users_info, index):
    joining_date, name, height, weight, dob, age, gender, bmi, bmi_range, activity_level_choice, bmr, tee, alergy_string, edit_date = \
        users_info[index]
    print(f"Hello {name}")
    choice = "0"  # initali value to enter the second while loop for checking input
    number_of_receipes = 0
    generateed = False
    tee = float(tee)

    while (not generateed):  # if the user did not generate meals before (reason can be he didn't have alergy or
        # didnot use the option before) , he can
        while (choice != "1" and choice != "2" and choice != "3" and choice != "4"):
            choice = input(
                "You can perform the following tasks (only select 1 2 3 4):\n1) Generate recipes randomly\n2) Generate recipes randomly based on your caloric needs\n3) Generate recipes randomly based on food allergies\n4) Generate recipes randomly based on caloric needs and food allergies ")

        if (choice == "1"):
            number_of_receipes = take_receipe_amount()  # 4-6
            create_random_alergy_calorie_intake_receipes(number_of_receipes, name, None, -1)
            generateed = True
        if (choice == "2"):
            number_of_receipes = take_receipe_amount()
            caloric_need = tee / int(number_of_receipes)
            create_random_alergy_calorie_intake_receipes(number_of_receipes, name, None, caloric_need)
            generateed = True
        if (choice == "3"):
            if (alergy_string.strip() == "-"):
                print("Sorry You cannot generate meals based on your alergy food")
                continue
            else:
                number_of_receipes = take_receipe_amount()
                create_random_alergy_calorie_intake_receipes(number_of_receipes, name, alergy_string, -1)
                generateed = True

        if (choice == "4"):
            number_of_receipes = take_receipe_amount()
            caloric_need = tee / int(number_of_receipes)
            if (alergy_string.strip() == "-"):
                print("Sorry You cannot generate meals based on your alergy food")
                continue
            else:
                # number_of_receipes = take_receipe_amount()
                create_random_alergy_calorie_intake_receipes(number_of_receipes, name, alergy_string, caloric_need)
                generateed = True
    return number_of_receipes


# The next two functions are helper functions , that helps us creating the receipes based on user needs
def create_random_alergy_calorie_intake_receipes(number_of_receipes, name, alergy_food, caloric_need):
    bad_food = False
    receipes = []
    f = open('recipes.csv', 'r')
    lines = f.readlines()  # reading all lines as list of lines
    f.close()
    accepted_receipes_counter = 0  # holds the count of receipes user chosen
    index = random.randint(1, len(lines))
    while (accepted_receipes_counter != int(number_of_receipes)):
        # Random index of the meals ...
        one_receipe = lines[index].strip().split(";")

        # User supploed a string for alergy_food , then we have to check for it
        if (alergy_food is not None):
            # For each ingredient
            for ingredient in one_receipe[7].split(","):
                # for each user alergy , compare with each ingredient,if found , break
                for user_alergy_index in alergy_food.strip().split("-"):
                    if (get_ingredient_index(ingredient) == user_alergy_index):
                        bad_food = True
                        break
                if (bad_food == True):
                    break

            if (bad_food == True):
                bad_food = False  # resetting so that other food can be checked
                continue  # try choosing another food

        # Caloric intake does not equal -1 means user supplied caloric intake , then we have to check
        if (caloric_need != -1):
            if ((float(one_receipe[9]) / float(one_receipe[10])) > caloric_need):
                continue

        select_receipe = input(
            f"Found A receipe: {one_receipe[1]} , choose (Y or y) to select and see details or (N or n) to skip receipe ")
        if (select_receipe.lower() == "y"):

            # RecipeID;Recipe_Name;Author;Review_Count;Prepare_Time;Cook_Time;Total_Time;Ingredients;Directions;Calories;Servings;Recipe_Photo
            one_receipe = lines[index].strip().split(";")
            print(
                f"The recipe name {one_receipe[1]}\nThe total calories {one_receipe[9]}\nThe serving size. {one_receipe[10]}\nThe prep time. {one_receipe[4]}\nThe cook time. {one_receipe[5]}\nThe total time.{one_receipe[6]}\n")
            display_image(one_receipe[11])  # displaying the image
            print("~Ingredients~:")
            for ingredient in one_receipe[7].split(","):  # potato,egg,fdfgf
                print(f"{ingredient}")
            print(f"The Directions:\n {one_receipe[8]}")
            receipes.append(one_receipe)
            accepted_receipes_counter += 1
        index += 1  # this will work for line by line for
    print("\n\n Thanks for choosing Your receipes =)....Saving them to file\n")
    display_write_receipes_to_file(receipes, name)
    return 1  # means the user successfully created for the current session




# Given a list of receipe names , return a list of their info
def get_receipes_info(receipes_names):
    # Open file , read lines as list elements
    f = open("recipes.csv", 'r')
    lines = f.readlines()
    f.close()
    all_receipe_info = []
    # search in the list
    for receipe_name in receipes_names:
        for line in lines:
            receipe = line.strip().split(";")
            if (receipe[1].strip() == receipe_name.strip()):
                all_receipe_info.append(receipe)
                break  # break from the inner loop
    return all_receipe_info
