from locust import HttpLocust, TaskSet, task


class LoadTest(TaskSet):
    @task
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    host = "https://your.site"
    task_set = LoadTest
    min_wait = 5000
    max_wait = 15000
