# Run your circuits with OpenQASM 3.0

Amazon Braket now supports [OpenQASM
3.0](https://openqasm.com/ "https://openqasm.com/") for gate-based quantum devices and simulators. This user guide provides
information about the subset of OpenQASM 3.0 supported by Braket. Braket customers now
have the choice of submitting Braket circuits with the [SDK](braket-constructing-circuit.md "braket-constructing-circuit.md") or by directly providing OpenQASM 3.0
strings to all gate-based devices with the [Amazon Braket
API](../APIReference/Welcome.md "../APIReference/Welcome.md") and the [Amazon Braket Python SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python").

The topics in this guide walk you through various examples of how to complete the
following quantum tasks.

- [Create and submit OpenQASM quantum tasks
  on different Braket devices](braket-openqasm-create-submit-task.md "braket-openqasm-create-submit-task.md")
- [Access the
  supported operations and result types](braket-openqasm-device-support.md#braket-openqasm-supported-operations-results-result-types "braket-openqasm-device-support.md#braket-openqasm-supported-operations-results-result-types")
- [Simulate noise with OpenQASM](braket-openqasm-noise-simulation.md "braket-openqasm-noise-simulation.md")
- [Use verbatim compilation with
  OpenQASM](braket-openqasm-verbatim-compilation.md "braket-openqasm-verbatim-compilation.md")
- [Troubleshoot OpenQASM issues](braket-troubleshooting-openqasm.md "braket-troubleshooting-openqasm.md")
  This guide also provides an introduction to certain hardware-specific features that can
  be implemented with OpenQASM 3.0 on Braket and links to further resources.

###### In this section:

- [What is OpenQASM 3.0?](#braket-openqasm-what-is "#braket-openqasm-what-is")
- [When to use OpenQASM 3.0](#braket-openqasm-when-to-use "#braket-openqasm-when-to-use")
- [How OpenQASM 3.0 works](#braket-openqasm-how-it-works "#braket-openqasm-how-it-works")
- [Prerequisites](#braket-openqasm-prerequisites "#braket-openqasm-prerequisites")
- [What OpenQASM features does
  Braket support?](braket-openqasm-supported-features.md "braket-openqasm-supported-features.md")
- [Create and submit an example
  OpenQASM 3.0 quantum task](braket-openqasm-create-submit-task.md "braket-openqasm-create-submit-task.md")
- [Support for OpenQASM on different
  Braket devices](braket-openqasm-device-support.md "braket-openqasm-device-support.md")
- [Simulate noise with OpenQASM 3.0](braket-openqasm-noise-simulation.md "braket-openqasm-noise-simulation.md")
- [Qubit rewiring with OpenQASM 3.0](braket-openqasm-rewire-qubits.md "braket-openqasm-rewire-qubits.md")
- [Verbatim compilation with
  OpenQASM 3.0](braket-openqasm-verbatim-compilation.md "braket-openqasm-verbatim-compilation.md")
- [The Braket console](#braket-openqasm-braket-console "#braket-openqasm-braket-console")
- [Additional resources](#braket-openqasm-more-resources "#braket-openqasm-more-resources")
- [Computing gradients with OpenQASM 3.0](braket-openqasm-computing-gradients.md "braket-openqasm-computing-gradients.md")
- [Measuring specific qubits with OpenQASM 3.0](braket-openqasm-measure-qubits.md "braket-openqasm-measure-qubits.md")

## What is OpenQASM 3.0?

The Open Quantum Assembly Language (OpenQASM) is an [intermediate
representation](https://en.wikipedia.org/wiki/Intermediate_representation "https://en.wikipedia.org/wiki/Intermediate_representation") for quantum instructions. OpenQASM is an open-source framework
and is widely used for the specification of quantum programs for gate-based devices.
With OpenQASM, users can program the quantum gates and measurement operations that form
the building blocks of quantum computation. The previous version of OpenQASM (2.0) was
used by a number of quantum programming libraries to describe basic programs.

The new version of OpenQASM (3.0) extends the previous version to include more
features, such as pulse-level control, gate timing, and classical control flow to bridge
the gap between end-user interface and hardware description language. Details and
specification on the current version 3.0 are available on the GitHub [OpenQASM 3.x Live Specification](https://github.com/openqasm/openqasm "https://github.com/openqasm/openqasm").
OpenQASM's future development is governed by the OpenQASM 3.0 [Technical Steering Committee](https://aws.amazon.com/blogs/quantum-computing/aws-joins-the-openqasm-3-0-technical-steering-committee/ "https://aws.amazon.com/blogs/quantum-computing/aws-joins-the-openqasm-3-0-technical-steering-committee/"), of which AWS is a member alongside IBM,
Microsoft, and the University of Innsbruck.

## When to use OpenQASM 3.0

OpenQASM provides an expressive framework to specify quantum programs through
low-level controls that are not architecture specific, making it well suited as a
representation across multiple gate-based devices. The Braket support for OpenQASM
furthers its adoption as a consistent approach to developing gate-based quantum
algorithms, reducing the need for users to learn and maintain libraries in multiple
frameworks.

If you have existing libraries of programs in OpenQASM 3.0, you can adapt them for
use with Braket rather than completely rewriting these circuits. Researchers and
developers should also benefit from an increasing number of available third-party
libraries with support for algorithm development in OpenQASM.

## How OpenQASM 3.0 works

Support for OpenQASM 3.0 from Braket provides feature parity with the current
Intermediate Representation. This means that anything you can do today on hardware
devices and on-demand simulators with Braket, you can do with OpenQASM using the
Braket API. You can run OpenQASM 3.0 programs by directly supplying
OpenQASM strings to all gate-based devices in a manner that is similar to how circuits
are currently supplied to devices on Braket. Braket users can also integrate
third-party libraries that support OpenQASM 3.0. The rest of this guide details how to
develop OpenQASM representations for use with Braket.

## Prerequisites

To use OpenQASM 3.0 on Amazon Braket, you must have version v1.8.0
of the [Amazon Braket
Python Schemas](https://github.com/aws/amazon-braket-schemas-python "https://github.com/aws/amazon-braket-schemas-python") and v1.17.0 or higher of the [Amazon Braket Python
SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python").

If you are a first time user of Amazon Braket, you need to enable
Amazon Braket. For instructions, see [Enable Amazon Braket](braket-enable-overview.md "braket-enable-overview.md").

## The Braket console

OpenQASM 3.0 tasks are available and can be managed within the
Amazon Braket console. On the console, you have the same experience submitting quantum tasks in
OpenQASM 3.0 as you had submitting existing quantum tasks.

## Additional resources

OpenQASM is available in all Amazon Braket Regions.

For an example notebook for getting started with OpenQASM on Amazon Braket, see [Braket Tutorials GitHub](https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Getting_Started_with_OpenQASM_on_Braket.ipynb "https://github.com/aws/amazon-braket-examples/blob/main/examples/braket_features/Getting_Started_with_OpenQASM_on_Braket.ipynb").
