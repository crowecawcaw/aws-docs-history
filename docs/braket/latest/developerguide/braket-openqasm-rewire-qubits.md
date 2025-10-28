# Qubit rewiring with OpenQASM 3.0

Amazon Braket supports the physical qubit notation
within OpenQASM on Rigetti devices (to learn more see this [page](https://github.com/openqasm/openqasm/blob/main/source/language/types.rst "https://github.com/openqasm/openqasm/blob/main/source/language/types.rst")). When using physical qubits with the [naive rewiring
strategy](https://pyquil-docs.rigetti.com/en/v2.28.1/compiler.html#naive "https://pyquil-docs.rigetti.com/en/v2.28.1/compiler.html#naive"), ensure that the qubits are connected on the selected
device. Alternatively, if qubit registers are used instead, the PARTIAL
rewiring strategy is enabled by default on Rigetti devices.

```
// ghz.qasm
// Prepare a GHZ state
OPENQASM 3;

h $0;
cnot $0, $1;
cnot $1, $2;

measure $0;
measure $1;
measure $2;
```
