from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors

def generate_pdf():
    # Create a PDF document
    doc = SimpleDocTemplate("table.pdf", pagesize=letter)

    # Define table data as a nested list
    table_data = [
        ['Patient ID', 'Name', 'Age', 'Gender', 'Condition'],
        ['001', 'Ahmed Mohammed', 30, 'Male', 'Fever'],
        ['002', 'Fatima Ali', 45, 'Female', 'Diabetes'],
        ['003', 'Mohamed Jamal', 55, 'Male', 'High Blood Pressure'],
        ['004', 'Sara Abdullah', 62, 'Female', 'Arthritis'],
        ['005', 'Abdulrahman Youssef', 38, 'Male', 'Headache'],
    ]

    # Create a table object and specify the table data
    table = Table(table_data)

    # Define table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
    ])

    # Apply the table style
    table.setStyle(table_style)

    # Add the table to the PDF document
    elements = [table]
    doc.build(elements)

    print("PDF generated successfully.")

# Call the function to generate the PDF
generate_pdf()
