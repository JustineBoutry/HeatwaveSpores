#!/usr/bin/env python3
# Extract sections from HTML file

with open('Final_analysis_0102.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define sections by line numbers (from grep output)
sections = [
    ('section1_data.html', 1, 579),           # Section 1
    ('section2_infectious.html', 580, 1325),  # Section 2
    ('section3_survival.html', 1326, 1691),   # Section 3
    ('section4_reproduction.html', 1692, 5021), # Section 4
    ('section5_lifecycle.html', 5022, 9026),  # Section 5
    ('section6_castration.html', 9027, 9633), # Section 6
]

# Get header (everything before first h2) and footer (everything after last section)
header_lines = lines[:375]  # Lines before first h2
footer_lines = lines[9634:]  # Lines after last h2

for filename, start, end in sections:
    # Combine: header + section content + footer
    content = header_lines + lines[start-1:end] + footer_lines
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(content)
    print(f"✓ Created {filename}")

print("\nDone! All section files created.")
