# Hello Python

Try and learn something in python.

I have no idea why I like the word "hello".

## Behave Demo

make sure python2.7, selenium and behave have been installed

```
pip install selenium
pip install behave
```

make sure Chrome is installed and ChromeDriver is in the path

```
brew install chromedriver
```

For Windows, find the chromedriver 2.20 [here](https://github.com/heaton/easy-selenium/tree/master/drivers)

### Start a test sever

```
cd simple-site
python -m SimpleHTTPServer 8000
```

### Run the demo

```
behave
```

## Transform the json in behave format to the foramt of cucubmer report

run behave

```
behave --format=json --outfile=result/behave.json
python transform_json_to_cucumber.py
```

then see reslut/cucumber.json

