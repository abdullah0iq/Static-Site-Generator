import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    # Test equality for nodes with identical attributes
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    # Test inequality for nodes with different attributes
    def test_not_eq_different_text(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_text_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_url(self):
        node1 = TextNode("This is a text node", TextType.LINK, url="http://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, url="http://different.com")
        self.assertNotEqual(node1, node2)

    # Test the representation method
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_repr = "TextNode(This is a text node, bold, None)"
        self.assertEqual(repr(node), expected_repr)

    # Test with optional URL
    def test_with_url(self):
        node = TextNode("Click here", TextType.LINK, url="http://example.com")
        self.assertEqual(node.text, "Click here")
        self.assertEqual(node.text_type, TextType.LINK)
        self.assertEqual(node.url, "http://example.com")

    # Test without optional URL
    def test_without_url(self):
        node = TextNode("This is normal text", TextType.TEXT)
        self.assertEqual(node.text, "This is normal text")
        self.assertEqual(node.text_type, TextType.TEXT)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()