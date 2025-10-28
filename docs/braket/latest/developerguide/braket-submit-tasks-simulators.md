# Submitting quantum tasks to simulators

Amazon Braket provides access to several simulators that can test your quantum
tasks. You can submit quantum tasks individually or you can
[run multiple programs](braket-batching-tasks.md "braket-batching-tasks.md").

**Simulators**

- **Density matrix simulator, DM1** : `arn:aws:braket:::device/quantum-simulator/amazon/dm1`
- **State vector simulator, SV1** : `arn:aws:braket:::device/quantum-simulator/amazon/sv1`
- **Tensor network simulator, TN1** : `arn:aws:braket:::device/quantum-simulator/amazon/tn1`
- **The local simulator** :
  `LocalSimulator()`

###### Note

You can cancel quantum tasks in the `CREATED` state for QPUs and on-demand
simulators. You can cancel quantum tasks in the `QUEUED` state on a best-effort basis
for on-demand simulators and QPUs. Note that QPU `QUEUED` quantum tasks are unlikely
to be cancelled successfully during QPU availability windows.

###### In this section:

- [Local state vector simulator
  (braket_sv)](#braket-simulator-sv "#braket-simulator-sv")
- [Local density matrix simulator
  (braket_dm)](#braket-simulator-dm "#braket-simulator-dm")
- [Local AHS simulator
  (braket_ahs)](#braket-simulator-ahs-local "#braket-simulator-ahs-local")
- [State vector simulator (SV1)](#braket-simulator-sv1 "#braket-simulator-sv1")
- [Density matrix simulator
  (DM1)](#braket-simulator-dm1 "#braket-simulator-dm1")
- [Tensor network simulator
  (TN1)](#braket-simulator-tn1 "#braket-simulator-tn1")
- [About embedded simulators](embedded-simulator.md "embedded-simulator.md")
- [Compare Amazon Braket simulators](choose-a-simulator.md "choose-a-simulator.md")
- [Example quantum tasks on Amazon Braket](braket-submit-tasks-to-braket.md "braket-submit-tasks-to-braket.md")
- [Testing a quantum task with the local
  simulator](braket-send-to-local-simulator.md "braket-send-to-local-simulator.md")

## Local state vector simulator

(`braket_sv`)

The local state vector simulator (`braket_sv`) is part of the
Amazon Braket SDK that runs locally in your environment. It is
well-suited for rapid prototyping on small circuits (up to 25 qubits)
depending on the hardware specifications of your Braket notebook instance or your local
environment.

The local simulator supports all gates in the Amazon Braket SDK, but
QPU devices support a smaller subset. You can find the supported gates of a device in the
device properties.

###### Note

The local simulator supports advanced OpenQASM features which may not be supported on
QPU devices or other simulators. For more information on supported features, see the
examples provided in the [OpenQASM Local Simulator notebook](https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Simulating_Advanced_OpenQASM_Programs_with_the_Local_Simulator.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Simulating_Advanced_OpenQASM_Programs_with_the_Local_Simulator.ipynb").

For more information about how to work with simulators, see [the Amazon Braket examples](https://github.com/aws/amazon-braket-examples/blob/main/examples/getting_started/1_Running_quantum_circuits_on_simulators/1_Running_quantum_circuits_on_simulators.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/getting_started/1_Running_quantum_circuits_on_simulators/1_Running_quantum_circuits_on_simulators.ipynb").

## Local density matrix simulator

(`braket_dm`)

The local density matrix simulator (`braket_dm`) is part of the
Amazon Braket SDK that runs locally in your environment. It is
well-suited for rapid prototyping on small circuits with noise (up to 12
qubits) depending on the hardware specifications of your Braket
notebook instance or your local environment.

You can build common noisy circuits from the ground up using gate noise operations such
as bit-flip and depolarizing error. You can also apply noise operations to specific
qubits and gates of existing circuits that are intended to run both with
and without noise.

The `braket_dm` local simulator can provide the following results, given the
specified number of shots:

- Reduced density matrix: Shots = 0

###### Note

The local simulator supports advanced OpenQASM features, which may not be supported
on QPU devices or other simulators. For more information about supported features, see
the examples provided in the [OpenQASM Local Simulator notebook](https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Simulating_Advanced_OpenQASM_Programs_with_the_Local_Simulator.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Simulating_Advanced_OpenQASM_Programs_with_the_Local_Simulator.ipynb").

To learn more about the local density matrix simulator, see [the Braket introductory noise simulator example](https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Simulating_Noise_On_Amazon_Braket.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Simulating_Noise_On_Amazon_Braket.ipynb").

## Local AHS simulator

(`braket_ahs`)

The local AHS (Analog Hamiltonian Simulation) simulator (`braket_ahs`) is
part of the Amazon Braket SDK that runs locally in your environment. It can be used to
simulate results from an AHS program. It is well-suited for prototyping on small registers
(up to 10-12 atoms) depending on the hardware specifications of your Braket notebook
instance or your local environment.

The local simulator supports AHS programs with one uniform driving field, one
(non-uniform) shifting field, and arbitrary atom arrangements. For details, refer to
the Braket [AHS class](https://github.com/aws/amazon-braket-sdk-python/blob/main/src/braket/ahs/analog_hamiltonian_simulation.py#L29 "https://github.com/aws/amazon-braket-sdk-python/blob/main/src/braket/ahs/analog_hamiltonian_simulation.py#L29") and the Braket [AHS program schema](https://github.com/aws/amazon-braket-schemas-python/blob/main/src/braket/ir/ahs/program_v1.py "https://github.com/aws/amazon-braket-schemas-python/blob/main/src/braket/ir/ahs/program_v1.py").

To learn more about the local AHS simulator, see the [Hello AHS: Run your first Analog Hamiltonian
Simulation](braket-get-started-hello-ahs.md "braket-get-started-hello-ahs.md") page and the [Analog Hamiltonian Simulation example notebooks](https://github.com/aws/amazon-braket-examples/tree/main/examples/analog_hamiltonian_simulation "https://github.com/aws/amazon-braket-examples/tree/main/examples/analog_hamiltonian_simulation").

## State vector simulator (SV1)

SV1 is an on-demand, high-performance, universal state vector simulator. It
can simulate circuits of up to 34 qubits. You can expect a
34-qubit, dense, and square circuit (circuit depth = 34) to take
approximately 1–2 hours to complete, depending on the type of gates used and other factors.
Circuits with all-to-all gates are well suited for SV1. It returns results
in forms such as a full state vector or an array of amplitudes.

SV1 has a maximum runtime of 6 hours. It has a default of 35 concurrent
quantum tasks, and a maximum of 100 (50 in us-west-1 and eu-west-2) concurrent quantum tasks.

**SV1 results**

SV1 can provide the following results, given the specified number of
shots:

- Sample: Shots > 0
- Expectation: Shots >= 0
- Variance: Shots >= 0
- Probability: Shots > 0
- Amplitude: Shots = 0
- Adjoint Gradient: Shots = 0

For more about results, see [Result types](braket-result-types.md "braket-result-types.md").

SV1 is always available, it runs your circuits on demand, and it can run
multiple circuits in parallel. The runtime scales linearly with the number of operations
and exponentially with the number of qubits. The number of
shots has a small impact on the runtime. To learn more, visit [Compare simulators](braket-devices.md#choose-a-simulator "braket-devices.md#choose-a-simulator").

Simulators support all gates in the Braket SDK, but QPU devices support a smaller
subset. You can find the supported gates of a device in the device properties.

## Density matrix simulator

(DM1)

DM1 is an on-demand, high-performance, density matrix simulator. It can
simulate circuits of up to 17 qubits.

DM1 has a maximum runtime of 6 hours, a default of 35 concurrent quantum tasks, and
a maximum of 50 concurrent quantum tasks.

**DM1 results**

DM1 can provide the following results, given the specified number of
shots:

- Sample: Shots > 0
- Expectation: Shots >= 0
- Variance: Shots >= 0
- Probability: Shots > 0
- Reduced density matrix: Shots = 0, up to max 8
  qubits

For more information about results, see [Result types](braket-result-types.md "braket-result-types.md").

DM1 is always available, it runs your circuits on demand, and it can run
multiple circuits in parallel. The runtime scales linearly with the number of operations
and exponentially with the number of qubits. The number of
shots has a small impact on the runtime. To learn more, see [Compare simulators](braket-devices.md#choose-a-simulator "braket-devices.md#choose-a-simulator").

**Noise gates and limitations**

```
AmplitudeDamping
    Probability has to be within [0,1]
BitFlip
    Probability has to be within [0,0.5]
Depolarizing
    Probability has to be within [0,0.75]
GeneralizedAmplitudeDamping
    Probability has to be within [0,1]
PauliChannel
    The sum of the probabilities has to be within [0,1]
Kraus
    At most 2 qubits
    At most 4 (16) Kraus matrices for 1 (2) qubit
PhaseDamping
    Probability has to be within [0,1]
PhaseFlip
    Probability has to be within [0,0.5]
TwoQubitDephasing
    Probability has to be within [0,0.75]
TwoQubitDepolarizing
    Probability has to be within [0,0.9375]
```

## Tensor network simulator

(TN1)

TN1 is an on-demand, high-performance, tensor network simulator.
TN1 can simulate certain circuit types with up to 50
qubits and a circuit depth of 1,000 or smaller. TN1 is
particularly powerful for sparse circuits, circuits with local gates, and other circuits
with special structure, such as quantum Fourier transform (QFT) circuits.
TN1 operates in two phases. First, the _rehearsal
phase_ attempts to identify an efficient computational path for your circuit,
so TN1 can estimate the runtime of the next stage, which is called the
_contraction phase_. If the estimated contraction time exceeds the
TN1 simulation runtime limit, TN1 does not attempt
contraction.

TN1 has a runtime limit of 6 hours. It is limited to a maximum of 10 (5 in
eu-west-2) concurrent quantum tasks.

**TN1 results**

The contraction phase consists of a series of matrix multiplications. The series of
multiplications continues until a result is reached or until it is determined that a result
cannot be reached.

**Note**: Shots must be > 0.

Result types include:

- Sample
- Expectation
- Variance

For more about results, see [Result types](braket-result-types.md "braket-result-types.md").

TN1 is always available, it runs your circuits on demand, and it can run
multiple circuits in parallel. To learn more, see [Compare simulators](braket-devices.md#choose-a-simulator "braket-devices.md#choose-a-simulator").

Simulators support all gates in the Braket SDK, but QPU devices support a smaller
subset. You can find the supported gates of a device in the device properties.

Visit the Amazon Braket GitHub repository for a [TN1 example notebook](https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Using_the_tensor_network_simulator_TN1.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Using_the_tensor_network_simulator_TN1.ipynb") to help you get started with TN1.

**Best practices for working with TN1**

- Avoid all-to-all circuits.
- Test a new circuit or class of circuits with a small number of
  shots, to learn the circui's "hardness" for
  TN1.
- Split large shot simulations over multiple quantum tasks.
