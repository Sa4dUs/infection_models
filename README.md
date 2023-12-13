# Infection Model Simulator

This Python project simulates and plots various infection models: SIR, SIRD, and SIER.

## Introduction

This simulation utilizes three distinct infection models: 

- **SIR Model**: Tracks the number of individuals susceptible (S), infected (I), and recovered (R).
- **SIRD Model**: Extends the SIR model by incorporating a category for deaths (D).
- **SIER Model**: Enhances the SIRD model by introducing an exposed category (E) before individuals become infectious.

## Usage

### Requirements

- Python 3.x
- Required Python packages (install via `pip install -r requirements.txt`)

### Running the Simulation

1. Clone this repository (`git clone https://github.com/sa4dus/infection_models`).
2. Navigate to the project directory (`cd infection_models`).

To run the simulation, execute the main script using the command line:

```bash
python main.py <model> [--parameter_name parameter_value]
```

Replace `<model>` with the desired infection model: `SIR`, `SIRD`, or `SIER`.

You can specify model parameters (optional). If not specified, default values will be used.

### Available Parameters

The following parameters can be adjusted for each model:

- `BETA`: Transmission rate
- `GAMMA`: Recovery rate
- `DELTA`: Death rate (for SIRD and SIER models)
- `ALPHA`: Exposed to infectious rate (for SIER model)
- `S0`: Initial proportion of susceptible individuals
- `I0`: Initial proportion of infected individuals
- `R0`: Initial proportion of recovered individuals
- `D0`: Initial proportion of deceased individuals (for SIRD and SIER models)
- `T_MAX`: Maximum time for simulation (in days)

### Examples

**Example 1:** Run the SIR model with default parameters:
```bash
python main.py SIR
```

**Example 2:** Run the SIRD model with custom parameters:
```bash
python main.py SIRD --BETA 0.3 --GAMMA 0.04 --DELTA 0.02
```

### Outputs

The simulation generates a plot visualizing the progression of the chosen infection model based on the provided or default parameters.

## Notes

- If additional parameters are provided but not used for the selected model, a warning will be displayed.
- To interrupt the script, use Ctrl+C.

