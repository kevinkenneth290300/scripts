import re
import json

log_file_path = "prof.log"
result = {}

with open(log_file_path, "r") as file:
    for line in file:
        matches = re.findall(r'(\w+)=([^ ]+)', line)
        if matches:
            result.update(dict(matches))

json_output = json.dumps(result, indent=4)
print(json_output)
