# Plots various neural net activation functions.

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

from pyprobml_utils import save_fig


def sigmoid(z: np.array) -> np.array:
    return 1 / (1 + np.exp(-z))


def relu(z: np.array) -> np.array:
    return np.maximum(0, z)


def heaviside(z: np.array) -> np.array:
    return z > 0


def softplus(z: np.array) -> np.array:
    return np.log(1 + np.exp(z))


def lrelu(z: np.array, lam: float = 0.1) -> np.array:
    return np.maximum(lam * z, z)


def elu(z: np.array, alpha: float = 1.0) -> np.array:
    return np.where(z < 0, alpha * (np.exp(z) - 1), z)


def elu2(z: np.array, lam: float = 0.5) -> np.array:
    return np.maximum(0, z) + np.minimum(0, lam * (np.exp(z) - 1))


def swish(z: np.array) -> np.array:
    return z * sigmoid(z)


print('plot some activation functions')

# alpha and scale to self normalize with mean 0 and standard deviation 1
# (see equation 14 in the SELU paper):
alpha_0_1 = -np.sqrt(2 / np.pi) / (erfc(1 / np.sqrt(2)) * np.exp(1 / 2) - 1)
scale_0_1 = (1 - erfc(1 / np.sqrt(2)) * np.sqrt(np.e)) * np.sqrt(2 * np.pi) * (
        2 * erfc(np.sqrt(2)) * np.e ** 2 + np.pi * erfc(1 / np.sqrt(2)) ** 2 * np.e - 2 * (2 + np.pi) * erfc(
            1 / np.sqrt(2)) * np.sqrt(np.e) + np.pi + 2) ** (-1 / 2)


def selu(z, scale=scale_0_1, alpha=alpha_0_1):
    return scale * elu(z, alpha)


z = np.linspace(-5, 5, 200)

# plt.figure(figsize=(11,4))
plt.figure()
plt.plot(z, heaviside(z), "r-", linewidth=2, label="Heaviside")
plt.plot(z, sigmoid(z), "g--", linewidth=2, label="Sigmoid")
plt.plot(z, np.tanh(z), "b-", linewidth=2, label="Tanh")
plt.plot(z, relu(z), "m-.", linewidth=2, label="ReLU")
plt.grid(True)
plt.legend(loc="lower right", fontsize=14)
plt.title("Activation functions", fontsize=14)
plt.axis([-5, 5, -1.2, 1.2])
save_fig('activationFuns.pdf')
plt.show()

# plt.figure(figsize=(11,4))
plt.plot(z, relu(z), "r-", linewidth=2, label="ReLU")
plt.plot(z, lrelu(z), "g--", linewidth=2, label="LReLU")
plt.plot(z, elu(z), "b-", linewidth=2, label="ELU")
plt.plot(z, selu(z), "k:", linewidth=2, label="SELU")
plt.plot(z, swish(z), "m-.", linewidth=2, label="swish")
plt.grid(True)
plt.legend(loc="upper left", fontsize=14)
plt.title("Activation functions", fontsize=14)
plt.axis([-2, 2, -1.2, 2])
save_fig('activationFuns2.pdf')
plt.show()

# From https://github.com/ageron/handson-ml2/blob/master/11_training_deep_neural_networks.ipynb
z = np.linspace(-5, 5, 200)
plt.plot([-5, 5], [0, 0], 'k-')
plt.plot([-5, 5], [1, 1], 'k--')
plt.plot([0, 0], [-0.2, 1.2], 'k-')
plt.plot([-5, 5], [-3 / 4, 7 / 4], 'g--')
plt.plot(z, sigmoid(z), "b-", linewidth=2)
props = dict(facecolor='black', shrink=0.1)
plt.annotate('Saturating', xytext=(3.5, 0.7), xy=(5, 1), arrowprops=props, fontsize=14, ha="center")
plt.annotate('Saturating', xytext=(-3.5, 0.3), xy=(-5, 0), arrowprops=props, fontsize=14, ha="center")
plt.annotate('Linear', xytext=(2, 0.2), xy=(0, 0.5), arrowprops=props, fontsize=14, ha="center")
plt.grid(True)
plt.title("Sigmoid activation function", fontsize=14)
plt.axis([-5, 5, -0.2, 1.2])
save_fig("sigmoid_saturation_plot")
plt.show()
