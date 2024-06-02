import re

def clean_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    cleaned_lines = []
    for line in lines:
        # Remove extra commas after the level
        cleaned_line = re.sub(r'([A-Z][0-9]),{2,}', r'\1,', line.strip())
        cleaned_lines.append(cleaned_line)
    
    with open('düzenli.csv', 'w', encoding='utf-8') as file:
        for line in cleaned_lines:
            file.write(line + '\n')

# Provide the path to your dataset file
file_path = 'düzenlenecek.csv'
clean_dataset(file_path)
