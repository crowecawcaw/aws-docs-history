# Amazon Braket terms and concepts

###### Tip

**Learn the foundations of quantum computing with AWS!**
Enroll in the [Amazon Braket Digital Learning Plan](https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs "https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs")
and earn your own Digital badge after completing a series of learning courses and a digital assessment.

The following terms and concepts are used in Braket:

**Analog Hamiltonian Simulation**

Analog Hamiltonian Simulation (AHS) is a distinct quantum computing paradigm
for direct simulation of time-dependent quantum dynamics of many-body systems. In
AHS, users directly specify a time-dependent Hamiltonian and the quantum computer
is tuned in such a way that it directly emulates the continuous time evolution
under this Hamiltonian. AHS devices are typically special-purpose devices and not
universal quantum computers like gate-based devices. They are limited to a class
of Hamiltonians they can simulate. However, since these Hamiltonians are naturally
implemented on the device, AHS does not suffer from the overhead required to
formulate algorithms as circuits and implement gate operations.

**Braket**

We named the Braket service after the [bra-ket
notation](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation "https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation"), a standard notation in quantum mechanics. It was introduced
by Paul Dirac in 1939 to describe the state of quantum systems, and it is also
known as the Dirac notation.

**Braket Direct**

With Braket Direct, you can reserve dedicated access to different quantum devices
of your choice, connect with quantum computing specialists to receive guidance for your
workload, and gain early access to next-generation capabilities, such as new quantum
devices with limited availability.

**Braket hybrid job**

Amazon Braket has a feature called Amazon Braket
Hybrid Jobs that provides fully managed executions of
hybrid algorithms. A Braket hybrid job consists of three components:

1. The definition of your algorithm, which can be provided as a script,
   Python module, or Docker container.
2. The _hybrid job instance_, based on Amazon EC2, on which to run
   your algorithm. The default is an ml.m5.xlarge instance.
3. The _quantum device_ on which to run the
   _quantum tasks_ that are part of your algorithm. A
   single hybrid job typically contains a collection of many quantum tasks.

**Device**

In Amazon Braket, a device is a backend that can run
_quantum tasks_. A device can be a _QPU_
or a _quantum circuit simulator_. To learn more, see [Amazon Braket supported devices](braket-devices.md "braket-devices.md").

**Error mitigation**

Error mitigation involves running multiple physical circuits and combining
their measurements to give an improved result. For more information, see
[Error mitigation techniques](braket-error-mitigation.md "braket-error-mitigation.md").

**Gate-based quantum computing**

In gate-based quantum computing (QC), also called circuit-based QC,
computations are broken down into elementary operations (gates). Certain sets of
gates are universal, meaning that every computation can be expressed as a finite
sequence of those gates. Gates are the building blocks of _quantum
circuits_ and are analogous to the logic gates of classical digital
circuits.

**Gateshot limit**

A gateshot limit refers to the total gate count per shot (the sum of all gate types)
and shot count per task. Mathematically, the gateshot limit can be expressed as:

`Gateshot limit = (Gate count per shot) * (Shot count per task)`

**Hamiltonian**

The quantum dynamics of a physical system are determined by its Hamiltonian,
which encodes all information about the interactions between constituents of the
system and the effects of exogenous driving forces. The Hamiltonian of an N-qubit
system is commonly represented as a 2N by
2N matrix of complex numbers on classical machines.
By running an Analog Hamiltonian Simulation on a quantum device, you can avoid
these exponential resource requirements.

**Pulse**

A pulse is a transient physical signal transmitted to the qubits. It is
described by a waveform played in a frame that serves as a support for the carrier
signal and is bound to the hardware channel or port. Customers can design their
own pulses by providing the analog envelope that modulates the high-frequency
sinusoidal carrier signal. The frame is uniquely described by a frequency and a
phase that are often chosen to be on resonance with the energy separation between
the energy levels for |0⟩ and |1⟩ of the qubit. Gates are thus enacted as pulses
with a predetermined shape and calibrated parameters such as its amplitude,
frequency and duration. Use cases that are not covered by template waveforms will
be enabled through custom waveforms which will be specified at the single sample
resolution by providing a list of values separated by a fixed, physical
cycle-time.

**Quantum circuit**

A quantum circuit is the instruction set that defines a computation on a
gate-based quantum computer. A quantum circuit is a sequence of quantum gates,
which are reversible transformations on a qubit register, together
with measurement instructions.

**Quantum circuit simulator**

A quantum circuit simulator is a computer program that runs on classical
computers and calculates the measurement outcomes of a _quantum
circuit_. For general circuits, the resource requirements of a
quantum simulation grow exponentially with the number of qubits to
simulate. Braket provides access to both managed (accessed through the Braket
API) and local (part of the Amazon Braket SDK)
quantum circuit simulators.

