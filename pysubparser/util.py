from datetime import time


def time_to_millis(t: time) -> int:
    seconds = (t.hour * 60 + t.minute) * 60 + t.second
    return seconds * 1000 + t.microsecond // 1000

def millis_to_time(millis: int) -> time:
    s, ml = divmod(millis, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    ms = ml * 1000

    return time(hour=int(h), minute=int(m), second=int(s), microsecond=int(ms))

def time_to_seconds(t: time) -> float:
    seconds = (t.hour * 60 + t.minute) * 60 + t.second
    return float(seconds) + float(t.microsecond) / 1000000
    
def seconds_to_time(seconds: float) -> time:
    s = int(seconds)
    ms = (seconds - int(s)) * 1000000
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)

    return time(hour=int(h), minute=int(m), second=int(s), microsecond=int(ms))
    
