import requests
import pandas as pd
import time

# List of domain names
domains = [
"serlogprod-dicv.daimlertruck.com",
"serloguat-dicv.daimlertruck.com",  
  
"ascent.daimler-indiacv.com",
"saleswidget.daimler-indiacv.com",
"dms.i.daimler.com",
"dms.daimler-indiacv.com",
"digitalsupplychain.bharatbenz.com",
"networkportal.bharatbenz.com",
# "part-planning.in365.lia.corpintra.net",
"pbi-int.bharatbenz.com",
"dmsuatbi.daimler-indiacv.com",
"uat-dms.bharatbenz.com",
"ibms.bharatbenz.com",
"diagnostics-proscan.bharatbenz.com",
"diagnostics-proscan-test.bharatbenz.com",
"bbempowerapp.com",
"ckdconnect-trucksasia.daimler.com",
"sra.bharatbenz.com",
"connectedvault.bharatbenz.com",
"uat.bbempowerapp.com",
"connectedvault-prod.bharatbenz.com",
"ibms-qa.bharatbenz.com",
"tlms.bharatbenz.com",
"dmsbi.bharatbenz.com",
"gcc-connect.daimlertruck.com",
"dms2-poc.bharatbenz.com",
"digitalsupplychain-qa.bharatbenz.com",
"dmsvss-uat.bharatbenz.com",
"dmsvss.bharatbenz.com",
"bo-uat.bharatbenz.com",
"bo.bharatbenz.com",
"tcu-test.bharatbenz.com",
"sappo-prod.bharatbenz.com"]

# Qualys SSL Labs API endpoint
api_url = "https://api.ssllabs.com/api/v3/analyze"

# Function to get SSL report
def get_ssl_report(domain):
    try:
        response = requests.get(api_url, params={"host": domain})
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching report for {domain}: {e}")
        return None

# List to store domain ratings
domain_ratings = []

# Function to apply color based on rating
def color_rating(val):
    color = 'white'
    if val == 'A+':
        color = 'green'
    elif val == 'A':
        color = 'lightgreen'
    elif val == 'B':
        color = 'yellow'
    elif val == 'T':
        color = 'red'
    return f'background-color: {color}'

# Loop through each domain
def main():
    for domain in domains:
        print(f"Scanning {domain}...")
        report = get_ssl_report(domain)
        
        if report is None:
            continue
        
        # Wait for the analysis to complete
        while report['status'] not in ['READY', 'ERROR']:
            time.sleep(10)
            report = get_ssl_report(domain)
            if report is None:
                break
        
        if report and report['status'] == 'READY':
            rating = report['endpoints'][0].get('grade', 'N/A')
            domain_ratings.append({"Application": domain, "Qualys Rating": rating})
        else:
            print(f"Error analyzing {domain}: {report.get('statusMessage', 'Unknown error')}")

    # Create a DataFrame
    df = pd.DataFrame(domain_ratings)
    
    # Apply color based on rating
    df_styled = df.style.applymap(color_rating, subset=['Qualys Rating'])
    
    # Save the styled DataFrame as an Excel file
    df_styled.to_excel("domain_ratings.xlsx", index=False)
    print("SSL Qualys Test completed!")

if __name__ == "__main__":
    main()
