import os, requests
SEMANTIC_SCHOLAR_URL = os.getenv('SEMANTIC_SCHOLAR_URL','https://api.semanticscholar.org/graph/v1/paper/search')
DEFAULT_LIMIT = int(os.getenv('SEMANTIC_SCHOLAR_LIMIT','5'))

def search_papers(query, limit=None):
    limit = limit or DEFAULT_LIMIT
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,abstract,url,citationCount,year,authors,doi,venue"
    }
    r = requests.get(SEMANTIC_SCHOLAR_URL, params=params, timeout=15)
    r.raise_for_status()
    data = r.json().get('data', [])
    papers = []
    for p in data:
        papers.append({
            'title': p.get('title'),
            'abstract': p.get('abstract'),
            'url': p.get('url'),
            'citationCount': p.get('citationCount') or 0,
            'year': p.get('year'),
            'authors': [a.get('name') for a in p.get('authors',[])] if p.get('authors') else [],
            'venue': p.get('venue') or ''
        })
    return papers
