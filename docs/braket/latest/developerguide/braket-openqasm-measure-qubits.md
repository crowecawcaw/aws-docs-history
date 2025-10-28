# Measuring specific qubits with OpenQASM 3.0

The local state vector simulator and local density matrix simulator provided by Amazon Braket support the
submission of OpenQASM programs where a subset of the circuit's qubits can be selectively measured.
This capability, often referred to as partial measurement, allows for more targeted and efficient quantum computations.
For example, in the following code snippet, you can create a two-qubit circuit and choose to only measure the first
qubit, while leaving the second qubit unmeasured.

```
partial_measure_qasm = """
OPENQASM 3.0;
bit[1] b;
qubit[2] q;
h q[0];
cnot q[0], q[1];
b[0] = measure q[0];
"""
```

In this example, we have a quantum circuit with two qubits, `q[0]` and `q[1]`,
but we are only interested in measuring the state of the first qubit. This is achieved by the line
`b[0] = measure q[0]`, which measures the state of qubit[0] and stores the result in the
classical bit b[0]. To run this partial measurement scenario, we can run the following code on the
local state vector simulator provided by Amazon Braket.

```
from braket.devices import LocalSimulator

local_sim = LocalSimulator()
partial_measure_local_sim_task = local_sim.run(OpenQASMProgram(source=partial_measure_qasm), shots = 10)
partial_measure_local_sim_result = partial_measure_local_sim_task.result()
print(partial_measure_local_sim_result.measurement_counts)
print("Measured qubits: ", partial_measure_local_sim_result.measured_qubits)
```

You can check whether a device supports partial measurement by inspecting the `requiresAllQubitsMeasurement` field
in its action properties; if it is `False`, then partial measurement is supported.

```
from braket.devices import Devices

AwsDevice(Devices.Rigetti.Ankaa3).properties.action['braket.ir.openqasm.program'].requiresAllQubitsMeasurement
```

Here, `requiresAllQubitsMeasurement` is `False`, which indicates that not all qubits must be measured.
