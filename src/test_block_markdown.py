import unittest
from block_markdown import (
    markdown_to_blocks, 
    block_type_unordered_list, 
    block_type_code, 
    block_type_quote, 
    block_type_heading, 
    block_type_paragraph,
    block_type_ordered_list, 
    block_to_block_type,
    markdown_to_html_node,
)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_block(self):
        markdown = "This is a single block."
        expected_blocks = ["This is a single block."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_multiple_blocks(self):
        markdown = "This is the first block.\n\nThis is the second block."
        expected_blocks = ["This is the first block.", "This is the second block."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)
    
    def test_excessive_blocks(self):
        markdown = "This is the first block.\n\n\nThis is the second block."
        expected_blocks = ["This is the first block.", "This is the second block."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_empty_block(self):
        markdown = ""
        expected_blocks = []
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_block_with_whitespace(self):
        markdown = "   This block has leading and trailing whitespace.   "
        expected_blocks = ["This block has leading and trailing whitespace."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_block_with_newlines(self):
        markdown = "This block\nhas\nmultiple\nlines."
        expected_blocks = ["This block\nhas\nmultiple\nlines."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    def test_heading_block(self):
            block = "# This is a heading"
            expected_block_type = block_type_heading
            self.assertEqual(block_to_block_type(block), expected_block_type)
        
    def test_code_block(self):
        block = "```python\nprint('Hello, World!')\n```"
        expected_block_type = block_type_code
        self.assertEqual(block_to_block_type(block), expected_block_type)

    def test_quote_block(self):
        block = "> This is a quote"
        expected_block_type = block_type_quote
        self.assertEqual(block_to_block_type(block), expected_block_type)

    def test_unordered_list_block(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        expected_block_type = block_type_unordered_list
        self.assertEqual(block_to_block_type(block), expected_block_type)

    def test_paragraph_block(self):
        block = "This is a paragraph"
        expected_block_type = block_type_paragraph
        self.assertEqual(block_to_block_type(block), expected_block_type)
    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
    
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == '__main__':
    unittest.main()
    