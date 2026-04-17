_queue = []


def enqueue(channel, payload):
    _queue.append({"channel": channel, "payload": payload})
    return len(_queue)
