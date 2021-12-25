
# data = []
# with open("train_and_test_data/test.txt", "r") as test_data_file:
#     data = test_data_file.readlines()
#
# new_test_file = open("CF_test.txt", "w")
# for image in data:
#     if "CF" in image:
#         new_test_file.write(image)
# new_test_file.close()

# data = []
# with open("train_and_test_data/train.txt", "r") as train_data_file:
#     data = train_data_file.readlines()
#
# new_train_file = open("CF_train.txt", "w")
# for image in data:
#     if "CF" in image:
#         new_train_file.write(image)
# new_train_file.close()

import numpy as np
from scipy import special
from PIL import Image
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# TODO: Normalize all values in CF_test.txt and CF_train.txt files by dividing all numbers by 5


class NeuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.outputnodes = outputnodes
        self.inputnodes = inputnodes
        self.hiddennodes = hiddennodes

        self.weights_input_hidden = np.random.normal(0.0, pow(self.hiddennodes, -0.5), (self.hiddennodes, self.inputnodes))
        self.weights_hidden_output = np.random.normal(0.0, pow(self.outputnodes, -0.5), (self.outputnodes, self.hiddennodes))

        self.learningrate = learningrate

        self.activation_function = lambda x: special.expit(x)
        pass

    def train(self, input_list, target_list):
        inputs = np.array(input_list, ndmin=2).T
        targets = np.array(target_list, ndmin=2).T

        hidden_inputs = np.dot(self.weights_input_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.weights_hidden_output, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.weights_hidden_output.T, output_errors)

        self.weights_hidden_output += self.learningrate * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        self.weights_input_hidden += self.learningrate * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))
        pass

    def query(self, input_list):
        inputs = np.array(input_list, ndmin=2).T

        hidden_inputs = np.dot(self.weights_input_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = np.dot(self.weights_hidden_output, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs


input_nodes = 350*350
hidden_nodes = 1000
output_nodes = 2
learningrate = 0.5

nn = NeuralNetwork(inputnodes=input_nodes, hiddennodes=hidden_nodes, outputnodes=output_nodes, learningrate=learningrate)
file = open("train_and_test_data/CF_train.txt", "r")
file_data = {}
for line in file:
    key, value = line.split()
    file_data[key] = value

file.close()

for key, value in file_data.items():
    image = Image.open(f"Images/{key}").convert('L')
    image_array = np.array(image).flatten('F')
    image_list = image_array.tolist()

    scaled_input = (np.asfarray(image_list[0:]) / 255.0 * 0.99) + 0.01

    targets = np.zeros(output_nodes) + 0.01
    # img = mpimg.imread(f'Images/CF{i}.jpg')
    # imgplot = plt.imshow(img)
    # plt.show()

    targets[int(float(value)/5)] = 0.99

    nn.train(scaled_input, targets)

with open("weights.txt", "w") as file_weights:
    file_weights.write(nn.weights_input_hidden)
    file_weights.write(nn.weights_hidden_output)

test_data = {}
file = open("train_and_test_data/CF_test.txt", "r")
for line in file:
    key, value = line.split()
    file_data[key] = value
file.close()

scoreboard = []
for key, value in file_data.items():
    test_image = Image.open(f"Images/{key}").convert('L')
    test_array = np.array(image).flatten('F')
    test_list = image_array.tolist()
    test_scaled_input = (np.asfarray(test_list[0:]) / 255.0 * 0.99) + 0.01
    outputs = nn.query(test_scaled_input)

    label = np.argmax(outputs[:,0])
    if label == int(float(value)/5):
        scoreboard.append(1)
    else:
        scoreboard.append(0)

scorecard_array = np.asarray(scoreboard)
print("performance: ", scorecard_array.sum() / scorecard_array.size)