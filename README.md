# Morathi-Academic: Full RAG Azure Functions Backend

This repo contains a modular Retrieval-Augmented Generation backend for academic research use.
Functions included:
- orchestrator (master flow)
- retriever (Semantic Scholar)
- summarizer (LLM-backed or fallback)
- quality_rater
- report_generator
- pdf_generator
- verifier
- planner
- memory (simple stub)

Deployment (GitHub -> Azure Functions)
1. Push this repository to GitHub (root must contain host.json and requirements.txt)
2. In Azure Portal -> Function App -> Deployment Center -> choose GitHub, repo, branch main (Linux Python 3.12)
3. Set App Settings (Configuration):
   - AzureWebJobsStorage: <storage connection string>
   - AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT (optional for summaries)
   - SEMANTIC_SCHOLAR_URL (optional)
4. After deployment, call POST /api/orchestrator with JSON: {"query":"your topic","limit":5}

Notes:
- weasyprint is not required; PDF falls back to HTML if not installed on the host.
- The LLM runner tries to use Azure OpenAI if provided, otherwise uses a simple fallback.
