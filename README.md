# interview_task


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