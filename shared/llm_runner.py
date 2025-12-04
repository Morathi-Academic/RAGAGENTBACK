import os
try:
    from azure.ai.openai import OpenAIClient
except Exception:
    OpenAIClient = None

ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
KEY = os.getenv('AZURE_OPENAI_KEY')
DEPLOYMENT = os.getenv('AZURE_OPENAI_DEPLOYMENT')

def openai_available():
    return bool(ENDPOINT and KEY and DEPLOYMENT and OpenAIClient is not None)

class LLMRunner:
    def __init__(self):
        if openai_available():
            self.client = OpenAIClient(ENDPOINT, KEY)
        else:
            self.client = None

    def generate(self, prompt, max_tokens=300, temperature=0.2):
        if not self.client:
            # fallback: simple truncation-based summarization indicator
            return 'LLM_UNAVAILABLE: ' + (prompt[:400])
        # Azure OpenAI SDK uses client.chat_completions.create or similar depending on version
        resp = self.client.chat_completions.create(
            deployment_id=DEPLOYMENT,
            messages=[{'role':'user','content':prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        # defensive access
        try:
            return resp.choices[0].message.content
        except Exception:
            return str(resp)
