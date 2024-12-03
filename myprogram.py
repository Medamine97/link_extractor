import json
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import time

def get_links_from_url(url):
    response = requests.get(url, verify=False)
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

def main():
    with open('/config/config.json') as config_file:
        config = json.load(config_file)
    
    urls = config['url']
    output_format = config['output_format']
    output_file = config['output_file']


    all_links = []
    for url in urls:
        links = get_links_from_url(url)
        all_links.extend(links)

    if output_format == 'stdout':
        for link in all_links:
            print(link)
    elif output_format == 'json':
        domain_links = get_links_by_domain(all_links)
        print(json.dumps(domain_links, indent=4))
    elif output_format == 'csv':
        if output_file:
            save_links_to_csv(all_links, output_file)
        else:
            print("Please provide a filename using the -f or --file option to save the results in a CSV file.")

    print("Script executed, sleeping forever...")
    while True:
        time.sleep(3600)

if __name__ == "__main__":
    main()