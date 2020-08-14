## Largest Prime Factor with client / server

* calculates largest prime factor for given number 
* prints statistics about elapsed request-response times.
* client and server
* program can run on many threads (specified in input)

###Server:
Served on 127.0.0.1:8000 listens for GET requests, responds with LPF answer and prints to the output:

    $ python server.py
    
    Server is running on 127.0.0.1:8000
    127.0.0.1 - - [14/Aug/2020 15:49:34] "GET /?number=284 HTTP/1.1" 200 -
    largest prime factor for 284 is 71.0
    127.0.0.1 - - [14/Aug/2020 15:49:34] "GET /?number=130 HTTP/1.1" 200 -
    largest prime factor for 130 is 13.0


###Client:
Input:
* **min-range, max range** - for randomizing input
* **number of requests**
* **number of workers** - number of workers for sending requests

Output:
* maximum request-response elapsed time
* minimum request-response elapsed time
* average request-response elapsed time
* total program execution time


        
        $ python client.py
        min range: 4
        max range: 300
        number of requests: 60
        number of workers: 5
        Maximum request-response elapsed time: 0:00:00.020478
        Minimum request-response elapsed time: 0:00:00.002109
        Average request-response elapsed time: 0:00:00.009241
        Total elapsed time: 0:00:00.554456
        Program executed in: 0.18581199645996094

###Installation:
Make virtual enviroment and install dependencies (pipenv is recommended):

    pipenv install --ignore-pipfile

Run server and client:

    python.py server
    python.py client
