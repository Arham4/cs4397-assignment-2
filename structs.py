#structs consists of shared structures for the program

#MessageQueue is a FIFO queue for communication across tasks or threads
class MessageQueue:

    def push(element):
        self._queue.append(element)

    def poll():
        if self._queue.length > 0:
            return self._queue.pop(0)

    def length():
        return self._queue.length

    def __init__(self):
        self._queue = []
