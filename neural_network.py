
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
import numpy
import numpy as np
import scipy

# TODO: Normalize all values in CF_test.txt and CF_train.txt files by dividing all numbers by 5


class NeuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.outputnodes = outputnodes
        self.inputnodes = inputnodes
        self.hiddennodes = hiddennodes

        self.weights_input_hidden = np.random.normal(0.0, pow(self.hiddennodes, -0.5), (self.hiddennodes, self.inputnodes))
        self.weights_hidden_output = np.random.normal(0.0, pow(self.outputnodes, -0.5), (self.outputnodes, self.hiddennodes))

        self.learningrate = learningrate

        self.activation_function = lambda x: scipy.special.expit(x)
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