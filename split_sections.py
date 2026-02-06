#!/usr/bin/env python3
# Extract sections and create standalone HTML files with just that section

from pathlib import Path

with open('Final_analysis_0102.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract head (everything up to closing </head>)
head_end = content.find('</head>')
head_part = content[:head_end + 7]

# Extract body start (from <body> to first <h2>)
body_start = content.find('<body')
body_start = content.find('>', body_start) + 1

# Find all h2 headers and their positions
h2_positions = []
search_pos = 0
while True:
    pos = content.find('<h2>', search_pos)
    if pos == -1:
        break
    h2_positions.append(pos)
    search_pos = pos + 1

# Define sections by their h2 positions
sections = [
    ('section1_data.html', 'Data preparation and processing', h2_positions[0], h2_positions[1] if len(h2_positions) > 1 else None),
    ('section2_infectious.html', 'Infectious Rate Analysis', h2_positions[1], h2_positions[2] if len(h2_positions) > 2 else None),
    ('section3_survival.html', 'Survival Analysis', h2_positions[2], h2_positions[3] if len(h2_positions) > 3 else None),
    ('section4_reproduction.html', 'Host reproduction', h2_positions[3], h2_positions[4] if len(h2_positions) > 4 else None),
    ('section5_lifecycle.html', 'Parasite life-cycle', h2_positions[4], h2_positions[5] if len(h2_positions) > 5 else None),
    ('section6_castration.html', 'Relationship between host castration', h2_positions[5], h2_positions[6] if len(h2_positions) > 6 else len(content)),
]

# Get footer (closing body and html tags)
body_close = content.rfind('</body>')
footer_part = content[body_close:]

for filename, section_name, start_pos, end_pos in sections:
    if end_pos is None:
        end_pos = len(content)
    
    # Extract just this section's content
    section_content = content[start_pos:end_pos]
    
    # Create standalone HTML with head + section + footer
    html = head_part + '\n<body>\n' + section_content + '\n' + footer_part
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Created {filename}")

print("\nDone! All section files created with only their content.")
