from vowpalwabbit import pyvw
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import csv

DATASET_PATH = "results_csv.csv"
DATASET_ENCODING = "UTF-8"

with open(DATASET_PATH, "r", encoding=DATASET_ENCODING) as dataset_file:
    dataset_csv = list(csv.reader(dataset_file, delimiter=','))

headers = dataset_csv[0]
dataset_csv.pop(0)

dataset = list()
datasets_final = list()

for i in range(len(dataset_csv)):
    dataset.append(dataset_csv[i])

for data in dataset:
    after_pipe = str()
    for i in range(1, len(data), 1):
        if i != 2 and i != 5 and i != 7:
            after_pipe += " " + headers[i] + ":" + data[i]

    new_element = data[0] + " |" + after_pipe + " " + data[5].replace(",", " ")
    datasets_final.append(new_element)

train_data, test_data = train_test_split(datasets_final, train_size=0.9, test_size=0.1, shuffle=True)

model = pyvw.vw('--quiet -c -f model.vwmodel')

for data in train_data:
    model.learn(data)

imdb_ratings, calculated_rating = [], []

for data in test_data:
    imdb_ratings.append(float(data.split(" | ")[0]))
    calculated_rating.append(model.predict("| " + data.split(" | ")[1]))

model.finish()
print("RMSE: " + str(mean_squared_error(imdb_ratings, calculated_rating, squared=False)))
