# API references and repos for Amazon Braket

###### Tip

**Learn the foundations of quantum computing with AWS!**
Enroll in the [Amazon Braket Digital Learning Plan](https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs "https://skillbuilder.aws/learning-plan/EH35DWGU3R/amazon-braket--knowledge-badge-readiness-path-includes-labs")
and earn your own Digital badge after completing a series of learning courses and a digital assessment.

Amazon Braket provides APIs, SDKs, and a command line interface that you can use to create and manage notebook instances and train and deploy models.

- [Amazon Braket Python SDK (Recommended)](https://amazon-braket-sdk-python.readthedocs.io/en/latest/# "https://amazon-braket-sdk-python.readthedocs.io/en/latest/#")
- [Amazon Braket API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md")
- [AWS Command Line Interface](../../../cli/latest/reference/braket/index.md "../../../cli/latest/reference/braket/index.md")
- [AWS SDK for .NET](../../../sdkfornet/v3/apidocs/items/Braket/NBraket.md "../../../sdkfornet/v3/apidocs/items/Braket/NBraket.md")
- [AWS SDK for C++](https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_braket.html "https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_braket.html")
- [AWS SDK for GoAPI Reference](../../../sdk-for-go/api/service/braket.md "../../../sdk-for-go/api/service/braket.md")
- [AWS SDK for Java](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/braket/package-summary.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/braket/package-summary.md")
- [AWS SDK for JavaScript](../../../AWSJavaScriptSDK/latest/AWS/Braket.md "../../../AWSJavaScriptSDK/latest/AWS/Braket.md")
- [AWS SDK for PHP](../../../aws-sdk-php/v3/api/class-Aws.Braket.md "../../../aws-sdk-php/v3/api/class-Aws.Braket.md")
- [AWS SDK for Python (Boto)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html")
- [AWS SDK for Ruby](../../../sdk-for-ruby/v3/api/Aws/Braket.md "../../../sdk-for-ruby/v3/api/Aws/Braket.md")
  You can also get code examples from the Amazon Braket Tutorials GitHub repository.

- [Braket Tutorials GitHub](https://github.com/aws/amazon-braket-examples "https://github.com/aws/amazon-braket-examples")

## Core repositories

The following displays a list of core repositories that contain key packages that are
used for Braket:

- [Braket Python
  SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python") - Use the Braket Python SDK to set up your code on
  Jupyter notebooks in the Python programming language. After your
  Jupyter notebooks are set up, you can run your code on Braket
  devices and simulators
- [Braket
  Schemas](https://github.com/aws/amazon-braket-schemas-python "https://github.com/aws/amazon-braket-schemas-python") - The contract between the Braket SDK and the Braket
  service.
- [Braket Default Simulator](https://github.com/aws/amazon-braket-default-simulator-python "https://github.com/aws/amazon-braket-default-simulator-python") - All our local quantum simulators for
  Braket (state vector and density matrix).

## Plugins

Then there are the various plugins that are used along with various devices and
programming tools. These include Braket supported plugins as well as plugins that are
supported by third parties as shown below.

**Amazon Braket supported**:

- [Amazon Braket algorithm library](https://github.com/aws-samples/amazon-braket-algorithm-library "https://github.com/aws-samples/amazon-braket-algorithm-library") - A catalog of pre-built quantum
  algorithms written in Python. Run them as they are or use them as a starting point
  to build more complex algorithms.
- [Braket-PennyLane plugin](https://github.com/aws/amazon-braket-pennylane-plugin-python "https://github.com/aws/amazon-braket-pennylane-plugin-python") - Use PennyLane as the QML
  framework on Braket.

**Third-party (Braket team monitors and
contributes)**:

- [Qiskit-Braket provider](https://github.com/qiskit-community/qiskit-braket-provider "https://github.com/qiskit-community/qiskit-braket-provider") - Use the Qiskit SDK to access
  Braket resources.
- [Braket-Julia SDK](https://github.com/awslabs/Braket.jl "https://github.com/awslabs/Braket.jl") -
  (EXPERIMENTAL) A Julia native version of the Braket SDK
