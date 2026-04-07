# Hospital Patient Queue Management System
# The Hospital Patient Queue Management System is a Python-based command-line application designed to manage patient queues in a hospital.
# It utilizes object-oriented programming (OOP) principles and includes three main classes: Patient, Specialization, and OperationsManager.
# This project provides a simple yet effective way to handle patient data and queue management within a hospital setting.
# The Hospital Patient Queue Management System is an illustration of OOP concepts in Python. It consists of three primary classes,
# each serving a specific purpose:

# Patient
# The Patient class represents an individual patient and includes the following attributes:
# •	name: The name of the patient.
# •	status: The patient's status, which can be 0 (normal), 1 (urgent), or 2 (super-urgent).
# This class provides methods for string representation and status formatting for patients.

# Specialization
# The Specialization class manages patient queues within different specializations. It offers functionalities such as:
# •	Adding patients with various urgency levels.
# •	Retrieving the next patient from the queue.
# •	Removing patients by name.
# •	Checking queue capacity.

# OperationsManager
# The OperationsManager class serves as the user interface for interacting with the Specialization instances. Users can perform actions
# like:
# •	Adding new patients to specializations.
# •	Listing patients in specializations.
# •	Retrieving the next patient.
# •	Removing patients.
# •	Ending the program gracefully.

## -------------------- Patient Class --------------------
class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status  # 0 = normal, 1 = urgent, 2 = super urgent

    def get_status(self):
        if self.status == 0:
            return "Normal"
        elif self.status == 1:
            return "Urgent"
        else:
            return "Super Urgent"

    def __str__(self):
        return f"{self.name} ({self.get_status()})"


# -------------------- Specialization Class --------------------
class Specialization:
    def __init__(self):
        self.specializations = {
            "Cardiology": [],
            "Orthopedics": [],
            "Neurology": [],
            "Pediatrics": [],
            "Pulmonology": []
        }
        self.max_capacity = 5

    def choose_specialization(self):
        print("""
Choose a specialization:
1. Cardiology
2. Orthopedics
3. Neurology
4. Pediatrics
5. Pulmonology
""")
        choice = int(input("Enter choice: "))
        spec_list = list(self.specializations.keys())

        if 1 <= choice <= len(spec_list):
            return spec_list[choice - 1]
        else:
            print("Invalid choice")
            return None

    def add_patient(self, patient):
        spec = self.choose_specialization()
        if not spec:
            return

        if len(self.specializations[spec]) >= self.max_capacity:
            print("Queue is full")
            return

        # Priority logic
        if patient.status == 2:
            self.specializations[spec].insert(0, patient)

        elif patient.status == 1:
            index = 0
            for p in self.specializations[spec]:
                if p.status < 2:
                    break
                index += 1
            self.specializations[spec].insert(index, patient)

        else:
            self.specializations[spec].append(patient)

        print(f"Added: {patient}")

    def get_next_patient(self):
        spec = self.choose_specialization()
        if not spec:
            return

        if not self.specializations[spec]:
            print("No patients")
            return

        patient = self.specializations[spec].pop(0)
        print(f"Next patient: {patient}")

    def remove_patient(self, name):
        spec = self.choose_specialization()
        if not spec:
            return

        for i, patient in enumerate(self.specializations[spec]):
            if patient.name == name:
                self.specializations[spec].pop(i)
                print(f"Removed {name}")
                return

        print("Patient not found")

    def list_patients(self):
        spec = self.choose_specialization()
        if not spec:
            return

        if not self.specializations[spec]:
            print("No patients in queue")
            return

        print(f"\nPatients in {spec}:")
        for patient in self.specializations[spec]:
            print(patient)


# -------------------- Operations Manager --------------------
class OperationsManager:
    def __init__(self):
        self.system = Specialization()

    def run(self):
        while True:
            print("\n--- Hospital System ---")
            print("1. Add Patient")
            print("2. List Patients")
            print("3. Get Next Patient")
            print("4. Remove Patient")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter patient name: ")
                status = int(input("Enter status (0-normal, 1-urgent, 2-super urgent): "))

                patient = Patient(name, status)
                self.system.add_patient(patient)

            elif choice == "2":
                self.system.list_patients()

            elif choice == "3":
                self.system.get_next_patient()

            elif choice == "4":
                name = input("Enter patient name: ")
                self.system.remove_patient(name)

            elif choice == "5":
                print("Exiting system...")
                break

            else:
                print("Invalid choice")


# -------------------- Run Program --------------------
if __name__ == "__main__":
    app = OperationsManager()
    app.run()






