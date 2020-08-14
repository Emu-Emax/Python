class InputValidator:

    def get_input(self):
        while True:
            try:
                self.min_range = int(input('min range: '))
                self.max_range = int(input('max range: '))
                self.no_of_requests = int(input('number of requests: '))
                self.no_of_workers = int(input('number of workers: '))
            except ValueError:
                print('please, provide integer number.')
                continue

            if self.min_range > self.max_range:
                print('min value cannot be larger than max value!')
                continue

            break

    def get_data(self):
        return {'min_range': self.min_range,
                'max_range': self.max_range,
                'no_of_requests': self.no_of_requests,
                'no_of_workers': self.no_of_workers
                }