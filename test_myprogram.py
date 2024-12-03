import pytest
from urllib.parse import urlparse, urljoin
import csv
from myprogram import get_links_from_url, get_links_by_domain, save_links_to_csv

def test_get_links_from_url(requests_mock):
    url = "http://example.com"
    html_content = '''
    <html>
        <body>
            <a href="http://example.com/page1">Page 1</a>
            <a href="http://example.com/page2">Page 2</a>
            <a href="http://example.com/page3">Page 3</a>
        </body>
    </html>
    '''
    requests_mock.get(url, text=html_content)
    links = get_links_from_url(url)
    assert links == [
        "http://example.com/page1",
        "http://example.com/page2",
        "http://example.com/page3"
    ]

def test_get_links_by_domain():
    all_links = [
        "http://example.com/page1",
        "http://example.com/page2",
        "http://another.com/page1"
    ]
    domain_links = get_links_by_domain(all_links)
    assert domain_links == {
        "example.com": [
            "http://example.com/page1",
            "http://example.com/page2"
        ],
        "another.com": [
            "http://another.com/page1"
        ]
    }

def test_save_links_to_csv(tmp_path):
    all_links = [
        "http://example.com/page1",
        "http://example.com/page2"
    ]
    csv_file = tmp_path / "output.csv"
    save_links_to_csv(all_links, csv_file)
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        assert rows == [
            ["URL"],
            ["http://example.com/page1"],
            ["http://example.com/page2"]
        ]

if __name__ == "__main__":
    pytest.main()