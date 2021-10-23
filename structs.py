#structs consists of shared structures for the program

#MessageQueue is a FIFO queue for communication across tasks or threads
class MessageQueue:

    queue = []

    def push(element):
        queue.append(element)

    def poll():
        return queue.pop(0)
