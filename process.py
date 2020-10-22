from multiprocessing import Process, JoinableQueue
import requests
import os

session = requests.Session()

CONSUMERS_NUMBER = 150

URLS = [f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png' for number in range(1, 151)]


class Consumer(Process):
    def __init__(self, task_queue: JoinableQueue):
        super().__init__()
        self.task_queue = task_queue

    # overwrite run method from Process class called by start method
    def run(self):
        while True:
            task = self.task_queue.get() # waits for a task here until get one! (lock)
            if task is None or not isinstance(task, Task):
                # ends this consumer
                break
            task.process()


class Task:
    def __init__(self, url):
        self.url = url

    def process(self):
        try:
            response = session.get(self.url)
            if response.ok:
                if not os.path.exists('images/process_alg/'):
                    os.makedirs('images/process_alg/')
                image_name = self.url.split('pokemon/')[1]
                with open(f'images/process_alg/{image_name}', 'wb') as f:
                    f.write(response.content)
        except requests.exceptions.ConnectionError as err:
            pass


def main() -> None:
    task_queue = JoinableQueue()
    consumers = [Consumer(task_queue) for _ in range(CONSUMERS_NUMBER)]

    # starting consumers
    for consumer in consumers:
        consumer.start()

    # creating taks
    for url in URLS:
        task_queue.put(Task(url))

    # stoping consumers
    for _ in  range(CONSUMERS_NUMBER):
        task_queue.put(None)


if __name__ == "__main__":
    main()
