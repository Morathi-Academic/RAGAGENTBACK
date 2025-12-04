import azure.functions as func
import json, requests
from shared.utils import make_paper_id

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(json.dumps({'error':'invalid json'}), status_code=400)
    paper = data.get('paper')
    if not paper:
        return func.HttpResponse(json.dumps({'error':'paper required'}), status_code=400)
    url = paper.get('url')
    reachable = False
    try:
        if url:
            r = requests.head(url, timeout=8)
            reachable = (200 <= r.status_code < 400)
    except:
        reachable = False
    pid = make_paper_id(paper)
    return func.HttpResponse(json.dumps({'paper_id':pid,'reachable':reachable}), mimetype='application/json')
