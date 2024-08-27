from locust import FastHttpUser, TaskSet, task


class MyUserlesstimeout(FastHttpUser):
    connection_timeout = 0.2
    network_timeout = 0.4
    weight = 2

    @task
    class taskSet(TaskSet):
        @task
        def indexdot5(self):
            response = None

            try:
                response = self.client.get("/timeout?timeout=0.3s")
            except Exception as e:
                if response != None:
                    response.failure(e)


class MyUser(FastHttpUser):
    connection_timeout = 0.1
    network_timeout = 0.6
    weight = 1

    @task
    class taskSet(TaskSet):
        @task
        def indexdot5(self):
            response = None

            try:
                response = self.client.get("/timeout?timeout=0.5s")
            except Exception as e:
                if response != None:
                    response.failure(e)

        @task
        def indexdot7(self):
            response = None

            try:
                response = self.client.get("/timeout?timeout=0.7s")
            except Exception as e:
                if response != None:
                    response.failure(e)

        @task
        def indexdot8(self):
            response = None
            try:
                response = self.client.get("/timeout?timeout=0.8s")
            except Exception as e:
                if response != None:
                    response.failure(e)

        @task
        def index1s(self):
            response = None
            try:
                response = self.client.get("/timeout?timeout=1s")
            except Exception as e:
                if response != None:
                    response.failure(e)

        @task
        def index2s(self):
            response = None
            try:
                response = self.client.get("/timeout?timeout=3s")
            except Exception as e:
                if response != None:
                    response.failure(e)


#    @task
#    def t(self):
#      def concurrent_request(url):
#        self.client.get(url)
#
#        pool = gevent.pool.Pool()
#        urls = ["/url1", "/url2", "/url3"]
#        for url in urls:
#          pool.spawn(concurrent_request, url)
#
#        pool.join()
#
