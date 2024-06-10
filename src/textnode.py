text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

from htmlnode import LeafNode, HtmlNode


class TextNode:
    def __init__(self, text: str, text_type: str, url: str=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(node: TextNode) -> LeafNode:
    if node.text_type == text_type_text:
        return LeafNode(node.text)
    
    if node.text_type == text_type_bold:
        return LeafNode(node.text, "b")
    
    if node.text_type == text_type_italic:
        return LeafNode(node.text, "i")
    
    if node.text_type == text_type_code:
        return LeafNode(node.text, "code")
    
    if node.text_type == text_type_link:
        return LeafNode(node.text, "a", {"href": node.url})
    
    if node.text_type == text_type_image:
        return LeafNode(node.text, "img", {"src": node.url, "alt": node.text})
    raise ValueError(f"Invalid text type: {node.text_type}")

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:str) -> list[TextNode]:
    newNodes = []
    for node in old_nodes:
        if node.text_type == text_type_link or node.text_type == text_type_image:
            newNodes.append(node)
            continue
        if node.text.count(delimiter) > 0 and node.text.count(delimiter) % 2 == 0:
            split_nodes = node.text.split(delimiter)
            for i, split_node in split_nodes:
                if split_node != "":
                    if i % 2 == 0:
                        newNodes.append(TextNode(split_node, text_type_text))
                    else:
                        match delimiter:
                            case "`":
                                newNodes.append(TextNode(split_node, text_type_code))
                            case "*":
                                newNodes.append(TextNode(split_node, text_type_italic))
                            case "**":
                                newNodes.append(TextNode(split_node, text_type_bold))
        else:
            raise ValueError("Invalid markdown")
    


