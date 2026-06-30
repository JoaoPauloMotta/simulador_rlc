# Simulador Numérico de Circuito RLC Série

Este repositório contém um simulador de circuito elétrico RLC em série (Resistor, Indutor e Capacitor) desenvolvido com foco em alta maturidade de software. O projeto traduz as equações diferenciais que governam o circuito para o espaço de estados e aplica o método numérico de **Runge-Kutta de 4ª Ordem (RK4)** para resolver a resposta do sistema no tempo.

O grande diferencial deste projeto é a sua **arquitetura sênior**, desenvolvida sob os princípios **SOLID** (notavelmente o Princípio da Responsabilidade Única - SRP) e aplicando tipagem estática robusta (*Type Hinting*).

---

## Arquitetura do Projeto

Ao contrário de scripts acadêmicos tradicionais que misturam a física, a matemática e a interface em um único arquivo, este software foi planejado como um sistema escalável e desacoplado:

```text
simulador_rlc/
│
├── engines/
│   ├── __init__.py        # Inicializador que transforma a pasta em um Pacote Python
│   ├── ode_solver.py      # Motor Numérico Puro (Algoritmo RK4 independente da física)
│   └── rlc_model.py       # Modelo Físico (Traduz as leis de circuitos em equações estocásticas)
│
└── app.py                 # Orquestrador (Interface de terminal com o usuário e plotagem de gráficos)
