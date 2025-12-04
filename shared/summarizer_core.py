from .llm_runner import LLMRunner

def summarize(title, abstract, llm=None):
    if not abstract or abstract.strip()=='':
        return 'No abstract available.'
    if llm is None:
        llm = LLMRunner()
    if llm.client is None:
        text = abstract.strip()
        s = text.split('. ')
        summary = '. '.join(s[:3])
        return summary + ('...' if len(s)>3 else '')
    prompt = f"Summarize the following academic abstract in 3 concise sentences.\nTitle: {title}\nAbstract: {abstract}\nSummary:"
    return llm.generate(prompt, max_tokens=200, temperature=0.1)
