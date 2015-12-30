# -*- coding: utf-8 -*-
# Author: Heaton
# Source: https://github.com/heaton/hello-python

import json
import re

def location(l):
  return re.match(r'(.*?):(\d+)', l).group(1, 2)

def addAdditionalFieldsToStep(step):
  step["line"] = location(step['location'])[1]
  step["result"]["duration"] = long(step["result"]["duration"] * 1000 * 1000 * 1000)
  return step

def addAdditionalFieldsToElement(element, feature_id):
  element["id"] = feature_id + ';' + element['name'].replace(' ', '-').lower()
  element["line"] = location(element['location'])[1]
  element["description"] = ""
  element["steps"] = [addAdditionalFieldsToStep(step) for step in element['steps']]
  return element

def addAdditionalFieldsTo(feature):
  feature["id"] = feature['name'].replace(' ', '-').lower()
  l = location(feature['location'])
  feature["uri"] = l[0]
  feature["line"] = l[1]
  feature["description"] = ""
  feature["comments"] = []
  feature['elements'] = [addAdditionalFieldsToElement(ele, feature['id']) for ele in feature['elements']]
  return feature

def transform(json_string):
  return [addAdditionalFieldsTo(feature) for feature in json.loads(json_string)]

cucumber_json = transform(open('result/behave.json').read())
f = open('result/cucumber.json', 'w')
f.write(json.dumps(cucumber_json))
f.close()

