
from MarkdownProcessor import MarkdownProcessor
import os
from datetime import datetime

if __name__=="__main__":
    # Process markdown and generate html
    proc = MarkdownProcessor()
    links = "<links>"

    for file in sorted(os.listdir('markdown')):
        data = ""
        if file.endswith('.md'):
            filename = file.replace(".md", ".html")
            timestamp = datetime.strptime(file.split("-")[0], "%m_%d_%Y")
            timestamp = timestamp.strftime("%b %d, %Y")

            proc.load(f"markdown/{file}")
            html = proc.convert()
            data += f"<article data-timestamp='{timestamp}'>\n{html}\n</article><hr>\n"
            
            with open('template.html', 'r') as f:
                template = f.read()
                template = template.replace("static/", "../")
                updated = template.replace("#CONTENT#", data)

            with open(f"static/articles/{filename}", 'w') as f:
                f.write(updated)
            
            links += f"<a href='static/articles/{filename}'>{filename}</a>\n"
    links += "</links>"

    if len(links) <= 16:
        links = f"<div>nothing here right now</div>"
    # move html data into index.html template
    with open('template.html', 'r') as f:
        template = f.read()
        with open('index.html', 'w') as f:
            updated = template.replace("#CONTENT#", links)
            f.write(updated)