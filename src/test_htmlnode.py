import unittest
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HtmlNode(tag="div", props={"class": "container", "id": "main-div"})
        expected_props = ' class="container" id="main-div"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_no_props(self):
        node = HtmlNode(tag="p", value="Hello, World!")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HtmlNode(tag="span", value="Click me", props={"class": "button"})
        expected_repr = 'HtmlNode(tag="span", value="Click me", children=0, props= class="button")'
        self.assertEqual(repr(node), expected_repr)

    

if __name__ == "__main__":
    unittest.main()