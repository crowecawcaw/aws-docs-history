# About embedded simulators

Embedded simulators operate by having the simulation embedded directly within the algorithm code. Also, it is contained within
the same container and runs the simulation directly on the hybrid job instance. This approach is
useful for removing bottlenecks typically associated with communicating between the simulation and a
remote device. By keeping all computations in a single, cohesive environment, embedded simulators can greatly
reduce memory requirements and decrease the number of circuit executions needed to achieve a target result.
This can lead to substantial performance improvements, often by a factor of ten or more, as compared to
traditional setups that rely on remote simulation.
For more information about how embedded simulators enhance performance and enable streamlined hybrid jobs, refer to the [Run a hybrid job with Amazon Braket Hybrid Jobs](braket-jobs-works.md "braket-jobs-works.md") documentation page.

## PennyLane's lightning simulators

You can use PennyLane's lightning simulators as embedded simulators on Braket. With
PennyLane's lightning simulators, you can use advanced gradient computation
methods, such as [adjoint differentiation](https://docs.pennylane.ai/en/stable/introduction/interfaces.html#simulation-based-differentiation "https://docs.pennylane.ai/en/stable/introduction/interfaces.html#simulation-based-differentiation"), to evaluate gradients faster. The [lightning.qubit simulator](https://docs.pennylane.ai/projects/lightning/en/stable/lightning_qubit/device.html "https://docs.pennylane.ai/projects/lightning/en/stable/lightning_qubit/device.html") is available as a device through Braket NBIs and as
an embedded simulator, whereas the lightning.gpu simulator needs to be run as an
embedded simulator with a GPU instance. See the [Embedded simulators in Braket Hybrid Jobs](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/4_Embedded_simulators_in_Braket_Hybrid_Jobs/Embedded_simulators_in_Braket_Hybrid_Jobs.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/4_Embedded_simulators_in_Braket_Hybrid_Jobs/Embedded_simulators_in_Braket_Hybrid_Jobs.ipynb") notebook for an example of using
lightning.gpu.
