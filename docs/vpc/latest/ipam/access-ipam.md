# Access IPAM

As with other AWS services, you can create, access, and manage your IPAM using the following methods:

- **AWS Management Console**: Provides a web interface that you
  can use to create and manage your IPAM. See [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
- **AWS Command Line Interface (AWS CLI)**: Provides commands
  for a broad set of AWS services, including Amazon VPC. The AWS CLI is supported on
  Windows, macOS, and Linux. To get the AWS CLI, see [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").
- **AWS SDKs**: Provide language-specific APIs. The AWS SDKs
  take care of many of the connection details, such as calculating signatures,
  handling request retries, and handling errors. For more information, see [AWS SDKs](http://aws.amazon.com/tools/#SDKs "http://aws.amazon.com/tools/#SDKs").
- **Query API**: Provides low-level API actions that you call using
  HTTPS requests. Using the Query API is the most direct way to access IPAM. However,
  it requires your application to handle low-level details such as generating the hash
  to sign the request, and handling errors. For more information, see Amazon IPAM
  actions in the [Amazon EC2 API Reference](../../../AWSEC2/latest/APIReference.md "../../../AWSEC2/latest/APIReference.md").
  This guide primarily focuses on using the AWS Management Console to create, access, and
  manage your IPAM. In each description of how to complete a process in the console, we
  include links to the _AWS CLI Command Reference_ so that you can do the same tasks by
  using the AWS CLI.

If you are a first-time user of IPAM, review [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md") to learn about the role of IPAM in Amazon VPC and then
continue with the instructions in [Configure integration options for your IPAM](choose-single-user-or-orgs-ipam.md "choose-single-user-or-orgs-ipam.md").
