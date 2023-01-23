import sys
import sqlite3
from typing import TextIO


INITIAL_SQL = """
CREATE TABLE IF NOT EXISTS sentence (
    id INTEGER PRIMARY KEY,
    japanese TEXT,
    english TEXT
);
"""

QUIET = False

def log(output: str, stream: TextIO=sys.stdout) -> None:
    """
    Logs a message to the given stream while respecting the `QUIET` setting
    (unless the stream is `sys.stderr`).
    """

    if QUIET and stream is not sys.stderr:
        return

    print(output, file=stream)


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        log('Please specify the resulting database\'s filename as the second argument')
        exit(1)

    dbFilename = argv[1]
    db = sqlite3.connect(dbFilename)

    log('Connected to SQLite')

    db.close()
    

if __name__ == '__main__':
    main(sys.argv)