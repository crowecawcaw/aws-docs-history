

# Setting up Amazon GameLift Streams as a developer
<a name="setting-up"></a>

To start using the Amazon GameLift Streams service with your projects, complete these basic setup tasks. If you already have an AWS account and a user under that account that you want to use with Amazon GameLift Streams, you can skip to [Download the Web SDK](#setting-up-materials). 

For more information on what you can do with an AWS account, see [Getting started with AWS](https://aws.amazon.com/getting-started/).

After you've completed these setup tasks, we recommend that you go to [Starting your first stream in Amazon GameLift Streams](streaming-process.md) and step through the tutorial, which covers the entire workflow for getting your content streaming in a web client.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Get programmatic access](#setting-up-access-keys)
+ [Download the Amazon GameLift Streams Web SDK](#setting-up-materials)
+ [Download the AWS CLI](#setting-up-prereqs)
+ [Set up billing alerts](#setting-up-billing)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Get programmatic access
<a name="setting-up-access-keys"></a>

In addition to your user sign-in credentials for the AWS Management Console, you need credentials for programmatic access, such as when working with the AWS Command Line Interface (AWS CLI). Programmatic credentials consist of a two-part set of access keys. Use one of the following methods to generate your access keys:
+ Method 1 – If you're using an administrative user created with the IAM Identity Center, see [ Getting IAM role credentials for AWS CLI access](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) to generate temporary security credentials for short-term access to AWS resources. When following these instructions, make sure you're signed in through your account's AWS access portal URL with your administrative user name and password (not your root user).
+ Method 2 – If you're using an existing IAM user and you haven't yet transitioned to using the IAM Identity Center, see [ Managing access keys for IAM users (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey) to generate long-term credentials for your user.

**Note**  
 As a best practice, use temporary credentials instead of long-term access keys. Temporary credentials include an access key ID, a secret access key, and a security token that indicates when the credentials expire. For more information, see [ Best practices for managing AWS access keys](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html) in the *AWS General Reference*. 

## Download the Amazon GameLift Streams Web SDK
<a name="setting-up-materials"></a>

 You can get started without any additional materials by using the in-console streaming experience. We recommend this as a starting point because it allows you to evaluate how your application performs on the Amazon GameLift Streams without setting up any additional infrastructure. For more information, proceed to [Getting started with Amazon GameLift Streams](getting-started.md). 

 When you're ready to build your own Amazon GameLift Streams integration, download the Amazon GameLift Streams Web SDK, available in the Resources section of the [Getting Started product page](https://aws.amazon.com/gamelift/streams/getting-started/). Amazon GameLift Streams is built to be integrated into your web applications. You will need to integrate our JavaScript-based Web SDK to setup streaming from your website or browser-based applications. The download also contains a sample web server that uses the Amazon GameLift Streams service, and a sample web client for connecting to streams. 

 For more information about setting up your own Amazon GameLift Streams solution, refer to [Amazon GameLift Streams backend service and web client](sdk.md). 

## Download the AWS CLI
<a name="setting-up-prereqs"></a>

 To use Amazon GameLift Streams with your content, we recommend that you get the AWS Command Line Interface (AWS CLI). The AWS CLI is an open source tool that gives you equivalent AWS SDK functionality by running commands from a terminal program.

1. Download and install the latest version of the AWS CLI for your operating system. See these [install instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

1. Configure the tool with your user access credentials and other preferences, as described in [Setting up the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html). With this configuration, you won't have to explicitly specify your credentials and other settings with every command.

1. Use the following command to verify your installation and get a list of available Amazon GameLift Streams commands:

   ```
   aws gameliftstreams help
   ```

## Set up billing alerts
<a name="setting-up-billing"></a>

 A stream group incurs cost per active stream capacity per second. To make sure your cost and usage stays within your budget, see [Create billing alerts to monitor usage](pricing.md#pricing-billing-alerts). 