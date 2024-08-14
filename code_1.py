import requests
import certifi

def get_project_links(base_url):
    ca_cert_path = "E:\\python-certifi-master\\python-certifi-master\\certifi\\ca_cert_path"
    try:
        response = requests.get(base_url, verify=certifi.where())
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching project links: {e}")
        return None

def get_project_details(project_url):
    try:
        response = requests.get(project_url, verify=certifi.where())
        response.raise_for_status()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        gstin = soup.find(text="GSTIN No:").find_next().text.strip()
        pan = soup.find(text="PAN No:").find_next().text.strip()
        name = soup.find(text="Name:").find_next().text.strip()
        address = soup.find(text="Permanent Address:").find_next().text.strip()
        return {
            'GSTIN No': gstin,
            'PAN No': pan,
            'Name': name,
            'Permanent Address': address
        }
    except requests.RequestException as e:
        print(f"Error fetching project details: {e}")
        return None

def main():
    base_url = "https://hprera.nic.in/PublicDashboard"
    project_links = get_project_links(base_url)
    if project_links:
        for link in project_links:
            details = get_project_details(link)
            if details:
                print(details)
    else:
        print("No project links found.")

if __name__ == "__main__":
    main()

