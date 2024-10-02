import os

subsections = [
    ("11", "Motivation und Problemstellung"),
    ("12", "Zielsetzung und Forschungsfrage"),
    ("13", "Methodik und Untersuchungsgegenstand"),
    ("14", "Aufbau der Arbeit"),
    ("21", "Methode bei der Literaturrecherche"),
    ("22", "Künstliche Intelligenz und NLP in Unternehmen"),
    ("23", "Microsoft 365 Copilot"),
    ("24", "Das Unternehmen und das Pilotprojekt"),
    ("25", "Aktuelle Herausforderungen und Forschungslücken"),
    ("31", "Forschungsdesign"),
    ("32", "Zielgruppe der Befragung"),
    ("33", "Datenerhebungsmethode"),
    ("41", "Interviews"),
    ("42", "Interviewentwicklung"),
    ("61", "Interpretation der Ergebnisse"),
    ("62", "Kritische Reflexion der Ergebnisse im Vergleich zur Literatur"),
    ("63", "Diskussion der Methodik"),
    ("64", "Vergleich zu anderen Branchen"),
    ("65", "Forschungsperspektiven")
]

# Change to the parent directory
# os.chdir('..')

for number, name in subsections:
    # Create a valid filename
    filename = f"{number}_{name.replace(' ', '_')}.tex"
    
    # Create the file content
    content = f"""% !TeX root=main.tex
\\subsection{{{name}}}
\\label{{subsec:{number}}}
"""
    
    # Create the file and write the content
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created file: {filename}")

print("All subsection files have been created successfully.")