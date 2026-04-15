import os

# Map of common UTF-8 characters interpreted as Latin-1/Windows-1252
fix_map = {
    'Ã³': 'ó',
    'Ã­': 'í',
    'Ãª': 'ê',
    'Ã©': 'é',
    'Ã¡': 'á',
    'Ã ': 'à',
    'Ã§': 'ç',
    'Ã£': 'ã',
    'Ã±': 'ñ', # Just in case
    'Ãš': 'Ú',
    'Ãº': 'ú',
    'Ã ': 'à',
    'Ã€': 'À',
    'Ã‚': 'Â',
    'Ã¢': 'â',
    'Ã‰': 'É',
    'ÃŠ': 'Ê',
    'Ã ': 'í',
    'Ã ': 'í',
}

path = 'c:\\Users\\kamylly\\Documents\\1 coding\\Michelle Aquino'
html_files = [f for f in os.listdir(path) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(path, filename)
    
    # Read as binary to avoid encoding issues during reading
    with open(filepath, 'rb') as f:
        content = f.read()
    
    # Check if the file is UTF-8 encoded but contains these literal "corrupted" strings
    # or if we need to decode it first.
    # Often, the simplest way is to decode as utf-8 and then replace.
    try:
        text = content.decode('utf-8')
        modified = False
        for corrupted, fixed in fix_map.items():
            if corrupted in text:
                text = text.replace(corrupted, fixed)
                modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Fixed encoding in {filename}")
        else:
            print(f"No corruption found in {filename}")
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")
