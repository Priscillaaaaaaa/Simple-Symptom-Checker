
def get_user_symptoms():
    user_input = input("Enter your symptoms separated by commas: ").lower()
    user_symptoms = user_input.split(',')
    return [symptom.strip() for symptom in user_symptoms]
