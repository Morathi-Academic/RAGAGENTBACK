import hashlib
def make_paper_id(p):
    key = (p.get('title') or '') + '|' + (p.get('url') or '')
    return hashlib.sha256(key.encode('utf-8')).hexdigest()
