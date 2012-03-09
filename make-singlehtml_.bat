sphinx-build -b singlehtml -c _ext -d _build/doctree . _build/singlehtml

"C:\Program Files\wkhtmltopdf\wkhtmltopdf.exe" _build/singlehtml/index.html index.pdf