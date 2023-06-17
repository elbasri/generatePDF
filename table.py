from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors

def generate_pdf():
    # Create a PDF document
    doc = SimpleDocTemplate("table.pdf", pagesize=letter)

    # Define table data as nested lists
    patient_data = [
        ['Patient ID', 'Name', 'Age', 'Gender', 'Condition'],
        ['001', 'Ahmed Mohammed', 30, 'Male', 'Fever'],
        ['002', 'Fatima Ali', 45, 'Female', 'Diabetes'],
        ['003', 'Mohamed Jamal', 55, 'Male', 'High Blood Pressure'],
        ['004', 'Sara Abdullah', 62, 'Female', 'Arthritis'],
        ['005', 'Abdulrahman Youssef', 38, 'Male', 'Headache'],
    ]

    appointment_data = [
        ['Appointment ID', 'Date', 'Time', 'Doctor', 'Patient ID'],
        ['101', '2023-06-16', '09:00', 'Dr. Ahmed', '001'],
        ['102', '2023-06-17', '14:30', 'Dr. Fatima', '002'],
        ['103', '2023-06-18', '11:15', 'Dr. Mohamed', '003'],
        ['104', '2023-06-19', '16:45', 'Dr. Sara', '004'],
        ['105', '2023-06-20', '10:30', 'Dr. Abdulrahman', '005'],
    ]

    medication_data = [
        ['Medication ID', 'Name', 'Dosage', 'Frequency', 'Patient ID'],
        ['201', 'Paracetamol', '500 mg', '3 times a day', '001'],
        ['202', 'Insulin', '10 units', 'Once daily', '002'],
        ['203', 'Lisinopril', '10 mg', 'Twice daily', '003'],
        ['204', 'Ibuprofen', '400 mg', 'As needed', '004'],
        ['205', 'Aspirin', '81 mg', 'Once daily', '005'],
    ]

    # Create table objects and specify the table data
    patient_table = Table(patient_data)
    appointment_table = Table(appointment_data)
    medication_table = Table(medication_data)

    # Define table styles
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
    ])

    # Apply the table styles
    patient_table.setStyle(table_style)
    appointment_table.setStyle(table_style)
    medication_table.setStyle(table_style)

    # Add the tables to the PDF document
    elements = [patient_table, appointment_table, medication_table]
    doc.build(elements)

    print("PDF generated successfully.")

# Call the function to generate the PDF
generate_pdf()
