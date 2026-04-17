_queue = []


def enqueue(channel, payload):
    _queue.append({"channel": channel, "payload": payload})
    return len(_queue)


def stats():
    """Return per-channel queue depth."""
    counts = {}
    for item in _queue:
        ch = item["channel"]
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def drop_channel(channel):
    """Remove all queued items for a channel."""
    for i, item in enumerate(_queue):
        if item["channel"] == channel:
            _queue.pop(i)
    return True
