from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score


# Create and train the perceptron

p = Perceptron()

data = []
lables = []

#read the file
with open("data_banknote_authentication.txt", "r") as f:
    for line in f.readlines():
        data.append([float(x) for x in line.split(",")[:-1]])
        lables.append(int(line.split(",")[-1]))


#print th edata
print(data)
print(lables)


p.fit(data, labels)
predictions_train = p.predict(train_data)
train_score = accuracy_score(predictions_train, train_labels)
print("Training accuracy: ", train_score)

