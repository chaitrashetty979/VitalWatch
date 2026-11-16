
from datetime import datetime

patients = {}
vitals = {}
alerts = {}


# 1. Add Patient
def add_patient():
    pid = input("Enter Patient ID: ").strip().upper()

    if not pid or pid in patients:
        print("Invalid or existing Patient ID!")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ")
    ward = input("Enter Ward: ")

    if not name or not age.isdigit() or int(age) <= 0:
        print("Invalid patient details!")
        return

    patients[pid] = {"name": name, "age": int(age), "ward": ward}
    vitals[pid] = []
    alerts[pid] = []

    print("Patient added successfully!")


# 2. Record Patient Vitals
def record_vitals():
    pid = input("Enter Patient ID: ").strip().upper()

    if pid not in patients:
        print("Patient not found!")
        return

    try:
        bp = input("Enter BP (120/80): ")
        sys, dia = map(int, bp.split("/"))
        pulse = int(input("Enter Pulse: "))
        temp = float(input("Enter Temperature: "))
        spo2 = int(input("Enter SpO2: "))

        if not (40 <= sys <= 250 and 20 <= dia <= 150):
            print("Invalid BP!")
            return
        if not 20 <= pulse <= 250:
            print("Invalid pulse!")
            return
        if not 30 <= temp <= 45:
            print("Invalid temperature!")
            return
        if not 50 <= spo2 <= 100:
            print("Invalid SpO2!")
            return

        a = []
        if sys < 90 or sys > 140 or dia < 60 or dia > 90:
            a.append("Abnormal BP")
        if pulse < 60 or pulse > 100:
            a.append("Abnormal Pulse")
        if temp < 36 or temp > 38:
            a.append("Abnormal Temperature")
        if spo2 < 95:
            a.append("Low Oxygen Level")

        reading = {
            "bp": bp, "pulse": pulse, "temp": temp,
            "spo2": spo2,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "alerts": a
        }

        vitals[pid].append(reading)
        alerts[pid] = a

        print("Vitals recorded successfully!")
        if a:
            for alert in a:
                print("WARNING:", alert)
        else:
            print("No alerts detected.")

    except ValueError:
        print("Invalid input! Please enter correct values.")


# 3. View Patient Trend
def view_trend():
    pid = input("Enter Patient ID: ").strip().upper()

    if pid not in patients:
        print("Patient not found!")
        return

    records = vitals[pid]

    if len(records) < 3:
        print("At least 3 readings are required!")
        return

    last = records[-3:]

    for r in last:
        print("\nTime:", r["time"])
        print("BP:", r["bp"], "Pulse:", r["pulse"])
        print("Temperature:", r["temp"], "SpO2:", r["spo2"])
        print("Alerts:", len(r["alerts"]))

    first_count = len(last[0]["alerts"])
    last_count = len(last[2]["alerts"])

    if last_count < first_count:
        print("Trend: IMPROVING")
    elif last_count > first_count:
        print("Trend: WORSENING")
    else:
        print("Trend: STABLE")


# 4. View Active Alerts
def view_alerts():
    found = False

    for pid, a in alerts.items():
        if a:
            found = True
            print("\nPatient:", patients[pid]["name"])
            print("Ward:", patients[pid]["ward"])

            for alert in a:
                print("WARNING:", alert)

    if not found:
        print("No active alerts!")


# 5. Shift Handover Summary
def handover():
    print("\n===== SHIFT HANDOVER SUMMARY =====")

    if not patients:
        print("No patients registered!")
        return

    for pid, p in patients.items():
        print("\nPatient ID:", pid)
        print("Name:", p["name"], "Age:", p["age"])
        print("Ward:", p["ward"])

        if vitals[pid]:
            r = vitals[pid][-1]

            print("BP:", r["bp"])
            print("Pulse:", r["pulse"])
            print("Temperature:", r["temp"])
            print("SpO2:", r["spo2"])
            print("Time:", r["time"])

            if r["alerts"]:
                for a in r["alerts"]:
                    print("WARNING:", a)
            else:
                print("No active alerts.")
        else:
            print("No readings available.")

    print("\n===== END OF SUMMARY =====")


# 6. Main Menu
while True:
    print("\n===== VITALWATCH SYSTEM =====")
    print("1. Add Patient")
    print("2. Record Patient Vitals")
    print("3. View Patient Trend")
    print("4. View Active Alerts")
    print("5. Shift Handover Summary")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        record_vitals()
    elif choice == "3":
        view_trend()
    elif choice == "4":
        view_alerts()
    elif choice == "5":
        handover()
    elif choice == "6":
        print("Thank you for using VitalWatch!")
        break
    else:
        print("Invalid choice!")
