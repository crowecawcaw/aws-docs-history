# Using PennyLane with Amazon Braket

Hybrid algorithms are algorithms that contain both classical and
quantum instructions. The classical instructions are ran on classical
hardware (an EC2 instance or your laptop), and the quantum instructions
are ran either on a simulator or on a quantum computer. We recommend that
you run hybrid algorithms using the Hybrid Jobs feature. For more information,
see [When to use Amazon Braket Jobs](braket-jobs.md#braket-jobs-use "braket-jobs.md#braket-jobs-use").

Amazon Braket enables you to set up and run hybrid quantum algorithms
with the assistance of the **Amazon Braket PennyLane
plugin**, or with the **Amazon Braket
Python SDK** and example notebook repositories. Amazon Braket
example notebooks, based on the SDK, enable you to set up and run certain hybrid
algorithms without the PennyLane plugin. However, we recommend PennyLane because
it provides a richer experience.

**About hybrid quantum algorithms**

Hybrid quantum algorithms are important to the industry today because contemporary quantum computing devices generally produce noise, and therefore, errors. Every quantum gate added to a computation increases the chance of adding noise; therefore, long-running algorithms can be overwhelmed by noise, which results in faulty computation.

Pure quantum algorithms such as Shor's [(Quantum Phase Estimation example)](https://github.com/amazon-braket/amazon-braket-examples/tree/main/examples/advanced_circuits_algorithms/Quantum_Phase_Estimation "https://github.com/amazon-braket/amazon-braket-examples/tree/main/examples/advanced_circuits_algorithms/Quantum_Phase_Estimation") or Grover's [(Grover's example)](https://github.com/aws/amazon-braket-examples/tree/main/examples/advanced_circuits_algorithms/Grover "https://github.com/aws/amazon-braket-examples/tree/main/examples/advanced_circuits_algorithms/Grover") require thousands, or millions, of operations. For this reason, they can be impractical for existing quantum devices, which are generally referred to as _noisy intermediate-scale quantum_ (NISQ) devices.

In hybrid quantum algorithms, quantum processing units (QPUs) work as co-processors for classic CPUs, specifically to speed up certain calculations in a classical algorithm. Circuit executions become much shorter, within reach of the capabilities of today's devices.

###### In this section:

- [Amazon Braket with PennyLane](#pennylane-option "#pennylane-option")
- [Hybrid algorithms in Amazon Braket example notebooks](#braket-hybrid-workflow "#braket-hybrid-workflow")
- [Hybrid algorithms with embedded PennyLane simulators](#hybrid-alorithms-pennylane "#hybrid-alorithms-pennylane")
- [Adjoint gradient on PennyLane with Amazon Braket simulators](#adjoint-gradient-pennylane "#adjoint-gradient-pennylane")
- [Using Hybrid Jobs and PennyLane to run a QAOA algorithm](braket-jobs-run-qaoa-algorithm.md "braket-jobs-run-qaoa-algorithm.md")
- [Run hybrid workloads with PennyLane embedded simulators](pennylane-embedded-simulators.md "pennylane-embedded-simulators.md")

## Amazon Braket with PennyLane

Amazon Braket provides support for [PennyLane](https://pennylane.ai "https://pennylane.ai"),
an open-source software framework built around the concept of _quantum differentiable
programming_. You can use this framework to train quantum circuits in the same
way that you would train a neural network to find solutions for computational problems in
quantum chemistry, quantum machine learning, and optimization.

The PennyLane library provides interfaces to familiar machine learning tools, including PyTorch
and TensorFlow, to make training quantum circuits quick and intuitive.

- **The PennyLane Library** -– PennyLane is pre-installed in Amazon
  Braket notebooks. For access to Amazon
  Braket devices from PennyLane, open a notebook and import the PennyLane library with the following command.

```
import pennylane as qml
```

Tutorial notebooks help you get started quickly. Alternatively, you can use PennyLane on Amazon
Braket from an IDE of your choice.

- **The Amazon
  Braket PennyLane plugin** — To use your own IDE, you can install the Amazon
  Braket PennyLane plugin manually. The plugin connects PennyLane with the [Amazon Braket Python SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python"), so you can run circuits in PennyLane on Amazon
  Braket devices. To install the the PennyLane plugin, use the following command.

```
pip install amazon-braket-pennylane-plugin
```

The following example demonstrates how to set up access to Amazon
Braket devices in PennyLane:

```
# to use SV1
import pennylane as qml
sv1 = qml.device("braket.aws.qubit", device_arn="arn:aws:braket:::device/quantum-simulator/amazon/sv1", wires=2)

# to run a circuit:
@qml.qnode(sv1)
def circuit(x):
    qml.RZ(x, wires=0)
    qml.CNOT(wires=[0,1])
    qml.RY(x, wires=1)
    return qml.expval(qml.PauliZ(1))

result = circuit(0.543)


#To use the local sim:
local = qml.device("braket.local.qubit", wires=2)
```

For tutorial examples and more information about PennyLane, see the [Amazon Braket examples repository](https://github.com/aws/amazon-braket-examples/tree/main/examples/pennylane "https://github.com/aws/amazon-braket-examples/tree/main/examples/pennylane").

The Amazon
Braket PennyLane plugin enables you to switch between Amazon
Braket QPU and embedded simulator devices in PennyLane with a single line of code. It offers two Amazon
Braket quantum devices to work with PennyLane:

- `braket.aws.qubit` for running with the Amazon
  Braket service's quantum devices, including QPUs and simulators
- `braket.local.qubit` for running with the Amazon
  Braket SDK's local simulator

The Amazon
Braket PennyLane plugin is open source. You can install it from the [PennyLane Plugin GitHub repository](https://github.com/aws/amazon-braket-pennylane-plugin-python "https://github.com/aws/amazon-braket-pennylane-plugin-python").

For more information about PennyLane, see the documentation on the [PennyLane website](https://pennylane.ai "https://pennylane.ai").

## Hybrid algorithms in Amazon Braket example notebooks

Amazon Braket does provide a variety of example notebooks that
do not rely on the PennyLane plugin for running hybrid algorithms.
You can get started with any of these
[Amazon Braket
hybrid example notebooks](https://github.com/aws/amazon-braket-examples/tree/main/examples/hybrid_quantum_algorithms "https://github.com/aws/amazon-braket-examples/tree/main/examples/hybrid_quantum_algorithms") that illustrate _variational methods_, such as the
Quantum Approximate Optimization Algorithm (QAOA) or Variational Quantum Eigensolver (VQE).

The Amazon Braket example notebooks rely on the [Amazon Braket Python SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python"). The SDK provides a framework to interact with quantum computing hardware devices through Amazon
Braket. It is an open source library that is designed to assist you with the quantum portion of your hybrid workflow.

You can explore Amazon
Braket further with our [example notebooks](https://github.com/aws/amazon-braket-examples "https://github.com/aws/amazon-braket-examples").

## Hybrid algorithms with embedded PennyLane simulators

Amazon Braket Hybrid Jobs now comes with high performance
CPU- and GPU-based embedded simulators from
[PennyLane](https://github.com/PennyLaneAI/pennylane-lightning "https://github.com/PennyLaneAI/pennylane-lightning").
This family of embedded simulators can be embedded directly
within your hybrid jobs container and includes the fast
state-vector `lightning.qubit` simulator, the
`lightning.gpu` simulator accelerated using NVIDIA's
[cuQuantum library](https://developer.nvidia.com/cuquantum-sdk "https://developer.nvidia.com/cuquantum-sdk"),
and others. These embedded simulators are ideally suited for variational
algorithms such as quantum machine learning that can benefit from advanced methods such as the
[adjoint differentiation method](https://docs.pennylane.ai/en/stable/introduction/interfaces.html#simulation-based-differentiation "https://docs.pennylane.ai/en/stable/introduction/interfaces.html#simulation-based-differentiation").
You can run these embedded simulators on one or multiple CPU or GPU instances.

With Hybrid Jobs, you can now run your variational algorithm code using a combination of a classical co-processor and a QPU, an Amazon
Braket on-demand simulator such as SV1, or directly using the embedded simulator from PennyLane.

The embedded simulator is already available with the Hybrid Jobs container, you need to decorate your main Python
function with the `@hybrid_job` decorator. To use the PennyLane `lightning.gpu` simulator, you also
need to specify a GPU instance in the `InstanceConfig` as shown in the following code snippet:

```
import pennylane as qml
from braket.jobs import hybrid_job
from braket.jobs.config import InstanceConfig


@hybrid_job(device="local:pennylane/lightning.gpu", instance_config=InstanceConfig(instanceType="ml.g4dn.xlarge"))
def function(wires):
    dev = qml.device("lightning.gpu", wires=wires)
    ...
```

Refer to the [example notebook](https://github.com/aws/amazon-braket-examples/blob/main/examples/hybrid_jobs/4_Embedded_simulators_in_Braket_Hybrid_Jobs/Embedded_simulators_in_Braket_Hybrid_Jobs.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/hybrid_jobs/4_Embedded_simulators_in_Braket_Hybrid_Jobs/Embedded_simulators_in_Braket_Hybrid_Jobs.ipynb") to get started with using a PennyLane embedded simulator with Hybrid Jobs.

## Adjoint gradient on PennyLane with Amazon Braket simulators

With the PennyLane plugin for Amazon Braket, you can compute gradients using the adjoint differentiation method when running on the local state vector simulator or SV1.

**Note:** To use the adjoint differentiation method, you must specify `diff_method='device'` in your `qnode`, and **not**
`diff_method='adjoint'`. See the following example.

```
device_arn = "arn:aws:braket:::device/quantum-simulator/amazon/sv1"
dev = qml.device("braket.aws.qubit", wires=wires, shots=0, device_arn=device_arn)

@qml.qnode(dev, diff_method="device")
def cost_function(params):
    circuit(params)
    return qml.expval(cost_h)

gradient = qml.grad(circuit)
initial_gradient = gradient(params0)
```

###### Note

Currently, PennyLane will compute grouping indices for QAOA Hamiltonians and use them to split the Hamiltonian into multiple expectation values. If you want to use SV1's adjoint differentiation capability when running QAOA from PennyLane, you will need reconstruct the cost Hamiltonian by removing the grouping indices, like so: `cost_h, mixer_h = qml.qaoa.max_clique(g, constrained=False)
 cost_h = qml.Hamiltonian(cost_h.coeffs, cost_h.ops)`
