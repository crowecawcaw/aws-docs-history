# Using parametric compilation to speed

up Hybrid Jobs

Amazon Braket supports parametric compilation on certain QPUs. This enables you to
reduce the overhead associated with the computationally expensive compilation step by
compiling a circuit only once and not for every iteration in your hybrid algorithm. This
can improve runtimes dramatically for Hybrid Jobs, since you avoid the need to recompile
your circuit at each step. Just submit parametrized circuits to one of our supported QPUs
as a Braket Hybrid Job. For long running hybrid jobs, Braket automatically uses the
updated calibration data from the hardware provider when compiling your circuit to ensure
the highest quality results.

To create a parametric circuit, you first need to provide parameters as inputs in your
algorithm script. In this example, we use a small parametric circuit and ignore any
classical processing between each iteration. For typical workloads, you would submit many
circuits in batch and perform classical processing such as updating the parameters in each
iteration.

```
import os

from braket.aws import AwsDevice
from braket.circuits import Circuit, FreeParameter

def start_here():

    print("Test job started.")

    # Use the device declared in the job script
    device = AwsDevice(os.environ["AMZN_BRAKET_DEVICE_ARN"])

    circuit = Circuit().rx(0, FreeParameter("theta"))
    parameter_list = [0.1, 0.2, 0.3]

    for parameter in parameter_list:
        result = device.run(circuit, shots=1000, inputs={"theta": parameter})

    print("Test job completed.")
```

You can submit the algorithm script to run as a Hybrid Job with the following job
script. When running the Hybrid Job on a QPU that supports parametric compilation, the
circuit is compiled only on the first run. In following runs, the compiled circuit is
reused, increasing the runtime performance of the Hybrid Job without any additional lines
of code.

```
from braket.aws import AwsQuantumJob

job = AwsQuantumJob.create(
    device=device_arn,
    source_module="algorithm_script.py",
)
```

###### Note

Parametric compilation is supported on all superconducting, gate-based QPUs
from Rigetti Computing with the exception of pulse level programs.
