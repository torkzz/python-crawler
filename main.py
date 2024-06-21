import requests
import argparse
import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def get_arguments():
    parser = argparse.ArgumentParser(description="A simple web crawler")
    parser.add_argument("-u", "--url", dest="url", required=True, help="URL that you want to crawl")
    return parser.parse_args()

def extract_all_href(url):
    try:
        print(f"[DEBUG] Requesting URL: {url}")
        res = requests.get(url)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] Failed to retrieve URL: {url} with error: {e}")
        return []

    soup = BeautifulSoup(res.content, 'html.parser')
    hrefs = [a.get('href') for a in soup.find_all('a', href=True)]
    print(f"[DEBUG] Found {len(hrefs)} links on {url}")
    return hrefs

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def crawler(url, base_url, visited_links):
    print(f"[DEBUG] Crawling URL: {url}")
    hrefs = extract_all_href(url)
    for href in hrefs:
        l = urljoin(base_url, href)
        l = l.split("#")[0]
        if l not in visited_links and is_valid_url(l):
            visited_links.add(l)
            print("[+] Link found! > " + l)
            crawler(l, base_url, visited_links)

if __name__ == "__main__":
    options = get_arguments()
    target_url = options.url
    visited_links = set()
    print(f"[DEBUG] Starting crawl on: {target_url}")
    crawler(target_url, target_url, visited_links)
