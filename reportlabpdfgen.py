from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def generate_pdf():
    # Create the PDF object
    p = canvas.Canvas("fichier.pdf", pagesize=letter)

    # Set the font and font size for the header and footer
    p.setFont("Helvetica-Bold", 12)

    # Load and draw the header image
    header_image = "header.png"  # Replace with your own image file
    header_width = 4.5 * inch
    header_height = 1.0 * inch
    header_x = 150
    header_y = 700
    p.drawImage(header_image, header_x, header_y, width=header_width, height=header_height)

    # Draw the left header text with underline
    # left_header_lines = [
     #    "ROYAUME DU MAROC",
    #     "MINISTERE DE LA SANTE ET DE LA",
    #     "PROTECTION SOCIALE",
    #     "INSTITUT SUPERIEUR DES",
    #     "PROFESSIONS INFIRMIERES ET DES"
    # ]
    # header_text_y = header_y - header_height - 20
    # for line in left_header_lines:
    #     line_width = p.stringWidth(line)
    #     line_x = header_x + (header_width - line_width) / 2  # Center the line within the available space
    #     p.drawString(line_x, header_text_y, line)
    #     p.line(line_x, header_text_y - 3, line_x + line_width, header_text_y - 3)  # Draw underline
    #     header_text_y -= 20

    # Load and draw the footer image
    footer_image = "footer.png"  # Replace with your own image file
    footer_width = 2.5 * inch
    footer_height = 0.5 * inch
    footer_x = 200
    footer_y = 20
    p.drawImage(footer_image, footer_x, footer_y, width=footer_width, height=footer_height)

    # Write the form data to the PDF body
    body_x = 100
    body_y = 600
    # Rest of the code for generating the PDF content...
    # Retrieve form data
    nom_prenom = "Abdennacer EL" # request.POST.get('NomPrenom')
    date_entree = "01-06-2023" # request.POST.get('DateEntree')
    date_sortie = "02-06-2023" # request.POST.get('DateSortie')
    admission = "123456" # request.POST.get('Admission')
    service = "Consultation" # request.POST.get('Service')
    motif_hospitalisation = "test" # request.POST.get('Motif')
    compte_rendu_hospitalisation = "test2" # request.POST.get('CompteRendu')
    compte_rendu_operatoire = "test3" # request.POST.get('CompteOperatoire')


    # Write the form data to the PDF
    p.setFont("Helvetica", 14)
    p.drawString(100, 600, f"Nom et prénom du patient: {nom_prenom}")
    p.setFont("Helvetica", 12)
    p.drawString(100, 580, f"Date d'entrée: {date_entree}")
    p.drawString(300, 580, f"Date de sortie: {date_sortie}")
    p.drawString(100, 560, f"N°d'Admission: {admission}")
    p.drawString(300, 560, f"Service: {service}")
    p.drawString(300, 520, f"Objet: PI Confidentiel")
    p.drawString(100, 500, f"Motif d'hospitalisation: {motif_hospitalisation}")
    p.drawString(100, 400, f"Compte rendu d'hospitalisation: {compte_rendu_hospitalisation}")
    p.drawString(100, 350, f"Compte rendu Opératoire: {compte_rendu_operatoire}")
    p.setFont("Helvetica", 10)
    p.drawString(400, 300, f"Signature et cachet du mdecin")

    # Save the PDF
    p.showPage()
    p.save()


# Call the function to generate the PDF
generate_pdf()
