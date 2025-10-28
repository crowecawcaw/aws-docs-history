# Testing a quantum task with the local

simulator

You can send quantum tasks directly to a local simulator for rapid prototyping and testing.
This simulator runs in your local environment, so you do not need to specify an Amazon S3
location. The results are computed directly in your session. To run a quantum task on the local
simulator, you must only specify the shots parameter.

###### Note

The execution speed and maximum number of qubits the local
simulator can process depends on the Amazon Braket notebook instance
type, or on your local hardware specifications.

The following commands are all identical and instantiate the state vector (noise
free) local simulator.

```
# Import the LocalSimulator module
from braket.devices import LocalSimulator

# The following are identical commands
device = LocalSimulator()
device = LocalSimulator("default")
device = LocalSimulator(backend="default")
device = LocalSimulator(backend="braket_sv")
```

Then run a quantum task with the following.

```
my_task = device.run(circ, shots=1000)
```

To instantiate the local density matrix (noise) simulator customers change the
backend as follows.

```
# Import the LocalSimulator module
from braket.devices import LocalSimulator

device = LocalSimulator(backend="braket_dm")
```

## Measuring specific qubits on the local simulator

The local state vector simulator and local density matrix simulator support running circuits
where a subset of the circuit's qubits can be measured, which is often called
_partial measurement_.

For example, in the following code you can create a two-qubit circuit and only measure the first qubit by
adding a `measure` instruction with the target qubits to the end of the circuit.

```
# Import the LocalSimulator module
from braket.devices import LocalSimulator

# Use the local simulator device
device = LocalSimulator()

# Define a bell circuit and only measure
circuit = Circuit().h(0).cnot(0, 1).measure(0)

# Run the circuit
task = device.run(circuit, shots=10)

# Get the results
result = task.result()

# Print the measurement counts for qubit 0
print(result.measurement_counts)
```
