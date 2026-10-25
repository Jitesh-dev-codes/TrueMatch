import re
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + " "
        return text
    except Exception as e:
        print(f"PDF reading failed: {e}")
        return None

def calculate_match_score(resume_text, job_description):
    if not resume_text or not job_description:
        return 0
        
    def get_word_set(text):
        # Keep only alphabets and convert to lowercase for accurate matching
        cleaned = re.sub(r'[^a-zA-Z\s]', '', text).lower()
        # Using sets automatically removes duplicate words
        return set(cleaned.split())

    resume_words = get_word_set(resume_text)
    job_words = get_word_set(job_description)

    if not job_words:
        return 0

    matched_words = resume_words.intersection(job_words)
    score = (len(matched_words) / len(job_words)) * 100
    
    return round(score, 2)