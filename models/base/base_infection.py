import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class Infection_Model:
    def __init__(self, parameters, initial_conditions, t_max, labels=None, colors=None, simulation_name="Infection Simulation"):
        self.parameters = parameters
        self.initial_conditions = initial_conditions
        self.t_max = t_max
        self.labels = labels
        self.colors = colors
        self.simulation_name = simulation_name

    def model(self, y, t):
        raise NotImplementedError("Subclasses must implement model method")

    def plot(self):
        t = np.linspace(0, self.t_max, 1000)
        sol = odeint(self.model, self.initial_conditions, t)
        variables = sol.T

        plt.figure(figsize=(10, 6))
        for i, variable in enumerate(variables):
            label = f'Variable {i}' if self.labels is None else self.labels[i]
            color = None if self.colors is None else self.colors[i]
            plt.plot(t, variable, label=label, color=color)
        plt.xlabel('Days')
        plt.ylabel('Fraction of Population')
        plt.title(self.simulation_name)
        plt.legend()
        plt.grid()
        plt.show()
