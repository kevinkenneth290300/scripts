import pdfkit
import pandas as pd
import time
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Path to wkhtmltopdf executable
path_wkhtmltopdf = r"C:\\Users\\KevinKennethPakkiado\\Downloads\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# List of domain names
domains = [
    # "sappo-prod.bharatbenz.com",
    # "part-planning.in365.lia.corpintra.net",
    # "pbi-int.bharatbenz.com",
    # "dms.i.daimler.com",
    # "sra.bharatbenz.com",
    # "bbempowerapp.com",
    # "dmsuatbi.daimler-indiacv.com",

    # No Issue URI
    "ascent.daimler-indiacv.com",
    "saleswidget.daimler-indiacv.com",
    "dms.daimler-indiacv.com",
    "digitalsupplychain.bharatbenz.com",
    "networkportal.bharatbenz.com",
    "uat-dms.bharatbenz.com",
    "ibms.bharatbenz.com",
    "diagnostics-proscan.bharatbenz.com",
    "diagnostics-proscan-test.bharatbenz.com",
    "ckdconnect-trucksasia.daimler.com",
    "serlogprod-dicv.daimlertruck.com",
    "serloguat-dicv.daimlertruck.com",
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
    "tcu-test.bharatbenz.com"
]

# Function to save report as PDF
def save_report_as_pdf(domain):
    try:
        # Construct the SSL Labs report URL
        report_url = f"https://www.ssllabs.com/ssltest/analyze.html?d={domain}"
        options = {
            'enable-local-file-access': '',
            'no-stop-slow-scripts': '',
            'javascript-delay': 10000  # Adjust the delay as needed
        }
        pdfkit.from_url(report_url, f"{domain}_report.pdf", configuration=config, options=options)
        print(f"Report saved for {domain}")
    except Exception as e:
        logging.error(f"Failed to save report for {domain}: {e}", exc_info=True)

# Loop through each domain
def main():
    for domain in domains:
        print(f"Scanning {domain}...")
        save_report_as_pdf(domain)
        time.sleep(10)
    print("SSL Qualys Test completed!")

if __name__ == "__main__":
    main()