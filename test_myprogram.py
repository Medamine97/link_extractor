import pytest
from urllib.parse import urlparse, urljoin
import csv
from myprogram import get_links_from_url, get_links_by_domain, get_secret, save_links_to_csv

def test_get_links_from_url(requests_mock):
    url = "https://example.com"
    html_content = '''
    <html>
        <body>
            <a href="https://example.com/page1">Page 1</a>
            <a href="https://example.com/page2">Page 2</a>
            <a href="https://example.com/page3">Page 3</a>
        </body>
    </html>
    '''
    requests_mock.get(url, text=html_content)
    links = get_links_from_url(url)
    assert links == [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
    ]

def test_get_links_by_domain():
    all_links = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://another.com/page1"
    ]
    domain_links = get_links_by_domain(all_links)
    assert domain_links == {
        "example.com": [
            "https://example.com/page1",
            "https://example.com/page2"
        ],
        "another.com": [
            "https://another.com/page1"
        ]
    }

def test_save_links_to_csv(tmp_path):
    all_links = [
        "https://example.com/page1",
        "https://example.com/page2"
    ]
    csv_file = tmp_path / "output.csv"
    save_links_to_csv(all_links, csv_file)
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [
            ["URL"],
            ["https://example.com/page1"],
            ["https://example.com/page2"]
        ]

def test_get_secret(tmp_path):
    secret_file = tmp_path / "secret.txt"
    secret_file.write_text("my_secret_key")
    secret = get_secret(secret_file)
    assert secret == "my_secret_key"

if __name__ == "__main__":
    pytest.main()