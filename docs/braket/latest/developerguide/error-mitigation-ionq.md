# Error mitigation techniques on IonQ devices

Error mitigation involves running multiple physical circuits and combining their
measurements to give an improved result.

###### Note

For all IonQ's devices: When using an on-demand model, there is a 1 Million
[gateshot](braket-terms.md#gateshot-limit-term "braket-terms.md#gateshot-limit-term")
limit, and a minimum of 2500 shots for [Error mitigation](braket-error-mitigation.md "braket-error-mitigation.md") tasks.
For a direct reservation, there is no gateshot limit, and a minimum of 500 shots for Error mitigation tasks.

## Debiasing

IonQ devices features an error mitigation method called _debiasing_.

Debiasing maps a circuit into multiple variants that act on different qubit permutations
or with different gate decompositions. This reduces the effect of systematic errors such as
gate over-rotations or a single faulty qubit by using different implementations of a
circuit that could otherwise bias measurement results. This comes at the expense of extra
overhead to calibrate multiple qubits and gates.

For more information on debiasing, see [Enhancing quantum computer performance through symmetrization](https://arxiv.org/abs/2301.07233 "https://arxiv.org/abs/2301.07233").

###### Note

Using debiasing requires a minimum of 2500 shots.

You can run a quantum task with debiasing on an IonQ device using the
following code:

```
from braket.aws import AwsDevice
from braket.circuits import Circuit
from braket.error_mitigation import Debias

# choose an IonQ device
device = AwsDevice("arn:aws:braket:us-east-1::device/qpu/ionq/Forte-Enterprise-1")
circuit = Circuit().h(0).cnot(0, 1)

task = device.run(circuit, shots=2500, device_parameters={"errorMitigation": Debias()})

result = task.result()
print(result.measurement_counts)
`>>> {"00": 1245, "01": 5, "10": 10 "11": 1240} # result from debiasing`
```

When the quantum task is complete, you can see the measurement probabilities and any result types
from the quantum task. The measurement probabilities and counts from all variants are aggregated
into a single distribution. Any result types specified in the circuit, such as expectation
values, are computed using the aggregate measurement counts.

## Sharpening

You can also access measurement probabilities computed with a different
post-processing strategy called _sharpening_. Sharpening compares the
results of each variant and discards inconsistent shots, favoring the most likely
measurement outcome across variants. For more information, see [Enhancing quantum computer performance through
symmetrization](https://arxiv.org/abs/2301.07233 "https://arxiv.org/abs/2301.07233").

Importantly, sharpening assumes the form of the output distribution to be sparse with
few high-probability states and many zero-probability states. It may distort the
probability distribution if this assumption is not valid.

You can access the probabilities from a sharpened distribution in the
`additional_metadata` field on the `GateModelTaskResult` in the
Braket Python SDK. Note that sharpening does not return the measurement counts, but
instead returns a re-normalized probability distribution. The following code snippet
shows how to access the distribution after sharpening.

```
print(result.additional_metadata.ionqMetadata.sharpenedProbabilities)
`>>> {"00": 0.51, "11": 0.549} # sharpened probabilities`
```
