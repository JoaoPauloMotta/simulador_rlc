import numpy as np


class RLCSeriesCircuit:
    """
    Represents a series RLC circuit and translates its electrical properties
    into state-space differential equations.
    """

    def __init__(self, resistance: float, inductance: float, capacitance: float, voltage_source: float = 0.0):
        self.R = resistance
        self.L = inductance
        self.C = capacitance
        self.V_source = voltage_source
        self._validate_parameters()

    def _validate_parameters(self) -> None:
        if self.L <= 0 or self.C <= 0:
            raise ValueError("Inductance and Capacitance must be strictly greater than zero.")
        if self.R < 0:
            raise ValueError("Resistance cannot be negative.")

    def state_space_equations(self, t: float, state: np.ndarray) -> np.ndarray:
        """
        Defines the system of first-order ODEs for the circuit.
        State vector: [q, i] (charge, current)
        dq/dt = i
        di/dt = (V - R*i - q/C) / L
        """
        q, i = state[0], state[1]

        dq_dt = i
        di_dt = (self.V_source - self.R * i - (q / self.C)) / self.L

        return np.array([dq_dt, di_dt])
    