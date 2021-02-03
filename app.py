# I am importing math, it is just a basic module for calculation, I hope I didn't break the rule!
# I imported json for Flask dump, and Flask was prescribed in the problem for bonus point.

import math
import json
from flask import Flask, request

# Declare the app
app = Flask(__name__)

# start an app route.
@app.route('/', methods=['GET'])
def compare():
    # getting two strings by GET method, i reccomend using POST MAN
    str1 = request.args.get('str1')
    str2 = request.args.get('str2')

    # calling the driver method
    result = stringSimilarity(str1, str2)
    to_return = {'result': result}
    # returns as json object
    return json.dumps(to_return)

# This method will get rid of punctuations, split the string and return a list
def cureString(str):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in str:
        if i in punctuation:
            str = str.replace(i, "")
    word_list = list((str.lower().split(" ")))

    return word_list

# This method will return a dictionary with individual word count
def generalMapper(word_list):
    d = {}
    for i in word_list:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d

# returns dot product of two strings
def scalerProduct(d1, d2):
    Sum = 0.0
    for i in d1:
        if i in d2:
            Sum += (d1[i] * d2[i])

    return Sum

# Finds the theta which will indicate the correlation. Lower the value, higher the similarity.
# Returns the result in radians. If two strings are same, it will return 0
# If there is no match, it will be 1.57 rad, which equals to approximately 90 degree
# formula for theta = cos^-1(a.b)/sqrt|a|.|b|
def vector_angle_theta(d1, d2):
    numerator = scalerProduct(d1, d2)
    denominator = math.sqrt(scalerProduct(d1, d1) * scalerProduct(d2, d2))

    return math.acos(numerator / denominator)

# Driver
def stringSimilarity(text1, text2):
    text1 = generalMapper(cureString(text1))
    text2 = generalMapper(cureString(text2))
    difference = vector_angle_theta(text1, text2)
    return str(difference)

# I used POSTMAN, and the result was 0.47 rad for sample 1 and sample 2, indicating more similarity
# and approximately 1.17 rad for sample 1 and sample 3, indicating less similarity.

# Running in debug mode
if __name__ == "__main__":
    app.debug = True
    app.run()
