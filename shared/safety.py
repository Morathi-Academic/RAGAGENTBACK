import re
SENSITIVE = ['password','ssn','social security','harm','terror','illegal','bypass']
def validate_query(q: str):
    if not q or not q.strip():
        return False, 'Empty query'
    low = q.lower()
    for s in SENSITIVE:
        if s in low:
            return False, f'Restricted keyword detected: {s}'
    if re.search(r'\b(fuck|shit|bitch)\b', low):
        return False, 'Inappropriate language'
    return True, 'ok'
