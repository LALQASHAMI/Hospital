import random
print()
print("Welcome to Python Hospital!")
print()
print("Please enter your information below to see a Doctor:")
print()

clinics = ["Orthopedics", "General Medicine", "Neurology", "ENT", "Vascular"]

patients = []

for _ in range(5):
    Pname = str(input("Name: "))
    Page = int(input("Age: "))
    if Page < 18:
        print(f"{Pname}, you'll be transferred to the Children's Hospital.")
        print()
        continue
    Pid=int(input("ID:  "))
    print()
    clinicChoice = int(input(f"Choose Clinic (1-{len(clinics)}): ")) - 1
    chosenClinic = clinics[clinicChoice]
    print()
    while True:
        waitingNumber = random.randint(0,100)
        if not any(p[1] == waitingNumber for p in patients):
            break
    print()
    patients.append((Pname, waitingNumber, chosenClinic))
    print(f" Hello  {Pname} , your Doctor at {chosenClinic} will see you soon! Your waiting number is {waitingNumber} .")
    print()


print("Thank you for visiting Python Hospital,We wish you will!")
print()



