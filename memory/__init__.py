import azure.functions as func
import json
from shared.memory_stub import MemoryStub
mem = MemoryStub()
def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(json.dumps({'error':'invalid json'}), status_code=400)
    action = data.get('action')
    if action == 'store_query':
        q = data.get('query','')
        qid = mem.store_query(q)
        return func.HttpResponse(json.dumps({'query_id': qid}), mimetype='application/json')
    elif action == 'store_feedback':
        pid = data.get('paper_id')
        helpful = data.get('helpful', True)
        comment = data.get('comment','')
        mem.store_feedback(pid, helpful, comment)
        return func.HttpResponse(json.dumps({'status':'ok'}), mimetype='application/json')
    else:
        return func.HttpResponse(json.dumps({'error':'unknown action'}), status_code=400)
