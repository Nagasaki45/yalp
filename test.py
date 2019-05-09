import yalp

_result = yalp.parse_log_message('3.123456: Nodding')
_expected = {'timestamp': 3.123456, 'event': 'Nodding', 'metadata': {}}
assert _result == _expected, (_result, _expected)

_result = yalp.parse_log_message('3.896772: Talking - State: False')
_expected = {'timestamp': 3.896772, 'event': 'Talking', 'metadata': {'state': False}}
assert _result == _expected, (_result, _expected)

_result = yalp.parse_log_message('5.041295: Partner automation started - Model: mimicry. Speaker: False')
_expected = {'timestamp': 5.041295, 'event': 'Partner automation started',
             'metadata': {'model': 'mimicry', 'speaker': False}}
assert _result == _expected, (_result, _expected)

_result = list(yalp.parse_log(['3.123456: Nodding\n']))
_expected = [{'timestamp': 3.123456, 'event': 'Nodding', 'metadata': {}}]
assert _result == _expected, (_result, _expected)

_result = yalp.write_log_message({'timestamp': 3.123456, 'event': 'Nodding', 'metadata': {}})
_expected = '3.12: Nodding'
assert _result == _expected, (_result, _expected)

_result = yalp.write_log_message({'timestamp': 3.123456, 'event': 'Nodding', 'metadata': {'model': 'disfluency'}})
_expected = '3.12: Nodding - Model: disfluency'
assert _result == _expected, (_result, _expected)
