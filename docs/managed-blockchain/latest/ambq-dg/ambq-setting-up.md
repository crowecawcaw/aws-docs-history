

# Setting up Amazon Managed Blockchain (AMB) Query
<a name="ambq-setting-up"></a>

Before you use Amazon Managed Blockchain (AMB) Query for the first time, follow the steps in this section to create an AWS account. The following section discusses how to get started using AMB Query.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Create an IAM user with appropriate permissions
<a name="create-an-iam-user"></a>

To create and work with AMB Query, you must create an AWS Identity and Access Management (IAM) principal (user or group) with permissions that allow necessary Managed Blockchain actions.

Only IAM principals can make AMB Query API requests. When making calls to the AMB Query APIs, you can do so over an HTTPS connection authenticated using the [Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This means that only authorized IAM principals in the AWS account can make AMB Query API calls. To do this, AWS credentials (an access key ID and secret access key) must be provided with the call.

For information about how to create an IAM user, see [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html). For more information about how to attach a permissions policy to a user, see [Changing permissions for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html). For an example of a permissions policy that you can use to give a user permission to work with AMB Query, see [Identity-based policy examples for Amazon Managed Blockchain (AMB) Query](security_iam_id-based-policy-examples.md).

## Install and configure the AWS Command Line Interface
<a name="install-aws-cli"></a>

If you have not already done so, install the latest AWS Command-Line Interface (CLI) to work with AWS resources from a terminal. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Note**  
For CLI access, you need an access key ID and a secret access key. Use temporary credentials instead of long-term access keys when possible. Temporary credentials include an access key ID, a secret access key, and a security token that indicates when the credentials expire. For more information, see [ Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the *IAM User Guide*.

## Use the AWS Management Console to query blockchains using Amazon Managed Blockchain (AMB) Query
<a name="query-console-access"></a>

You can access Amazon Managed Blockchain (AMB) Query and make queries on supported blockchain networks using the AWS Management Console. The following steps show how to do this:

1. Open the Amazon Managed Blockchain console at [https://console.aws.amazon.com/managedblockchain/](https://console.aws.amazon.com/managedblockchain/).

1. Choose **Query editor** from the **Query **section.

1. Choose from one of the supported **Blockchain network**s.

1. Choose the **Query type** you want to run.

1. Enter the relevant parameters for the **Query type** you selected and **Run query**.

AMB Query will run your query and you will see results in the **Query results** window.