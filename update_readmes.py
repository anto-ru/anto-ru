import re
from pathlib import Path

root = Path(__file__).parent
# readme_files = list(root.glob("README.*.md"))
readme_files = list(root.glob("README.*"))
# readme_files = [f for f in readme_files if f.name != "README.md"]

# Regex per trovare i blocchi INCLUDE completi
pattern = re.compile(
    r"(<!--\s*INCLUDE:\s*(.*?)\s*-->\s*\n?)" +         # gruppo 1: commento INCLUDE
    r"(<!-- START INCLUDE -->\n.*?\n<!-- END INCLUDE -->)",  # gruppo 2: blocco da sostituire
    re.DOTALL
)

for path in readme_files:
    content = path.read_text(encoding="utf-8")

    def replacer(match):
        include_comment = match.group(1)
        file_path = match.group(2).strip()
        include_file = (root / file_path).resolve()

        if not include_file.exists():
            return include_comment + "\n<!-- START INCLUDE -->\n<!-- FILE NOT FOUND -->\n<!-- END INCLUDE -->"

        included_text = include_file.read_text(encoding="utf-8").strip()
        return f"{include_comment}\n<!-- START INCLUDE -->\n{included_text}\n<!-- END INCLUDE -->"

    new_content = pattern.sub(replacer, content)
    path.write_text(new_content, encoding="utf-8")
    print(f"Aggiornato: {path.name}")
