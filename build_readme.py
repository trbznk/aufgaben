import yaml

from glob import glob
from collections import defaultdict

files = glob("*/**/info.yaml")
data = defaultdict(list)

for file in files:
    with open(file) as f:
        info = yaml.load(f)
    problem = file.split("/")[1]

    for tag in info["tags"]:
        data[tag].append(problem)


sorted_tags = sorted(data.keys(), key=lambda k: k)
data = {tag: data[tag] for tag in sorted_tags}


text = """
# Aufgaben

"""

for tag, problems in data.items():
    links = ", ".join([f"[{problem}](all/{problem})" for problem in problems])
    text += f"**{tag}:** {links}"
    text += "\n\n"

with open("README.md", "w") as f:
    f.write(text)
