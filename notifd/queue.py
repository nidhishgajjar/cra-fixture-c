_queue = []


def enqueue(channel, payload):
    _queue.append({"channel": channel, "payload": payload})
    return len(_queue)


def flush():
    """Send everything in the queue, return count."""
    sent = 0
    for item in _queue:
        send(item)
        _queue.pop(0)
        sent += 1
    return sent


def send(item):
    pass  # delivery integration goes here
