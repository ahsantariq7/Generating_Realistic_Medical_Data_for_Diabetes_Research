import random
from datetime import datetime

# Lists of common Pakistani first names for males and females
pakistan_male_names = [
    "Muhammad",
    "Ali",
    "Ahmed",
    "Hassan",
    "Usman",
    "Bilal",
    "Saeed",
    "Omar",
    "Nasir",
    "Khalid",
    "Faisal",
    "Imran",
    "Tariq",
    "Waqar",
    "Tahir",
    "Arif",
    "Rizwan",
    "Naveed",
    "Asif",
    "Adnan",
]

pakistan_female_names = [
    "Ayesha",
    "Fatima",
    "Zainab",
    "Amna",
    "Maryam",
    "Sara",
    "Khadija",
    "Bushra",
    "Farah",
    "Amina",
    "Nadia",
    "Samina",
    "Sobia",
    "Tayyaba",
    "Noreen",
    "Shazia",
    "Mehreen",
    "Amber",
    "Hina",
]

# List of common Pakistani last names
pakistan_last_names = [
    "Khan",
    "Ahmed",
    "Ali",
    "Raza",
    "Hussain",
    "Siddiqui",
    "Malik",
    "Shah",
    "Akhtar",
    "Iqbal",
    "Sheikh",
    "Mahmood",
    "Malik",
    "Qureshi",
    "Anwar",
    "Awan",
    "Zafar",
    "Farooq",
    "Khattak",
    "Hassan",
]

# List of anti-diabetic treatments
anti_diabetic_treatments = [
    "Viglip M 50/500mg",
    "Viglip M 50/850mg",
    "Viglip M 50/1000mg",
]

# Create a list to store the generated data
people_data = []

# Generate data for 40 individuals
for _ in range(40):
    gender = random.choice(["Male", "Female"])
    if gender == "Male":
        first_name = random.choice(pakistan_male_names)
    else:
        first_name = random.choice(pakistan_female_names)
    last_name = random.choice(pakistan_last_names)
    while first_name == last_name:  # Ensure first and last names are different
        last_name = random.choice(pakistan_last_names)
    full_name = f"{first_name} {last_name}"
    father_first_name = random.choice(pakistan_male_names)
    father_last_name = random.choice(pakistan_last_names)
    while (
        father_first_name == father_last_name
    ):  # Ensure father's first and last names are different
        father_last_name = random.choice(pakistan_last_names)
    father_name = f"{father_first_name} {father_last_name}"
    age = random.randint(35, 80)
    height = round(random.uniform(150, 190), 2)  # Height in centimeters
    weight = round(random.uniform(45, 120), 2)  # Weight in kilograms
    # Calculate the "Diabetes Since" date based on age
    current_year = datetime.now().year
    earliest_diabetes_year = current_year - age
    diabetes_since_month = random.randint(1, 12)
    diabetes_since_year = random.randint(earliest_diabetes_year, current_year)
    diabetes_since_date = datetime(diabetes_since_year, diabetes_since_month, 1)
    diabetes_since = diabetes_since_date.strftime("%B %Y")
    systolic_bp = random.randint(90, 160)
    diastolic_bp = random.randint(60, 100)
    duration_of_previous_treatment = random.randint(0, 36)  # Months
    previous_anti_diabetic_treatment = random.choice(anti_diabetic_treatments)

    person_data = {
        "Full Name": full_name,
        "Father Name": father_name,
        "Gender": gender,
        "Age": age,
        "Height (cm)": height,
        "Weight (kg)": weight,
        "Diabetes Since": diabetes_since,
        "Systolic BP (mmHg)": systolic_bp,
        "Diastolic BP (mmHg)": diastolic_bp,
        "Duration of Previous Treatment (months)": duration_of_previous_treatment,
        "Previous Anti-Diabetic Treatment": previous_anti_diabetic_treatment,
    }

    people_data.append(person_data)

# Print the generated data
for i, person in enumerate(people_data, start=1):
    print(f"Person {i}:")
    for key, value in person.items():
        print(f"{key}: {value}")
    print("\n")
