import re

with open('acne-scars.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace specific strings to match 'Acne Scars' context
replacements = [
    (r'Advanced Acne Treatment in Gurgaon', 'Advanced Acne Scars Treatment in Gurgaon'),
    (r'focused acne treatment at', 'focused acne scars treatment at'),
    (r'>Acne Treatment<', '>Acne Scars<'),
    (r'Advanced Acne\s*<br>\s*Treatment', 'Acne Scars<br>Treatment'),
    (r'Understanding Acne <br>& <span', 'Understanding Acne Scars <br>& <span'),
    (r'Acne is more than just', 'Acne scarring is more than just'),
    (r'id="concerns-acne"', 'id="concerns-acne-scars"'),
    (r'#concerns-acne \{', '#concerns-acne-scars {'),
    (r'Hormonal Acne', 'Ice Pick Scars'),
    (r'Cystic Acne', 'Boxcar Scars'),
    (r'Adult Acne', 'Rolling Scars'),
    (r'Comedonal Acne', 'Hypertrophic Scars'),
    (r'Severe Cystic Acne', 'Severe Acne Scarring'),
    (r'Persistent Adult Acne', 'Persistent Acne Scars'),
    (r'balancing acne treatment', 'balancing acne scar treatment'),
    (r'cause of your acne,', 'cause of your acne scars,'),
    (r'Clearing acne is', 'Clearing acne scars is'),
    (r'personalized acne', 'personalized acne scars'),
    (r'specialized acne protocols', 'specialized acne scar protocols'),
    (r'Is the acne treatment painful\?', 'Are acne scar treatments painful?'),
    (r'Most of our acne treatments', 'Most of our acne scar treatments'),
    (r'acne and the body\'s', 'acne scars and the body\'s'),
    (r'Will my acne come back\?', 'Will my acne scars come back?'),
    (r'Post-Acne Scarring', 'Post-Acne Pigmentation')
]

for old, new in replacements:
    content = re.sub(old, new, content, flags=re.IGNORECASE)

with open('acne-scars.html', 'w', encoding='utf-8') as f:
    f.write(content)
