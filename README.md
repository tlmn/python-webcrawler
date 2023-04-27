# Python Web Crawler for Image Downloading

This is a simple web crawler script that downloads images from a given website and its linked pages (on the same domain). The script is written in Python and uses the `requests`, `BeautifulSoup`, and `urllib` libraries.

## Requirements

- Python 3.6 or higher
- `requests`
- `beautifulsoup4`
- `lxml`
- `chardet`

## Installation

1. Clone the repository:

```
git clone https://github.com/tlmn/python-webcrawler.git
```


2. Change to the project directory:

```
cd python-webcrawler
```



3. Create a virtual environment (recommended):

```
python -m venv venv
```


4. Activate the virtual environment:

- For Windows:

  ```
  venv\Scripts\activate
  ```

- For Unix or MacOS:

  ```
  source venv/bin/activate
  ```

5. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

1. Run the script:

```
python crawlImages.py
```


2. Enter the website URL when prompted. The script will download all the images from the website and its linked pages (on the same domain) and save them in a folder named "downloaded_images".
