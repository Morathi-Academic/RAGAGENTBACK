import azure.functions as func
import json
from shared.semantic_search import search_papers

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(json.dumps({'error':'invalid json'}), status_code=400)
    q = data.get('query')
    limit = data.get('limit',5)
    try:
        papers = search_papers(q, limit=limit)
    except Exception as e:
        return func.HttpResponse(json.dumps({'error':str(e)}), status_code=500)
    return func.HttpResponse(json.dumps({'papers':papers}), mimetype='application/json')
