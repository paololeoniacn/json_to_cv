# JSON to PDF Generator

## Overview
This Python script reads a JSON file containing resume data and generates a well-formatted PDF document. It structures the information into sections like **Personal Information**, **Work Experience**, and **Certifications**, ensuring a clean and professional layout.

## Features
- **Reads structured resume data** from a JSON file.
- **Formats the PDF** with sections, headings, and spacing for clarity.
- **Dynamically supports multiple sections**, ensuring flexibility in the resume format.
- **Uses ReportLab** for PDF generation.

## Installation
To run this script, install the required dependencies using:

```bash
pip install reportlab
```

## Usage
Run the script by executing:

```bash
python generate_resume_pdf.py
```

Ensure that the JSON file (`resumeData.json`) is in the same directory or specify its path.

## JSON Structure
The script expects the JSON file to have the following structure:

```json
{
    "main": {
        "cv": {
            "cvNameSurname": "John Doe",
            "cvMail": "john.doe@example.com",
            "cvPhone": "+1234567890",
            "cvAddress": "City, Country",
            "cvPersonalStatement": "Passionate about software architecture and AI."
        }
    },
    "certifications": {
        "certifications": [
            {
                "title": "AWS Certified Solutions Architect",
                "description": "Understanding of AWS services and cloud architecture."
            }
        ]
    },
    "resume": {
        "work": [
            {
                "company": "TechCorp",
                "title": "Senior Software Engineer",
                "years": "2020 - Present",
                "description": "Developing AI-driven solutions for enterprise clients."
            }
        ]
    }
}
```

## Output
The script generates a `resume_output.pdf` file containing:
- Name, Email, Phone, Address
- Personal Statement
- Work Experience
- Certifications

## Customization
- Modify the JSON structure to include additional sections.
- Adjust styles and formatting by modifying the ReportLab styles in the script.

## License
This script is open-source and can be modified as needed.
