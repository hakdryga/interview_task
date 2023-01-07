import time
import random
import subprocess

from locust import FastHttpUser, task


class RestUser(FastHttpUser):

    def __init__(self, environment):
        super().__init__(environment)
        self.server_process = None

    def on_start(self):
        self.server_process = subprocess.Popen(["python", "../common/run_server.py", "-h", "localhost", "-p", "8052", "delay", "&"])
        time.sleep(3)

    def on_stop(self):
        self.server_process.terminate()

    @task
    def run_test(self):
        id = random.randint(90, 105)
        self.client.get(f'/people/{id}')