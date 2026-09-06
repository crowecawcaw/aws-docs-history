

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Setting up AWS WAF Classic
<a name="classic-setting-up-waf"></a>

**Warning**  
AWS WAF Classic is is going through a planned end-of-life process. Refer to your AWS Health dashboard for the milestones and dates specific to your Region.

**Note**  
This is **AWS WAF Classic** documentation. You should only use this version if you created AWS WAF resources, like rules and web ACLs, in AWS WAF prior to November 2019, and you have not migrated them over to the latest version yet. To migrate your web ACLs, see [Migrating your AWS WAF Classic resources to AWS WAF](waf-migrating-from-classic.md).  
**For the latest version of AWS WAF**, see [AWS WAF](waf-chapter.md). 

This topic describes preliminary steps, such as creating a user account, to prepare you to use AWS WAF Classic. You aren't charged for these. You are charged only for AWS services that you use. 

**Note**  
If you're a new user to AWS WAF, don't follow these setup steps for AWS WAF Classic. Instead, follow the steps for the latest version of AWS WAF, at [Setting up your account to use the services](setting-up-waf.md). 

After you complete these steps, see [Getting started with AWS WAF Classic](classic-getting-started.md) to continue getting started with AWS WAF Classic.

**Note**  
AWS Shield Standard is included with AWS WAF Classic and does not require additional setup. For more information, see [How AWS Shield and Shield Advanced work](ddos-overview.md).

Before you use AWS WAF Classic or AWS Shield Advanced for the first time, complete the steps in this section. 

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Download tools](#classic-setting-up-waf-tools)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Download tools
<a name="classic-setting-up-waf-tools"></a>

The AWS Management Console includes a console for AWS WAF Classic, but if you want to access AWS WAF Classic programmatically, see the following:
+ If you want to call the AWS WAF Classic API without having to handle low-level details like assembling raw HTTP requests, you can use an AWS SDK. The AWS SDKs provide functions and data types that encapsulate the functionality of AWS WAF Classic and other AWS services. To download an AWS SDK, see the applicable page, which also includes prerequisites and installation instructions:
  + [Java](https://aws.amazon.com/sdk-for-java/)
  + [JavaScript](http://aws.amazon.com/sdkforbrowser/)
  + [.NET](https://aws.amazon.com/sdk-for-net/)
  + [Node.js](https://aws.amazon.com/sdk-for-node-js/)
  + [PHP](https://aws.amazon.com/sdk-for-php/)
  + [Python](https://github.com/boto/boto)
  + [Ruby](https://aws.amazon.com/sdk-for-ruby/)

  For a complete list of AWS SDKs, see [Tools for Amazon Web Services](http://aws.amazon.com/tools/).
+ If you're using a programming language for which AWS doesn't provide an SDK, the [AWS WAF API Reference](https://docs.aws.amazon.com/waf/latest/APIReference/) documents the operations that AWS WAF Classic supports. 
+ The AWS Command Line Interface (AWS CLI) supports AWS WAF Classic. The AWS CLI lets you control multiple AWS services from the command line and automate them through scripts. For more information, see [AWS Command Line Interface](https://aws.amazon.com/cli/).
+ AWS Tools for Windows PowerShell supports AWS WAF Classic. For more information, see [AWS Tools for PowerShell Cmdlet Reference](http://aws.amazon.com/documentation/powershell/).