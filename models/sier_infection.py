from models.base.base_infection import Infection_Model

class SIER_Infection(Infection_Model):
    def __init__(self, beta, gamma, alpha, S0, E0, I0, R0, t_max):
        parameters = {'beta': beta, 'gamma': gamma, 'alpha': alpha}
        initial_conditions = [S0, E0, I0, R0]
        labels = ['Susceptible', 'Exposed', 'Infected', 'Recovered']
        colors = ['blue', 'orange', 'red', 'green']  # Default colors if not specified
        simulation_name = "SIER Model Simulation"  # Custom simulation name
        super().__init__(parameters, initial_conditions, t_max, labels, colors, simulation_name)

    def model(self, y, t):
        S, E, I, R = y
        dSdt = -self.parameters['beta'] * S * I
        dEdt = self.parameters['beta'] * S * I - self.parameters['alpha'] * E
        dIdt = self.parameters['alpha'] * E - self.parameters['gamma'] * I
        dRdt = self.parameters['gamma'] * I
        return [dSdt, dEdt, dIdt, dRdt]
