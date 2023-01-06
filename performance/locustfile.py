import time
import random
import subprocess

from locust import FastHttpUser, task, events

def on_init(environment, **kwargs):
    environment.server_process = subprocess.Popen(["python", "../common/run_server.py", "-h", "localhost", "-p", "8052", "delay", "&"])
    time.sleep(3)


def on_quit(environment, **kwargs):
    environment.server_process.terminate()

events.init.add_listener(on_init)
events.quitting.add_listener(on_quit)

class RestUser(FastHttpUser):

    def setup(self):
        print("setup of TaskSet")

    # def on_start(self):
    #     self.server_process = subprocess.Popen(["python", "../common/run_server.py", "-h", "localhost", "-p", "8051", "delay", "&"])
    #     time.sleep(3)

    # def on_stop(self):
    #     self.server_process.terminate()

    @task
    def run_test(self):
        id = random.randint(90, 105)
        self.client.get(f'/people/{id}')