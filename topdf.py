import pdfkit
import os

path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

options = {
    'page-size': 'A4',
    'margin-top': '1in',
    'margin-right': '0.75in',
    'margin-bottom': '1in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    "background": True,
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    # "user-style-sheet": r"docs\static\global.css"
    # 'no-outline': None,
    # 'toc': True
}
cover = 'docs/cover.html'
toc = {
    "toc-header-text": "Table of Contents",
    # "disable-dotted-lines": True,
    "toc-level-indentation": "0.15in",
    "toc-text-size-shrink": 0.8,
}
css = r'docs\static\global.css'
input = ['docs/core.html']
input.extend([f"docs/core/{file}" for file in os.listdir('docs/core')])
input.remove('docs/core/base.html')

pdfkit.from_file(
    input=input, 
    output_path='out.pdf', 
    options=options, 
    configuration=config,
    cover=cover,
    toc=toc,
    cover_first=True,
)