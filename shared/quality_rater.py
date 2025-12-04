import math
def citation_score(citations):
    try:
        c = int(citations or 0)
    except:
        c = 0
    return min(1.0, math.log10(c+1)/3.0)

def venue_score(venue):
    if not venue: return 0.5
    v = venue.lower()
    if 'nature' in v or 'science' in v: return 1.0
    if any(x in v for x in ['neurips','icml','iclr','acl','aaai','cvpr']): return 0.95
    if 'arxiv' in v: return 0.4
    return 0.6

def rate_paper(paper):
    c = citation_score(paper.get('citationCount',0))
    v = venue_score(paper.get('venue',''))
    year = paper.get('year') or 0
    recency = 0.5
    try:
        from datetime import datetime
        now = datetime.utcnow().year
        if year >= now-1: recency = 1.0
        elif year >= now-3: recency = 0.8
        else: recency = 0.5
    except:
        recency = 0.5
    score = (0.45*c + 0.35*v + 0.2*recency) * 5
    return round(max(1.0, min(5.0, score)),2)
