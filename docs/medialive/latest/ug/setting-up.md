

# Preliminary steps for setting up to use MediaLive
<a name="setting-up"></a>

This topic describes preliminary steps, such as creating an account, that prepare you to use MediaLive. You aren't charged for these preliminary items. You are charged only for AWS services that you use. 

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Download tools](#setting-up-medialive-tools)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## Download tools
<a name="setting-up-medialive-tools"></a>

The AWS Management Console includes a console for AWS Elemental MediaLive, but if you want to access the services programmatically, see the following:
+ The API guides document the operations that the services support and provide links to the related SDK and CLI documentation:
  + [AWS Elemental MediaLive API Reference](https://docs.aws.amazon.com/medialive/latest/apireference/)
+ To call an API without having to handle low-level details like assembling raw HTTP requests, you can use an AWS SDK. The AWS SDKs provide functions and data types that encapsulate the functionality of AWS services. To download an AWS SDK and access installation instructions, see the applicable page: 
  + [Go](https://aws.amazon.com/sdk-for-go/)
  + [JavaScript](http://aws.amazon.com/sdkforbrowser/)
  + [.NET](https://aws.amazon.com/sdk-for-net/)
  + [Node.js](https://aws.amazon.com/sdk-for-node-js/)
  + [Python](https://github.com/boto/boto)
  + [Ruby](https://aws.amazon.com/sdk-for-ruby/)

  For a complete list of AWS SDKs, see [Tools for Amazon Web Services](http://aws.amazon.com/tools/).
+ You can use the AWS Command Line Interface (AWS CLI) to control multiple AWS services from the command line. You can also automate your commands using scripts. For more information, see [AWS Command Line Interface](https://aws.amazon.com/cli/).
+ AWS Tools for Windows PowerShell supports these AWS services. For more information, see [AWS Tools for PowerShell Cmdlet Reference](http://aws.amazon.com/documentation/powershell/).