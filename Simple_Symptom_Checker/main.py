
from database import database
from user_input import get_user_symptoms
from matching_algorithm import match_conditions
from output import display_results

# Main function to run the Symptom Checker
def main():
    user_symptoms = get_user_symptoms()
    matching_conditions = match_conditions(user_symptoms, database)
    display_results(matching_conditions)

if __name__ == "__main__":
    main()
