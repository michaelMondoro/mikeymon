import re

class MarkdownProcessor:
    def __init__(self):
        self.data = None
        self.chunks = []

    def load(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
        self.chunks = data.split("```")
        self.data = data
    
    def process_bold(self, line):
        bolds = re.findall("\*\*.*\*\*", line)
        for bold in bolds:
            tag = bold.replace("**", "<b>",1).replace("**", "</b>")
            line = line.replace(bold, tag)
        return line 
    
    def process_strong(self, line):
        strongs = re.findall("__.*__", line)
        for strong in strongs:
            tag = strong.replace("__", "<strong>").replace("__", "</strong>")
            line = line.replace(strong, tag)
        return line 

    def process_links(self, line):
        links = re.findall("\[.*\]\(.*\)", line)
        for link in links:
            url = re.findall("\(.*\)", link)[0].strip("(").strip(")")
            txt = re.findall("\[.*\]", link)[0].strip("[").strip("]")
            line = line.replace(link, f"<a href='{url}'>{txt}</a>")
        return line
    
    def process_heading(self, line):
        for i in range(1, 7):
            heading = "#"*i
            if line.startswith(f"{heading} "):
                return line.replace(f"{heading} ", f"<h{i}>") + f"</h{i}>"
        return line

    def process_code(self, line):
        code = re.findall("`.*`", line)
        for c in code:
            line = line.replace("`", "<code>", 1).replace("`", "</code>")
        return line
    
    def process_img(self, line):
        imgs = re.findall("!\[.*\]\(.*\)", line)
        for img in imgs:
            url = re.findall("\(.*\)", img)[0].strip("(").strip(")")
            txt = re.findall("\[.*\]", img)[0].strip("[").strip("]")
            line = line.replace(img, f"<img src='{url}' alt='{txt}'>")

        return line
    def convert_line(self, line):
        line = line.strip()
        if line.startswith("#"):
            return self.process_heading(line)
        
        line = self.process_bold(line)
        line = self.process_strong(line)
        line = self.process_img(line)
        line = self.process_links(line)
        line = self.process_code(line)
        # Default normal text
        return f"<p>{line}</p>"

    def convert(self):
        data = ""
        for i, chunk in enumerate(self.chunks):
            chunk = chunk.strip()
            if (i % 2 != 0):
                data += f"<pre>\n{chunk}\n</pre>\n"
            elif (len(chunk) > 0):
                for c in chunk.split("\n\n"):
                    data += self.convert_line(c) + "\n"
        return data
