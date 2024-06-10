class HtmlNode:
    def __init__(self, tag: str = None, value: str = None, children = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if self.props == None:
            return ""
        html = " "
        for key, value in self.props.items():
            html += f"{key}=\"{value}\" "
        return html.rstrip()
    
    def __repr__(self) -> str:
        return f"tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}"

class LeafNode(HtmlNode):
    def __init__(self, value: str, tag: str = None, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HtmlNode):
    def __init__(self, children: list[HtmlNode], tag: str = None, props: dict = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("tag not provided")
        if self.children == None:
            raise ValueError("no child nodes")
        html = f"<{self.tag}{self.props_to_html()}>"

        for i in self.children:
            html += i.to_html()
        
        html += f"</{self.tag}>"

        return html
        
        
        
