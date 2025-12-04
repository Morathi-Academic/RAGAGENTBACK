import azure.functions as func
import json, base64
from shared.report_core import markdown_to_pdf

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(json.dumps({'error':'invalid json'}), status_code=400)
    md = data.get('markdown','')
    if not md:
        return func.HttpResponse(json.dumps({'error':'markdown required'}), status_code=400)
    try:
        path = markdown_to_pdf(md)
        with open(path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('ascii')
        return func.HttpResponse(json.dumps({'pdf_base64': b64}), mimetype='application/json')
    except Exception as e:
        return func.HttpResponse(json.dumps({'error':str(e)}), status_code=500)
