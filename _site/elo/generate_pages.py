import os

script_dir = os.path.dirname(os.path.abspath(__file__))

template_path = os.path.join(script_dir, "team_pages", "template.html")
team_json_dir = os.path.join(script_dir, "team_json")
output_dir = os.path.join(script_dir, "team_pages", "output")

os.makedirs(output_dir, exist_ok=True)

with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

for f in os.listdir(team_json_dir):
    if f.endswith(".json"):
        team_abbr = f.replace(".json", "")
        html_file = os.path.join(output_dir, f"{team_abbr.replace(' ', '-').lower()}.html")
        with open(html_file, "w", encoding="utf-8") as out:
            page_content = template.replace("{{TEAM_ABBR}}", team_abbr)
            out.write(page_content)

print("All team pages generated in:", output_dir)
