# Submitting quantum tasks to QPUs

Amazon Braket provides access to several devices that can run quantum
tasks. You can submit quantum tasks individually or you can set up
[quantum task batching](braket-batching-tasks.md "braket-batching-tasks.md").

**Quantum processing units (QPUs)**

You can submit quantum tasks to QPUs at any time, but the task runs within certain availability
windows that are displayed on the **Devices** page of the
Amazon Braket console. You can retrieve the results of the quantum task with
the quantum task ID, which is introduced in the next section.

- **AQT IBEX-Q1** : `arn:aws:braket:eu-north-1::device/qpu/aqt/Ibex-Q1`
- **IonQ Aria-1** : `arn:aws:braket:us-east-1::device/qpu/ionq/Aria-1`
- **IonQ Forte-1** : `arn:aws:braket:us-east-1::device/qpu/ionq/Forte-1`
- **IonQ Forte-Enterprise-1** : `arn:aws:braket:us-east-1::device/qpu/ionq/Forte-Enterprise-1`
- **IQM Garnet** : `arn:aws:braket:eu-north-1::device/qpu/iqm/Garnet`
- **IQM Emerald** : `arn:aws:braket:eu-north-1::device/qpu/iqm/Emerald`
- **QuEra
  Aquila** : `arn:aws:braket:us-east-1::device/qpu/quera/Aquila`
- **Rigetti Ankaa-3** : `arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3`

###### Note

You can cancel quantum tasks in the `CREATED` state for QPUs and on-demand
simulators. You can cancel quantum tasks in the `QUEUED` state on a best-effort basis
for on-demand simulators and QPUs. Note that QPU `QUEUED` quantum tasks are unlikely
to be cancelled successfully during QPU availability windows.

###### In this section:

