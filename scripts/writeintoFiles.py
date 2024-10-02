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
parent_dir = 'C:\Users\asa06\Documents\Bachelor'
os.chdir(parent_dir)

print(f"Changed to directory: {os.getcwd()}")

for number, name in subsections:
    # Create the filename based on the existing pattern
    filename = f"{number}_{name.replace(' ', '_')}.tex"
    
    # Check if the file exists
    if os.path.exists(filename):
        # Create the content to be written
        content = f"""% !TeX root=main.tex
\\subsection{{{name}}}
\\label{{subsec:{number}}}

"""
        
        # Read the existing content
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()
        
        # Combine new content with existing content
        full_content = content + existing_content
        
        # Write the combined content back to the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"Updated file: {filename}")
    else:
        print(f"Warning: File not found: {filename}")

print("All existing subsection files have been updated successfully.")