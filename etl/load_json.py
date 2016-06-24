from erppeek import Client
import json
import sys

if not len(sys.argv) == 2:
    print 'Usage load_json.py <file>'
    sys.exit(1)

data = json.loads(open(sys.argv[1]).read())

client = Client.from_config('DEFAULT')
print client.execute(data[0], 'load', data[1], data[2])

