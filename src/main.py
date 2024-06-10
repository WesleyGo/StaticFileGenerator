import os
import shutil
from copy_static import copy_directory
from generate_html_from_markdown import generate_page_recursive

PUBLIC_DIR = "public"
STATIC_DIR = "static"
CONTENT = "content"
TEMPLATE = "template.html"
DESTINATION = "public"
  
def main():
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)

    os.makedirs(PUBLIC_DIR)

    copy_directory(STATIC_DIR, PUBLIC_DIR)

    generate_page_recursive(CONTENT, TEMPLATE, DESTINATION)

main()