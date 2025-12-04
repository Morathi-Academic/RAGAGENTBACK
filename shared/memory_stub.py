import threading, time
_lock = threading.Lock()
STORE = {'queries':[], 'feedback': []}
class MemoryStub:
    def store_query(self, q):
        with _lock:
            qid = len(STORE['queries'])+1
            STORE['queries'].append({'id': qid, 'query': q, 'ts': time.time()})
            return qid
    def store_feedback(self, paper_id, helpful, comment=''):
        with _lock:
            STORE['feedback'].append({'paper_id': paper_id, 'helpful': bool(helpful), 'comment': comment, 'ts': time.time()})
