import azure.functions as func
import json
from shared.semantic_search import search_papers
from shared.summarizer_core import summarize
from shared.quality_rater import rate_paper
from shared.report_core import build_markdown, markdown_to_pdf
from shared.memory_stub import MemoryStub
mem = MemoryStub()

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(json.dumps({'error':'invalid json'}), status_code=400)
    query = data.get('query','')
    limit = int(data.get('limit',5))
    qid = mem.store_query(query)
    try:
        papers = search_papers(query, limit=limit)
    except Exception as e:
        return func.HttpResponse(json.dumps({'error':'retrieval_failed','details':str(e)}), status_code=500)
    for p in papers:
        p['summary'] = summarize(p.get('title',''), p.get('abstract',''))
        p['quality'] = rate_paper(p)
    md = build_markdown(query, papers)
    pdf_path = markdown_to_pdf(md)
    try:
        with open(pdf_path, 'rb') as fh:
            import base64
            b64 = base64.b64encode(fh.read()).decode('ascii')
    except Exception:
        b64 = ''
    resp = {'query_id': qid, 'papers': papers, 'markdown': md, 'pdf_base64': b64}
    return func.HttpResponse(json.dumps(resp), mimetype='application/json')
