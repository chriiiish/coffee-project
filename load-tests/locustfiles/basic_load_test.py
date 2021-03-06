import sys, os
sys.path.append(os.getcwd())
from locust import HttpLocust, TaskSet, TaskSequence, task, seq_task
import common.auth

class UserBehavior(TaskSequence):

    def on_start(self):
      print("Running SETUP")
      common.auth.login(self)

    @seq_task(1)
    def get_home(self):
      #print("Getting Home Page...")
      self.locust.client.get("/")

    @seq_task(2)
    def get_about(self):
      #print("Getting About Page...")
      self.locust.client.get("/about")

    @seq_task(3)
    @task(10)
    def get_error(self):
      #print("Getting Error Page...")
      self.locust.client.get("/error")

    def on_stop(self):
      print("Running TEARDOWN")
      common.auth.logout(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 1500