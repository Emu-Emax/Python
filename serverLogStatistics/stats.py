import re
import sys
from collections import defaultdict

HOST = r'^(?P<host>.*?)'
SPACE = r'\s'
IDENTITY = r'\S+'
USER = r'\S+'
TIME = r'(?P<time>\[.*?\])'
REQUEST = r'\"(?P<request>.*?)\"'
STATUS = r'(?P<status>\d{3})'
SIZE = r'(?P<size>\S+)'
ADDRESS = r'\"(?P<address>.*?)\"'

REGEX = HOST + SPACE + IDENTITY + SPACE + USER + SPACE + TIME + \
        SPACE + REQUEST + SPACE + STATUS + SPACE + SIZE + SPACE + ADDRESS


class RequestStatistics:
    def __init__(self):
        self.no_of_requests = 0
        self.unique_status_codes = defaultdict(int)
        self.unique_ip_addresses = []
        self.non_existing_addresses = []

    def parse_log(self, filename):
        with open(filename, "r") as f:
            l = f.readlines()
            self.no_of_requests = len(l)
            self.start_time = re.search(REGEX, l[0]).group('time')
            self.end_time = re.search(REGEX, l[-1]).group('time')

            for i in range(self.no_of_requests):
                match = re.search(REGEX, l[i])
                self.unique_status_codes[match.group('status')] += 1

                if match.group('host') not in self.unique_ip_addresses:
                    self.unique_ip_addresses.append(match.group('host'))

                if match.group('status') == '404':
                    self.non_existing_addresses.append(match.group('address'))

    def dump_results(self):
        with open('results.txt', "w") as f:
            f.write('Log statistics from %s to %s \n \n' % (self.start_time, self.end_time))
            f.write('Number of requests: %s \n' % self.no_of_requests)

            f.write('\nSTATUS CODES \n---\n')
            f.write('Unique code requests: %s \n' % dict(self.unique_status_codes))
            f.write('Percentage of success codes: %s \n' % self.calc_percentage(self.calc_code_dict('2')))
            f.write('Percentage of redirects: %s \n' % self.calc_percentage(self.calc_code_dict('3')))
            f.write('Percentage of not found codes: %s \n' % self.calc_percentage(self.calc_code_dict('4')))
            f.write('Percentage of error codes: %s \n' % self.calc_percentage(self.calc_code_dict('5')))

            f.write('\nIP ADDRESSES \n---\n')
            f.write('Number of unique IP addresses: %s \n' % len(self.unique_ip_addresses))
            f.write('Unique IP addresses: %s \n' % self.unique_ip_addresses)

            f.write('\nURLS \n---\n')
            f.write('Non-existing URLS (which users tried to enter): %s \n' % self.non_existing_addresses)
            f.close()

    def calc_percentage(self, amount):
        return str((amount / self.no_of_requests) * 100) + '%'

    def calc_code_dict(self, code_type):
        s = 0
        for k, v in self.unique_status_codes.items():
            if k.startswith(code_type):
                s += v
        return s


if __name__ == '__main__':
    if len(sys.argv) > 1:
        log_name = sys.argv[1]
        rs = RequestStatistics()
        rs.parse_log(log_name)
        rs.dump_results()
    else:
        print('No log file provided. ')
        exit(0)
