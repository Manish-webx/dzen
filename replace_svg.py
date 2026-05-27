import sys, re

def replace_arrow_with_sun(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    sun_svg = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="4"/>
  <path d="M12 2v2"/>
  <path d="M12 20v2"/>
  <path d="m4.93 4.93 1.41 1.41"/>
  <path d="m17.66 17.66 1.41 1.41"/>
  <path d="M2 12h2"/>
  <path d="M20 12h2"/>
  <path d="m6.34 17.66-1.41 1.41"/>
  <path d="m19.07 4.93-1.41 1.41"/>
</svg>'''

    # Pattern to match ANY svg that contains ONLY the arrow path
    pattern = re.compile(r'<svg[^>]*>\s*<path\s+d="M5\s+12h14M12\s+5l7\s+7-7\s+7"\s*/>\s*</svg>', re.IGNORECASE)
    
    new_content, count = pattern.subn(sun_svg, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Replaced {count} instances in {filepath}')

replace_arrow_with_sun('index.html')
replace_arrow_with_sun('index1.html')
