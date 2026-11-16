
from datetime import datetime

# Store patient information while the program is running
patients = {}
vitals = {}
alerts = {}


# 1. DISPLAY MAIN MENU
def show_menu():
    print("\n========== VITALWATCH SYSTEM ==========")
    print("1. Add Patient")
    print("2. Record Patient Vitals")
    print("3. View Patient Trend")
    print("4. View Active Alerts")
    print("5. Print Shift Handover Summary")
    print("6. Exit")
    print("=======================================")


# 2. ADD NEW PATIENT
def add_patient():
    print("\n--- ADD NEW PATIENT ---")

    patient_id = input("Enter Patient ID: ").strip().upper()

    if not patient_id:
        print("Patient ID cannot be empty!")
        return

    if patient_id in patients:
        print("Patient ID already exists!")
        return

    name = input("Enter Patient Name: ").strip()

    if not name:
        print("Patient name cannot be empty!")
        return

    age = input("Enter Patient Age: ").strip()

    if not age.isdigit() or int(age) <= 0:
        print("Please enter a valid age!")
        return

    ward = input("Enter Ward Number: ").strip()

    patients[patient_id] = {
        "name": name,
        "age": int(age),
        "ward": ward
    }

    vitals[patient_id] = []
    alerts[patient_id] = []

    print("\nPatient added successfully!")


# 3. RECORD PATIENT VITALS
def record_vitals():
    print("\n--- RECORD PATIENT VITALS ---")

    patient_id = input("Enter Patient ID: ").strip().upper()

    if patient_id not in patients:
        print("Patient not found!")
        return

    try:
        bp = input("Enter Blood Pressure (e.g. 120/80): ").strip()

        systolic, diastolic = map(int, bp.split("/"))

        pulse = int(input("Enter Pulse Rate: "))
        temperature = float(input("Enter Temperature: "))
        spo2 = int(input("Enter Oxygen Saturation: "))

        # Validate input values
        if not (40 <= systolic <= 250 and 20 <= diastolic <= 150):
            print("Invalid blood pressure input!")
            return

        if not (20 <= pulse <= 250):
            print("Invalid pulse input!")
            return

        if not (30 <= temperature <= 45):
            print("Invalid temperature input!")
            return

        if not (50 <= spo2 <= 100):
            print("Invalid oxygen saturation input!")
            return

        # Store vital readings
        reading = {
            "blood_pressure": bp,
            "systolic": systolic,
            "diastolic": diastolic,
            "pulse": pulse,
            "temperature": temperature,
            "spo2": spo2,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        # Generate educational example alerts
        patient_alerts = []

        if systolic < 90 or systolic > 140 or diastolic < 60 or diastolic > 90:
            patient_alerts.append(
                "Blood pressure outside example range"
            )

        if pulse < 60 or pulse > 100:
            patient_alerts.append(
                "Pulse outside example range"
            )

        if temperature < 36.0 or temperature > 38.0:
            patient_alerts.append(
                "Temperature outside example range"
            )

        if spo2 < 95:
            patient_alerts.append(
                "Oxygen saturation below example threshold"
            )

        # Attach alerts to this reading
        reading["alerts"] = patient_alerts

        # Save reading in memory
        vitals[patient_id].append(reading)
        alerts[patient_id] = patient_alerts

        print("\nVital readings recorded successfully!")

        if patient_alerts:
            print("\nWARNING: Educational alerts generated!")

            for alert in patient_alerts:
                print("-", alert)
        else:
            print("No educational threshold alerts detected.")

    except ValueError:
        print("Invalid input! Check your values and BP format.")


# 4. VIEW PATIENT TREND
def view_patient_trend():
    print("\n--- PATIENT VITAL TREND ---")

    pid = input("Enter Patient ID: ").strip().upper()

    if pid not in patients:
        print("Patient not found!")
        return

    readings = vitals.get(pid, [])

    if len(readings) < 3:
        print("At least 3 readings are required!")
        return

    last_three = readings[-3:]

    for i, r in enumerate(last_three, 1):
        print(f"\nReading {i}: {r['time']}")
        print(f"BP: {r['blood_pressure']}")
        print(f"Pulse: {r['pulse']}")
        print(f"Temperature: {r['temperature']}")
        print(f"SpO2: {r['spo2']}")
        print("Alerts:", len(r.get("alerts", [])))

    # Compare alert counts
    counts = [
        len(r.get("alerts", []))
        for r in last_three
    ]

    if counts[2] < counts[0]:
        print("\nTrend: IMPROVING")

    elif counts[2] > counts[0]:
        print("\nTrend: WORSENING")

    else:
        print("\nTrend: STABLE")

    print("\nNote: This is a simplified educational trend based on alert counts.")


# 5. VIEW ACTIVE ALERTS
def view_active_alerts():
    print("\n--- ACTIVE PATIENT ALERTS ---")

    found = False

    for pid, patient_alerts in alerts.items():

        if patient_alerts:
            found = True

            patient = patients[pid]

            print("\nPatient ID:", pid)
            print("Name:", patient["name"])
            print("Ward:", patient["ward"])

            for alert in patient_alerts:
                print("WARNING:", alert)

    if not found:
        print("No active alerts!")


# 6. SHIFT HANDOVER SUMMARY
def shift_handover_summary():
    print("\n========== SHIFT HANDOVER SUMMARY ==========")

    if not patients:
        print("No patients registered!")
        return

    for pid, patient in patients.items():

        print("\n--------------------------------")
        print("Patient ID:", pid)
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Ward:", patient["ward"])

        readings = vitals.get(pid, [])

        if readings:
            latest = readings[-1]

            print("\nLatest Vital Readings:")
            print("Blood Pressure:", latest["blood_pressure"])
            print("Pulse:", latest["pulse"])
            print("Temperature:", latest["temperature"])
            print("SpO2:", latest["spo2"])
            print("Recorded Time:", latest["time"])

            patient_alerts = latest.get("alerts", [])

            if patient_alerts:
                print("\nActive Alerts:")

                for alert in patient_alerts:
                    print("WARNING:", alert)

            else:
                print("\nNo active alerts.")

        else:
            print("\nNo vital readings recorded yet.")

    print("\n========== END OF SUMMARY ==========")


# 7. MAIN PROGRAM
while True:

    show_menu()

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_patient()

    elif choice == "2":
        record_vitals()

    elif choice == "3":
        view_patient_trend()

    elif choice == "4":
        view_active_alerts()

    elif choice == "5":
        shift_handover_summary()

    elif choice == "6":
        print("\nThank you for using VitalWatch!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
