# Inspecting the circuit

Quantum circuits in Amazon Braket have a pseudo-time concept called
`Moments`. Each qubit can experience a single gate per
`Moment`. The purpose of `Moments` is to make circuits and
their gates easier to address and to provide a temporal structure.

###### Note

Moments generally do not correspond to the real time at which gates are executed
on a QPU.

The depth of a circuit is given by the total number of Moments in that circuit. You
can view the circuit depth calling the method `circuit.depth` as shown in the
following example.

```
from braket.circuits import Circuit

# Define a circuit with parametrized gates
circ = Circuit().rx(0, 0.15).ry(1, 0.2).cnot(0, 2).zz(1, 3, 0.15).x(0)
print(circ)
print('Total circuit depth:', circ.depth)
```

```
T  : │     0      │        1         │  2  │
      ┌──────────┐                    ┌───┐
q0 : ─┤ Rx(0.15) ├───●────────────────┤ X ├─
      └──────────┘   │                └───┘
      ┌──────────┐   │   ┌──────────┐
q1 : ─┤ Ry(0.20) ├───┼───┤ ZZ(0.15) ├───────
      └──────────┘   │   └────┬─────┘
                   ┌─┴─┐      │
q2 : ──────────────┤ X ├──────┼─────────────
                   └───┘      │
                         ┌────┴─────┐
q3 : ────────────────────┤ ZZ(0.15) ├───────
                         └──────────┘
T  : │     0      │        1         │  2  │
Total circuit depth: 3
```

The total circuit depth of the circuit above is 3 (shown as moments `0`,
`1`, and `2`). You can check the gate operation for each
moment.

`Moments` functions as a dictionary of _key-value_
pairs.

- The key is `MomentsKey()`, which contains pseudo-time and
  qubit information.
- The value is assigned in the type of `Instructions()`.

```
moments = circ.moments
for key, value in moments.items():
    print(key)
    print(value, "\n")
```

```
MomentsKey(time=0, qubits=QubitSet([Qubit(0)]), moment_type=<MomentType.GATE: 'gate'>, noise_index=0, subindex=0)
Instruction('operator': Rx('angle': 0.15, 'qubit_count': 1), 'target': QubitSet([Qubit(0)]), 'control': QubitSet([]), 'control_state': (), 'power': 1)

MomentsKey(time=0, qubits=QubitSet([Qubit(1)]), moment_type=<MomentType.GATE: 'gate'>, noise_index=0, subindex=0)
Instruction('operator': Ry('angle': 0.2, 'qubit_count': 1), 'target': QubitSet([Qubit(1)]), 'control': QubitSet([]), 'control_state': (), 'power': 1)

MomentsKey(time=1, qubits=QubitSet([Qubit(0), Qubit(2)]), moment_type=<MomentType.GATE: 'gate'>, noise_index=0, subindex=0)
Instruction('operator': CNot('qubit_count': 2), 'target': QubitSet([Qubit(0), Qubit(2)]), 'control': QubitSet([]), 'control_state': (), 'power': 1)

MomentsKey(time=1, qubits=QubitSet([Qubit(1), Qubit(3)]), moment_type=<MomentType.GATE: 'gate'>, noise_index=0, subindex=0)
Instruction('operator': ZZ('angle': 0.15, 'qubit_count': 2), 'target': QubitSet([Qubit(1), Qubit(3)]), 'control': QubitSet([]), 'control_state': (), 'power': 1)

MomentsKey(time=2, qubits=QubitSet([Qubit(0)]), moment_type=<MomentType.GATE: 'gate'>, noise_index=0, subindex=0)
Instruction('operator': X('qubit_count': 1), 'target': QubitSet([Qubit(0)]), 'control': QubitSet([]), 'control_state': (), 'power': 1)
```

You can also add gates to a circuit through `Moments`.

```
from braket.circuits import Instruction, Gate

new_circ = Circuit()
instructions = [Instruction(Gate.S(), 0),
                Instruction(Gate.CZ(), [1, 0]),
                Instruction(Gate.H(), 1)
                ]

new_circ.moments.add(instructions)
print(new_circ)
```

```
T  : │  0  │  1  │  2  │
      ┌───┐ ┌───┐
q0 : ─┤ S ├─┤ Z ├───────
      └───┘ └─┬─┘
              │   ┌───┐
q1 : ─────────●───┤ H ├─
                  └───┘
T  : │  0  │  1  │  2  │
```
