# Verbatim compilation with

OpenQASM 3.0

When you run a quantum circuit on quantum computers provided by vendors such as Rigetti,
and IonQ, you can direct the compiler to run your
circuits exactly as defined, without any modifications. This feature is known as
_verbatim compilation_. With Rigetti devices, you can specify
precisely what gets preserved-either an entire circuit or only specific parts of it. To
preserve only specific parts of a circuit, you will need to use native gates within the
preserved regions. Currently, IonQ only supports
verbatim compilation for the entire circuit, so every instruction in the circuit needs
to be enclosed in a verbatim box.

With OpenQASM, you can explicitly specify a verbatim pragma around a box of code that
is then left untouched and not optimized by the low-level compilation routine of the hardware. The
following code example shows how to use the `#pragma braket verbatim` directive to achieve this.

```
OPENQASM 3;

bit[2] c;

#pragma braket verbatim
box{
    rx(0.314159) $0;
    rz(0.628318) $0, $1;
    cz $0, $1;
}

c[0] = measure $0;
c[1] = measure $1;
```

For more detailed information on the process of verbatim compilation,
including examples and best practices, see the [Verbatim compilation](https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Verbatim_Compilation.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Verbatim_Compilation.ipynb") sample notebook available in the amazon-braket-examples github repository.
