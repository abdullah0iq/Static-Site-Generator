

class HtmlNode():
    def __init__(self, tag=None ,value = None, children = None, props= None):
        self.tag  = tag
        self.value = value
        self.children = children 
        self.props = props

    def add_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:  # Ensure props is not None or empty
            return ""

        prop_list = []
        for k, v in self.props.items():
            prop_list.append(f' {k}="{v}"')  # Add each property in the correct HTML format
        
        return "".join(prop_list)  # Join all properties with a single space
        
    def __repr__(self):
        return (
            f'HtmlNode(tag="{self.tag}", value="{self.value}", '
            f'children={len(self.children) if self.children is not None else 0}'
            f'{(", props="+ self.props_to_html()) if self.props is not None else ("")})'
        )