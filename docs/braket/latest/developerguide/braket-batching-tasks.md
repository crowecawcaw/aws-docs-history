# Running multiple programs

Amazon Braket offers two approaches for running multiple quantum programs efficiently: Program
sets and quantum task batching.

**Program sets** are the preferred way to run workloads with
multiple programs. They allow you to package multiple programs into a single Amazon Braket quantum
task. Program sets provides
[performance improvements](https://aws.amazon.com/blogs/quantum-computing/amazon-braket-introduces-program-sets-enabling-customers-to-run-quantum-programs-up-to-24x-faster/ "https://aws.amazon.com/blogs/quantum-computing/amazon-braket-introduces-program-sets-enabling-customers-to-run-quantum-programs-up-to-24x-faster/")
and cost savings compared to submitting programs individually, especially when the number of program
executions approaches 100.

Currently, IQM and Rigetti devices support program sets. Before
submitting program sets to QPUs, it is recommend to [test on the Amazon Braket Local Simulator](braket-send-to-local-simulator.md "braket-send-to-local-simulator.md")
first. To check whether a device supports program sets, you can view the
[device's properties](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/braket_features/Getting_Devices_and_Checking_Device_Properties.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/braket_features/Getting_Devices_and_Checking_Device_Properties.ipynb") using Amazon Braket
SDK or view the device page in [Amazon Braket Console](https://console.aws.amazon.com/braket/ "https://console.aws.amazon.com/braket/").

The following example shows how to run a program set.

```
from math import pi
from braket.devices import LocalSimulator
from braket.program_sets import ProgramSet
from braket.circuits import Circuit

program_set = ProgramSet([
    Circuit().h(0).cnot(0,1),
    Circuit().rx(0, pi/4).ry(1, pi/8).cnot(1,0),
    Circuit().t(0).t(1).cz(0,1).s(0).cz(1,2).s(1).s(2),
])

device = LocalSimulator()
result = device.run(program_set, shots=300).result()
print(result[0][0].counts)  # The result of the first program in the program set
```

To learn more about different ways of constructing a program set (For example, construct a program
set from many observables or parameters with a single program) and retrieving program set results, see the
[program sets](braket-constructing-circuit.md#braket-program-set "braket-constructing-circuit.md#braket-program-set")
section in the _Amazon Braket Developer Guide_ and the
[program sets folder](https://github.com/amazon-braket/amazon-braket-examples/tree/main/examples/braket_features/program_sets "https://github.com/amazon-braket/amazon-braket-examples/tree/main/examples/braket_features/program_sets")
in the Braket examples Github repository.

**Quantum task batching** is available on every Amazon Braket device.
Batching is especially useful for quantum tasks you run on the on-demand simulators (SV1,
DM1 or TN1) because they can process multiple quantum tasks in parallel.
Batching allows you to launch quantum tasks in parallel. For example, if you wish to make a calculation
that requires 10 quantum tasks and the programs in those quantum tasks are independent of each other,
it is recommended to use task batching. Use quantum task batching when running workloads with multiple
programs on a device that does not support program sets.

The following example shows how to run a batch of quantum tasks.

```
from braket.circuits import Circuit
from braket.devices import LocalSimulator

bell = Circuit().h(0).cnot(0, 1)
circuits = [bell for _ in range(5)]

device = LocalSimulator()
batch = device.run_batch(circuits, shots=100)
print(batch.results()[0].measurement_counts)  # The result of the first quantum task in the batch
```

For more specific information about batching, see the
[Amazon Braket examples](https://github.com/amazon-braket/amazon-braket-examples "https://github.com/amazon-braket/amazon-braket-examples") on
GitHub.

###### In this section:

- [About program set and costs](#braket-program-sets-costs "#braket-program-sets-costs")
- [About quantum task batching and costs](#braket-batching-costs "#braket-batching-costs")
- [Quantum task batching and PennyLane](#braket-batching-pennylane "#braket-batching-pennylane")
- [Task batching and parametrized circuits](#braket-batching-parametrized-circuits "#braket-batching-parametrized-circuits")

## About program set and costs

Program sets efficiently run multiple quantum programs by packaging up to 100 programs or parameter
sets into a single quantum task. With program sets, you pay only one per-task fee plus per-shot fees
based on the total shots across all programs, significantly reducing costs compared to submitting programs
individually. This approach is particularly beneficial for workloads with many programs and with low
number of shots per program. Program sets are currently supported on IQM and Rigetti
devices, as well as the Amazon Braket Local Simulator.

For more information, see the
[Program sets](braket-constructing-circuit.md#braket-program-set "braket-constructing-circuit.md#braket-program-set")
section for detailed implementation steps, best practices, and code examples.

## About quantum task batching and costs

A few caveats to keep in mind regarding quantum task batching and billing costs:

- By default, quantum task batching retries all time out or fail quantum tasks 3 times.
- A batch of long running quantum tasks, such as 34 qubits for
  SV1, can incur large costs. Be sure to double check the
  `run_batch` assignment values carefully before you start a batch
  of quantum tasks. We do not recommend using TN1 with
  `run_batch`.
- TN1 can incur costs for failed rehearsal phase tasks (see [the TN1 description](braket-devices.md#braket-simulator-tn1 "braket-devices.md#braket-simulator-tn1") for more information). Automatic retries can
  add to the cost and so we recommend setting the number of 'max_retries' on
  batching to 0 when using TN1 (see [Quantum Task Batching, Line 186](https://github.com/aws/amazon-braket-sdk-python/blob/4c7c3b28e5a17b8f0cddf94377b7734fcbe2ebfc/src/braket/aws/aws_quantum_task_batch.py#L186 "https://github.com/aws/amazon-braket-sdk-python/blob/4c7c3b28e5a17b8f0cddf94377b7734fcbe2ebfc/src/braket/aws/aws_quantum_task_batch.py#L186")).

## Quantum task batching and PennyLane

Take advantage of batching when you're using PennyLane on
Amazon Braket by setting `parallel = True` when you instantiate an
Amazon Braket device, as shown in the following example.

```
import pennylane as qml

# Define the number of wires (qubits) you want to use
wires = 2  # For example, using 2 qubits

# Define your S3 bucket
my_bucket = "amazon-braket-s3-demo-bucket"
my_prefix = "pennylane-batch-output"
s3_folder = (my_bucket, my_prefix)

device = qml.device("braket.aws.qubit",
                    device_arn="arn:aws:braket:::device/quantum-simulator/amazon/sv1",
                    wires=wires,
                    s3_destination_folder=s3_folder,
                    parallel=True)
```

For more information about batching with PennyLane, see [Parallelized optimization of quantum circuits](https://github.com/aws/amazon-braket-examples/blob/main/examples/pennylane/1_Parallelized_optimization_of_quantum_circuits/1_Parallelized_optimization_of_quantum_circuits.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/pennylane/1_Parallelized_optimization_of_quantum_circuits/1_Parallelized_optimization_of_quantum_circuits.ipynb").

## Task batching and parametrized circuits

When submitting a quantum task batch that contains parametrized circuits, you can either
provide an `inputs` dictionary, which is used for all quantum tasks in the batch,
or a `list` of input dictionaries, in which case the `i`-th
dictionary is paired with the `i`-th task, as shown in the following
example.

```
from braket.circuits import Circuit, FreeParameter, Observable
from braket.aws import AwsQuantumTaskBatch, AwsDevice

# Define your quantum device
device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")

# Create the free parameters
alpha = FreeParameter('alpha')
beta = FreeParameter('beta')

# Create two circuits
circ_a = Circuit().rx(0, alpha).ry(1, alpha).cnot(0, 2).xx(0, 2, beta)
circ_a.variance(observable=Observable.Z(), target=0)

circ_b = Circuit().rx(0, alpha).rz(1, alpha).cnot(0, 2).zz(0, 2, beta)
circ_b.expectation(observable=Observable.Z(), target=2)

# Use the same inputs for both circuits in one batch
tasks = device.run_batch([circ_a, circ_b], inputs={'alpha': 0.1, 'beta': 0.2})

# Or provide each task its own set of inputs
inputs_list = [{'alpha': 0.3, 'beta': 0.1}, {'alpha': 0.1, 'beta': 0.4}]

tasks = device.run_batch([circ_a, circ_b], inputs=inputs_list)
```

You can also prepare a list of input dictionaries for a single parametric
circuit and submit them as a quantum task batch. If there is N input dictionaries
in the list, the batch contains N quantum task. The `i`-th quantum task corresponds to
the circuit executed with `i`-th input dictionary.

```
from braket.circuits import Circuit, FreeParameter

# Create a parametric circuit
circ = Circuit().rx(0, FreeParameter('alpha'))

# Provide a list of inputs to execute with the circuit
inputs_list = [{'alpha': 0.1}, {'alpha': 0.2}, {'alpha': 0.3}]

tasks = device.run_batch(circ, inputs=inputs_list, shots=100)
```
