import spacy
from spacy.matcher import Matcher
import re
from pdfminer.high_level import extract_text




def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_contact_number_from_resume(text):
    contact_number = None

    pattern = r"(9[1236]\d) ?(\d{3}) ?(\d{3})"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()
    
    return contact_number

def extract_email_from_resume(text):
    email = None

    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    match = re.search(pattern, text)
    if match:
        email = match.group()
    
    return email

def extract_linkedIn_profile_from_resume(text):
    linkedIn_profile = None

    pattern = r"(?:(?:https?://)?(?:www\.)?linkedin\.com/in/([A-Za-z0-9\u00C0-\u00FF\.\-_]+))"
    match = re.search(pattern, text)
    if match:
        linkedIn_profile = match.group()
    
    return linkedIn_profile

def extract_summary_from_resume(text):
    summary = None

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    for entity in doc.ents:
        if entity.label_ == "PERSON":
            summary = entity.text
            break
    
    return summary




if __name__ == '__main__':
    resume_paths = [r"C:\Users\alvar\OneDrive\Ambiente de Trabalho\My Information\Projects\NER_Resume\Resume.pdf"]

    for resume_path in resume_paths:
        text = extract_text_from_pdf(resume_path)

        print("Resume:", resume_path)

        #print(text)

        contact_number = extract_contact_number_from_resume(text)
        if contact_number:
            print("Contact Number:", contact_number)
        else:
            print("Contact Number not found")

        email = extract_email_from_resume(text)
        if email:
            print("Email:", email)
        else:
            print("Email not found")

        linkedIn_profile = extract_linkedIn_profile_from_resume(text)
        if linkedIn_profile:
            print("LinkedIn Profile:", linkedIn_profile)
        else:
            print("LinkedIn Profile not found")

        