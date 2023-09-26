
def match_conditions(user_symptoms, database):
    matching_conditions = {}
    for condition, symptoms in database.items():
        common_symptoms = set(user_symptoms) & set(symptoms)
        if common_symptoms:
            matching_conditions[condition] = len(common_symptoms)
    return matching_conditions
