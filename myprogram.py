import json
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import time
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3 needed
warnings.simplefilter('ignore', InsecureRequestWarning)

def get_links_from_url(url):
    response = requests.get(url, verify=True)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a") if link.get("href") and link.get("href").startswith("http")]
    return links

def get_links_by_domain(all_links):
    domain_links = {}
    for link in all_links:
        domain = urlparse(link).netloc
        if domain not in domain_links:
            domain_links[domain] = []
        domain_links[domain].append(urljoin(link, urlparse(link).path))
    return domain_links

def save_links_to_csv(all_links, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL'])
        for link in all_links:
            writer.writerow([link])

def get_secret(secret_path):
    with open(secret_path, 'r') as secret_file:
        api_key = secret_file.read().strip()
        print(f"Secret Key: {api_key}")
    return api_key

def main():
    print("Starting script...")
    with open('/config/config.json') as config_file:
        config = json.load(config_file)
    
    print("Config loaded:", config)
    url = config['url']
    output_format = config['output_format']
    output_file = config['output_file']
    secret_path = config['secret_path']
    
    all_links = []
    links = get_links_from_url(url)
    all_links.extend(links)

    print("Links fetched:", all_links)

    if output_format == 'stdout':
        for link in all_links:
            print(link)
    elif output_format == 'json':
        domain_links = get_links_by_domain(all_links)
        print(json.dumps(domain_links, indent=4))
    elif output_format == 'csv':
        if output_file:
            save_links_to_csv(all_links, output_file)
            print(f"Links saved to {output_file}")
        else:
            print("Please provide a filename using the -f or --file option to save the results in a CSV file.")

    print("Script executed, sleeping forever...")
    get_secret(secret_path)
    while True:
        time.sleep(3600)

if __name__ == "__main__":
    main()