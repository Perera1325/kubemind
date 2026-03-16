import random
import time

def predict_traffic():
    base_load = 100
    predicted = base_load + random.randint(-10, 40)

    if predicted > 130:
        print("Traffic spike predicted. Recommend scaling pods.")

while True:
    predict_traffic()
    time.sleep(5)
