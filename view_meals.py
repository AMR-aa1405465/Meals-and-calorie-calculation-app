from help_functions import plot_the_calories_per_session
from generate_receipes import get_receipes_info


def view_user_meals_health(users_info, index):
    tee = float( users_info[index][11] )
    # open file for reading info , we have only 4 lines here , one for each info
    f = open(f"{users_info[index][1]}-receipes.txt", "r")
    lines = f.readlines()
    f.close()

    # Loop over all the session data for a user , then create a list of the info loaded for each session
    sessions_info = []
    for line in lines:
        line = line.strip().split(";")  # split by semi-colon
        session_time = line[0]
        meals = line[1].strip().split(",")  # since i split names by ;
        total_calories = float(line[2])
        avg_calories = float(line[3])
        sessions_info.append([session_time, meals, total_calories, avg_calories])

    for s_info in sessions_info:
        total_calories_per_session = 0
        session_time, meals, total_calories, avg_calories = s_info
        name_and_new_calories_per_meal = []

        num_serving = int(input("Please enter the number of serving to perform analysis on"))
        receipe_information = get_receipes_info(meals)
        for one_receipe in receipe_information:
            print(
                f"The recipe name: {one_receipe[1]}\nThe total calories: {one_receipe[9]}\nThe serving size: {one_receipe[10]}\nThe prep time: {one_receipe[4]}\nThe cook time: {one_receipe[5]}\nThe total time: {one_receipe[6]}\n")
            # Appending calories name & serving in a list that we can use later
            name_and_new_calories_per_meal.append([one_receipe[1], float(one_receipe[9]) * num_serving])
            print([one_receipe[1], float(one_receipe[9]) * num_serving],"\n")

        # For every meal in the session , we check for caloric surplus , get total & avg per session
        for record in name_and_new_calories_per_meal:
            name = record[0]
            new_calories = record[1]
            if (new_calories > (tee / len(meals))):
                # a caloric surplus happened
                print(f"Caloric surplus in meal: {name}")
            total_calories_per_session += new_calories
        print(
            f"Total Calories per session for new serving is {total_calories_per_session}, Avg is {total_calories_per_session / len(name_and_new_calories_per_meal)}")
        if (total_calories_per_session > tee):
            print("The user is having a calorie surplus for this session\n")
        plot_the_calories_per_session(name_and_new_calories_per_meal)

        print("-------------------------------")
