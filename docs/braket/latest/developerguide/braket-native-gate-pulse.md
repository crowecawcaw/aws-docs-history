# Accessing native gates using pulses

Researchers often need to know exactly how the _native_ gates supported by a
particular QPU are implemented as pulses. Pulse sequences are carefully calibrated by
hardware providers, but accessing them provides researchers the opportunity to design
better gates or explore protocols for error mitigation such as zero noise extrapolation by
stretching the pulses of specific gates.

Amazon Braket supports programmatic access to native gates from Rigetti.

```
import math
from braket.aws import AwsDevice
from braket.circuits import Circuit, GateCalibrations, QubitSet
from braket.circuits.gates import Rx

device = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3")

calibrations = device.gate_calibrations
print(f"Downloaded {len(calibrations)} calibrations.")
```

###### Note

Hardware providers periodically calibrate the QPU, often more than once a day. The
Braket SDK enables you to obtain the latest gate calibrations.

```
device.refresh_gate_calibrations()
```

To retrieve a given native gate, such as the RX or XY gate, you need to pass the
`Gate` object and the qubits of interest. For example, you can inspect the
pulse implementation of the RX(π/2) applied on qubit 0.

```
rx_pi_2_q0 = (Rx(math.pi/2), QubitSet(0))

pulse_sequence_rx_pi_2_q0 = calibrations.pulse_sequences[rx_pi_2_q0]
```

You can create a filtered set of calibrations using the `filter` function.
You pass a list of gates or a list of `QubitSet`. The following code creates two
sets that contain all of the calibrations for RX(π/2) and for qubit 0.

```
rx_calibrations = calibrations.filter(gates=[Rx(math.pi/2)])
q0_calibrations = calibrations.filter(qubits=QubitSet([0]))
```

Now you can provide or modify the action of native gates by attaching a custom
calibration set. For example, consider the following circuit.

```
bell_circuit = (
    Circuit()
    .rx(0, math.pi/2)
    .rx(1, math.pi/2)
    .iswap(0, 1)
    .rx(1, -math.pi/2)
)
```

You can run it with a custom gate calibration for the `rx` gate on
`qubit 0` by passing a dictionary of `PulseSequence` objects to
the `gate_definitions` keyword argument. You can construct a dictionary from the
attribute `pulse_sequences` of the `GateCalibrations` object. All
gates not specified are replaced with the quantum hardware provider's pulse
calibration.

```
nb_shots = 50
custom_calibration = GateCalibrations({rx_pi_2_q0: pulse_sequence_rx_pi_2_q0})
task = device.run(bell_circuit, gate_definitions=custom_calibration.pulse_sequences, shots=nb_shots)

```
