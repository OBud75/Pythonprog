from requests import get
from bs4 import BeautifulSoup
from app.models import Asset

def get_sitemap() -> str:
    return get(url="https://readi.fi/sitemap.xml").text

def get_urls(sitemap: str, section: str) -> list[str]:
    ...
    #return list(set(url.split(sep="</loc>")[0]))for url in sitemap.split(sep="<loc>") if f"{section}/" in url

if __name__ == "__main__":
    sitemap = get_sitemap()
    urls = get_urls(sitemap = sitemap, section = 'assert')
    for url in urls:
        soup = BeautifulSoup(
            markup = get(url=url).text,
            features="html.parser"
        )
        asset = Asset.create(url, soup.title.text)

        