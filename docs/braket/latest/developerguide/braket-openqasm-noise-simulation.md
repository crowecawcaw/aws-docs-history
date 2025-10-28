# Simulate noise with OpenQASM 3.0

To simulate noise with OpenQASM3, you use _pragma_ instructions to
add noise operators. For example, to simulate the noisy version of the [GHZ program](braket-openqasm-create-submit-task.md#braket-openqasm-example-program "braket-openqasm-create-submit-task.md#braket-openqasm-example-program") provided previously, you
can submit the following OpenQASM program.

```
// ghz.qasm
// Prepare a GHZ state
OPENQASM 3;

qubit[3] q;
bit[3] c;

h q[0];
#pragma braket noise depolarizing(0.75) q[0] cnot q[0], q[1];
#pragma braket noise depolarizing(0.75) q[0]
#pragma braket noise depolarizing(0.75) q[1] cnot q[1], q[2];
#pragma braket noise depolarizing(0.75) q[0]
#pragma braket noise depolarizing(0.75) q[1]

c = measure q;
```

Specifications for all supported pragma noise operators are provided in the following
list.

```
#pragma braket noise bit_flip(<float in [0,1/2]>) <qubit>
#pragma braket noise phase_flip(<float in [0,1/2]>) <qubit>
#pragma braket noise pauli_channel(<float>, <float>, <float>)  <qubit>
#pragma braket noise depolarizing(<float in [0,3/4]>) <qubit>
#pragma braket noise two_qubit_depolarizing(<float in [0,15/16]>) <qubit>, <qubit>
#pragma braket noise two_qubit_dephasing(<float in [0,3/4]>) <qubit>, <qubit>
#pragma braket noise amplitude_damping(<float in [0,1]>) <qubit>
#pragma braket noise generalized_amplitude_damping(<float in [0,1]> <float in [0,1]>)  <qubit>
#pragma braket noise phase_damping(<float in [0,1]>) <qubit>
#pragma braket noise kraus([[<complex m0_00>, ], ...], [[<complex m1_00>, ], ...], ...) <qubit>[, <qubit>]     // maximum of 2 qubits and maximum of 4 matrices for 1 qubit, 16 for 2

```

## Kraus operator

To generate a Kraus operator, you can iterate through a list of matrices,
printing each element of the matrix as a complex expression.

When using Kraus operators, remember the following:

- The number of qubits must not exceed 2. The [current definition in the schemas](https://github.com/aws/amazon-braket-sdk-python/blob/0d28a8fa89263daf5d88bc706e79200d8dc091a8/src/braket/circuits/noises.py#L811-L814) "https://github.com/aws/amazon-braket-sdk-python/blob/0d28a8fa89263daf5d88bc706e79200d8dc091a8/src/braket/circuits/noises.py#L811-L814)") sets this limit.
- The length of the argument list must be a multiple of 8. This means it must
  be composed only of 2x2 matrices.
- The total length does not exceed 22\*num_qubits
  matrices. This means 4 matrices for 1 qubit and 16 for 2
  qubits.
- All supplied matrices are [completely positive trace preserving (CPTP)](https://github.com/aws/amazon-braket-sdk-python/blob/0d28a8fa89263daf5d88bc706e79200d8dc091a8/src/braket/circuits/quantum_operator_helpers.py#L94-L108 "https://github.com/aws/amazon-braket-sdk-python/blob/0d28a8fa89263daf5d88bc706e79200d8dc091a8/src/braket/circuits/quantum_operator_helpers.py#L94-L108").
- The product of the Kraus operators with their transpose conjugates need to
  add up to an identity matrix.
