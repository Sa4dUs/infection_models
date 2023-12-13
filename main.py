import argparse
from models.sir_infection import SIR_Infection
from models.sird_infection import SIRD_Infection
from models.sier_infection import SIER_Infection

# Constants
DEFAULT_PARAMS = {
    "SIR": ["BETA", "GAMMA", "S0", "I0", "R0", "T_MAX"],
    "SIRD": ["BETA", "GAMMA", "DELTA", "S0", "I0", "R0", "D0", "T_MAX"],
    "SIER": ["BETA", "GAMMA", "ALPHA", "S0", "I0", "R0", "D0", "T_MAX"]
}

DEFAULT_VALUES = {
    "BETA": 0.28,
    "GAMMA": 0.03,
    "DELTA": 0.01,
    "ALPHA": 0.1,
    "S0": 0.99,
    "I0": 0.01,
    "R0": 0.0,
    "D0": 0.0,
    "T_MAX": 365
}

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Simulate and plot infection models.')
        parser.add_argument('model', choices=['SIR', 'SIRD', 'SIER'], help='Choose the infection model: SIR, SIRD, or SIER')

        for param in DEFAULT_VALUES:
            parser.add_argument(f"--{param}", type=float, default=DEFAULT_VALUES[param],
                                help=f'{param} (default: {DEFAULT_VALUES[param]})')

        args = parser.parse_args()

        print("[*] Running simulation for the", args.model, "model with the following parameters:")
        required_params = DEFAULT_PARAMS[args.model]

        for param in required_params:
            value = getattr(args, param)
            print(f"[+] {param}: {value}")

        used_params = {arg: getattr(args, arg) for arg in vars(args) if arg != 'model'}
        unused_args = [arg for arg in used_params if arg not in required_params and getattr(args, arg) != DEFAULT_VALUES[arg]]
        
        if unused_args:
            print("\n[!] Warning: The following additional parameters are not used for the", args.model, "model:",
                ", ".join([arg for arg in unused_args]))
            print("[-] Please note that these parameters will not affect the simulation.")

        if args.model == "SIR":
            model = SIR_Infection(args.BETA, args.GAMMA, args.S0, args.I0, args.R0, args.T_MAX)
        elif args.model == "SIRD":
            model = SIRD_Infection(args.BETA, args.GAMMA, args.DELTA, args.S0, args.I0, args.R0, args.D0, args.T_MAX)
        elif args.model == "SIER":
            model = SIER_Infection(args.BETA, args.GAMMA, args.ALPHA, args.S0, args.I0, args.R0, args.D0, args.T_MAX)

        model.plot()

    except KeyboardInterrupt:
        print("\n[!] Script interrupted by user (Ctrl+C). Exiting gracefully.")
