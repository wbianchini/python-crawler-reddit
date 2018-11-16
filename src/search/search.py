class Search:
    def __init__(self, parameter, method):
        self.searchParameter = parameter
        self.callable_method = method

    def set_parameter(self, parameter):
        self.searchParameter = parameter
        pass

    def set_callable(self, callable):
        callable_instance = callable()
        self.callable_method = callable_instance

    def run(self, thread):
        return self.callable_method(thread)
