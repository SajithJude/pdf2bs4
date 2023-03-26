import PyPDF2
from bs4 import BeautifulSoup
import streamlit as st


uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # pdf_doc = fitz.open(stream=uploaded_file.getvalue(), filetype="pdf")
    
# # Open the PDF file
# with open('example.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)

    # Create a BeautifulSoup object to store the XML
    soup = BeautifulSoup(features='lxml')

    # Create a new XML element to store the table of contents
    toc_element = soup.new_tag('toc')
    pages = []

    # Loop through the pages in the PDF
    for page_num in range(num_pages):
        # Get the page object
        page = pdf_reader.pages[page_num]

        # Extract the text from the page
        page_text = page.extract_text()

        # Create a new XML element to store the page content
        page_elem = {'page': []}

        # Split the text into paragraphs
        paragraphs = page_text.split('\n\n')

        # Skip the first three paragraphs (or lines) on each page
        for i in range(3, len(paragraphs)):
            # Strip any leading or trailing whitespace
            paragraph = paragraphs[i].strip()

            # Create a new paragraph element
            para_elem = {'para': []}

            # Check if the paragraph is a heading
            if paragraph.startswith("D:\Bank-17Sep"):
                # Add the heading level to the element
                level = paragraph.count(' ') + 1
                para_elem['para'].append(('heading', level))

                # Add the heading text to the element
                text = paragraph.lstrip('0123456789. ')
                para_elem['para'].append(('text', text))
            else:
                # Add the paragraph text to the element
                para_elem['para'].append(('text', paragraph))

            # Add the paragraph element to the page element
            page_elem['page'].append(para_elem)

        # Add the page element to the container
        pages.append(page_elem)

# Output the result as XML
        xml_str = '<pages>'
        for page in pages:
            xml_str += str(page)
        xml_str += '</pages>'
        st.write(xml_str)
