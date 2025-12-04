import azure.functions as func
import json
from shared.safety import validate_query

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(json.dumps({'error':'invalid json'}), status_code=400)
    q = data.get('query','')
    ok,msg = validate_query(q)
    if not ok:
        return func.HttpResponse(json.dumps({'error':msg}), status_code=400)
    plan = {'query': q, 'steps': ['retrieve','rate','summarize','report']}
    return func.HttpResponse(json.dumps(plan), mimetype='application/json')
