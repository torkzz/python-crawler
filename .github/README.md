# Simple Web Crawler

A simple Python-based web crawler that recursively extracts and prints all the hyperlinks found on a given webpage.

## Features

- Recursively crawls web pages starting from a given URL.
- Extracts and prints all unique hyperlinks.
- Handles common web crawling issues such as broken links and malformed URLs.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

First, clone the repository:

```sh
git clone https://github.com/torkzz/python-crawler.git
cd simple-web-crawler
```

Next, install the required libraries:

```sh
pip install requests beautifulsoup4
```

## Usage

To run the crawler, use the following command:

```sh
python main.py -u <URL>
```

Replace `<URL>` with the target website you want to crawl. For example:

```sh
python main.py -u https://example.com
```

## Example Output

```
[DEBUG] Starting crawl on: https://example.com
[DEBUG] Requesting URL: https://example.com
[DEBUG] Found 10 links on https://example.com
[+] Link found! > https://example.com/about
[+] Link found! > https://example.com/contact
...
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
