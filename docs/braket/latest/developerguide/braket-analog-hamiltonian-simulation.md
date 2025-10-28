# Analog Hamiltonian Simulation

[Analog Hamiltonian
Simulation](https://en.wikipedia.org/wiki/Hamiltonian_simulation "https://en.wikipedia.org/wiki/Hamiltonian_simulation") (AHS) is an emerging paradigm in quantum computing that differs significantly
from the traditional quantum circuit model. Instead of a sequence of gates, where each circuit acts only on a couple of qubits at a
time. An AHS program is defined by the time-dependent and space-dependent parameters of the
Hamiltonian in question. The [Hamiltonian of a
system](<https://en.wikipedia.org/wiki/Hamiltonian_(quantum_mechanics)> "https://en.wikipedia.org/wiki/Hamiltonian_(quantum_mechanics)") encodes its energy levels and the effects of external forces, which
together govern the time evolution of its states. For an N-qubit systems, the
Hamiltonian can be represented by a
2NX2N square matrix of complex numbers.

Quantum devices capable of performing AHS are designed to closely approximate the time evolution of
a quantum system under a custom Hamiltonian by carefully tuning their internal control parameters.
Such as, adjusting the amplitude and detuning parameters of a coherent driving field. The AHS paradigm is well-suited for
simulating the static and dynamic properties of quantum systems with many interacting particles,
such as in condensed matter physics or quantum chemistry. Purpose-built quantum processing units (QPUs), like the [Aquila device](https://aws.amazon.com/braket/quantum-computers/quera/ "https://aws.amazon.com/braket/quantum-computers/quera/")
from QuEra, have been developed to use the power of AHS
and tackle problems beyond the reach of conventional digital quantum computing approaches in innovative ways.

###### In this section:

- [Hello AHS: Run your first Analog Hamiltonian
  Simulation](braket-get-started-hello-ahs.md "braket-get-started-hello-ahs.md")
- [Submit an analog program using QuEra Aquila](braket-quera-submitting-analog-program-aquila.md "braket-quera-submitting-analog-program-aquila.md")
