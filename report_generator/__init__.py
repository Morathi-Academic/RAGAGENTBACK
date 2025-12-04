import azure.functions as func
import json
from shared.report_core import build_markdown

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(json.dumps({'error':'invalid json'}), status_code=400)
    topic = data.get('topic','Research Report')
    papers = data.get('papers',[])
    md = build_markdown(topic, papers)
    return func.HttpResponse(json.dumps({'markdown':md}), mimetype='application/json')
