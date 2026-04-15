import os
import re

files = [
    'artigo-humor.html',
    'artigo-relacionamento.html',
    'artigo-borderline.html',
    'artigo-conversas.html',
    'artigo-depressao.html'
]

path = 'c:\\Users\\kamylly\\Documents\\1 coding\\Michelle Aquino'

for filename in files:
    filepath = os.path.join(path, filename)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Use regex to replace whatever is between the quote and "Voltar"
    # Target: class="btn-back">â†  Voltar
    new_content = re.sub(r'class="btn-back">.*?Voltar', 'class="btn-back">← Voltar', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Regex fixed {filename}")
