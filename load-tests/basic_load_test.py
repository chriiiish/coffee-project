from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def get_home(self):
      print("Getting Home Page...")
      self.locust.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 5000