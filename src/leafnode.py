from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props= None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value == None:
            raise ValueError()
        elif self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'