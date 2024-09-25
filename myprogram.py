import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import argparse
import json

#source : https://www.quora.com/How-do-I-extract-all-links-from-a-website-in-Python
import requests 
from bs4 import BeautifulSoup 

def get_links_from_url(url):
    # Send a GET request to the URL
    response = requests.get(url)
    html_content = response.content 
    
    soup = BeautifulSoup(html_content, "html.parser") 
    
    links = [link.get("href") for link in soup.find_all("a") if link.get("href").startswith("http")] 
    
    # Return  the extracted links 
    # for link in links: 
    #     print(link) 
    return links

def get_links_by_domain(all_links):
    domain_links = {}
    for link in all_links:
        domain = urlparse(link).netloc
        if domain not in domain_links:
            domain_links[domain] = []
        domain_links[domain].append(urljoin(link, urlparse(link).path))
    return domain_links
    

# Setup command-line argument parsing
parser = argparse.ArgumentParser(description='Extract and output URLs from webpages.')
parser.add_argument('-u', '--url', action='append', help='URL(s) to process', required=True)
parser.add_argument('-o', '--output', choices=['stdout', 'json'], help='Output format', required=True)
args = parser.parse_args()
print("Hello")
print("args.output : ", args.output)
print("args.url : ", args.url)

all_links = []
for url in args.url:
    links = get_links_from_url(url)
    all_links.extend(links)

if args.output == 'stdout':
    # Output one URL per line
    for link in all_links:
        print(link)
        
elif args.output == 'json':
    # Output as JSON hash with base domain and relative paths
    domain_links = get_links_by_domain(all_links)
    print(json.dumps(domain_links, indent=4))
    
print("Script executed, sleeping forever...")
# Sleep forever to prevent container from exiting
while True:
    time.sleep(3600)