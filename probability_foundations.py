import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Make random sequences reproducible, just like the course notebook
np.random.seed(42)

print("Environment setup successfully in VS Code!")


# Simulating 10 days of an activity tracker
# 1 = Work Day, 0 = Off Day
days_history = np.array([1, 0, 1, 1, 0, 1, 0, 1, 1, 1])

# Count how many times each outcome happens
counts = Counter(days_history)
print("Counts of outcomes:", counts)

# Calculate the probability of working
# We divide the total number of work days (7) by the overall length of our history array (10)
prob_work = counts[1] / len(days_history)

print(f"The probability of a Work Day is: {prob_work}")
print(f"In percentage format: {prob_work * 100}%")


# A simple function representing a single neural network neuron
def simple_neuron(input1, weight1, input2, weight2, bias):
    # Calculate combined raw output
    raw_output = (input1 * weight1) + (input2 * weight2) + bias
    return raw_output


# Let's test our neuron with a sample input
# Imagine user_input is '1' (e.g., it is a weekday)
sample_input1 = 1      # It is a weekday
sample_weight1 = 0.8   # Weekday importance

sample_input2 = 1      # There is a deadline
sample_weight2 = 1.5   # Deadline importance (highly weighted!)

sample_bias = -0.2     # Base adjustment

# Run the updated neuron function
neuron_result = simple_neuron(sample_input1, sample_weight1, sample_input2, sample_weight2, sample_bias)


# The Sigmoid Activation Function to squash values between 0 and 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Let's pass our raw neuron output (0.6) through the sigmoid function
final_prediction = sigmoid(neuron_result)

print("Squashed Prediction (Probability):", final_prediction)
print(f"Confidence Percentage: {final_prediction * 100:.2f}%")
