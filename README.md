# Arabic-Table-PDF-to-Excel
# PDF Table Extraction with Arabic Text

This Python script demonstrates how to extract tables from a PDF file containing Arabic text and reshape the Arabic text using the `arabic-reshaper` library.

## Dependencies

Before running the script, make sure you have the following dependencies installed:

- [tabula-py](https://pypi.org/project/tabula-py/): A Python library for extracting tables from PDFs.
- [arabic-reshaper](https://pypi.org/project/arabic-reshaper/): A Python library for reshaping Arabic text.
- [python-bidi](https://pypi.org/project/python-bidi/): A Python library for handling bidirectional text.

You can install these dependencies using `pip`:

```bash
pip install tabula-py arabic-reshaper python-bidi

Usage
1. Clone this repository or download the script to your local machine.

2. Make sure you have a PDF file (test.pdf) containing tables with Arabic text.

3. Modify the pdf_path variable in the script to point to your PDF file:
pdf_path = 'test.pdf'

4. Run the script:
python extract_tables.py
 5. The script will extract tables from the PDF and save the first table to a CSV file named first_table.csv with reshaped Arabic text.

Options
You can customize the page range to extract tables from specific pages by modifying the pages parameter in the script.

If you encounter issues with table extraction, you can experiment with different tabula-py options and settings, such as the lattice option.

Feedback and Contributions
If you find issues or have suggestions for improvements, please open an issue or create a pull request in this repository.

Happy PDF table extraction!


Author
Eng. Ahmad Eid
GitHub: github.com/AhmadEid121
