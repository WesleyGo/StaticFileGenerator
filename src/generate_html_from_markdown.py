import os
from block_markdown import markdown_to_html_node

def extract_title(markdown:str):
    lines = markdown.split("\n")
    for line in lines:
        if line[:2] == "# ":
            return line[2:]
    raise ValueError("No title found")

def generate_page(from_path:str, template_path:str, to_path:str):
    print(f"Generating {to_path} from {from_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()

    node = markdown_to_html_node(markdown)

    html = node.to_html()

    template = template.replace("{{ Title }}", extract_title(markdown))

    template = template.replace("{{ Content }}", html)

    with open(to_path, "w") as f:
        f.write(template)

def generate_page_recursive(from_path:str, template_path:str, to_path:str):
    for item in os.listdir(from_path):
        s = os.path.join(from_path, item)
        d = os.path.join(to_path, item.replace(".md", ".html"))
        if os.path.isdir(s):
            if os.path.exists(d) == False:
                os.mkdir(d)
            
            generate_page_recursive(s, template_path, d)
        else:
            generate_page(s, template_path, d)

    
