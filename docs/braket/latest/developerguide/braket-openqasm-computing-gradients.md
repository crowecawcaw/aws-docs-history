# Computing gradients with OpenQASM 3.0

Amazon Braket supports the computation of gradients on both on-demand and local simulators
when running in the `shots=0` (exact) mode. This is achieved through the use of the
adjoint differentiation method. To specify the gradient you want to compute, you can provide the
appropriate pragma, as demonstrated in code in the following example.

```
OPENQASM 3.0;
input float alpha;

bit[2] b;
qubit[2] q;

h q[0];
h q[1];
rx(alpha) q[0];
rx(alpha) q[1];
b[0] = measure q[0];
b[1] = measure q[1];

#pragma braket result adjoint_gradient h(q[0]) @ i(q[1]) alpha
```

Instead of listing all the individual parameters explicitly, you can also specify the
`all` keyword within the pragma. This will compute the gradient with respect to
all of the `input` parameters listed, which can be a convenient option when the
number of parameters is very large. In this case, the pragma will look like the code in the following example.

```
#pragma braket result adjoint_gradient h(q[0]) @ i(q[1]) all
```

All observable types are supported in Amazon Braket's OpenQASM 3.0 implementation,
including individual operators, tensor products, Hermitian observables, and `Sum`
observables. The specific operator you want to use when computing gradients must be wrapped
within the `expectation()` function, and the qubits that each term of the observable
acts upon must be explicitly specified.
