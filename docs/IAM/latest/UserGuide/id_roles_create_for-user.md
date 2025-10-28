# Create a role to give permissions to an IAM

user

You can use IAM roles to provide access to your AWS resources. With IAM roles, you
can establish trust relationships between your _trusting_
account and other AWS _trusted_ accounts. The trusting
account owns the resource to be accessed and the trusted account contains the users who need
access to the resource. However, it is possible for another account to own a resource in your
account. For example, the trusting account might allow the trusted account to create new
resources, such as creating new objects in an Amazon S3 bucket. In that case, the account that
creates the resource owns the resource and controls who can access that resource.

After you create the trust relationship, an IAM user or an application from the trusted
account can use the AWS Security Token Service (AWS STS) [`AssumeRole`](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API operation. This operation provides temporary security
credentials that enable access to AWS resources in your account.

The accounts can both be controlled by you, or the account with the users can be controlled
by a third party. If the other account with the users is an AWS account that you do not
control, then you can use the `externalId` attribute. The external ID can be any word
or number that is agreed upon between you and the administrator of the third-party account. This
option automatically adds a condition to the trust policy that allows the user to assume the
role only if the request includes the correct `sts:ExternalID`. For more information,
see [Access to AWS accounts owned by third
parties](id_roles_common-scenarios_third-party.md "id_roles_common-scenarios_third-party.md").

For information about how to use roles to delegate permissions, see [Roles terms and concepts](id_roles.md#id_roles_terms-and-concepts "id_roles.md#id_roles_terms-and-concepts"). For
information about using a service role to allow services to access resources in your account,
see [Create a role to delegate permissions to an
AWS service](id_roles_create_for-service.md "id_roles_create_for-service.md").

## Creating an IAM role (console)

You can use the AWS Management Console to create a role that an IAM user can assume. For example,
assume that your organization has multiple AWS accounts to isolate a development environment
from a production environment. For high-level information about creating a role that allows
users in the development account to access resources in the production account, see [Example scenario using
separate development and production accounts](id_roles_common-scenarios_aws-accounts.md#id_roles_common-scenarios_aws-accounts-example "id_roles_common-scenarios_aws-accounts.md#id_roles_common-scenarios_aws-accounts-example").

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- `access-analyzer:ValidatePolicy`
- `iam:AttachRolePolicy`
- `iam:CreatePolicy`
- `iam:CreateRole`
- `iam:GetAccountSummary`
- `iam:GetPolicy`
- `iam:GetPolicyVersion`
- `iam:GetRole`
- `iam:ListAccountAliases`
- `iam:ListAttachedRolePolicies`
- `iam:ListOpenIDConnectProviders`
- `iam:ListPolicies`
- `iam:ListRolePolicies`
- `iam:ListRoles`
- `iam:ListRoleTags`
- `iam:ListSAMLProviders`

[Show moreShow less](# "#")

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the console, choose **Roles** and
   then choose **Create role**.
3. Choose **AWS account** role type.
4. To create a role for your account, choose **This account**. To
   create a role for another account, choose **Another AWS account**
   and enter the **Account ID** to which you want to grant access to
   your resources.

The administrator of the specified account can grant permission to assume this
role to any IAM user in that account. To do this, the administrator attaches a
policy to the user or a group that grants permission for the
`sts:AssumeRole` action. That policy must specify the role's ARN as the
`Resource`. 5. If you are granting permissions to users from an account that you do not
control, and the users will assume this role programmatically, select
**Require external ID**. The external ID can be any word or
number that is agreed upon between you and the administrator of the third party
account. This option automatically adds a condition to the trust policy that allows
the user to assume the role only if the request includes the correct
`sts:ExternalID`. For more information, see [Access to AWS accounts owned by third
parties](id_roles_common-scenarios_third-party.md "id_roles_common-scenarios_third-party.md").

###### Important

Choosing this option restricts access to the role only through the AWS CLI,
Tools for Windows PowerShell, or the AWS API. This is because you cannot use the AWS console to
switch to a role that has an `externalId` condition in its trust
policy. However, you can create this kind of access programmatically by writing a
script or an application using the relevant SDK. For more information and a sample
script, see [How to Enable Cross-Account Access to the AWS Management Console](https://aws.amazon.com/blogs/security/how-to-enable-cross-account-access-to-the-aws-management-console "https://aws.amazon.com/blogs/security/how-to-enable-cross-account-access-to-the-aws-management-console") in the AWS
Security Blog. 6. If you want to restrict the role to users who sign in with multi-factor
authentication (MFA), select **Require MFA**. This adds a condition
to the role's trust policy that checks for an MFA sign-in. A user who wants to
assume the role must sign in with a temporary one-time password from a configured
MFA device. Users without MFA authentication cannot assume the role. For more
information about MFA, see [AWS Multi-factor authentication in IAM](id_credentials_mfa.md "id_credentials_mfa.md") 7. Choose **Next**. 8. IAM includes a list of the AWS managed and customer managed policies in your
account. Select the policy to use for the permissions policy or choose
**Create policy** to open a new browser tab and create a new
policy from scratch. For more information, see [Creating IAM policies](access_policies_create-console.md#access_policies_create-start "access_policies_create-console.md#access_policies_create-start"). After you create the policy, close
that tab and return to your original tab. Select the checkbox next to the
permissions policies that you want anyone who assumes the role to have. If you
prefer, you can select no policies at this time, and then attach policies to the
role later. By default, a role has no permissions. 9. (Optional) Set a [permissions
boundary](access_policies_boundaries.md "access_policies_boundaries.md"). This is an advanced feature.

Open the **Set permissions boundary** section and choose
**Use a permissions boundary to control the maximum role
permissions**. Select the policy to use for the permissions
boundary. 10. Choose **Next**. 11. For **Role name**, enter a name for your role. Role names must
be unique within your AWS account. When a role name is used in a policy or as part
of an ARN, the role name is case sensitive. When a role name appears to customers in
the console, such as during the sign-in process, the role name is case insensitive.
Because various entities might reference the role, you can't edit the name of
the role after it is created. 12. (Optional) For **Description**, enter a description for the new
role. 13. Choose **Edit** in the **Step 1: Select trusted
entities** or **Step 2: Add permissions** sections to
edit the use cases and permissions for the role. You will be returned to previous
pages to make the edits. 14. (Optional) Add metadata to the role by attaching tags as key–value pairs.
For more information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](id_tags.md "id_tags.md"). 15. Review the role and then choose **Create role**.

###### Important

Remember that this is only the first half of the configuration required. You
must also give individual users in the trusted account permissions to switch to
the role in the console, or assume the role programmatically. For more information
about this step, see [Grant a user permissions to switch
roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md").

## Creating an IAM role (AWS CLI)

Creating a role from the AWS CLI involves multiple steps. When you use the console to create
a role, many of the steps are done for you, but with the AWS CLI you must explicitly perform
each step yourself. You must create the role and then assign a permissions policy to the role.
Optionally, you can also set the [permissions
boundary](access_policies_boundaries.md "access_policies_boundaries.md") for your role.

###### To create a role for cross-account access (AWS CLI)

1. Create a role: [aws iam
   create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md")
2. Attach a managed permissions policy to the role: [aws iam attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md")

or

Create an inline permissions policy for the role: [aws iam put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md") 3. (Optional) Add custom attributes to the role by attaching tags: [aws iam tag-role](../../../cli/latest/reference/iam/tag-role.md "../../../cli/latest/reference/iam/tag-role.md")

For more information, see [Managing tags on IAM roles (AWS CLI or
AWS API)](id_tags_roles.md#id_tags_roles_procs-cli-api "id_tags_roles.md#id_tags_roles_procs-cli-api"). 4. (Optional) Set the [permissions
boundary](access_policies_boundaries.md "access_policies_boundaries.md") for the role: [aws iam
put-role-permissions-boundary](../../../cli/latest/reference/iam/put-role-permissions-boundary.md "../../../cli/latest/reference/iam/put-role-permissions-boundary.md")

A permissions boundary controls the maximum permissions that a role can have.
Permissions boundaries are an advanced AWS feature.

The following example shows the first two, and most common steps for creating a
cross-account role in a simple environment. This example allows any user in the
`123456789012` account to assume the role and view the
`example_bucket` Amazon S3 bucket. This example also assumes that you are using a
client computer running Windows, and have already configured your command line interface with
your account credentials and Region. For more information, see [Configuring the AWS Command Line
Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").

In this example, include the following trust policy in the first command when you create
the role. This trust policy allows users in the `123456789012` account to
assume the role using the `AssumeRole` operation, but only if the user provides MFA
authentication using the `SerialNumber` and `TokenCode` parameters. For
more information about MFA, see [AWS Multi-factor authentication in IAM](id_credentials_mfa.md "id_credentials_mfa.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": { "AWS": "arn:aws:iam::123456789012:root" },
 "Action": "sts:AssumeRole",
 "Condition": { "Bool": { "aws:MultiFactorAuthPresent": "true" } }
 }
 ]
}`

```

###### Important

If your `Principal` element contains the ARN for a specific IAM role or
user, then that ARN is transformed to a unique principal ID when the policy is saved. This
helps mitigate the risk of someone escalating their permissions by removing and recreating
the role or user. You don't normally see this ID in the console because there is also a
reverse transformation back to the ARN when the trust policy is displayed. However, if you
delete the role or user, then the principal ID appears in the console because AWS can no
longer map it back to an ARN. Therefore, if you delete and recreate a user or role
referenced in a trust policy's `Principal` element, you must edit the role to
replace the ARN.

When you use the second command, you must attach an existing managed policy to the role.
The following permissions policy allows anyone who assumes the role to perform only the
`ListBucket` action on the `example_bucket` Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::example_bucket"
 }
 ]
}`

```

To create this `Test-UserAccess-Role` role, you must first save the previous
trust policy with the name `trustpolicyforacct123456789012.json` to the
`policies` folder in your local `C:` drive. Then save the previous
permissions policy as a customer managed policy in your AWS account with the name
`PolicyForRole`. You can then use the following commands to create the role and
attach the managed policy.

```
`# Create the role and attach the trust policy file that allows users in the specified account to assume the role.
$` `aws iam create-role --role-name Test-UserAccess-Role --assume-role-policy-document file://C:\policies\trustpolicyforacct123456789012.json`

`# Attach the permissions policy (in this example a managed policy) to the role to specify what it is allowed to do.
$` `aws iam attach-role-policy --role-name Test-UserAccess-Role --policy-arn arn:aws:iam::123456789012:policy/PolicyForRole`
```

###### Important

Remember that this is only the first half of the configuration required. You must also
give individual users in the trusted account permissions to switch to the role. For more
information about this step, see [Grant a user permissions to switch
roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md").

After you create the role and grant it permissions to perform AWS tasks or access AWS
resources, any users in the `123456789012` account can assume the role. For
more information, see [Switch to an IAM role (AWS CLI)](id_roles_use_switch-role-cli.md "id_roles_use_switch-role-cli.md").

## Creating an IAM role (AWS API)

Creating a role from the AWS API involves multiple steps. When you use the console to
create a role, many of the steps are done for you, but with the API you must explicitly
perform each step yourself. You must create the role and then assign a permissions policy to
the role. Optionally, you can also set the [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md") for your role.

###### To create a role in code (AWS API)

1. Create a role: [CreateRole](../APIReference/API_CreateRole.md "../APIReference/API_CreateRole.md")

For the role's trust policy, you can specify a file location. 2. Attach a managed permission policy to the role: [AttachRolePolicy](../APIReference/API_AttachRolePolicy.md "../APIReference/API_AttachRolePolicy.md")

or

Create an inline permission policy for the role: [PutRolePolicy](../APIReference/API_PutRolePolicy.md "../APIReference/API_PutRolePolicy.md")

###### Important

Remember that this is only the first half of the configuration required. You must
also give individual users in the trusted account permissions to switch to the role. For
more information about this step, see [Grant a user permissions to switch
roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md"). 3. (Optional) Add custom attributes to the user by attaching tags: [TagRole](../APIReference/API_TagRole.md "../APIReference/API_TagRole.md")

For more information, see [Managing tags on IAM users (AWS CLI or
AWS API)](id_tags_users.md#id_tags_users_procs-cli-api "id_tags_users.md#id_tags_users_procs-cli-api"). 4. (Optional) Set the [permissions
boundary](access_policies_boundaries.md "access_policies_boundaries.md") for the role: [PutRolePermissionsBoundary](../APIReference/API_PutRolePermissionsBoundary.md "../APIReference/API_PutRolePermissionsBoundary.md")

A permissions boundary controls the maximum permissions that a role can have.
Permissions boundaries are an advanced AWS feature.

After you create the role and grant it permissions to perform AWS tasks or access AWS
resources, you must grant permissions to users in the account to allow them to assume the
role. For more information about assuming a role, see [Switch to an IAM role (AWS API)](id_roles_use_switch-role-api.md "id_roles_use_switch-role-api.md").

## Creating an IAM role

(AWS CloudFormation)

For information about creating an IAM role in AWS CloudFormation, see the [resource and property reference](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md") and
[examples](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md#aws-resource-iam-role--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md#aws-resource-iam-role--examples") in the _AWS CloudFormation User Guide_.

For more information about IAM templates in AWS CloudFormation, see [AWS Identity and Access Management template snippets](../../../AWSCloudFormation/latest/UserGuide/quickref-iam.md "../../../AWSCloudFormation/latest/UserGuide/quickref-iam.md") in the
_AWS CloudFormation User Guide_.
