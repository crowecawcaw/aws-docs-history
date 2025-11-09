# AWS managed policies for AWS DataSync

To add permissions to users, groups, and roles, it's easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the `ReadOnlyAccess` AWS managed policy provides read-only
access to all AWS services and resources. When a service launches a new feature, AWS adds
read-only permissions for new operations and resources. For a list and descriptions of job
function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy:

AWSDataSyncReadOnlyAccess

You can attach the `AWSDataSyncReadOnlyAccess` policy to your IAM
identities. This policy grants read-only permissions for DataSync.

To view the permissions for this policy, see [AWSDataSyncReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSDataSyncReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSDataSyncReadOnlyAccess.md")
in the _AWS Managed Policy Reference_ .

## AWS managed policy:

AWSDataSyncFullAccess

You can attach the `AWSDataSyncFullAccess` policy to your IAM identities. This policy grants administrative permissions for DataSync and is required for
AWS Management Console access to the service. `AWSDataSyncFullAccess` provides full
access to DataSync API operations and the operations that interact with related resources
(such as Amazon S3 buckets, Amazon EFS file systems, AWS KMS keys, and Secrets Manager secrets). The policy also
grants permissions for Amazon CloudWatch, including creating log groups and creating or updating a
resource policy.

To view the permissions for this policy, see [AWSDataSyncFullAccess](../../../aws-managed-policy/latest/reference/AWSDataSyncFullAccess.md "../../../aws-managed-policy/latest/reference/AWSDataSyncFullAccess.md")
in the _AWS Managed Policy Reference_ .

## AWS managed policy:

AWSDataSyncServiceRolePolicy

You can't attach the `AWSDataSyncServiceRolePolicy` policy to your IAM
identities. This policy is attached to a service-linked role that allows DataSync to perform
actions on your behalf. For more information, see [Using service-linked roles for
DataSync](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants administrative permissions that allow the service-linked role to
create Amazon CloudWatch logs for DataSync tasks using Enhanced mode.

## Policy updates

| Change                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess "#security-iam-awsmanpol-awsdatasyncfullaccess") – Change                             | DataSync modified permission statements for<br>`AWSDataSyncFullAccess`:<br>The updated statements remove tagging conditions from the permissions<br>DataSync uses to create Secrets Manager secrets.                                                                                                                                                                                                                                                                     | May 13, 2025      |
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess "#security-iam-awsmanpol-awsdatasyncfullaccess") – Change                             | DataSync added new permissions to `AWSDataSyncFullAccess`:<br>• `secretsmanager:CreateSecret`<br>• `secretsmanager:PutSecretValue`<br>• `secretsmanager:DeleteSecret`<br>• `secretsmanager:UpdateSecret`<br>These permissions let DataSync create, edit, and delete AWS Secrets Manager<br>secrets.                                                                                                                                                                      | May 7, 2025       |
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess "#security-iam-awsmanpol-awsdatasyncfullaccess") – Change                             | DataSync added new permissions to `AWSDataSyncFullAccess`:<br>• `secretsmanager:ListSecrets`<br>• `kms:ListAliases`<br>• `kms:DescribeKey`<br>These permissions let DataSync retrieve metadata about your AWS Secrets Manager<br>secrets and AWS KMS keys, including any aliases associated with your<br>keys.                                                                                                                                                           | April 23, 2025    |
| [AWSDataSyncServiceRolePolicy](#security-iam-awsmanpol-awsdatasyncservicerolepolicy "#security-iam-awsmanpol-awsdatasyncservicerolepolicy") –<br>Change     | DataSync added new permissions to the<br>`AWSDataSyncServiceRolePolicy` policy that's used by the DataSync<br>service-linked role `AWSServiceRoleForDataSync`:<br>• `secretsmanager:DescribeSecret`<br>• `secretsmanager:GetSecretValue`<br>These permissions let DataSync read metadata and values for secrets managed<br>by AWS Secrets Manager.                                                                                                                       | April 15, 2025    |
| [AWSDataSyncServiceRolePolicy](#security-iam-awsmanpol-awsdatasyncservicerolepolicy "#security-iam-awsmanpol-awsdatasyncservicerolepolicy") – New<br>policy | DataSync added a policy that's used by the DataSync service-linked role<br>`AWSServiceRoleForDataSync`. This new managed policy<br>automatically creates Amazon CloudWatch logs for your DataSync tasks that use Enhanced<br>mode.                                                                                                                                                                                                                                       | October 30, 2024  |
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess "#security-iam-awsmanpol-awsdatasyncfullaccess") – Change                             | DataSync added new a permission to `AWSDataSyncFullAccess`:<br>• `iam:CreateServiceLinkedRole`<br>This permission lets DataSync create service-linked roles for you.                                                                                                                                                                                                                                                                                                     | October 30, 2024  |
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess "#security-iam-awsmanpol-awsdatasyncfullaccess") – Change                             | DataSync added new a permission to `AWSDataSyncFullAccess`:<br>• `ec2:DescribeRegions`<br>This permission lets you choose opt-in Regions when creating a DataSync task<br>for transfers between AWS Regions.                                                                                                                                                                                                                                                             | July 22, 2024     |
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess "#security-iam-awsmanpol-awsdatasyncfullaccess") – Change                             | DataSync added new a permission to `AWSDataSyncFullAccess`:<br>• `s3:ListBucketVersions`<br>This permission lets you choose a specific version of your [DataSync manifest](transferring-with-manifest.md "transferring-with-manifest.md").                                                                                                                                                                                                                               | February 16, 2024 |
| [AWSDataSyncFullAccess](#security-iam-awsmanpol-awsdatasyncfullaccess "#security-iam-awsmanpol-awsdatasyncfullaccess") – Change                             | DataSync added new permissions to `AWSDataSyncFullAccess`:<br>• `ec2:DescribeVpcEndpoints`<br>• `elasticfilesystem:DescribeAccessPoints`<br>• `fsx:DescribeStorageVirtualMachines`<br>• `outposts:ListOutposts`<br>• `s3:GetBucketLocation`<br>• `s3-outposts:ListAccessPoints`<br>• `s3-outposts:ListRegionalBuckets`<br>These permissions help you create DataSync agents and locations for Amazon EFS,<br>Amazon FSx for NetApp ONTAP, Amazon S3, and S3 on Outposts. | May 2, 2023       |
| DataSync started tracking changes                                                                                                                           | DataSync started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                          | March 1, 2021     |
