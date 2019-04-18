'''
Yet another log parser.
'''
import re


LOG_MESSAGE_PATTERN = re.compile(
    r'^(?P<timestamp>\d+\.?\d+?): ' # Timestamp
    r'(?P<event>[^-]+)'             # Event
    r'(\ -\ (?P<metadata>.+))?'     # Optional metadata
    r'$'
)


def parse_log(lines):
    for line in lines:
        if line:
            yield parse_log_message(line)

            
def parse_log_message(message):
    match = LOG_MESSAGE_PATTERN.match(message)
    metadata = parse_log_metadata(match.group('metadata'))
    return {
        'timestamp': float(match.group('timestamp')),
        'event': match.group('event'),
        'metadata': metadata,
    }


def parse_log_metadata(raw):
    if raw is None:
        return {}
    d = {}
    for pair in raw.split('. '):
        k, v = pair.split(': ')
        d[k.lower()] = True if v == 'True' else False if v == 'False' else v
    return d
