import threading
from queue import Empty, Queue

from cancel_token import CancellationToken


class QueueBossBase:
    def __init__(self):
        self._queue = Queue()
        self._token = CancellationToken()
        self._lock = threading.Lock()
        self._queue_size = 0

    def count(self):
        return self._queue_size

    def _decr_work(self):
        try:
            self._lock.acquire()
            self._queue_size = self._queue_size - 1
        except:
            pass
        finally:
            self._lock.release()

    def _incr_work(self):
        try:
            self._lock.acquire()
            self._queue_size = self._queue_size + 1
        except:
            pass
        finally:
            self._lock.release()

    def add_work(self, work, return_queue):
        self._queue.put((work, return_queue))
        self._incr_work()
        return return_queue.get()

    def stop(self):
        self._token.cancel()
        return self

    def __del__(self):
        clear_queue(self._queue)
        self._token = None

    def start(self, ):
        threading.Thread(target=self._loop).start()
        return self

    def _process(self, job):
        pass

    def _loop(self):
        while not self._token.cancelled:
            work = self._queue.get()
            data, return_queue = work
            if data is None:
                if return_queue is not None:
                    return_queue.put(None)
                    self._decr_work()
                continue
            return_queue.put(self._process())
            self._decr_work()


def clear_queue(buffer):
    try:
        while True:
            item = buffer.get(False)
            del item
    except Empty:
        pass
