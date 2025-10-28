# Working with Amazon Braket Hybrid Jobs

Amazon Braket Hybrid Jobs offers a way for you to run hybrid quantum-classical algorithms
requiring both classical AWS resources and quantum processing units (QPUs). Hybrid Jobs is
designed to spin up the requested classical resources, run your algorithm, and release the
instances after completion so you only pay for _what you use_.

Hybrid Jobs is ideal for long-running, iterative algorithms that involve the use of both classical computing resources and
quantum computing resources. With Hybrid Jobs, after submitting your algorithm to run, Braket will run your algorithm in a scalable, containerized
environment. Once the algorithm has completed, you can then retrieve the results.

Additionally, quantum tasks that are created from a hybrid job benefit from higher priority queueing
to the target QPU device. This prioritization ensures that your quantum computations are processed and ran ahead of other tasks waiting in the queue.
This is particularly advantageous for iterative hybrid algorithms, where the results of one quantum task depend on the outcomes of prior quantum tasks. Examples of such algorithms include the
[Quantum Approximate Optimization Algorithm (QAOA)](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_quantum_algorithms/QAOA/QAOA_braket.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_quantum_algorithms/QAOA/QAOA_braket.ipynb"),
[variational quantum eigensolver](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_quantum_algorithms/VQE_Chemistry/VQE_chemistry_braket.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_quantum_algorithms/VQE_Chemistry/VQE_chemistry_braket.ipynb"), or
[quantum machine learning](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/1_Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs/Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs.ipynb "https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/hybrid_jobs/1_Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs/Quantum_machine_learning_in_Amazon_Braket_Hybrid_Jobs.ipynb"). You can also monitor your algorithm progress in near-real
time, enabling you to keep track of costs, budget, or custom metrics such as training loss or expectation values.

You can access hybrid jobs in Braket using:

- The [Amazon Braket Python
  SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python").
- The [Amazon Braket
  console](https://console.aws.amazon.com/braket/home "https://console.aws.amazon.com/braket/home").
- The Amazon Braket API.

###### In this section:

- [When to use Amazon Braket Hybrid Jobs](#braket-jobs-use "#braket-jobs-use")
- [Running a hybrid job with Amazon Braket Hybrid Jobs](#braket-jobs-works "#braket-jobs-works")
- [Key concepts for Hybrid Jobs](braket-jobs-concepts.md "braket-jobs-concepts.md")
- [Prerequisites](braket-jobs-prerequisites.md "braket-jobs-prerequisites.md")
- [Create a Hybrid Job](braket-jobs-first.md "braket-jobs-first.md")
- [Cancel a Hybrid Job](braket-jobs-cancel.md "braket-jobs-cancel.md")
- [Customizing your Hybrid Job](braket-jobs-customize.md "braket-jobs-customize.md")
- [Using PennyLane with Amazon Braket](hybrid.md "hybrid.md")
- [Using CUDA-Q with Amazon Braket](braket-using-cuda-q.md "braket-using-cuda-q.md")

## When to use Amazon Braket Hybrid Jobs

Amazon Braket Hybrid Jobs enables you to run hybrid quantum-classical algorithms, such
as the Variational Quantum Eigensolver (VQE) and the Quantum Approximate Optimization
Algorithm (QAOA), that combine classical compute resources with quantum computing devices
to optimize the performance of today's quantum systems. Amazon Braket Hybrid Jobs provides
three main benefits:

1. **Performance**: Amazon Braket Hybrid Jobs provides
   better performance than running hybrid algorithms from your own environment. While
   your job is running, it has priority access to the selected target QPU. Tasks from
   your job run ahead of other tasks queued on the device. This results in shorter and
   more predictable runtimes for hybrid algorithms. Amazon Braket Hybrid Jobs also
   supports parametric compilation. You can submit a circuit using free parameters and
   Braket compiles the circuit once, without the need to recompile for subsequent
   parameter updates to the same circuit, resulting in even faster runtimes.
2. **Convenience**: Amazon Braket Hybrid Jobs simplifies
   setting up and managing your compute environment and keeping it running while your
   hybrid algorithm runs. You just provide your algorithm script and select a quantum
   device (either a quantum processing unit or a simulator) on which to run.
   Amazon Braket waits for the target device to become available, spins up the classical
   resources, runs the workload in pre-built container environments, returns the results
   to Amazon Simple Storage Service (Amazon S3), and releases the compute resources.
3. **Metrics**: Amazon Braket Hybrid Jobs provides
   on-the-fly insights into running algorithms and delivers customizable algorithm
   metrics in near real-time to Amazon CloudWatch and the Amazon Braket console so you can track
   the progress of your algorithms.

## Running a hybrid job with Amazon Braket Hybrid Jobs

To run a hybrid job with Amazon Braket Hybrid Jobs, you first need to define
your algorithm. You can define it by writing the _algorithm script_ and,
optionally, other dependency files using the [Amazon Braket Python SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python") or
[PennyLane](https://pennylane.ai "https://pennylane.ai"). If you want to use other (open
source or proprietary) libraries, you can define your own custom container image using
Docker, which includes these libraries. For more information, see
[Bring your own container (BYOC)](braket-jobs-byoc.md "braket-jobs-byoc.md").

In either case, next you create a hybrid job using the Amazon Braket
API, where you provide your algorithm script or container, select the
target quantum device the hybrid job is to use, and then choose from a variety of optional
settings. The default values provided for these optional settings work for the majority of
use cases. For the target device to run your Hybrid Job, you have a choice between a QPU,
an on-demand simulator (such as SV1, DM1 or
TN1), or the classical hybrid job instance itself. With an on-demand simulator
or QPU, your hybrid jobs container makes API calls to a remote device. With the embedded
simulators, the simulator is embedded in the same container as your algorithm script. The
[lightning
simulators](https://github.com/PennyLaneAI/pennylane-lightning "https://github.com/PennyLaneAI/pennylane-lightning") from PennyLane are embedded with the default pre-built hybrid jobs container
for you to use. If you run your code using an embedded PennyLane simulator or a custom
simulator, you can specify an instance type as well as how many instances you wish to use.
Refer to the [Amazon Braket Pricing
page](https://aws.amazon.com/braket/pricing/ "https://aws.amazon.com/braket/pricing/") for the costs associated with each choice.

![Flowchart diagram showing the user interactions with Amazon Braket components, API, Jobs Instance, and simulators for hybrid, QPU, on-demand, and embedded tasks. Results are stored in Amazon Simple Storage Service bucket and analyzed using Amazon CloudWatch on the Amazon Braket console.](images/braket-hybrid-job-run.png)

If your target device is an on-demand or embedded simulator, Amazon Braket starts running
the hybrid job right away. It spins up the hybrid job instance (you can customize the instance type in
the API call), runs your algorithm, writes the results to Amazon S3, and releases
your resources. This release of resources ensures that you only pay for what you
use.

The total number of concurrent hybrid jobs per quantum processing unit (QPU) is restricted.
Today, only one hybrid job can run on a QPU at any given time. Queues are used to control the
number of hybrid jobs allowed to run so as not to exceed the limit allowed. If your target device
is a QPU, your hybrid job first enters the _job queue_ of the selected QPU.
Amazon Braket spins up the hybrid job instance needed and runs your hybrid job on the device. For the
duration of your algorithm, your hybrid job has priority access, meaning that quantum tasks from your hybrid job
run ahead of other Braket quantum tasks queued up on the device, provided the job quantum tasks are
submitted to the QPU once every few minutes. Once your hybrid job is complete, resources are
released, meaning you only pay for what you use.

###### Note

Devices are regional and your hybrid job runs in the same AWS Region as your primary
device.

In both the simulator and QPU target scenarios, you have the option to define custom
algorithm metrics, such as the energy of your Hamiltonian, as part of your algorithm. These
metrics are automatically reported to Amazon CloudWatch and from there, they display in near
real-time in the Amazon Braket console.

###### Note

If you wish to use a GPU based instance, be sure to use one of the GPU-based
simulators available with the embedded simulators on Braket (for example,
`lightning.gpu`). If you choose one of the CPU-based embedded simulators
(for example, `lightning.qubit`, or `braket:default-simulator`),
the GPU will not be used and you may incur unnecessary costs.