- [AQT](#braket-qpu-partner-aqt "#braket-qpu-partner-aqt")
- [IonQ](#braket-qpu-partner-ionq "#braket-qpu-partner-ionq")
- [IQM](#braket-qpu-partner-iqm "#braket-qpu-partner-iqm")
- [Rigetti](#braket-qpu-partner-rigetti "#braket-qpu-partner-rigetti")
- [QuEra](#braket-qpu-partner-quera "#braket-qpu-partner-quera")
- [Example: Submitting a quantum task to a QPU](braket-submit-to-qpu.md "braket-submit-to-qpu.md")
- [Inspecting compiled circuits](braket-compiled-circuits-inspecting.md "braket-compiled-circuits-inspecting.md")

## AQT

AQT's IBEX-Q1 QPU is based on a crystal of 40Ca+
ions in a macroscopic radio frequency trap sitting in ultra-high vacuum chamber.
The device runs at room temperature and fits into two 19-inch datacenter compatible racks.

High-fidelity gates are enabled by the low heating rates of the trap and the use of a direct
optical transition for qubit rotation. The qubit transition is driven by a narrow linewidth laser
with a very high relative frequency stability. The qubits also feature efficient state preparation
and readout through optical shelfing. All-to-all connectivity is achieved by the long-range Coulomb
interaction in the ion crystal. Single-ion addressing and readout are achieved by use of a high
numerical aperture lens.

The AQT device support the following quantum gates.

```
'ccnot', 'cnot', 'cphaseshift', 'cphaseshift00', 'cphaseshift01', 'cphaseshift10', 'cswap', 'swap', 'iswap', 'pswap', 'ecr', 'cy', 'cz', 'xy', 'xx', 'yy', 'zz', 'h', 'i', 'phaseshift', 'rx', 'ry', 'rz', 's', 'si', 't', 'ti', 'v', 'vi', 'x', 'y', 'z', 'prx'
```

With verbatim compilation, the AQT device supports the following native
gates.

```
'prx', 'xx', 'rz'
```

###### Note

The following describes equivalent gates between AQT native gates and Amazon Braket:

- The AQT Mølmer-Sørensen (MS or RXX) gate corresponds to Braket's `'xx'` gate
- The AQT R gate corresponds to Braket's `'prx'` gate
- The `'rz'` gate naming is the same

## IonQ

IonQ offers gate-based QPUs based on ion trap technology.
IonQ's trapped ion QPUs are built on a chain of trapped 171Yb+ ions that
are spatially confined by means of a microfabricated surface electrode trap within a vacuum
chamber.

IonQ devices support the following quantum gates.

```
'x', 'y', 'z', 'rx', 'ry', 'rz', 'h', 'cnot', 's', 'si', 't', 'ti', 'v', 'vi', 'xx', 'yy', 'zz', 'swap'
```

With verbatim compilation, the IonQ QPUs support the following native
gates.

```
'gpi', 'gpi2', 'ms'
```

If you only specify two phase parameters when using the native MS gate, a fully-
entangling MS gate runs. A fully-entangling MS gate always performs a π/2 rotation. To
specify a different angle and run a partially-entangling MS gate, you specify the desired
angle by adding a third parameter. For more information, see the [braket.circuits.gate module](https://amazon-braket-sdk-python.readthedocs.io/en/latest/_apidoc/braket.circuits.gate.html "https://amazon-braket-sdk-python.readthedocs.io/en/latest/_apidoc/braket.circuits.gate.html").

These native gates can only be used with verbatim compilation. To learn more about
verbatim compilation, see [Verbatim Compilation](braket-constructing-circuit.md#verbatim-compilation "braket-constructing-circuit.md#verbatim-compilation").

## IQM

IQM quantum processors are universal gate-model devices based on
superconducting transmon qubits. The IQM Garnet is a 20-qubit
device, while IQM Emerald is a 54-qubit device. Both these devices use
a square lattice topology, also known as a Crystal lattice topology.

The IQM devices support the following quantum gates.

```
"ccnot", "cnot", "cphaseshift", "cphaseshift00", "cphaseshift01", "cphaseshift10", "cswap", "swap", "iswap", "pswap", "ecr", "cy", "cz", "xy", "xx", "yy", "zz", "h", "i", "phaseshift", "rx", "ry", "rz", "s", "si", "t", "ti", "v", "vi", "x", "y", "z"
```

With verbatim compilation, the IQM devices support the following native
gates.

```
'cz', 'prx'
```

## Rigetti

Rigetti quantum processors are universal, gate-model machines based on
all-tunable superconducting qubits.

- The Ankaa-3 system is an 84-qubit device that utilizes
  scalable multi-chip technology.

The Rigetti device supports the following quantum gates.

```
'cz', 'xy', 'ccnot', 'cnot', 'cphaseshift', 'cphaseshift00', 'cphaseshift01', 'cphaseshift10', 'cswap', 'h', 'i', 'iswap', 'phaseshift', 'pswap', 'rx', 'ry', 'rz', 's', 'si', 'swap', 't', 'ti', 'x', 'y', 'z'
```

With verbatim compilation, Ankaa-3 supports the following native gates.

```
'rx', 'rz', 'iswap'
```

Rigetti superconducting quantum processors can run the 'rx' gate with only
the angles of ±π/2 or ±π.

Pulse-level control is available on the Rigetti devices, which support a set of predefined
frames of the following types for the Ankaa-3 system.

```
`flux_tx`, `charge_tx`, `readout_rx`, `readout_tx`
```

## QuEra

QuEra offers neutral-atom based devices that can run Analog Hamiltonian
Simulation (AHS) quantum tasks. These special-purpose devices faithfully reproduce the
time-dependent quantum dynamics of hundreds of simultaneously interacting qubits.

One can program these devices in the paradigm of Analog Hamiltonian Simulation by
prescribing the layout of the qubit register and the temporal and spatial dependence of the
manipulating fields. Amazon Braket provides utilities to construct such programs through the AHS
module of the python SDK, `braket.ahs`.

For more information, see the [Analog Hamiltonian Simulation example notebooks](https://github.com/aws/amazon-braket-examples/tree/main/examples/analog_hamiltonian_simulation "https://github.com/aws/amazon-braket-examples/tree/main/examples/analog_hamiltonian_simulation") or the [Submit an analog program using
QuEra's Aquila](braket-quera-submitting-analog-program-aquila.md "braket-quera-submitting-analog-program-aquila.md") page.
