# Troubleshooting OpenQASM

This section provides troubleshooting pointers that might be useful when encountering errors using OpenQASM 3.0.

###### In this section:

- [Include statement error](#braket-troubleshooting-openqasm-include-statement-error "#braket-troubleshooting-openqasm-include-statement-error")
- [Non-contiguous qubits error](#braket-troubleshooting-openqasm-non-contiguous-qubits-error "#braket-troubleshooting-openqasm-non-contiguous-qubits-error")
- [Mixing physical qubits with virtual qubits error](#braket-troubleshooting-openqasm-mixing-physical-and-virtual-qubits-error "#braket-troubleshooting-openqasm-mixing-physical-and-virtual-qubits-error")
- [Requesting result types and measuring qubits in the same program error](#braket-troubleshooting-openqasm-result-types-measuring-qubits-error "#braket-troubleshooting-openqasm-result-types-measuring-qubits-error")
- [Classical and qubit register limits exceeded error](#braket-troubleshooting-openqasm-register-limits-error "#braket-troubleshooting-openqasm-register-limits-error")
- [Box not preceded by a verbatim pragma error](#braket-troubleshooting-openqasm-box-not-preceded-by-pragma-error "#braket-troubleshooting-openqasm-box-not-preceded-by-pragma-error")
- [Verbatim boxes missing native gates error](#braket-troubleshooting-openqasm-verbatim-box-missing-native-gates-error "#braket-troubleshooting-openqasm-verbatim-box-missing-native-gates-error")
- [Verbatim boxes missing physical qubits error](#braket-troubleshooting-openqasm-verbatim-box-missing-physical-qubits-error "#braket-troubleshooting-openqasm-verbatim-box-missing-physical-qubits-error")
- [The verbatim pragma is missing "braket" error](#braket-troubleshooting-openqasm-pragma-naming-error "#braket-troubleshooting-openqasm-pragma-naming-error")
- [Single qubits cannot be indexed error](#braket-troubleshooting-openqasm-qubit-index-error "#braket-troubleshooting-openqasm-qubit-index-error")
- [The physical qubits
  in a two qubit gate are not connected error](#braket-troubleshooting-openqasm-disconnected-physical-qubits-error "#braket-troubleshooting-openqasm-disconnected-physical-qubits-error")
- [Local simulator support warning](#braket-troubleshooting-openqasm-local-simulator-support-warning "#braket-troubleshooting-openqasm-local-simulator-support-warning")

## Include statement error

Braket currently doesn't have a standard gate library file to be included in OpenQASM programs. For example, the following example raises a parser error.

```
OPENQASM 3;
include "standardlib.inc";
```

This code generates the error message: `No terminal matches '"' in the current parser context, at line 2 col 17.`

## Non-contiguous qubits error

Using non-contiguous qubits on devices that `requiresContiguousQubitIndices`
be set to `true` in the device capability result in an error.

When running quantum tasks on simulators and IonQ, the following program triggers the error.

```
OPENQASM 3;

qubit[4] q;

h q[0];
cnot q[0], q[2];
cnot q[0], q[3];
```

This code generates the error message: `Device requires contiguous qubits. Qubit register q has unused qubits q[1], q[4].`

## Mixing physical qubits with virtual qubits error

Mixing physical qubits with virtual qubits in the same
program is not allowed and results in an error. The following code generates the error.

```
OPENQASM 3;

qubit[2] q;
cnot q[0], $1;
```

This code generates the error message: `[line 4] mixes physical qubits and qubits registers.`

## Requesting result types and measuring qubits in the same program error

Requesting result types and that qubits are explicitly measured
in the same program results in an error. The following code generates the error.

```
OPENQASM 3;

qubit[2] q;

h q[0];
cnot q[0], q[1];
measure q;

#pragma braket result expectation x(q[0]) @ z(q[1])
```

This code generates the error message: `Qubits should not be explicitly measured when result types are requested.`

## Classical and qubit register limits exceeded error

Only one classical register and one qubit register are allowed. The following code generates the error.

```
OPENQASM 3;

qubit[2] q0;
qubit[2] q1;
```

This code generates the error message: `[line 4] cannot declare a qubit register. Only 1 qubit register is supported.`

## Box not preceded by a verbatim pragma error

All boxes must be preceded by a verbatim pragma. The following code generates the error.

```
box{
rx(0.5) $0;
}
```

This code generates the error message: `In verbatim boxes, native gates are required. x is not a device native gate.`

## Verbatim boxes missing native gates error

Verbatim boxes should have native gates and physical qubits. The following code generates the native gates error.

```
#pragma braket verbatim
box{
x $0;
}
```

This code generates the error message: `In verbatim boxes, native gates are required. x is not a device native gate.`

## Verbatim boxes missing physical qubits error

Verbatim boxes must have physical qubits. The following code generates the missing physical qubits error.

```
qubit[2] q;

#pragma braket verbatim
box{
rx(0.1) q[0];
}
```

This code generates the error message: `Physical qubits are required in verbatim box.`

## The verbatim pragma is missing "braket" error

You must include “braket” in the verbatim pragma. The following code generates the error.

```
#pragma braket verbatim           // Correct
#pragma verbatim                  // wrong
```

This code generates the error message: `You must include “braket” in the verbatim pragma`

## Single qubits cannot be indexed error

Single qubits cannot be indexed. The following code generates the error.

```
OPENQASM 3;

qubit q;
h q[0];
```

This code generates the error: `[line 4] single qubit cannot be indexed.`

However, single qubit arrays can be indexed as follows:

```
OPENQASM 3;

qubit[1] q;
h q[0];   // This is valid
```

## The physical qubits

in a two qubit gate are not connected error

To use physical qubits, first confirm that the device uses physical
qubits by checking `device.properties.action[DeviceActionType.OPENQASM].supportPhysicalQubits`
and then verify the connectivity graph by checking `device.properties.paradigm.connectivity.connectivityGraph`
or `device.properties.paradigm.connectivity.fullyConnected`.

```
OPENQASM 3;

cnot $0, $14;
```

This code generates the error message: `[line 3] has disconnected qubits 0 and 14`

## Local simulator support warning

The `LocalSimulator` supports advanced features in OpenQASM that may
not be available on QPUs or on-demand simulators. If your program contains language
features specific only to the `LocalSimulator`, as seen in the following
example, you will receive a warning.

```
qasm_string = """
qubit[2] q;

h q[0];
ctrl @ x q[0], q[1];
"""
qasm_program = Program(source=qasm_string)
```

This code generates the warning: `This program uses OpenQASM language features only supported in the LocalSimulator. Some of these features may not be supported on QPUs or on-demand simulators.

For more information on supported OpenQASM features, explore the page [Advanced feature support for OpenQASM on the Local Simulator](braket-openqasm-supported-features.md#braket-openqasm-supported-features-advanced-feature-local-simulator "braket-openqasm-supported-features.md#braket-openqasm-supported-features-advanced-feature-local-simulator").
