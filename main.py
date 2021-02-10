from generate_receipes import *
from edit_delete_Profile import *
from create_load import *
from help_functions import *
import datetime  # to get date and time

# Here are the user choices , we take it as a string to validate them , because user may enter a string, int(input) causes exception
from view_meals import view_user_meals_health

USER_CREATION_LOADING = "1"
EDITING_USER_PROFILE = "2"
USER_PROFILE_VIEW = "3"
RECEIPE_GENERATION = "4"
USER_MEAL_HEALTH_INFO = "5"
QUIT = "6"

if __name__ == '__main__':
    choice = "0"
    users_info, index = [], -1  # users_info : list that have information of all users [[],[],[]]
    generated_before = 0

    while (choice != QUIT):
        choice = input(
            "Please enter the input from the following options\n1.Create or load a user profile\n2.Edit or delete a user profile\n3.View user profile\n4.Generate recipe recommendations for the session\n5.View user meals and generate health information\n6.Exit the program  ")

        if (choice == USER_CREATION_LOADING):
            users_info, index = create_load_profile() # creates or loads profile,  then return the list of users and the index of the profile created or loaded
        elif (choice == EDITING_USER_PROFILE):
            # Checking if the user profile already loaded .... it index = -1 , that means he didnt load user in the list
            if (index == -1):
                print("User information is not loaded ... please choose option 1 first\n")
                continue
            users_info, index =  edit_delete_profile(users_info, index)
        elif (choice == USER_PROFILE_VIEW):
            # Checking if the user profile already loaded .... it index = -1 , that means he didnt load user in the list

            if (index == -1):
                print("User information is not loaded ... please choose option 1 first\n")
                continue
            view_user_profile(users_info, index)
        elif (choice == RECEIPE_GENERATION):
            # Checking if the user profile already loaded .... it index = -1 , that means he didnt load user in the list

            if (index == -1):
                print("User information is not loaded ... please choose option 1 first")
                continue
            if (generated_before != 0):  # User chosen the option before in the session , he cannot create more in session
                print("Sorry You cannot generate more than once for the same session!\n")
                continue
            generated_before = generate_recommended_receipes(users_info, index)
        elif (choice == USER_MEAL_HEALTH_INFO):

            if (index == -1):
                print("User information is not loaded ... please choose option 1 first")
                continue
                # if user profile receipes doesnt exist , we inform him to create receipes first
            if (not os.path.exists(f"{users_info[index][1]}-receipes.txt")):
                print("The receipes file is missing... please choose option 4 before display health info\n")
                continue
            view_user_meals_health(users_info, index)

        elif (choice == QUIT):
            print("It was my pleasure to Help you =) , see you soon mr/madam\n")
            break
        else:
            print("Invalid option....\n\n")
