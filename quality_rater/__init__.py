import azure.functions as func
import json
from shared.quality_rater import rate_paper

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(json.dumps({'error':'invalid json'}), status_code=400)
    paper = data.get('paper')
    if not paper:
        return func.HttpResponse(json.dumps({'error':'paper required'}), status_code=400)
    score = rate_paper(paper)
    return func.HttpResponse(json.dumps({'quality':score}), mimetype='application/json')
