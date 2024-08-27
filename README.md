# Scrapy Web Scraping

This project is a web scraping application built using the Scrapy framework. It extracts data from websites and saves the information into text files.

## Requirements

- Python 3.x
- Scrapy framework

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/zeysnepk/ScrapyFramework.git
    ```

2. Navigate into the project directory:

    ```bash
    cd tutorial
    ```
   or
   
   ```bash
    cd kitapYurdu
    ```

3. Install the required Python packages:

    ```bash
    pip install scrapy
    ```

## How to Use

1. **Running the Spider:**

    - To run the quotes spider and start scraping quotes, use the following command:

    ```bash
    scrapy crawl quotes
    ```
   
   - To run the books spider and start scraping book informations, use the following command:

    ```bash
    scrapy crawl books
    ```
   
    - The scraped data will be saved in `quotes.txt` or `books.txt`.

1. **Modifying the Spider:**

    - The spiders are defined in the `quotes_spider.py` and  `books.py` files located in the `spiders` directory.
    - To modify the spider for other websites, update the `start_urls` list and the `parse` method with the appropriate CSS selectors for the desired data.

## Exporting Data in JSON Format

If you prefer to export the data in JSON format, you can do so with the following command for the books spider:

```bash
scrapy crawl books -o books.json
```

This will create a books.json file with the scraped data in JSON format. You can delete the existing books.json file if needed before running the command.


## Example Output

After running the spiders, you will see the output file named quotes.txt or books.txt (or books.json if using the JSON export). The files will contain the scraped data as specified in the spiders.


