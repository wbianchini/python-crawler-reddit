from abc import ABC, abstractmethod


class AbstractRule(ABC): 

	@abstractmethod
	def __call__(self, soup):
		pass

