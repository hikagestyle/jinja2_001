import csv
from jinja2 import Template

source_file = "VLAN.csv"
vlan_template_file = "vlan2.txt"
output_file = "sample.txt"

with open(vlan_template_file) as tf:
    vlan_template = Template(tf.read(), keep_trailing_newline=True)

with open(source_file) as sf:
    reader = csv.DictReader(sf)
    vlan_config = vlan_template.render(csv=reader)

with open(output_file, 'w') as f:
    f.write(vlan_config)

# python3 test_.py
