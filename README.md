# Pytutor

A library for Phillip Guo's (@pgbovine) Python Tutor.

![image](https://cloud.githubusercontent.com/assets/882381/25778600/a8d7b6c8-32b7-11e7-8c8c-345885433cb3.png)

Designed for Python 3

# Installation

`pip install pytutor`

# Usage

## Generating Traces
```
import json
from pytutor import generate_trace, server

modules = {'helper': 'foo = 1'}
setup_code = "y = 4"
trace = generate_trace.run_logger('x = 1 + y' , setup_code , modules)
trace_dict = json.loads(trace)

server.run_server(trace) # Serves HTML
```

```
>>> trace_dict
{
  "code": {
    "main_code": "x = 1 + y",
    "custom_modules": {
      "pg_setup": "y = 4"
    },
    "helper": "foo = 1"
  },
  "trace": [
    {
      "line": 1,
      "event": "step_line",
      "func_name": "<module>",
      "file_name": "<string>",
      "globals": {
        "y": 4
      },
      "ordered_globals": [
        "y"
      ],
      "stack_to_render": [],
      "heap": {},
      "stdout": ""
    },
    {
      "line": 1,
      "event": "return",
      "func_name": "<module>",
      "file_name": "<string>",
      "globals": {
        "y": 4,
        "x": 5
      },
      "ordered_globals": [
        "y",
        "x"
      ],
      "stack_to_render": [],
      "heap": {},
      "stdout": ""
    }
  ]
}
```

# License

MIT License

# Credits:

Phillip Guo - Python Tutor
Sumukh Sridhara - @sumukh (Modifications to support multiple python files)
