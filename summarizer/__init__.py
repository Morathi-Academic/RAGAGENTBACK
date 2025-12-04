import azure.functions as func
import json
from shared.summarizer_core import summarize
from shared.llm_runner import LLMRunner

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(json.dumps({'error':'invalid json'}), status_code=400)
    title = data.get('title','')
    abstract = data.get('abstract','')
    llm = LLMRunner()
    summary = summarize(title, abstract, llm=llm)
    return func.HttpResponse(json.dumps({'summary':summary}), mimetype='application/json')
