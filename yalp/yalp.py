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
        line = line.strip()
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


def write_log(messages):
    for message in messages:
        yield write_log_message(message)


def write_log_message(message):
    base = '{timestamp:.3f}: {event}'.format_map(message)
    if message['metadata']:
        base += ' - ' + write_log_metadata(message['metadata'])
    return base


def write_log_metadata(metadata):
    return '. '.join([f'{k}: {v}' for k, v in metadata.items()])
