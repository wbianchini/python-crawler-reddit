import sys
from src.search.search import Search
from src.search.rules.reddit_popping_threads import RedditPoppingThreads
from src.crawler.crawler import Crawler


class RedditCrawler:
    def __init__(self):
        self.threads = []
        self.baseUrl = "http://www.reddit.com"
        self.subReddits = ["cats", "brazil", "worldnews", "AskReddit"]

    def set_sub_reddits(self, sub_reddits):
        self.subReddits = sub_reddits.split(';')

    def crawl(self):
        crawler_instance = Crawler()
        for subReddit in self.subReddits:
            crawler_instance.add_seed(self.baseUrl + '/r/' + subReddit)

        reddit_search = Search('div.scrollerItem', RedditPoppingThreads())

        crawler_instance.append_search_callback(reddit_search)

        crawler_instance.crawl()
        self.threads = crawler_instance.get_matches()

    def get_text_message(self):
        text = ""
        for thread in self.threads:
            upvotes_button = thread.soup.find("button", {"aria-label" : "upvote"})
            total_upvotes = "0"
            if upvotes_button:
                count_upvotes_container = upvotes_button.find_next_sibling('div')
                total_upvotes = count_upvotes_container.text

            text += '**upvotes** : ' + total_upvotes + '\n'

            text += '**Titulo** : ' + str(thread.soup.find('h2').text) + '\n'

            text += '**Comentarios** : (' + self.baseUrl + thread.soup.find("a", {"data-click-id" : "comments"}).get('href') + ')\n'

            text += '**Sub Reddit** : (' + thread.url + ')\n\n'

        return text
