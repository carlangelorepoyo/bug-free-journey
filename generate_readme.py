import json
from jinja2 import Template

# Load data from JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Load Jinja2 template
with open('template.md', 'r') as template_file:
    template_content = template_file.read()

# Render template with data
template = Template(template_content)
rendered_content = template.render(data=data)

# Write rendered content to README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(rendered_content)
