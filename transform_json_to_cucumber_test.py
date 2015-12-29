# -*- coding: utf-8 -*-

from transform_json_to_cucumber import *

re = transform('''[\
{
  "name": "Login Test", 
  "keyword": "Feature", 
  "location": "features/login.feature:1", 
  "status": "passed", 
  "tags": [],
  "elements": [
    {
      "name": "Run a simple test", 
      "keyword": "Scenario", 
      "location": "features/example.feature:3", 
      "tags": [], 
      "type": "scenario",
      "steps": [
        {
          "keyword": "Given", 
          "name": "we have behave installed", 
          "location": "features/example.feature:4", 
          "match": {
            "arguments": [], 
            "location": "features/steps/example_steps.py:3"
          }, 
          "result": {
            "duration": 0.00011491775512695312, 
            "status": "passed"
          }, 
          "step_type": "given"
        }, 
        {
          "keyword": "When", 
          "location": "features/example.feature:5", 
          "match": {
            "arguments": [
              {
                "name": "number", 
                "original": "5", 
                "value": 5
              }
            ], 
            "location": "features/steps/example_steps.py:7"
          }, 
          "name": "we implement 5 tests", 
          "result": {
            "duration": 0.00010585784912109375, 
            "status": "passed"
          }, 
          "step_type": "when"
        }, 
        {
          "keyword": "Then", 
          "location": "features/example.feature:6", 
          "match": {
            "arguments": [], 
            "location": "features/steps/example_steps.py:12"
          }, 
          "name": "behave will test them for us!", 
          "result": {
            "duration": 0.00010204315185546875, 
            "status": "passed"
          }, 
          "step_type": "then"
        }
      ]
    }
  ]
}
]''')[0]

assert re["id"] == "login-test"
assert re["uri"] == "features/login.feature"
assert re["line"] == "1"
assert re["description"] == ""
assert re["comments"] == []

elements1 = re["elements"][0]
assert elements1["id"] == "login-test;run-a-simple-test"
assert elements1["line"] == '3'
assert elements1["description"] == ""

steps = elements1["steps"]
assert steps[0]["line"] == '4'
assert steps[0]["result"]["duration"] == 114917
assert steps[1]["line"] == '5'

print 'success'
