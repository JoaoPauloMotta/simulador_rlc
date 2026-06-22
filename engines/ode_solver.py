from typing import Callable, Tuple
import numpy as np


class RungeKutta4Solver:
    """
    Classe responsável por resolver numericamente sistemas de Equações
    Diferenciais Ordinárias (EDOs) usando o método de Runge-Kutta de 4ª Ordem.
    """

    def __init__(self, step_size: float = 0.001):
        if step_size <= 0:
            raise ValueError("O tamanho do passo (h) deve ser estritamente positivo.")
        self.h = step_size

    def solve(self,
              system_equations: Callable[[float, np.ndarray], np.ndarray],
              initial_conditions: np.ndarray,
              time_span: Tuple[float, float]) -> Tuple[np.ndarray, np.ndarray]:
        """
        Resolve o sistema de EDOs dy/dt = f(t, y) de t_start até t_end.
        """
        t_start, t_end = time_span
        if t_start >= t_end:
            raise ValueError("O tempo inicial deve ser menor que o tempo final.")

        t_points = np.arange(t_start, t_end, self.h)
        num_steps = len(t_points)
        num_equations = len(initial_conditions)

        # Pré-alocação de memória para performance sênior
        y_solutions = np.zeros((num_steps, num_equations))
        y_solutions[0] = initial_conditions

        # Loop Principal do RK4
        for i in range(1, num_steps):
            t = t_points[i - 1]
            y = y_solutions[i - 1]

            k1 = system_equations(t, y)
            k2 = system_equations(t + self.h / 2, y + self.h * k1 / 2)
            k3 = system_equations(t + self.h / 2, y + self.h * k2 / 2)
            k4 = system_equations(t + self.h, y + self.h * k3)

            y_solutions[i] = y + (self.h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        return t_points, y_solutions
