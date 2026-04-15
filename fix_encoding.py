import os

files = [
    'artigo-humor.html',
    'artigo-relacionamento.html',
    'artigo-borderline.html',
    'artigo-conversas.html'
]

path = 'c:\\Users\\kamylly\\Documents\\1 coding\\Michelle Aquino'

for filename in files:
    filepath = os.path.join(path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to replace the weird sequence with the clean arrow
    new_content = content.replace('â† ', '←')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed {filename}")
