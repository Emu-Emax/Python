## Server log statistics

* Load log file to print statistics about requests

### Features:
* Time period of log
* Number of requests
* Unique status codes
* Percentages of codes types
* Unique IP addresses
* Non-existing URLS

### Usage:
You need to have Python installed. Run with log filename argument:

    $ python stats.py access.log
Sample format of request:

    X.X.X.X - - [13/Jul/2020:06:25:32 +0200] "GET / HTTP/1.1" 200 16 "-" "Python-urllib/2.7" 0.012 0.000 0.012 127.0.0.1:8080 .

In result, generates **results.txt**. Sample:
    
    Log statistics from [13/Jul/2020:06:25:32 +0200] to [14/Jul/2020:06:24:31 +0200] 
 
    Number of requests: 5965 
    
    STATUS CODES 
    ---
    Unique code requests: {'200': 4887, '302': 4, '404': 19, '204': 735, '201': 315, '499': 3, '301': 1, '400': 1} 
    Percentage of success codes: 99.5305951383068% 
    Percentage of redirects: 0.08382229673093043% 
    Percentage of not found codes: 0.38558256496228% 
    Percentage of error codes: 0.0% 
    
    IP ADDRESSES 
    ---
    Number of unique IP addresses: 49 
    Unique IP addresses: ['XX.XX.XX.XX']
    
    URLS 
    ---
    Non-existing URLS (which users tried to enter): ['https://XXX']