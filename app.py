from decimal import *
from flask import Flask
import time
getcontext().prec = 100

app = Flask(__name__)

@app.route("/home")
def myhome():
    return "Welcome to AWS Support Engineers Home Page!!!"

@app.route("/contact")
def contact():
    return "Contact AWS Support Engineers at info@awssupport.aws"

@app.route("/address")
def address():
    return "We are located at 410 Terry Ave N, Seattle, WA, United States"

@app.route("/")
def home():
    return "Hello AWS Support Engineers!"

from decimal import *
from flask import Flask, request
import time
getcontext().prec = 100

app = Flask(__name__)

@app.route('/calculatePI')
def calculatePI():
    # start timer
    st = time.time()
    reps = request.args.get('reps', 1)
    reps = int(reps)
    result = Decimal(3.0)
    op = 1
    n = 2
    for n in range(2, 2*reps+1, 2):
        result += 4/Decimal(n*(n+1)*(n+2)*op)
        op *= -1
    # end timer
    et = time.time()
    # calculate elapse time to see how long it took to calculate PI
    elapsed_time = et - st
    return "PI: " + str(result) + " Elapsed Time: " + str(elapsed_time)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
