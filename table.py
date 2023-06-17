from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf():
    # Create a PDF document
    doc = SimpleDocTemplate("table.pdf", pagesize=letter)

    # Define table data as nested lists
    patient_data = [
        ['ID Patient', 'Nom', 'Âge', 'Sexe', 'Condition'],
        ['001', 'Ahmed Mohammed', 30, 'Homme', 'Fièvre'],
        ['002', 'Fatima Ali', 45, 'Femme', 'Diabète'],
        ['003', 'Mohamed Jamal', 55, 'Homme', 'Hypertension artérielle'],
        ['004', 'Sara Abdullah', 62, 'Femme', 'Arthrite'],
        ['005', 'Abdulrahman Youssef', 38, 'Homme', 'Maux de tête'],
    ]

    doctor_data = [
        ['ID Médecin', 'Nom', 'Spécialité', 'Expérience'],
        ['D001', 'Dr. Ahmed Hassan', 'Cardiologie', '10 ans'],
        ['D002', 'Dr. Fatima Khalid', 'Pédiatrie', '8 ans'],
        ['D003', 'Dr. Mohamed Ali', 'Dermatologie', '15 ans'],
        ['D004', 'Dr. Sara Mahmoud', 'Orthopédie', '12 ans'],
        ['D005', 'Dr. Abdullah Khalil', 'Neurologie', '6 ans'],
    ]

    # Create a table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Create table objects and specify the table data and style
    patient_table = Table(patient_data)
    patient_table.setStyle(table_style)

    doctor_table = Table(doctor_data)
    doctor_table.setStyle(table_style)

    # Add the tables to the PDF document
    elements = [Paragraph("Données des Patients", style=getSampleStyleSheet()['Heading1']), patient_table,
                Paragraph("Données des Médecins", style=getSampleStyleSheet()['Heading1']), doctor_table]
    doc.build(elements)

    print("PDF generated successfully.")

# Call the function to generate the PDF
generate_pdf()
