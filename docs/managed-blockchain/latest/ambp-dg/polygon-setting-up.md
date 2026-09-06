

Amazon Managed Blockchain (AMB) Access Polygon is in preview release and is subject to change.

# Setting up Amazon Managed Blockchain (AMB) Access Polygon
<a name="polygon-setting-up"></a>

Before you use Amazon Managed Blockchain (AMB) Access Polygon for the first time, follow the steps in this section to create an AWS account. The following chapter discusses how to start using AMB Access Polygon.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Create an IAM user with appropriate permissions
<a name="create-an-iam-user"></a>

To create and work with AMB Access Polygon, you must have an AWS Identity and Access Management (IAM) principal (user or group) with permissions that allow necessary Managed Blockchain actions.

When making calls to the Polygon JSON-RPCs on Amazon Managed Blockchain, you can do so over an HTTPS connection authenticated using the [Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This means that only authorized IAM principals in the AWS account can make Polygon JSON-RPC calls. To do this, AWS credentials (an access key ID and a secret access key) must be provided with the call. 

You can also use *Accessor* tokens to make JSON-RPC calls to the Polygon network endpoints as a convenient alternative to the Signature Version 4 (SigV4) signing process. You must provide a `BILLING_TOKEN` from one of the Accessor tokens you [create](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateAccessor.html) and add as a parameter with your calls. However, you still need IAM access to get permissions to create Accessor tokens using the AWS Management Console, AWS CLI, and SDK.

For information about how to create an IAM user, see [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html). For more information about how to attach a permissions policy to a user, see [Changing permissions for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html). For an example of a permissions policy that you can use to give a user permission to work with AMB Access Polygon, see [Identity-based policy examples for Amazon Managed Blockchain (AMB) Access Polygon](security_iam_id-based-policy-examples.md).

## Install and configure the AWS Command Line Interface
<a name="install-aws-cli"></a>

If you have not already done so, install the latest AWS Command Line Interface (AWS CLI) to work with AWS resources from a terminal. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**Note**  
For CLI access, you need an access key ID and a secret access key. Use temporary credentials instead of long-term access keys when possible. Temporary credentials include an access key ID, a secret access key, and a security token that indicates when the credentials expire. For more information, see [ Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the *IAM User Guide*.