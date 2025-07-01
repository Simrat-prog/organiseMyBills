import re
from datetime import datetime

def classify(text):
    text_lower = text.lower()
    if "electricity" in text_lower or "bses" in text_lower:
        bill_type = "electricity"
    elif "water" in text_lower:
        bill_type = "water"
    elif "vodafone" in text_lower or "mobile" in text_lower:
        bill_type = "mobile"
    else:
        bill_type = "others"

    match = re.search(r'(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})', text)
    try:
        bill_date = datetime.strptime(match.group(1), "%d-%m-%Y")
    except:
        bill_date = None

    return bill_type, bill_date
