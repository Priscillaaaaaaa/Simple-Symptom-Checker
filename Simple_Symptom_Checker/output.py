
def display_results(matching_conditions):
    if matching_conditions:
        print("Based on your symptoms, you might have the following conditions:")
        for condition, common_symptom_count in matching_conditions.items():
            print(f"{condition} (Matching Symptoms: {common_symptom_count})")
    else:
        print("No matching conditions found.")
    print("Please consult with a healthcare professional for a proper diagnosis.")
