# VitalWatch – Patient Vitals Monitoring and Early-Alert System

## 1. About the Project

VitalWatch is a Python-based, console application designed to monitor patient vital signs and identify readings that fall outside predefined example thresholds.

The system allows users to register patients, record their vital signs, generate alerts, view basic trends, and prepare ward shift handover summaries.

## 2. Objectives

- To record and monitor patient vital signs.
- To identify abnormal readings using predefined thresholds.
- To generate alerts when readings cross those thresholds.
- To display basic trends using the latest three readings.
- To provide a summary of patient information during shift handovers.

## 3. Features

1. **Add Patient:** Register patients using their ID, name, age, and ward.
2. **Record Patient Vitals:** Record blood pressure, pulse, temperature, SpO2, and timestamp.
3. **View Patient Trend:** Compare the last three readings and display a basic trend.
4. **View Active Alerts:** Display patients with alerts from their latest readings.
5. **Shift Handover Summary:** Display patient details, latest vitals, and active alerts.

## 4. Technologies Used

- Python
- VS Code
- Git
- GitHub

## 5. Project Structure

```text
VitalWatch/
│
├── main.py
├── .gitignore
└── README.md
```

## 6. How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/chaitrashetty979/VitalWatch.git
```

### Step 2: Open the project folder

```bash
cd VitalWatch
```

### Step 3: Run the application

```bash
python main.py
```

## 7. How to Use

1. Run the Python program.
2. Select an option from the main menu.
3. Add a patient before recording their vitals.
4. Enter patient vital readings.
5. View alerts and trends.
6. Generate a shift handover summary.
7. Select Exit to close the application.

## 8. Future Enhancements

- Store patient records permanently using a database.
- Add a graphical user interface.
- Generate detailed patient reports.
- Improve trend analysis using more advanced methods.
- Add secure login and user authentication.

## 9. Important Note

VitalWatch is an educational project. Its thresholds and alerts are examples for demonstration and are not intended for clinical diagnosis or treatment decisions. The application stores data in memory, so records are lost when the program exits.

## 10. Author

Developed as an academic project using Python.