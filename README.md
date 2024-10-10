A New Hope

A new hope is my Algotrading Bot.

How It's Made:

Tech used: Python, MT4/5, Jupyter Notebooks, TBD

yfinance for stock data
ccxt for crypto data

How to run application for now:

Fetching Stock Data:

To run simply edit the ticker.txt files with the Stock data you want to gather.
cd to folder.
run venv source /bin/Scripts/activate
run python src/main.py

###
# How to run minikube service
###
to run in minikube
eval $(minikube docker-env)
docker build -t my-python-app:1.0.0 .
kubectl apply -f k8s/
kubectl get pods
kubectl get services
minikube ip
navigate in a browser to http://ip.given.:30007


For cleaning the data using pandas.
When to use Drop vs Fill
Drop:
    - you have infrequent data.
    - Avoid Bias
    - Short-term Strategies
Fill:
    - Need Continuous Data
    - Back-testing
    - Small Gaps in data
    - Infrequent missing data

Selecting Fill and Drop can be important when cleaning data and trying to ensure you have accurately backtested a strategy. 
Ideally, you won't need to drop or fill rows often.

TODO:

Implement Jupyter Notebooks