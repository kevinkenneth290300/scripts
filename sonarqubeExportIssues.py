import requests
import csv

# SonarQube details
sonarqube_url = "https://son.t3.daimlertruck.com/api/issues/search"
project_key = "q"
params = {
    'componentKeys': project_key,
    'statuses': 'OPEN',
    'pageSize': '500'  # Adjust page size as needed
}

# Replace 'your_token' with your actual SonarQube token
headers = {
    'Authorization': f'Bearer squ_cffa1eab1481d8766b2cc72f565712e720fb2a6c'
}

response = requests.get(sonarqube_url, params=params, headers=headers)
issues = response.json().get('issues', [])

# Save issues to a CSV file
with open('sonarqube_issues.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Issue Key', 'Severity', 'Message', 'File', 'Line'])
    for issue in issues:
        writer.writerow([issue['key'], issue['severity'], issue['message'], issue['component'], issue['line']])
