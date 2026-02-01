Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using the Amazon Redshift management interfaces for provisioned

clusters

###### Note

This topic focuses on Amazon Redshift management interfaces for provisioned clusters. There
are similar management interfaces for Amazon Redshift Serverless and Amazon Redshift Data API.

Amazon Redshift supports several management interfaces that you can use to create, manage, and
delete Amazon Redshift clusters: the AWS SDKs, the AWS Command Line Interface (AWS CLI), and the Amazon Redshift management
API.

The Amazon Redshift API – You can call this Amazon Redshift
management API by submitting a request. Requests are HTTP or HTTPS requests that use the
HTTP verbs `GET` or `POST` with a parameter named `Action`.
Calling the Amazon Redshift API is the most direct way to access the Amazon Redshift service. However, it
requires that your application handle low-level details such as error handling and
generating a hash to sign the request.

- For information about building and signing an Amazon Redshift API request, see [Signing an HTTP request](amazon-redshift-signing-requests.md "amazon-redshift-signing-requests.md").
- For information about the Amazon Redshift API actions and data types for Amazon Redshift, see the
  [Amazon Redshift API reference](../APIReference/Welcome.md "../APIReference/Welcome.md").
  AWS SDKs – You can use the AWS SDKs to perform
  Amazon Redshift cluster-related operations. Several of the SDK libraries wrap the underlying
  Amazon Redshift API. They integrate the API functionality into the specific programming language
  and handle many of the low-level details, such as calculating signatures, handling request
  retries, and error handling. Calling the wrapper functions in the SDK libraries can greatly
  simplify the process of writing an application to manage an Amazon Redshift cluster.

- Amazon Redshift is supported by the AWS SDKs for Java, .NET, PHP, Python, Ruby, and
  Node.js. The wrapper functions for Amazon Redshift are documented in the reference manual
  for each SDK. For a list of the AWS SDKs and links to their documentation, see
  [Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/").
- This guide provides examples of working with Amazon Redshift using the Java SDK. For more
  general AWS SDK code examples, see [Code examples for Amazon Redshift using AWS SDKs](service_code_examples.md "service_code_examples.md").
  AWS CLI – The CLI provides a set of command line tools
  that you can use to manage AWS services from Windows, Mac, and Linux computers. The AWS CLI
  includes commands based on the Amazon Redshift API actions.

- For information about installing and setting up the Amazon Redshift CLI, see [Setting up the Amazon Redshift CLI](setting-up-rs-cli.md "setting-up-rs-cli.md").
- For reference material on the Amazon Redshift CLI commands, see [Amazon Redshift](../../../cli/latest/reference/redshift/index.md "../../../cli/latest/reference/redshift/index.md") in the _AWS CLI Reference._
