# Setting up for AMB Access Ethereum

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Create an IAM user with appropriate permissions

To create and work with Ethereum resources in Amazon Managed Blockchain (AMB), you need an AWS Identity and Access Management (IAM)
principal (user or group) with permissions that allow necessary AMB Access actions on those resources.
Example actions include creating or deleting nodes.

An IAM principal is also required to make AMB Access API requests. Ethereum API calls to an Ethereum node in Amazon Managed Blockchain (AMB) can be authenticated by using the
[Signature Version 4 (SigV4) signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").
This means that only authorized IAM principals in the AWS account that created the node can interact with it using
the Ethereum APIs. AWS credentials (an access key ID and secret access key) must be provided with the call.

You can also use _Accessor_ tokens to make JSON-RPC calls to the Ethereum network as a
convenient alternative to the Signature Version 4 (SigV4) signing process. You must provide a `BILLING_TOKEN`
from one of the Accessor tokens you create and add as a parameter with your requests. However, you still need IAM
access to get permissions to create Accessor tokens using the AWS Management Console, AWS CLI, and SDK.

For information about how to create an IAM user, see [Creating an IAM user in your AWS
account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md"). For more information about how to attach a permissions policy to a user, see
[Changing
permissions for an IAM user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md"). For an example of a permissions policy that you can use to
give a user permission to work with AMB Access Ethereum resources, see [Performing all available actions for AMB Access Ethereum](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-example "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-example").

## Install and configure the AWS Command Line Interface

If you have not already done so, install the latest AWS Command Line Interface (AWS CLI) to work
with AWS resources from a terminal. For more information, see [Installing or updating the latest
version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

###### Note

For CLI access, you need an access key ID and a secret access key.
Use temporary credentials instead of long-term access keys when possible.
Temporary credentials include an access key ID, a secret access key, and a
security token that indicates when the credentials expire. For more information,
see [Using temporary credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.
