from typing import Iterable

from pysubparser.classes.subtitle import Subtitle

TIMESTAMP_FORMAT = "%S.%f"


def write(subtitles: Iterable[Subtitle], path: str):
    with open(path, "w+", encoding="utf-8") as file:
        for subtitle in subtitles:
            timestamp = "[{minute:03d}:{ss}]".format(
                minute= subtitle.start.hour * 24 + subtitle.start.minute,
                ss=subtitle.start.strftime(TIMESTAMP_FORMAT)[:-4],
            )

            lines = [timestamp]
            lines.extend(subtitle.lines)
            lines.extend('\n')

            file.write(" ".join(lines))
