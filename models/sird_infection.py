from models.base.base_infection import Infection_Model

class SIRD_Infection(Infection_Model):
    def __init__(self, beta, gamma, delta, S0, I0, R0, D0, t_max):
        parameters = {'beta': beta, 'gamma': gamma, 'delta': delta}
        initial_conditions = [S0, I0, R0, D0]
        labels = ['Susceptible', 'Infected', 'Recovered', 'Deceased']
        colors = ['blue', 'red', 'green', 'black']  # Default colors if not specified
        simulation_name = "SIRD Model Simulation"  # Custom simulation name
        super().__init__(parameters, initial_conditions, t_max, labels, colors, simulation_name)

    def model(self, y, t):
        S, I, R, D = y
        dSdt = -self.parameters['beta'] * S * I
        dIdt = self.parameters['beta'] * S * I - self.parameters['gamma'] * I - self.parameters['delta'] * I
        dRdt = self.parameters['gamma'] * I
        dDdt = self.parameters['delta'] * I
        return [dSdt, dIdt, dRdt, dDdt]
