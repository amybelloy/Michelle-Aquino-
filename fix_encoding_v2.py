import os

path = 'c:\\Users\\kamylly\\Documents\\1 coding\\Michelle Aquino'
html_files = [f for f in os.listdir(path) if f.endswith('.html')]

for filename in html_files:
    filepath = os.path.join(path, filename)
    
    # Read as bytes
    with open(filepath, 'rb') as f:
        content = f.read()
    
    # Try to decode as various encodings to find the truth
    try:
        # If it's UTF-8 with BOM, this will remove it
        if content.startswith(b'\xef\xbb\xbf'):
            content = content[3:]
            print(f"Removed BOM from {filename}")
        
        # Decode and re-encode to clean UTF-8
        text = content.decode('utf-8')
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
        print(f"Re-saved {filename} as clean UTF-8")
        
    except UnicodeDecodeError:
        try:
            # Maybe it's Windows-1252?
            text = content.decode('windows-1252')
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                f.write(text)
            print(f"Converted {filename} from Windows-1252 to UTF-8")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
