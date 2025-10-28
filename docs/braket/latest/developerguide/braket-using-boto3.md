# Working with AWS Boto3

Boto3 is the AWS SDK for Python. With Boto3, Python developers can create, configure,
and manage AWS services, such as Amazon Braket. Boto3 provides an
object-oriented API, as well as low-level access to Amazon Braket.

Follow the instructions in the [Boto3 Quickstart guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html") to learn how to install and configure Boto3.

Boto3 provides the core functionality that works along with the Amazon Braket
Python SDK to help you configure and run your quantum tasks. Python customers
always need to install Boto3, because that is the core implementation. If you want to make
use of additional helper methods, you also need to install the Amazon Braket SDK.

For example, when you call `CreateQuantumTask`, the
Amazon Braket SDK submits the request to Boto3, which then calls the AWS
API.

###### In this section:

- [Turn on the Amazon Braket Boto3
  client](braket-using-boto3-client.md "braket-using-boto3-client.md")
- [Configure AWS CLI profiles for Boto3 and the
  Braket SDK](braket-using-boto3-profiles.md "braket-using-boto3-profiles.md")
