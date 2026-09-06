

# Getting started with AWS Organizations
<a name="orgs_getting-started"></a>

The following topics provide information to help you start using AWS Organizations. You can also use the following tutorials to begin performing tasks using AWS Organizations.

[Tutorial: Creating and configuring an organization](orgs_tutorials_basic.md)  
Get up and running with step-by-step instructions to create your organization, invite your first member accounts, create an OU hierarchy that contains your accounts, and apply some service control policies (SCPs).

[Tutorial: Monitor important changes to your organization with Amazon EventBridge](orgs_tutorials_cwe.md)  
Monitor key changes in your organization by configuring Amazon EventBridge to trigger an alarm in the form of an email, SMS text message, or log entry when actions that you designate occur in your organization. For example, many organizations want to know when a new account is created or when an account attempts to leave the organization.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Accessing AWS Organizations](#how-to-access)
+ [Tutorial: Creating and configuring an organization](orgs_tutorials_basic.md)
+ [Tutorial: Monitor an organization with Amazon EventBridge](orgs_tutorials_cwe.md)
+ [Working with AWS SDKs](sdk-general-information-section.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Accessing AWS Organizations
<a name="how-to-access"></a>

You can work with AWS Organizations in any of the following ways:

**AWS Management Console**  
The [AWS Organizations console](https://console.aws.amazon.com/organizations/) is a browser-based interface that you can use to manage your organization and your AWS resources. You can perform any task in your organization by using the console.

**AWS Command Line Tools**  
With the AWS command line tools, you can issue commands at your system's command line to perform AWS Organizations and AWS tasks. Working with the command line can be faster and more convenient than using the console. The command line tools also are useful if you want to build scripts that perform AWS tasks.  
AWS provides two sets of command line tools:  
+  [AWS Command Line Interface](https://aws.amazon.com/cli/)

  The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

  For information about installing and using the AWS CLI, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).
+  [AWS Tools for Windows PowerShell](https://aws.amazon.com/powershell/)

  The Tools for Windows PowerShell let developers and administrators manage their AWS services and resources in the PowerShell scripting environment. You can manage your AWS resources with the same PowerShell tools you use to manage your Windows, Linux, and MacOS environments.

  For information about installing and using the Tools for Windows PowerShell, see the [AWS Tools for PowerShell User Guide](https://docs.aws.amazon.com/powershell/latest/userguide/).

**AWS SDKs**  
The AWS SDKs consist of libraries and sample code for various programming languages and platforms (for example, Java, Python, Ruby, .NET, iOS, and Android). The SDKs take care of tasks such as cryptographically signing requests, managing errors, and retrying requests automatically. For more information about the AWS SDKs, including how to download and install them, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/#sdk).

**AWS Organizations HTTPS Query API**  
The AWS Organizations HTTPS Query API gives you programmatic access to AWS Organizations and AWS. The HTTPS Query API lets you issue HTTPS requests directly to the service. When you use the HTTPS API, you must include code to digitally sign requests using your credentials. For more information, see [Calling the API by Making HTTP Query Requests](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_query-requests.html) and the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/).