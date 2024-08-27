import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    quote_count = 1
    file = open("quotes.txt", "a", encoding="utf-8")

    start_urls = [
        "https://quotes.toscrape.com/page/1/" 
    ]
    
    """def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)"""

    def parse(self, response):
        """page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")"""
        
        
        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            
            self.file.write(f"\n{self.quote_count} --> Title: {title}\nAuthor: {author}\nTags: {', '.join(tags)}\n")
            self.file.write("------------------------------------------------------------------------------------------------")
            
            self.quote_count += 1
                
        new_url = response.css("li.next a::attr(href)")
        if new_url:
            new_url = f"https://quotes.toscrape.com{response.css("li.next a::attr(href)").get()}"
            yield scrapy.Request(url=new_url, callback=self.parse)
        else:
            self.file.close()
            
        """yield {
                "title": title,
                "author": author,
                "tags": tags
        }"""
        
            
        
        
        