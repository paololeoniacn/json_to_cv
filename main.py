from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
import json

def generate_pdf_from_json(json_file, output_pdf):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    doc = SimpleDocTemplate(output_pdf, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()
    
    # Titolo
    title = f"{data['main']['cv']['cvNameSurname']} - {data['main']['occupation']}"
    elements.append(Paragraph(f"<b>{title}</b>", styles['Title']))
    elements.append(Spacer(1, 12))
    
    # Informazioni di contatto
    contact_info = (
        f"Email: {data['main']['cv']['cvMail']} | "
        f"Tel: {data['main']['cv']['cvPhone']} | "
        f"Indirizzo: {data['main']['cv']['cvAddress']}"
    )
    elements.append(Paragraph(contact_info, styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Descrizione personale
    elements.append(Paragraph("<b>Personal Statement</b>", styles['Heading2']))
    elements.append(Paragraph(data['main']['cv']['cvPersonalStatement'], styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Sezioni dinamiche
    sections = {
        "Work Experience": data.get('resume', {}).get('work', []),
        "Education": data.get('resume', {}).get('education', []),
        "Certifications": data.get('certifications', {}).get('certifications', []),
        "Skills": data.get('resume', {}).get('skills', []),
        "Projects": data.get('portfolio', {}).get('projects', [])
    }
    
    for section_title, section_data in sections.items():
        if section_data:
            elements.append(Paragraph(f"<b>{section_title}</b>", styles['Heading2']))
            for item in section_data:
                if isinstance(item, dict):
                    title = item.get('title', item.get('name', ''))
                    description = item.get('description', '')
                    years = item.get('years', '')
                    
                    if isinstance(description, list):
                        description = ' '.join(description)  # Converte liste in stringa unica
                    
                    elements.append(Paragraph(f"<b>{title}</b>", styles['Heading3']))
                    if years:
                        elements.append(Paragraph(f"{years}", styles['Italic']))
                    elements.append(Paragraph(description, styles['Normal']))
                    elements.append(Spacer(1, 12))
    
    # Creazione del PDF
    doc.build(elements)
    print(f"PDF generated successfully: {output_pdf}")

# Esempio di utilizzo
generate_pdf_from_json("resumeData.json", "resume_output.pdf")
