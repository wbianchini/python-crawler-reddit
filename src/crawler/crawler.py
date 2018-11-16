import requests
from bs4 import BeautifulSoup
from src.crawler.match import Match


class Crawler:

    def __init__(self):
        self.seeds = []
        self.requestUrl = ""
        self.soup = BeautifulSoup

        self.search = []
        self.matches = []

    def crawl(self):
        for seed in self.seeds:
            self.requestUrl = seed
            self.read_page()
            self.run_searches()

    def append_search(self, search):
        self.search.append(search)

    def insert_seeds(self, seeds):
        self.seeds = seeds

    def add_seed(self, new_seed):
        self.seeds.append(new_seed)

    def run_searches(self):
        for search in self.search:
            self.run_search(search)

    def run_search(self, search):
        for soup in self.soup.select(search.searchParameter):
            if search.run(soup):
                self.matches.append(Match(self.requestUrl, soup))

    def append_search_callback(self, search):
        self.search.append(search)

    def read_page(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(self.requestUrl, headers=headers)
        plain_text = response.text
        self.soup = BeautifulSoup(plain_text,features="lxml")

    def get_matches(self):
        return self.matches
