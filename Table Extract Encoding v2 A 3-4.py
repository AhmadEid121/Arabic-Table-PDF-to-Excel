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

# Extract tables from the first 3 pages with the specified encoding and lattice option
dfs = tabula.read_pdf(pdf_path, pages='3-14', encoding='utf-8', lattice=True)

# Check if tables were found
if not dfs:
    print("No tables found on the specified pages.")
else:
    # Save the first table from each page to a separate CSV file with UTF-8 encoding
    for i, df in enumerate(dfs):
        df.to_csv(f'page_{i+1}_table.csv', index=False, encoding='utf-8')
        
        # Reshape Arabic text in the table
        reshaped_df = df.applymap(reshape_arabic_text)
        print(reshaped_df)