**Quantum computer**

A quantum computer is a physical device that uses quantum-mechanical phenomena,
such as superposition and entanglement, to perform computations. There are
different paradigms to quantum computing (QC), such as
_gate-based_ QC.

**Quantum processing unit (QPU)**

A QPU is a physical quantum computing device that can run on a quantum task.
QPUs can be based on different QC paradigms, such as gate-based QC. To learn more,
see [Amazon Braket supported devices](braket-devices.md "braket-devices.md").

**QPU native gates**

QPU native gates can be directly mapped to control pulses by the QPU control
system. Native gates can be run on the QPU device without further compilation.
Subset of _QPU supported gates_. You can find the native gates
of a device on the **Devices** page in the
Amazon Braket console and through the Braket SDK.

**QPU supported gates**

QPU supported gates are the gates accepted by the QPU device. These gates might
not run directly on the QPU, meaning that they might need to be
decomposed into native gates. You can find the supported gates of a device on the
**Devices** page in the Amazon Braket console and
through the Amazon Braket SDK.

**Quantum task**

In Braket, a quantum task is the atomic request to a
_device_. For _gate-based QC_ devices,
this includes the quantum circuit (including the measurement instructions and
number of shots) and other request metadata. You can create quantum
tasks through the Amazon Braket SDK or by using the
CreateQuantumTask
API operation directly. After you create a quantum task, it will be queued
until the requested device becomes available. You can view your quantum tasks on
the **Quantum Tasks** page of the
Amazon Braket console or by using the GetQuantumTask or
SearchQuantumTasks
API operations.

**Qubit**

The basic unit of information in a quantum computer is called a
qubit (quantum bit), much like a bit in classical computing. A
qubit is a two-level quantum system that can be realized by
different physical implementations, such as superconducting circuits or individual
ions and atoms. Other qubit types are based on photons, electronic
or nuclear spins, or more exotic quantum systems.

**Queue depth**

Queue depth refers to the number of quantum tasks
and hybrid jobs queued for a particular device. A device's quantum
task and hybrid job queue count are accessible through the Braket Software
Development Kit (SDK) or Amazon Braket Management Console.

1. _Task queue depth_ refers to the
   total number of quantum tasks waiting to run in normal priority.
2. _Priority task queue depth_ refers
   to the total number of submitted quantum tasks waiting to run through Amazon Braket
   Hybrid Jobs. These tasks get priority over standalone tasks once a hybrid job starts.
3. _Hybrid jobs queue depth_ refers
   to the total number of hybrid jobs currently queued on a device.
   Quantum tasks submitted as part of a hybrid job have priority, and
   are aggregated in the Priority Task Queue.

**Queue position**

Queue position refers to the current position of your quantum task
or hybrid job within a respective device queue. It can be obtained for quantum tasks
or hybrid jobs through the Braket Software Development Kit (SDK) or
Amazon Braket Management Console.

**Shots**

Since quantum computing is inherently probabilistic, any circuit needs to be
evaluated multiple times to get an accurate result. A single circuit execution and
measurement is called a shot. The number of shots (repeated executions) for a
circuit is chosen based on the desired accuracy for the result.

## AWS terminology and tips for Amazon Braket

**IAM policies**

An IAM policy is a document that allows or denies permissions to
AWS services and resources. IAM policies enable you to customize users'
levels of access to resources. For example, you can allow users access to all
of the Amazon S3 buckets within your AWS account, or only a specific
bucket.

- **Best practice:** Follow the security
  principle of _least privilege_ when granting
  permissions. By following this principle, you help to prevent users or
  roles from having more permissions than needed to perform their quantum tasks.
  For example, if an employee needs access to only a specific bucket,
  specify the bucket in the IAM policy instead of granting the employee
  access to all of the buckets in your AWS account.

**IAM roles**

An IAM role is an identity that you can assume to gain temporary access to
permissions. Before a user, application, or service can assume an IAM role,
they must be granted permissions to switch to the role. When someone assumes an
IAM role, they abandon all previous permissions that they had under a previous
role and assume the permissions of the new role.

- **Best practice:** IAM roles are ideal for
  situations in which access to services or resources needs to be granted
  temporarily, instead of long-term.

  **Amazon S3 bucket**

Amazon Simple Storage Service (Amazon S3) is an AWS service that lets you store data as
_objects_ in _buckets_. Amazon S3 buckets
offer unlimited storage space. The maximum size for an object in an Amazon S3 bucket
is 5 TB. You can upload any type of file data to an Amazon S3 bucket, such as
images, videos, text files, backup files, media files for a website, archived
documents, and your Braket quantum task results.

- **Best practice:** You can set permissions
  to control access to your S3 bucket. For more information, see [Bucket policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") in the Amazon S3
  documentation.
