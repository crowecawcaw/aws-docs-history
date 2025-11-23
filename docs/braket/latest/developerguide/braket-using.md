# Running your quantum tasks with Amazon Braket

Braket provides secure, on-demand access to
different types of quantum computers. You have access to gate-based quantum computers from
AQT, IonQ, IQM, and Rigetti, as well as an Analog
Hamiltonian Simulator from QuEra. You also have no upfront commitment, and no need to procure
access through individual providers.

- The [Amazon Braket
  Console](https://console.aws.amazon.com/braket/home "https://console.aws.amazon.com/braket/home") provides device information and status to help you create, manage,
  and monitor your resources and quantum tasks.
- Submit and run quantum tasks through the [Amazon Braket Python
  SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python"), as well as through the console. The SDK is accessible through preconfigured
  Amazon Braket notebooks.
- The [Amazon Braket API](../APIReference/Welcome.md "../APIReference/Welcome.md") is accessible through the Amazon Braket
  Python SDK and notebooks. You can make calls directly to the API if
  you are building applications that work with quantum computing programmatically.
  The examples throughout this section demonstrate how you can work with the Amazon Braket
  API directly using the Amazon Braket Python SDK along with the [AWS Python SDK for Braket (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html").

**More about the Amazon Braket Python SDK**

To work with the Amazon Braket Python SDK, first install the AWS Python
SDK for Braket (Boto3) so that you can communicate with the AWS API. You
can think of the Amazon Braket Python SDK as a convenient wrapper around
Boto3 for quantum customers.

- Boto3 contains interfaces you need to tap into the AWS API. (Note
  that Boto3 is a large Python SDK that talks to the AWS API. Most
  AWS services support a Boto3 interface.)
- The Amazon Braket Python SDK contains software modules for circuits,
  gates, devices, result types, and other parts of a quantum task. Each time you create a
  program, you import the modules you need for that quantum task.
- The Amazon Braket Python SDK is accessible through notebooks, which
  are pre-loaded with all of the modules and dependencies you need for running quantum
  tasks.
- You can import modules from the Amazon Braket Python SDK into any
  Python script if you do not wish to work with notebooks.
  After you have [installed Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html"), an overview of steps for creating a quantum task through the
  Amazon Braket Python SDK resembles the following:

1. (Optionally) Open your notebook.
2. Import the SDK modules you need for your circuits.
3. Specify a QPU or simulator.
4. Instantiate the circuit.
5. Run the circuit.
6. Collect the results.
   The examples in this section show details of each step.

For more examples, see the [Amazon Braket Examples](https://github.com/aws/amazon-braket-examples "https://github.com/aws/amazon-braket-examples") repository on GitHub.

###### In this section:

- [Submitting quantum tasks to QPUs](braket-submit-tasks.md "braket-submit-tasks.md")
- [Running multiple programs](braket-batching-tasks.md "braket-batching-tasks.md")
- [When will my quantum task run?](braket-task-when.md "braket-task-when.md")
- [Working with reservations](braket-reservations.md "braket-reservations.md")
- [Error mitigation techniques](braket-error-mitigation.md "braket-error-mitigation.md")
