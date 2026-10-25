

# Setting up AWS Network Firewall
<a name="setting-up"></a>

This topic describes preliminary steps, such as getting an AWS account, to prepare you to use Network Firewall. You aren't charged to set up your account or for the other preliminary items. You are charged only for AWS services that you use. 

**Note**  
Network Firewall is a network traffic firewall for your Amazon Virtual Private Cloud VPCs. If you're already working with VPCs, the setup described here shouldn't be necessary.

After you complete these steps, see [Getting started with Network Firewall](getting-started.md) to continue getting started with Network Firewall.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Setting up tool access](#setting-up-tools)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## Setting up tool access
<a name="setting-up-tools"></a>

The AWS Management Console includes a console for Network Firewall, but if you want to access Network Firewall programmatically or through the command line, the following documentation and tools will help you:
+ If you want to call the Network Firewall API without handling low-level details like assembling raw HTTP requests, you can use an AWS SDK. The AWS SDKs provide functions and data types that encapsulate the functionality of Network Firewall and other AWS services. To download an AWS SDK, see the applicable page, which also includes prerequisites and installation instructions:
  + [Java](https://aws.amazon.com/sdk-for-java/)
  + [JavaScript](http://aws.amazon.com/sdkforbrowser/)
  + [.NET](https://aws.amazon.com/sdk-for-net/)
  + [Node.js](https://aws.amazon.com/sdk-for-node-js/)
  + [PHP](https://aws.amazon.com/sdk-for-php/)
  + [Python](https://github.com/boto/boto)
  + [Ruby](https://aws.amazon.com/sdk-for-ruby/)

  For a complete list of AWS SDKs, see [Tools for Amazon Web Services](http://aws.amazon.com/tools/).
+ If you're using a programming language for which AWS doesn't provide an SDK, the [AWS Network Firewall API Reference](https://docs.aws.amazon.com/network-firewall/latest/APIReference/) documents the operations that Network Firewall supports. 
+ The AWS Command Line Interface (AWS CLI) supports Network Firewall. The AWS CLI lets you control multiple AWS services from the command line and automate them through scripts. For more information, see [AWS Command Line Interface](https://aws.amazon.com/cli/).
+ AWS Tools for Windows PowerShell supports Network Firewall. For more information, see [AWS Tools for PowerShell Cmdlet Reference](http://aws.amazon.com/documentation/powershell/).