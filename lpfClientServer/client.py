import concurrent.futures
import datetime
import random
import threading
import time

import requests

from inputValidator import InputValidator

thread_local = threading.local()


class Client:
    def __init__(self, min_range, max_range, no_of_requests, no_of_workers):
        self.min_range = min_range
        self.max_range = max_range
        self.no_of_requests = no_of_requests
        self.no_of_workers = no_of_workers
        self.elapsed_times = []
        self.url = 'http://localhost:8000?number='

    def start(self):
        urls = []
        for _ in range(self.no_of_requests):
            arg = random.randint(self.min_range, self.max_range)
            url = self.url + str(arg)
            urls.append(url)

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.no_of_workers) as executor:
            executor.map(self.make_request, urls)

    def get_session(self):
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session

    def make_request(self, url):
        session = self.get_session()
        with session.get(url) as response:
            self.elapsed_times.append(response.elapsed)

    def print_stats(self):
        if self.elapsed_times:
            print('Maximum request-response elapsed time: ' + str(max(self.elapsed_times)))
            print('Minimum request-response elapsed time: ' + str(min(self.elapsed_times)))
            print('Average request-response elapsed time: ' + str(
                sum(self.elapsed_times, datetime.timedelta(0)) / len(self.elapsed_times)))
            print('Total elapsed time: ' + str(sum(self.elapsed_times, datetime.timedelta(0))))
        else:
            print('Server is offline.')


if __name__ == '__main__':
    inp = InputValidator()
    inp.get_input()
    c = Client(**inp.get_data())

    start_time = time.time()
    c.start()
    c.print_stats()
    print('Program executed in: ' + str(time.time() - start_time))
