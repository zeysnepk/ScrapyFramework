import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    page_count = 1
    book_count = 1
    file = open("books.txt", "a", encoding="utf-8")
    
    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&page=1&list_id=1"
    ]
    
    def parse(self, response):
        books = response.css("div.product-cr")
        for book in books:
            book_name = book.css("div.name.ellipsis a span::text").get()
            book_author = book.css("div.author span a span::text").get()
            book_publisher = book.css("div.publisher span a span::text").get()
            
            yield {
                "Book Name": book_name,
                "Author": book_author,
                "Publisher": book_publisher
            }
            self.file.write(f"-----{self.book_count}-----\n")
            self.file.write(f"Book Name: {book_name}\nAuthor: {book_author}\nPublisher: {book_publisher}\n")
            self.file.write("\n\n")
            self.book_count += 1
        self.page_count += 1
            
        next_page = response.css("a.next::attr(href)").get()
        if next_page and self.page_count < 6:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
        else:
            self.file.close()