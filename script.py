import spacy
from spacy.matcher import Matcher
import re
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_name_from_resume(text, nlp):

    # The name is likely the first line of the resume
    first_line = text.split('\n')[0].strip()
    first_line_doc = nlp(first_line)

    # Check if the first line contains a PERSON entity
    for ent in first_line_doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    # If no PERSON entity is found, return the first line as the name
    return first_line

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

def extract_university_from_resume(text):
    university = None
    nlp_blank = spacy.blank("en")
    entity_ruler = nlp_blank.add_pipe("entity_ruler")
    patterns = [{"label": "ORG", "pattern": "NOVA School of Science and Technology"}]
    entity_ruler.add_patterns(patterns)
    doc = nlp_blank(text)

    for entity in doc.ents:
        if entity.label_ == "ORG":
            university = entity.text
            break
    
    return university

def extract_languages_from_resume(text):
    languages = []
    nlp_blank = spacy.blank("en")
    entity_ruler = nlp_blank.add_pipe("entity_ruler")
    patterns = [{"label": "LANGUAGE", "pattern": "English"}, {"label": "LANGUAGE", "pattern": "Portuguese"}]
    entity_ruler.add_patterns(patterns)
    doc = nlp_blank(text)

    for entity in doc.ents:
        if entity.label_ == "LANGUAGE":
            languages.append(entity.text)
    
    return languages


if __name__ == '__main__':
    resume_paths = [r"C:\Users\alvar\OneDrive\Ambiente de Trabalho\My Information\Projects\NER_Resume\Resume.pdf"]
    
    nlp = spacy.load("en_core_web_sm")
    nlp_blank = spacy.blank("en")

    for resume_path in resume_paths:
        text = extract_text_from_pdf(resume_path)

        print("Resume:", resume_path)

        name = extract_name_from_resume(text, nlp)
        if name:
            print("Name:", name)
        else:
            print("Name not found")

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

        university = extract_university_from_resume(text)
        if university:
            print("University:", university)
        else:
            print("University not found")

        languages = extract_languages_from_resume(text)
        if languages:
            print("Languages:", languages)
        else:
            print("Languages not found")
        
        




