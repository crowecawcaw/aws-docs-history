

# Setting up for AMB Access Ethereum
<a name="ethereum-setting-up"></a>

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Create an IAM user with appropriate permissions
<a name="create-an-iam-user"></a>

To create and work with Ethereum resources in Amazon Managed Blockchain (AMB), you need an AWS Identity and Access Management (IAM) principal (user or group) with permissions that allow necessary AMB Access actions on those resources. Example actions include creating or deleting nodes.

An IAM principal is also required to make AMB Access API requests. Ethereum API calls to an Ethereum node in Amazon Managed Blockchain (AMB) can be authenticated by using the [Signature Version 4 (SigV4) signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This means that only authorized IAM principals in the AWS account that created the node can interact with it using the Ethereum APIs. AWS credentials (an access key ID and secret access key) must be provided with the call.

You can also use *Accessor* tokens to make JSON-RPC calls to the Ethereum network as a convenient alternative to the Signature Version 4 (SigV4) signing process. You must provide a `BILLING_TOKEN` from one of the Accessor tokens you create and add as a parameter with your requests. However, you still need IAM access to get permissions to create Accessor tokens using the AWS Management Console, AWS CLI, and SDK.

For information about how to create an IAM user, see [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html). For more information about how to attach a permissions policy to a user, see [Changing permissions for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html). For an example of a permissions policy that you can use to give a user permission to work with AMB Access Ethereum resources, see [Performing all available actions for AMB Access Ethereum](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-example).

## Install and configure the AWS Command Line Interface
<a name="install-aws-cli"></a>

If you have not already done so, install the latest AWS Command Line Interface (AWS CLI) to work with AWS resources from a terminal. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Note**  
For CLI access, you need an access key ID and a secret access key. Use temporary credentials instead of long-term access keys when possible. Temporary credentials include an access key ID, a secret access key, and a security token that indicates when the credentials expire. For more information, see [ Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the *IAM User Guide*.