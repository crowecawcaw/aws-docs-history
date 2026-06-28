**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Setting up your account to use the services

This topic describes preliminary steps, such as creating an account, to prepare you to
use AWS WAF, AWS Firewall Manager, and AWS Shield Advanced. You aren't charged for these preliminary
items. You are charged only for AWS services that you use.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Download tools](#setting-up-waf-tools "#setting-up-waf-tools")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Download tools

The AWS Management Console includes a console for AWS WAF, AWS Shield Advanced, and AWS Firewall Manager, but if you want to access the services
programmatically, see the following:

- The API guides document the operations that the services support and provide links to the related SDK and CLI documentation:

  - [AWS WAF API Reference](../APIReference.md "../APIReference.md")
  - [AWS Shield Advanced API Reference](../DDOSAPIReference.md "../DDOSAPIReference.md")
  - [AWS Firewall Manager API Reference](../../../fms/2018-01-01/APIReference/Welcome.md "../../../fms/2018-01-01/APIReference/Welcome.md")

- To call an API without having to handle low-level details like
  assembling raw HTTP requests, you can use an AWS SDK. The AWS SDKs provide
  functions and data types that encapsulate the functionality of AWS services.
  To download an AWS SDK and access installation instructions, see the applicable page:

  - [Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/")
  - [JavaScript](http://aws.amazon.com/sdkforbrowser/ "http://aws.amazon.com/sdkforbrowser/")
  - [.NET](https://aws.amazon.com/sdk-for-net/ "https://aws.amazon.com/sdk-for-net/")
  - [Node.js](https://aws.amazon.com/sdk-for-node-js/ "https://aws.amazon.com/sdk-for-node-js/")
  - [PHP](https://aws.amazon.com/sdk-for-php/ "https://aws.amazon.com/sdk-for-php/")
  - [Python](https://github.com/boto/boto "https://github.com/boto/boto")
  - [Ruby](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/")
    For a complete list of AWS SDKs, see [Tools for
    Amazon Web Services](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/").

- You can use the AWS Command Line Interface (AWS CLI) to control multiple AWS services
  from the command line. You can also automate your commands using scripts. For more information,
  see [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").
- AWS Tools for Windows PowerShell supports these AWS services. For more information, see [AWS Tools for PowerShell Cmdlet Reference](http://aws.amazon.com/documentation/powershell/ "http://aws.amazon.com/documentation/powershell/").
