# Yet another log parser.

For log messages with the following format:

    {timestamp}: {event_text}

Or with optional metadata like:

    {timestamp}: {event_text} - {key_1}: {value_1}. {key_2}: {value_2}

Parsed as a list of dicts with metadata as nested dicts.
With timestamps as floats, and lower case keys for metadata.

## Example

    > lines = [
    >     '1.23: Message',
    >     '2.34: Message with metadata - hello: world, greet: True',
    > ]
    > for message in yalp.parse_log(lines):
    >     print(message)
    {'timestamp': 1.23, 'event': 'Message', 'metadata': {}}
    {'timestamp': 2.34, 'event': 'Message with metadata', 'metadata': {'hello': 'world', 'greet': True}}

See `test.py` for concrete examples.

## Tests

    python test.py
