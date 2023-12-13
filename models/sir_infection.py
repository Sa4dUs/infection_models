from models.base.base_infection import Infection_Model

class SIR_Infection(Infection_Model):
    def __init__(self, beta, gamma, S0, I0, R0, t_max):
        parameters = {'beta': beta, 'gamma': gamma}
        initial_conditions = [S0, I0, R0]
        labels = ['Susceptible', 'Infected', 'Recovered']
        colors = ['blue', 'red', 'green']  # Default colors if not specified
        simulation_name = "SIR Model Simulation"  # Custom simulation name
        super().__init__(parameters, initial_conditions, t_max, labels, colors, simulation_name)


    def model(self, y, t):
        S, I, R = y
        dSdt = -self.parameters['beta'] * S * I
        dIdt = self.parameters['beta'] * S * I - self.parameters['gamma'] * I
        dRdt = self.parameters['gamma'] * I
        return [dSdt, dIdt, dRdt]
