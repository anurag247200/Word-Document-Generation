# Word-Document-Generation 
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/word-pdf-generator.git
cd word-pdf-generator
Install the required dependencies using pip:

bash
Copy code
pip install python-docx docx2pdf
Usage
Create a Word template (template.docx) with placeholders. The placeholders should be marked like this: {{name}}, {{address}}, {{date}}.

Use the provided Python script (generate_word_pdf.py) to replace these placeholders with actual values and generate a new Word document.

The script will also convert the Word document to a PDF.

Example
Run the script:

bash
Copy code
python generate_word_pdf.py
Output:

A new Word document output.docx will be generated with placeholders replaced.
The Word document will be converted to a PDF named output.pdf.
Sample Template
Here’s a sample template used in the project (placed inside template.docx):

css
Copy code
Name: {{name}}
Address: {{address}}
Date: {{date}}
This file should be in the same directory as the script for it to work correctly.

Code Explanation
The script generate_word_pdf.py consists of the following steps:

Loading the Template: The script loads a Word document (template.docx) using the python-docx library.

Replacing Placeholders: A dictionary of key-value pairs is used to replace the placeholders in the template with actual values.

Saving the Word Document: The modified Word document is saved as output.docx.

Converting to PDF: The docx2pdf library is used to convert output.docx to output.pdf.

License
This project is licensed under the MIT License. See the LICENSE file for details.
