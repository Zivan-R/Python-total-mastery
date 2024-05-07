# Prompts
welcome_prompt = "Hello buddy! Whatcha want?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
eye_prompt = "How is the patient's eyes?\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
skin_prompt = "How is the patient's skin when you pinch it?\n - 1: Normal skin pinch\n - 2: Slow skin pinch\n"

# Different diagnoses
severe = "Severe dehydration"
some = "Some dehydration"
none = "No dehydration"

error = "\nCould not save diagnosis due to invalid input\n"

diagnosis_list = [
    "Coco - Severe dehydration",
    "Rouki - No dehydration",
    "Momo - Some dehydration"
]

def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error)
        return

    final_diagnosis = name + " - " + diagnosis
    diagnosis_list.append(final_diagnosis)
    print("\nFinal diagnosis:", final_diagnosis, "\n")

def list_patients():
    print("\n")
    for patient in diagnosis_list:
        print(patient)
    print("\n")

def assess_skin(skin):
    if skin == "1":
        return some
    elif skin == "2":
        return severe
    else:
        return ""

def assess_eyes(eyes):
    if eyes == "1":
        return none
    elif eyes == "2":
        return severe
    else:
        return ""


def assess_appearance():
    appearance = input(appearance_prompt)

    if appearance == "1":
        e = input(eye_prompt)
        return assess_eyes(e)    
    elif appearance == "2":
        s = input(skin_prompt)
        return assess_skin(s)
    else:
        return ""

def start_new_diagnosis():
    name = input(name_prompt)
    final_diagnosis = assess_appearance()
    save_new_diagnosis(name, final_diagnosis)
    


def main():
    while True:
        selection = input(welcome_prompt)

        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return

main()

# Unit testing 
def test_assess_skin():
    print(assess_skin("1") == some)
    print(assess_skin("2") == severe)
    print(assess_skin(25) == "")

def test_assess_eyes():
    print(assess_eyes("1") == none)
    print(assess_eyes("2") == severe)
    print(assess_eyes("7") == "")

# test_assess_skin()
# test_assess_eyes()

# Integration testing example
def test_assess_appearance():
    print(assess_appearance())

# test_assess_appearance()

# test name and diagnosis entries
def test_save_new_diagnosis():
    save_new_diagnosis("", "")
    print(diagnosis_list == [
    "Coco - Severe dehydration",
    "Rouki - No dehydration",
    "Momo - Some dehydration"
    ])
    save_new_diagnosis("Kiki", "")
    print(diagnosis_list == [
    "Coco - Severe dehydration",
    "Rouki - No dehydration",
    "Momo - Some dehydration"
    ])
    save_new_diagnosis("", "No dehydration")
    print(diagnosis_list == [
    "Coco - Severe dehydration",
    "Rouki - No dehydration",
    "Momo - Some dehydration"
    ])
    save_new_diagnosis("Kiki", "Some dehydration")
    print(diagnosis_list == [
    "Coco - Severe dehydration",
    "Rouki - No dehydration",
    "Momo - Some dehydration",
    "Kiki - Some dehydration"
    ])
 # test_save_new_diagnosis()