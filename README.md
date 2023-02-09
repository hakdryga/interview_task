# interview_task
### Description:
```
Task #1: Functional test suite
Create a fake http server in Python with API that behaves similar to https://swapi.dev/
It should support the same three end-points (people/xx/, planets/xx/, starships/xx/)
and can always return the same json response for any id passed.
For some specific ids e.g. >100 should return a 404 Not Found error with a json body that describes the problem.
The server should keep a log file that logs all the incoming requested URLs and response codes.

Task #2: Create an automated test suite (using test framework like Robot Framework) that:
a) prepares the test environment by starting the http server
b) runs test cases per end-point that verify both happy path or edge cases (e.g. id not found)
c) shuts down the environment
d) prints out the test execution results to the console

Task #3: Performance test suite
a) Extend the http server to incur a random small delay per http request.
b) Create a performance test suite that:
- prepares the test environment by starting the http server
- accesses one of the end-points continuously for a time duration e.g. 1 minute (sequential access is fine)
- for each access it keeps track of the response time on the client side
- shuts down the environment
- prints out mean and standard deviation of the response time for the end-point
```

### Preconditions:
```
pip install -r requirements.txt
```


### How to run functional tests:
Go to functional directory and type:
```
robot *.robot
robot test_people.robot
robot test_planets.robot
robot test_starships.robot
```
After execution, server log and test report are created in functional directory.

### How to run performance tests:
Go to performance directory and type:
```
locust -f perf_people.py --headless --users 1 --spawn-rate 1 -t 30 -H http://localhost:8052 --html perf_report.html
```
Parameters:
- --users: Number of concurrent Locust users. Right now test is written to handle only one user.
- --spawn-rate: The rate per second in which users are spawned
- -t: Stop after the specified amount of time, e.g. (300s, 20m, 3h, 1h30m, etc.). By default value is given in seconds.
- -H: Host to load test in the following format: http://10.21.32.33:PORT
Port value has to be the same as in perf_people.py file.
- --html: name of HTML report

After execution, server log and test report are created in performance directory.
