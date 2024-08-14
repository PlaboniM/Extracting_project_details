This Python project is designed to scrape project details from the website hprera.nic.in. It uses the requests library to fetch data and BeautifulSoup to parse the HTML and extract relevant information. The primary goal is to extract and display project details, including GSTIN, PAN, name, and address.
Installation
Prerequisites
 1.Python 3.12 or higher
 2.Virtual Environment (recommended)
Installation Steps
 1.Clone the Repository
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
 2.Create and Activate Virtual Environment
    python -m venv myenv
    myenv\Scripts\activate  # On Windows
    source myenv/bin/activate  # On macOS/Linux

SSL/TLS Certificate Issue
 Description of the Problem
 When running the script, you might encounter an SSL/TLS certificate verification error:
 HTTPSConnectionPool(host='hprera.nic.in', port=443): Max retries exceeded with url: /PublicDashboard (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: 
 unable to get local issuer certificate (_ssl.c:1000)')))
Explanation
This error occurs because the SSL/TLS certificate used by hprera.nic.in is either misconfigured or not trusted by your local machine. This issue can be due to:

1.Missing Intermediate Certificates: The website might be missing intermediate certificates required to establish a complete chain of trust.

2.Outdated Certificate Authorities: Your local CA certificates might be outdated or missing necessary updates.

3.Custom CA Certificate: The website might use a custom CA certificate not included in the standard CA bundle.
