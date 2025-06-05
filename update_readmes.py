import re
from pathlib import Path

# Percorso base del progetto
root = Path(__file__).parent

# File README da processare (escludiamo README.md "principale")
readme_files = list(root.glob("README.*.md"))
readme_files = [f for f in readme_files if f.name != "README.md"]

# Pattern per cercare <!-- INCLUDE: path/to/file.md -->
include_pattern = re.compile(r"<!--\s*INCLUDE:\s*(.*?)\s*-->")

for readme_path in readme_files:
    content = readme_path.read_text(encoding="utf-8")

    def replace_include(match):
        include_path = root / match.group(1).strip()
        if include_path.exists():
            return include_path.read_text(encoding="utf-8").strip()
        else:
            return f"<!-- FILE NOT FOUND: {include_path} -->"

    new_content = include_pattern.sub(replace_include, content)

    # Sovrascrive il file con il contenuto aggiornato
    readme_path.write_text(new_content, encoding="utf-8")
    print(f"Aggiornato: {readme_path.name}")
