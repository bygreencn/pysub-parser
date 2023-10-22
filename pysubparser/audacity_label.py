from pysubparser.classes.exceptions import InvalidSubtitleTypeError


from datetime import datetime, time
from itertools import count
from typing import Iterator, Tuple

from pysubparser.classes.exceptions import InvalidTimestampError
from pysubparser.classes.subtitle import Subtitle
LINE_SEPARATOR = "\t"
TIMESTAMP_FORMAT = "%S.%f"

def labeltime_to_time(value: float) -> time:
    try:
        m, s = divmod(int(value), 60)
        h, m = divmod(m, 60)
        ms = (value - int(value)) * 1000000

        return time(hour=int(h), minute=int(m), second=int(s), microsecond=int(ms))
    except ValueError:
        raise InvalidTimestampError(value, "{float}", "label")
    

def parse_label(path: str, encoding: str = "utf-8", **_) -> Iterator[Subtitle]:
    index = count(0)

    with open(path, encoding=encoding) as file:
        for line in file:
            line = line.strip()

            start, end, line = line.split(LINE_SEPARATOR)
            
            start = labeltime_to_time(float(start))
            end = labeltime_to_time(float(end))

            subtitle = Subtitle(next(index), start, end)
            subtitle.add_line(line)

            yield subtitle
