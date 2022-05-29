class Scr1(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
        }

    def requests(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.text
            else:
                return "None"
        except RequestException as e:
            return e

    def parse(self):
        html = self.requests("https://static1.scrape.center/")
        soup = BeautifulSoup(html, "lxml")
        movie_title = soup.find('a', class_="name").text
        # for item in soup.find('div', class_="el-row"):
        #     html = item
        #     soup = BeautifulSoup(html, "lxml")
        #     return soup.find('a', id="data-v-7f856186").text
        movie_rating = soup.find("p", class_="score m-t-md m-b-n-sm").text.replace(" ", "")
        movie_cover = soup.find("img").text
        movie_release = soup.find("div", class_="m-v-sm info").text
        movie_category = soup.find("div", class_="categories").text
        # movie_summary = soup.find("div", class_="drama").text
        print(movie_title)
        print(movie_release)
        print(movie_category)
        return movie_rating

    def scrape_index(self, page="1"):
        index_url = f"{BASE_URL}/page/{page}"
        return self.requests(index_url)

    def parse_index(self, html):
        doc = pq(html)
        links = doc(".el-card .name")
        for link in links.items():
            href = link.attr("href")
            detail_url = urljoin(BASE_URL, href)
            return detail_url

    def scrape_details(self, url):
        return self.requests(url)

    def parse_details(self, html):
        soup = BeautifulSoup(html, "lxml")
        img_link = soup.select(".el-col .cover")
        print(img_link)


    def main(self):
        run_result = self.parse()
        for page in range(1, TOTAL_PAGE + 1):
            index_html = self.scrape_index(page)
        #     detail_urls = self.parse_index()
        #     # print(detail_urls)
        #     for url in detail_urls:
        #         html = self.scrape_details(url)
        #         r = self.parse_details(html)
        #     return index_html
        # return run_result



if __name__ == "__main__":
    Scr1().main()
