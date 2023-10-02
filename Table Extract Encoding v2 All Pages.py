import tabula
import arabic_reshaper
from bidi.algorithm import get_display
import pandas as pd

# Function to reshape Arabic text
def reshape_arabic_text(text):
    if isinstance(text, str):
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)
    return text

# Set the PDF file path
pdf_path = 'test.pdf'

# Extract tables from page 3 with the specified encoding and lattice option
dfs = tabula.read_pdf(pdf_path, pages='all', encoding='utf-8', lattice=True)

# Check if tables were found
if not dfs:
    print("No tables found on all pages.")
else:
    # Save the first table to a CSV file with UTF-8 encoding
    dfs[0].to_csv('all_tables.csv', index=False, encoding='utf-8')
    
    # Loop through tables and reshape Arabic text
    for df in dfs:
        reshaped_df = df.applymap(reshape_arabic_text)
        print(reshaped_df)
