block_type_heading = "heading"
block_type_paragraph = "paragraph"
block_type_unordered_list = "unordered list"
block_type_code = "code"
block_type_quote = "quote"
block_type_ordered_list = "ordered list"

from textnode import text_node_to_html_node, text_type_text, TextNode
from htmlnode import HtmlNode, ParentNode
from inline_markdown import text_to_textnodes

def markdown_to_blocks(markdown:str) -> list[str]:
    blocks = []
    for block in markdown.split("\n\n"):
        if block.strip() != "":
            blocks.append(block.strip())
    return blocks

def block_to_block_type(block:str) -> str:
    if block[0] == "#":
        return block_type_heading
    if block[:3] == "```":
        return block_type_code
    if block[0] == ">":
        return block_type_quote
    if block[0] == "-" or block[0] == "*":
        return block_type_unordered_list
    if block[0].isdigit():
        return block_type_ordered_list
    
    return block_type_paragraph

def remove_new_line_and_join(block:str) -> str:
    return " ".join(block.split("\n"))

def block_to_html_node(block:str) -> HtmlNode:
    block_type = block_to_block_type(block)

    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    elif block_type == block_type_heading:
        return header_to_html_node(block)
    elif block_type == block_type_quote:
        return quote_to_html_node(block)
    elif block_type == block_type_code:
        return code_to_html_node(block)
    elif block_type == block_type_unordered_list:
        return unordered_list_to_html_node(block)
    elif block_type == block_type_ordered_list:
        return ordered_list_to_html_node(block)
    
def text_to_children(nodes:list[TextNode]) -> list[HtmlNode]:
    children = []
    for text_node in nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def header_to_html_node(block):
    header_level: int = block.split()[0].count("#")
    header_slice = block[header_level+1:]
    content = remove_new_line_and_join(header_slice)
    childNodes = text_to_textnodes(content)
    children = text_to_children(childNodes)
    return ParentNode(children, f"h{header_level}")

def paragraph_to_html_node(block:str) -> HtmlNode:
    content = remove_new_line_and_join(block)
    childNodes = text_to_textnodes(content)
    children = text_to_children(childNodes)
    return ParentNode(children, "p")

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    childNodes = text_to_textnodes(" ".join(new_lines))
    children = text_to_children(childNodes)
    return ParentNode(children, "blockquote")

def code_to_html_node(block:str) -> HtmlNode:
    content = remove_new_line_and_join(block[3:-3])
    childNodes = text_to_textnodes(content)
    children = text_to_children(childNodes)
    return ParentNode(children, "code")

def unordered_list_to_html_node(block:str) -> HtmlNode:
    children = []
    for item in block.split("\n"):
        childNodes = text_to_textnodes(item[2:])
        childHtml = text_to_children(childNodes)
        children.append(ParentNode(childHtml, "li"))
            
    return ParentNode(children, "ul")

def ordered_list_to_html_node(block:str) -> HtmlNode:
    children = []
    for item in block.split("\n"):
        childNodes = text_to_textnodes(item[3:])
        childHtml = text_to_children(childNodes)
        children.append(ParentNode(childHtml, "li"))
    return ParentNode(children, "ol")
   
def markdown_to_html_node(markdown:str) -> HtmlNode:
    blocks = markdown_to_blocks(markdown)
    children: list[HtmlNode] = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode(children, "div")