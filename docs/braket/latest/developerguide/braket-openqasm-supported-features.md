# What OpenQASM features does

Braket support?

The following section lists the OpenQASM 3.0 data types, statements, and pragma
instructions supported by Braket.

###### In this section:

- [Supported OpenQASM data types](#braket-openqasm-supported-features-datatypes "#braket-openqasm-supported-features-datatypes")
- [Supported OpenQASM statements](#braket-openqasm-supported-features-statements "#braket-openqasm-supported-features-statements")
- [Braket OpenQASM pragmas](#braket-openqasm-supported-features-pragmas "#braket-openqasm-supported-features-pragmas")
- [Advanced feature support for OpenQASM on the Local Simulator](#braket-openqasm-supported-features-advanced-feature-local-simulator "#braket-openqasm-supported-features-advanced-feature-local-simulator")
- [Supported operations
  and grammar with OpenPulse](#braket-openpulse-supported-operations-grammar "#braket-openpulse-supported-operations-grammar")

## Supported OpenQASM data types

The following OpenQASM data types are supported by Amazon Braket.

- Non-negative integers are used for (virtual and physical) qubit
  indices:
  - `cnot q[0], q[1];`
  - `h $0;`

- Floating-point numbers or constants may be used for gate rotation
  angles:
  - `rx(-0.314) $0;`
  - `rx(pi/4) $0;`

###### Note

pi is a built-in constant in OpenQASM and cannot be used as a parameter
name.

- Arrays of complex numbers (with the OpenQASM `im` notation for
  imaginary part) are allowed in result type pragmas for defining general
  hermitian observables and in unitary pragmas:
  - `#pragma braket unitary [[0, -1im], [1im, 0]] q[0]`
  - `#pragma braket result expectation hermitian([[0, -1im], [1im, 0]])
q[0]`

## Supported OpenQASM statements

The following OpenQASM statements are supported by Amazon Braket.

- `Header: OPENQASM 3;`
- Classic bit declarations:
  - `bit b1;` (equivalently, `creg b1;`)
  - `bit[10] b2;` (equivalently, `creg b2[10];`)

- Qubit declarations:
  - `qubit b1;` (equivalently, `qreg b1;`)
  - `qubit[10] b2;` (equivalently, `qreg
b2[10];`)

- Indexing within arrays: `q[0]`
- Input: `input float alpha;`
- specification of physical qubits: `$0`
- Supported gates and operations on a device:
  - `h $0;`
  - `iswap q[0], q[1];`

###### Note

A device's supported gates can be found in the device properties for OpenQASM
actions; no gate definitions are needed to use these gates.

- Verbatim box statements. Currently, we do not support box duration notation.
  Native gates and physical qubits are required in verbatim
  boxes.

```
#pragma braket verbatim
box{
    rx(0.314) $0;
}
```

- Measurement and measurement assignment on qubits or a whole
  qubit register.
  - `measure $0;`
  - `measure q;`
  - `measure q[0];`
  - `b = measure q;`
  - `measure q → b;`

## Braket OpenQASM pragmas

The following OpenQASM pragma instructions are supported by Amazon Braket.

- Noise pragmas
  - `#pragma braket noise bit_flip(0.2) q[0]`
  - `#pragma braket noise phase_flip(0.1) q[0]`
  - `#pragma braket noise pauli_channel`

- Verbatim pragmas
  - `#pragma braket verbatim`

- Result type pragmas
  - Basis invariant result types:
    - State vector: `#pragma braket result state_vector`
    - Density matrix: `#pragma braket result
density_matrix`

  - Gradient computation pragmas:
    - Adjoint gradient: `#pragma braket result adjoint_gradient
expectation(2.2 * x[0] @ x[1]) all`

  - Z basis result types:
    - Amplitude: `#pragma braket result amplitude "01"`
    - Probability: `#pragma braket result probability q[0],
q[1]`

  - Basis rotated result types
    - Expectation: `#pragma braket result expectation x(q[0]) @
y([q1])`
    - Variance: `#pragma braket result variance hermitian([[0,
-1im], [1im, 0]]) $0`
    - Sample: `#pragma braket result sample h($1)`

###### Note

OpenQASM 3.0 is backwards compatible with OpenQASM 2.0, so programs written
using 2.0 can run on Braket. However the features of OpenQASM 3.0 supported by
Braket do have some minor syntax differences, such as `qreg` vs
`creg` and `qubit` vs `bit`. There are also
differences in measurement syntax, and these need to be supported with their
correct syntax.

## Advanced feature support for OpenQASM on the Local Simulator

The `LocalSimulator` supports advanced OpenQASM features which are not
offered as part of Braket's QPU's or on-demand simulators. The following list of
features are only supported in the `LocalSimulator`:

- Gate modifiers
- OpenQASM built-in gates
- Classical variables
- Classical operations
- Custom gates
- Classical control
- QASM files
- Subroutines

For examples of each advanced feature, see this [sample notebook](https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Simulating_Advanced_OpenQASM_Programs_with_the_Local_Simulator.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Simulating_Advanced_OpenQASM_Programs_with_the_Local_Simulator.ipynb"). For the full OpenQASM specification, see the [OpenQASM website](https://openqasm.com/language/index.html "https://openqasm.com/language/index.html").

## Supported operations

and grammar with OpenPulse

**Supported OpenPulse Data Types**

Cal blocks:

```
cal {
    ...
}
```

Defcal blocks:

```
// 1 qubit
defcal x $0 {
...
}

// 1 qubit w. input parameters as constants
defcal my_rx(pi) $0 {
...
}

// 1 qubit w. input parameters as free parameters
defcal my_rz(angle theta) $0 {
...
}

// 2 qubit (above gate args are also valid)
defcal cz $1, $0 {
...
}
```

Frames:

```
frame my_frame = newframe(port_0, 4.5e9, 0.0);
```

Waveforms:

```
// prebuilt
waveform my_waveform_1 = constant(1e-6, 1.0);

//arbitrary
waveform my_waveform_2 = {0.1 + 0.1im, 0.1 + 0.1im, 0.1, 0.1};
```

**Custom Gate Calibration Example:**

```
cal {
    waveform wf1 = constant(1e-6, 0.25);
}

defcal my_x $0 {
   play(wf1, q0_rf_frame);
}

defcal my_cz $1, $0 {
    barrier q0_q1_cz_frame, q0_rf_frame;
    play(q0_q1_cz_frame, wf1);
    delay[300ns] q0_rf_frame
    shift_phase(q0_rf_frame, 4.366186381749424);
    delay[300ns] q0_rf_frame;
    shift_phase(q0_rf_frame.phase, 5.916747563126659);
    barrier q0_q1_cz_frame, q0_rf_frame;
    shift_phase(q0_q1_cz_frame, 2.183093190874712);
}

bit[2] ro;
my_x $0;
my_cz $1,$0;
c[0] = measure $0;
```

**Arbitrary pulse example:**

```
bit[2] ro;
cal {
    waveform wf1 = {0.1 + 0.1im, 0.1 + 0.1im, 0.1, 0.1};
    barrier q0_drive, q0_q1_cross_resonance;
    play(q0_q1_cross_resonance, wf1);
    delay[300ns] q0_drive;
    shift_phase(q0_drive, 4.366186381749424);
    delay[300dt] q0_drive;
   barrier q0_drive, q0_q1_cross_resonance;
   play(q0_q1_cross_resonance, wf1);
    ro[0] = capture_v0(r0_measure);
    ro[1] = capture_v0(r1_measure);
}
```
