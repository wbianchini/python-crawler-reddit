import re
from src.search.rules.abstract_rule import AbstractRule


class RedditPoppingThreads(AbstractRule):

    def __init__(self):
        pass

    def __call__(self, soup):
        self.limitUpvotes = 5000
        return self.crawler_upvotes_callback(soup)

    def crawler_upvotes_callback(self, soup):
        upvotes_button = soup.find("button", {"aria-label" : "upvote"})
        total_upvotes = "0"
        if upvotes_button:
            count_upvotes_container = upvotes_button.find_next_sibling('div')
            total_upvotes = count_upvotes_container.text

        return self.is_highlighted_thread(self.convert_value(total_upvotes))

    def is_highlighted_thread(self, upvotes):
        return upvotes > self.limitUpvotes

    def convert_value(self, value):

        multiplier = 1

        if value.endswith('k'):
            multiplier = 1000
            value = value[0:len(value)-1]
        elif value.endswith('m'):
            multiplier = 1000000
            value = value[0:len(value)-1]

        return int(float(value) * multiplier)
