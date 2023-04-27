import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import chardet

visited_links = set()
image_folder = "downloaded_images"


def get_soup(url):
    try:
        response = requests.get(url)
        encoding = chardet.detect(response.content)['encoding']
        return BeautifulSoup(response.content, "lxml", from_encoding=encoding)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}")
        return None


def save_image(url):
    try:
        response = requests.get(url, stream=True)
        file_name = os.path.join(
            image_folder, urlparse(url).path.split("/")[-1])

        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Image saved: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {url}")


def extract_images_links(soup):
    return [img["src"] for img in soup.find_all("img", src=True)]


def extract_links(soup, base_url):
    return [urljoin(base_url, link.get("href")) for link in soup.find_all("a", href=True)]


def is_internal_link(link, base_url):
    return urlparse(link).netloc == urlparse(base_url).netloc


def crawl(url, base_url):
    if url in visited_links:
        return

    visited_links.add(url)
    soup = get_soup(url)

    if not soup:
        return

    for link in extract_links(soup, base_url):
        if is_internal_link(link, base_url):
            crawl(link, base_url)

    for image_url in extract_images_links(soup):
        save_image(urljoin(base_url, image_url))


def main():
    website_url = input("Enter the website URL: ")
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    crawl(website_url, website_url)


if __name__ == "__main__":
    main()
