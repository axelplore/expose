import os

input_commands = [
    "1 Einleitung",
    "11 Motivation und Problemstellung",
    "12 Zielsetzung und Forschungsfrage",
    "13 Methodik und Untersuchungsgegenstand",
    "14 Aufbau der Arbeit",
    "2 Theoretischer Rahmen",
    "21 Methode bei der Literaturrecherche",
    "22 Künstliche Intelligenz und NLP in Unternehmen",
    "23 Microsoft 365 Copilot",
    "24 Das Unternehmen und das Pilotprojekt",
    "25 Aktuelle Herausforderungen und Forschungslücken",
    "3 Methodik",
    "31 Forschungsdesign",
    "32 Zielgruppe der Befragung",
    "33 Datenerhebungsmethode",
    "4 Durchführung der Expertenbefragung",
    "41 Interviews",
    "42 Interviewentwicklung",
    "5 Analyse der Ergebnisse",
    "6 Diskussion",
    "61 Interpretation der Ergebnisse",
    "62 Kritische Reflexion der Ergebnisse im Vergleich zur Literatur",
    "63 Diskussion der Methodik",
    "64 Vergleich zu anderen Branchen",
    "65 Forschungsperspektiven",
    "7 Fazit"
]

for filename in input_commands:
    # Create a valid filename by replacing spaces with underscores
    valid_filename = filename.replace(" ", "_") + ".tex"
    
    # Create the file
    with open(valid_filename, 'w') as f:
        f.write(f"% Content for {filename}\n")
    
    print(f"Created file: {valid_filename}")

print("All files have been created successfully.")