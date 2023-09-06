import json
from pytutor import generate_trace, server

code = """
num = input("Enter a number: ")
print(num)
"""
trace = generate_trace.run(code, "[]")
print(trace)

print("=========================================")
trace = generate_trace.run(code, "[10]")
print(trace)