import numpy as np
import matplotlib.pyplot as plt
from engines.rlc_model import RLCSeriesCircuit
from engines.ode_solver import RungeKutta4Solver


def get_float_input(prompt: str, min_value: float = 0.0) -> float:
    """Helper function to safely get and validate numeric inputs from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                print(f"Por favor, insira um valor maior ou igual a {min_value}.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")


def main() -> None:
    print("=" * 50)
    print("   SIMULADOR DE CIRCUITO RLC SÉRIE (MÉTODO RK4)   ")
    print("=" * 50)

    # 1. Coleta de dados do usuário (Sua ideia original)
    R = get_float_input("Digite a Resistência (R em Ohms): ")
    L = get_float_input("Digite a Indutância (L em Henrys): ", min_value=0.0001)
    C = get_float_input("Digite a Capacitância (C em Farads): ", min_value=0.0001)
    V_source = get_float_input("Digite a Tensão da Fonte (V em Volts): ")

    print("\n--- Condições Iniciais ---")
    q0 = get_float_input("Carga inicial no capacitor (q0 em Coulombs): ")
    i0 = get_float_input("Corrente inicial no circuito (i0 em Amperes): ")

    # 2. Inicialização dos componentes de software
    try:
        circuit = RLCSeriesCircuit(resistance=R, inductance=L, capacitance=C, voltage_source=V_source)
        solver = RungeKutta4Solver(step_size=0.001)
    except ValueError as e:
        print(f"\n[Erro de Configuração]: {e}")
        return

    # 3. Execução da simulação numérica
    time_span = (0.0, 10.0)  # Simula de t=0 até t=10 segundos
    initial_state = np.array([q0, i0])

    print("\nSimulando...")
    t, solution = solver.solve(circuit.state_space_equations, initial_state, time_span)

    charge = solution[:, 0]
    current = solution[:, 1]

    # 4. Apresentação dos resultados (Plotagem)
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, charge, 'b-', label='Carga q(t)')
    plt.title('Resposta do Circuito RLC no Tempo')
    plt.ylabel('Carga (C)')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(t, current, 'r-', label='Corrente i(t)')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Corrente (A)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    print("Simulação concluída! Exibindo gráficos...")
    plt.show()


if __name__ == "__main__":
    main()
