**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Identity-based policy

examples for Amazon Glacier

By default, users and roles don't have permission to create or modify Amazon Glacier
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon Glacier, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Glacier](../../../service-authorization/latest/reference/list_amazons3glacier.md "../../../service-authorization/latest/reference/list_amazons3glacier.md") in the _Service Authorization Reference_.

The following is an example policy that grants permissions for three Amazon Glacier vault-related actions (`glacier:CreateVault`, `glacier:DescribeVault` and
`glacier:ListVaults`) on a resource, using the Amazon Resource Name
(ARN) that identifies all of the vaults in the `us-west-2` AWS Region.
ARNs uniquely identify AWS resources. For more information about ARNs used with Amazon Glacier,
see [Policy resources for Amazon Glacier](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glacier:CreateVault",
 "glacier:DescribeVault",
 "glacier:ListVaults"
 ],
 "Resource": "arn:aws:glacier:us-west-2:123456789012:vaults/*"
 }
 ]
 }`

```

The policy grants permissions to create, list, and obtain descriptions of
vaults in the `us-west-2` Region. The wildcard character (\*) at the end of
the ARN means that this statement can match any vault name.

###### Important

When you grant permissions to create a vault using the `glacier:CreateVault` operation, you
must specify a wildcard character (\*) because you don't know the vault name until after
you create the vault.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon Glacier
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#id-based-policy-view-own-permissions "#id-based-policy-view-own-permissions")
- [Customer Managed Policy Examples](#id-based-policy-customer-managed "#id-based-policy-customer-managed")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Glacier resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Using the Amazon Glacier

console

To access the Amazon Glacier console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon Glacier resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

The Amazon Glacier console provides an integrated environment for you to create and manage Amazon Glacier vaults. At a minimum IAM identities that you create must be granted permissions for the `glacier:ListVaults` action to view the Amazon Glacier console as shown in the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "glacier:ListVaults"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
 }`

```

AWS addresses many common use cases by providing standalone IAM policies
that are created and administered by AWS. Managed policies grant necessary permissions for
common use cases so you can avoid having to investigate what permissions are needed. For more
information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your account, are specific to Amazon Glacier:

- **AmazonGlacierReadOnlyAccess** – Grants read
  only access to Amazon Glacier through the AWS Management Console.
- **AmazonGlacierFullAccess** – Grants full access
  to Amazon Glacier through the AWS Management Console.

You can also create your own custom IAM policies to allow permissions for Amazon Glacier
API actions and resources. You can attach these custom policies to the custom IAM roles that you create for your Amazon Glacier vaults.

Both of the Amazon Glacier AWS Managed policies discussed in the next section grant permissions for `glacier:ListVaults`.

For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

## Allow users

to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Customer Managed Policy Examples

In this section, you can find example user policies that grant permissions for various Amazon Glacier actions. These policies work when you are using Amazon Glacier REST API, the Amazon SDKs, the AWS CLI, or, if applicable, the Amazon Glacier management console.

###### Note

All examples use the US West (Oregon) Region (`us-west-2`) and contain
fictitious account IDs.

###### Examples

- [Example 1: Allow a User to Download
  Archives from a Vault](#vault-access-policy-example-init-jobs "#vault-access-policy-example-init-jobs")
- [Example 2: Allow a User to Create a
  Vault and Configure Notifications](#vault-access-policy-example-create-vault "#vault-access-policy-example-create-vault")
- [Example 3: Allow a User to Upload
  Archives to a Specific Vault](#vault-access-policy-example-upload-archives "#vault-access-policy-example-upload-archives")
- [Example 4: Allow a User Full Permissions on a Specific Vault](#vault-access-policy-example-full-permission "#vault-access-policy-example-full-permission")

### Example 1: Allow a User to Download

Archives from a Vault

To download an archive, you first initiate a job to retrieve the archive. After the
retrieval job is complete, you can download the data. The following example policy
grants permissions for the `glacier:InitiateJob` action to initiate a job
(which allows the user to retrieve an archive or a vault inventory from the vault), and
permissions for the `glacier:GetJobOutput` action to download the retrieved
data. The policy also grants permissions to perform the `glacier:DescribeJob` action
so that the user can get the job status. For more information, see [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md").

The policy grants these permissions on a vault named `examplevault`. You can get the
vault ARN from the [Amazon Glacier console](https://console.aws.amazon.com/glacier/home "https://console.aws.amazon.com/glacier/home"),
or programmatically by calling either the [Describe Vault (GET vault)](api-vault-get.md "api-vault-get.md") or the
[List Vaults (GET vaults)](api-vaults-get.md "api-vaults-get.md")
API actions.

### Example 2: Allow a User to Create a

Vault and Configure Notifications

The following example policy grants permissions to create a vault in the
us-west-2 Region as specified in the `Resource` element and configure
notifications. For more information about working with notifications, see [Configuring Vault Notifications in Amazon Glacier](configuring-notifications.md "configuring-notifications.md"). The policy also grants permissions to
list vaults in the AWS Region and get a specific vault description.

###### Important

When you grant permissions to create a vault using the
`glacier:CreateVault` operation, you must specify a wildcard character (\*)
in the `Resource` value because you don't know the vault name until after you
create the vault.

### Example 3: Allow a User to Upload

Archives to a Specific Vault

The following example policy grants permissions to upload archives to a specific vault
in the us-west-2 Region. These permissions allow a user to upload an archive all at once using the [Upload Archive (POST archive)](api-archive-post.md "api-archive-post.md") API operation
or in parts using the [Initiate Multipart Upload (POST
multipart-uploads)](api-multipart-initiate-upload.md "api-multipart-initiate-upload.md") API operation.

### Example 4: Allow a User Full Permissions on a Specific Vault

The following example policy grants permissions for all Amazon Glacier actions on a vault named
`examplevault`.
