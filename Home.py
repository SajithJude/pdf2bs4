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

    # Loop through the pages in the PDF
    for page_num in range(num_pages):
        # Get the page object
        page = pdf_reader.pages[page_num]

        # Extract the text from the page
        page_text = page.extractText()

        # Create a new XML element to store the page content
        page_element = soup.new_tag('page', number=page_num)

        # Add the page content to the XML element
        page_element.string = page_text

        # Add the page element to the table of contents
        toc_element.append(page_element)

    # Add the table of contents to the XML
    soup.append(toc_element)

# Save the XML to a file
# with open('example.xml', 'w') as xml_file:
    st.write(str(soup))
