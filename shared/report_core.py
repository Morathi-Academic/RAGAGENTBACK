import markdown2, os
from markdown2 import markdown
try:
    from weasyprint import HTML
    WEASY = True
except Exception:
    WEASY = False

REPORTS_DIR = os.getenv('REPORTS_DIR','/tmp/reports')
os.makedirs(REPORTS_DIR, exist_ok=True)

def build_markdown(topic, papers):
    md = f"# Research Report: {topic}\n\n"
    md += "|#|Title|Authors|Year|Citations|Quality|URL|\n"
    md += "|--:|--|--|--:|--:|--:|--|\n"
    for i,p in enumerate(papers, start=1):
        authors = ', '.join(p.get('authors',[]))
        md += f"|{i}|{p.get('title','')}|{authors}|{p.get('year','')}|{p.get('citationCount',0)}|{p.get('quality','N/A')}|{p.get('url','')}|\n"
    md += "\n\n"
    for p in papers:
        md += f"## {p.get('title')} ({p.get('year','')})\n\n"
        if p.get('authors'): md += f"**Authors:** {', '.join(p.get('authors',[]))}\n\n"
        md += f"**Citations:** {p.get('citationCount',0)}\n\n"
        md += f"**Quality Score:** {p.get('quality','N/A')} / 5\n\n"
        md += f"**Summary:**\n{p.get('summary','')}\n\n---\n\n"
    return md

def markdown_to_pdf(md, filename=None):
    filename = filename or os.path.join(REPORTS_DIR, f"report_{int(__import__('time').time())}.pdf")
    html = markdown(md)
    if WEASY:
        HTML(string=html).write_pdf(filename)
    else:
        filename = filename.replace('.pdf','.html')
        with open(filename,'w',encoding='utf-8') as fh:
            fh.write(html)
    return filename
