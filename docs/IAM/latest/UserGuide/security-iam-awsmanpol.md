# AWS managed policies for AWS Identity and Access Management and Access Analyzer

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](access_policies_managed-vs-inline.md#customer-managed-policies "access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](access_policies_managed-vs-inline.md#aws-managed-policies "access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## IAMReadOnlyAccess

Use the `IAMReadOnlyAccess` managed policy to allow read only access to IAM
resources. This policy grants permission to get and list all IAM resources. It allows
viewing details and activity reports for users, groups, roles, policies, identity
providers, and MFA devices. It does not include the ability to create or delete resources
or access to IAM Access Analyzer resources. View the [policy](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMReadOnlyAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMReadOnlyAccess") for
the full list of services and actions supported by this policy.

## IAMUserChangePassword

Use the `IAMUserChangePassword` managed policy to allow IAM users to change
their password.

You configure your IAM **Account settings** and the
**Password policy** to allow IAM users to change their IAM account
password. When you allow this action, IAM attaches the policy to each user.

To view the JSON policy, see [IAMUserChangePassword](../../../aws-managed-policy/latest/reference/IAMUserChangePassword.md "../../../aws-managed-policy/latest/reference/IAMUserChangePassword.md") in the AWS Managed Policy Reference Guide.

## IAMAccessAnalyzerFullAccess

Use the `IAMAccessAnalyzerFullAccess` AWS managed policy to allow your
administrators to access IAM Access Analyzer.

### Permissions groupings

This policy is grouped into statements based on the set of permissions
provided.

- **IAM Access Analyzer** – Allows full
  administrative permissions to all resources in IAM Access Analyzer.
- **Create service linked role** – Allows the
  administrator to create a [service-linked role](access-analyzer-using-service-linked-roles.md "access-analyzer-using-service-linked-roles.md"), which allows IAM Access Analyzer to analyze resources in
  other services on your behalf. This permission allows creating the service-linked
  role only for use by IAM Access Analyzer.
- **AWS Organizations** – Allows administrators to use
  IAM Access Analyzer for an organization in AWS Organizations. After [enabling
  trusted access](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") for IAM Access Analyzer in AWS Organizations, members of the management
  account can view findings across their organization.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "access-analyzer:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "access-analyzer.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit",
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:ListChildren",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListOrganizationalUnitsForParent",
 "organizations:ListParents",
 "organizations:ListRoots"
 ],
 "Resource": "*"
 }
 ]
}`

```

## IAMAccessAnalyzerReadOnlyAccess

Use the `IAMAccessAnalyzerReadOnlyAccess` AWS managed policy to allow
read-only access to IAM Access Analyzer.

To also allow read-only access to IAM Access Analyzer for AWS Organizations, create a customer managed
policy that allows the Describe and List actions from the [IAMAccessAnalyzerFullAccess](#security-iam-awsmanpol-IAMAccessAnalyzerFullAccess "#security-iam-awsmanpol-IAMAccessAnalyzerFullAccess") AWS managed
policy.

### Service-level permissions

This policy provides read-only access to IAM Access Analyzer. No other service permissions
are included in this policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IAMAccessAnalyzerReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "access-analyzer:CheckAccessNotGranted",
 "access-analyzer:CheckNoNewAccess",
 "access-analyzer:Get*",
 "access-analyzer:List*",
 "access-analyzer:ValidatePolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AccessAnalyzerServiceRolePolicy

You can't attach AccessAnalyzerServiceRolePolicy to your IAM entities. This policy is
attached to a service-linked role that allows IAM Access Analyzer to perform actions on your
behalf. For more information, see [Using
service-linked roles for AWS Identity and Access Management and Access Analyzer](access-analyzer-using-service-linked-roles.md "access-analyzer-using-service-linked-roles.md").

### Permissions groupings

This policy allows access to IAM Access Analyzer to analyze resource metadata from multiple
AWS services.

- **Amazon DynamoDB** – Allows permissions to view
  DynamoDB streams and tables.
- **Amazon Elastic Compute Cloud** – Allows permissions to
  describe IP addresses, snapshots, and VPCs.
- **Amazon Elastic Container Registry** – Allows permissions to
  describe image repositories, retrieve account settings, and retrieve registry and
  repository policies.
- **Amazon Elastic File System** – Allows permissions to view
  the description of an Amazon EFS file system and view the resource-level policy for an
  Amazon EFS file system.
- **AWS Identity and Access Management** – Allows permissions to
  retrieve information about a specified role and list the IAM roles that have a
  specified path prefix. Allows permissions to retrieve information about users,
  IAM groups, login profiles, access keys, and service last accessed
  data.
- **AWS Key Management Service** – Allows permissions to view
  detailed information about an KMS key and its key policies and grants.
- **AWS Lambda** – Allows permissions to view
  information about Lambda aliases, functions, layers, and aliases.
- **AWS Organizations** – Allows permissions to
  AWS Organizations and allows the creation of an analyzer within the AWS organization as
  the zone of trust.
- **Amazon Relational Database Service** – Allows permissions to view
  detailed information about Amazon RDS DB snapshots and Amazon RDS DB cluster
  snapshots.
- **Amazon Simple Storage Service** – Allows permissions to view
  detailed information about Amazon S3 access points, buckets, Amazon S3 directory bucket
  access points, and directory buckets.
- **AWS Secrets Manager** – Allows permissions to view
  detailed information about secrets and resource policies attached to
  secrets.
- **Amazon Simple Notification Service** – Allows permissions to view
  detailed information about a topic.
- **Amazon Simple Queue Service** – Allows permissions to view
  detailed information about specified queues.

To view the JSON policy, see [AccessAnalyzerServiceRolePolicy](../../../aws-managed-policy/latest/reference/AccessAnalyzerServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AccessAnalyzerServiceRolePolicy.md") in the AWS Managed Policy Reference
Guide.

## IAMAuditRootUserCredentials

Use the `IAMAuditRootUserCredentials` AWS managed policy to scope down
permissions when you [perform a privileged task
on an AWS Organizations member account](id_root-user-privileged-task.md "id_root-user-privileged-task.md") to audit root user credential status of a member
account. You can list or get individual root user credential information like:

- Whether there is a root user password
- If the root user has an access key and when it was last used
- If the root user has associated signing certificates
- The root user associated MFA devices
- List of the consolidated root user credential status

You can't attach `IAMAuditRootUserCredentials` to your IAM entities. This
policy is attached to [AssumeRoot](../../../STS/latest/APIReference/API_AssumeRoot.md "../../../STS/latest/APIReference/API_AssumeRoot.md") to perform
privileged tasks on a member account in your organization. For more information, see [Centrally manage root access for member
accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyAllOtherActionsOnAnyResource",
 "NotAction": [
 "iam:ListAccessKeys",
 "iam:ListSigningCertificates",
 "iam:GetLoginProfile",
 "iam:ListMFADevices",
 "iam:GetAccountSummary",
 "iam:GetUser",
 "iam:GetAccessKeyLastUsed"
 ],
 "Effect": "Deny",
 "Resource": "*"
 },
 {
 "Sid": "DenyAuditingCredentialsOnNonRootUserResource",
 "Action": [
 "iam:ListAccessKeys",
 "iam:ListSigningCertificates",
 "iam:GetLoginProfile",
 "iam:ListMFADevices" ,
 "iam:GetUser",
 "iam:GetAccessKeyLastUsed"
 ],
 "Effect": "Deny",
 "NotResource": "arn:aws:iam::*:root"
 }
 ]
}`

```

### Permissions groupings

This policy is grouped into statements based on the set of permissions
provided.

- **DenyAllOtherActionsOnAnyResource** –
  Denies access to credentials for all resources.
- **DenyAuditingCredentialsOnNonRootUserResource**
  – Denies access to credentials for all non-root user resources.

## IAMCreateRootUserPassword

Use the `IAMCreateRootUserPassword` AWS managed policy to scope down
permissions when you [perform a privileged task
on an AWS Organizations member account](id_root-user-privileged-task.md "id_root-user-privileged-task.md") to allow password recovery for a member account
with no root user credentials.

You can't attach `IAMCreateRootUserPassword` to your IAM entities. This
policy is attached to [AssumeRoot](../../../STS/latest/APIReference/API_AssumeRoot.md "../../../STS/latest/APIReference/API_AssumeRoot.md") to perform
privileged tasks on a member account in your organization. For more information, see [Centrally manage root access for member
accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyAllOtherActionsOnAnyResource",
 "NotAction": [
 "iam:CreateLoginProfile",
 "iam:GetLoginProfile"
 ],
 "Effect": "Deny",
 "Resource": "*"
 },
 {
 "Sid": "DenyCreatingPasswordOnNonRootUserResource",
 "Action": [
 "iam:CreateLoginProfile",
 "iam:GetLoginProfile"
 ],
 "Effect": "Deny",
 "NotResource": "arn:aws:iam::*:root"
 }
 ]
}`

```

### Permissions groupings

This policy is grouped into statements based on the set of permissions
provided.

- **DenyAllOtherActionsOnAnyResource** –
  Denies access to get or create a password for all resources.
- **DenyCreatingPasswordOnNonRootUserResource**
  – Denies access to get or create a password for all non-root user
  resources.

## IAMDeleteRootUserCredentials

Use the `IAMDeleteRootUserCredentials` AWS managed policy to scope down
permissions when you [perform a privileged task
on an AWS Organizations member account](id_root-user-privileged-task.md "id_root-user-privileged-task.md") to remove root user credentials including password,
access keys, signing certificates, and deactivating MFA. Additional permissions are
required for this privileged action, so you can view last used credential information,
verify last used information for the member account root user, and list permissions for all
root user credentials to be deleted.

You can't attach `IAMDeleteRootUserCredentials` to your IAM entities. This
policy is attached to [AssumeRoot](../../../STS/latest/APIReference/API_AssumeRoot.md "../../../STS/latest/APIReference/API_AssumeRoot.md") to perform
privileged tasks on a member account in your organization. For more information, see [Centrally manage root access for member
accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyAllOtherActionsOnAnyResource",
 "Effect": "Deny",
 "NotAction": [
 "iam:DeleteAccessKey",
 "iam:DeleteSigningCertificate",
 "iam:DeleteLoginProfile",
 "iam:DeactivateMFADevice",
 "iam:ListAccessKeys",
 "iam:ListSigningCertificates",
 "iam:GetLoginProfile",
 "iam:ListMFADevices",
 "iam:GetUser",
 "iam:GetAccessKeyLastUsed"
 ],

 "Resource": "*"
 },
 {
 "Sid": "DenyDeletingRootUserCredentialsOnNonRootUserResource",
 "Effect": "Deny",
 "Action": [
 "iam:DeleteAccessKey",
 "iam:DeleteSigningCertificate",
 "iam:DeleteLoginProfile",
 "iam:DeactivateMFADevice",
 "iam:ListAccessKeys",
 "iam:ListSigningCertificates",
 "iam:GetLoginProfile",
 "iam:ListMFADevices",
 "iam:GetUser",
 "iam:GetAccessKeyLastUsed"
 ],

 "NotResource": "arn:aws:iam::*:root"
 }
 ]
}`

```

### Permissions groupings

This policy is grouped into statements based on the set of permissions
provided.

- **DenyAllOtherActionsOnAnyResource** –
  Denies access to get or delete credentials for all resources.
- **DenyDeletingRootUserCredentialsOnNonRootUserResource** –
  Denies access to get or delete credentials for all non-root user resources.

## S3UnlockBucketPolicy

Use the `S3UnlockBucketPolicy` AWS managed policy to scope down permissions
when you [perform a privileged task
on an AWS Organizations member account](id_root-user-privileged-task.md "id_root-user-privileged-task.md") to remove a misconfigured bucket policy that
denies all principals from accessing an Amazon S3 bucket.

You can't attach `S3UnlockBucketPolicy` to your IAM entities. This policy
is attached to [AssumeRoot](../../../STS/latest/APIReference/API_AssumeRoot.md "../../../STS/latest/APIReference/API_AssumeRoot.md") to perform
privileged tasks on a member account in your organization. For more information, see [Centrally manage root access for member
accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyAllOtherActionsOnAnyResource",
 "NotAction": [
 "s3:DeleteBucketPolicy",
 "s3:PutBucketPolicy",
 "s3:GetBucketPolicy",
 "s3:ListAllMyBuckets"
 ],
 "Effect": "Deny",
 "Resource": "*"
 },
 {
 "Sid": "DenyManagingBucketPolicyForNonRootCallers",
 "Action": [
 "s3:DeleteBucketPolicy",
 "s3:PutBucketPolicy",
 "s3:GetBucketPolicy",
 "s3:ListAllMyBuckets"
 ],
 "Effect": "Deny",
 "Resource": "*",
 "Condition" : {
 "ArnNotLike" : {
 "aws:PrincipalArn" : "arn:aws:iam::*:root"
 }
 }
 }
 ]
}`

```

### Permissions groupings

This policy is grouped into statements based on the set of permissions
provided.

- **DenyAllOtherActionsOnAnyResource** –
  Denies access to bucket policies for all resources.
- **DenyManagingBucketPolicyForNonRootCallers**
  – Denies access to bucket policies for all non-root user resources.

## SQSUnlockQueuePolicy

Use the `SQSUnlockQueuePolicy` AWS managed policy to scope down permissions
when you [perform a privileged task
on an AWS Organizations member account](id_root-user-privileged-task.md "id_root-user-privileged-task.md") to delete an Amazon Simple Queue Service resource-based policy that
denies all principals from accessing an Amazon SQS queue.

You can't attach `SQSUnlockQueuePolicy` to your IAM entities. This policy
is attached to [AssumeRoot](../../../STS/latest/APIReference/API_AssumeRoot.md "../../../STS/latest/APIReference/API_AssumeRoot.md") to perform
privileged tasks on a member account in your organization. For more information, see [Centrally manage root access for member
accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management").

### Permissions groupings

This policy is grouped into statements based on the set of permissions
provided.

- **DenyAllOtherActionsOnAnyResource** –
  Denies access to Amazon SQS actions for all resources.
- **DenyGettingQueueAttributesOnNonOwnQueue**
  – Denies access to Amazon SQS queue attributes for queues owned by another
  account.
- **DenyActionsForNonRootUser** – Denies
  access to Amazon SQS actions for all non-root user resources.

## IAM and IAM Access Analyzer updates to AWS

managed policies

View details about updates to IAM and AWS managed policies since the service began
tracking these changes. For automatic alerts about changes to this page, subscribe to the
RSS feed on the IAM and IAM Access Analyzer Document history pages.

| Change                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                      | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [IAMUserChangePassword](https://console.aws.amazon.com/iam/home#policies/IAMUserChangePassword "https://console.aws.amazon.com/iam/home#policies/IAMUserChangePassword") – Added permissions                               | IAM added permissions to `IAMUserChangePassword` to allow<br>users specified within a path.                                                                                                                                                                                                                                      | May 28, 2025      |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added `iam:GetAccountAuthorizationDetails` to the<br>service-level permissions of<br>`AccessAnalyzerServiceRolePolicy`.                                                                                                                                                                                      | May 12, 2025      |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added support for Amazon S3 directory bucket access points to the<br>service-level permissions of<br>`AccessAnalyzerServiceRolePolicy`.                                                                                                                                                                      | March 31, 2025    |
| [IAMDeleteRootUserCredentials](https://console.aws.amazon.com/iam/home#policies/IAMDeleteRootUserCredentials "https://console.aws.amazon.com/iam/home#policies/IAMDeleteRootUserCredentials") – Removed permissions        | IAM removed the `iam:DeleteVirtualMFADevice` permission from<br>the managed policy.                                                                                                                                                                                                                                              | January 7, 2025   |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added support for permission to retrieve information about<br>Amazon ECR account settings and registry policies to the service-level permissions<br>of `AccessAnalyzerServiceRolePolicy`.                                                                                                                    | December 10, 2024 |
| [IAMAuditRootUserCredentials](https://console.aws.amazon.com/iam/home#policies/IAMAuditRootUserCredentials "https://console.aws.amazon.com/iam/home#policies/IAMAuditRootUserCredentials") – Added managed policy          | IAM added managed policies for [Centrally manage root access for<br>member accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management") to scope privileged tasks you can perform on AWS Organizations<br>member accounts.                                                         | November 14, 2024 |
| [IAMCreateRootUserPassword](https://console.aws.amazon.com/iam/home#policies/IAMCreateRootUserPassword "https://console.aws.amazon.com/iam/home#policies/IAMCreateRootUserPassword") – Added managed policy                | IAM added managed policies for [Centrally manage root access for<br>member accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management") to scope privileged tasks you can perform on AWS Organizations<br>member accounts.                                                         | November 14, 2024 |
| [IAMDeleteRootUserCredentials](https://console.aws.amazon.com/iam/home#policies/IAMDeleteRootUserCredentials "https://console.aws.amazon.com/iam/home#policies/IAMDeleteRootUserCredentials") – Added managed policy       | IAM added managed policies for [Centrally manage root access for<br>member accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management") to scope privileged tasks you can perform on AWS Organizations<br>member accounts.                                                         | November 14, 2024 |
| [S3UnlockBucketPolicy](https://console.aws.amazon.com/iam/home#policies/S3UnlockBucketPolicy "https://console.aws.amazon.com/iam/home#policies/S3UnlockBucketPolicy") – Added managed policy                               | IAM added managed policies for [Centrally manage root access for<br>member accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management") to scope privileged tasks you can perform on AWS Organizations<br>member accounts.                                                         | November 14, 2024 |
| [SQSUnlockQueuePolicy](https://console.aws.amazon.com/iam/home#policies/SQSUnlockQueuePolicy "https://console.aws.amazon.com/iam/home#policies/SQSUnlockQueuePolicy") – Added managed policy                               | IAM added managed policies for [Centrally manage root access for<br>member accounts](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management") to scope privileged tasks you can perform on AWS Organizations<br>member accounts.                                                         | November 14, 2024 |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added support for permission to retrieve information about<br>IAM user and role tags to the service-level permissions of<br>`AccessAnalyzerServiceRolePolicy`.                                                                                                                                               | October 29, 2024  |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added support for permission to retrieve information about<br>IAM user and role policies to the service-level permissions of<br>`AccessAnalyzerServiceRolePolicy`.                                                                                                                                           | May 30, 2024      |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added support for permission to retrieve the current state of<br>the block public access for Amazon EC2 snapshots to the service-level permissions of<br>`AccessAnalyzerServiceRolePolicy`.                                                                                                                  | January 23, 2024  |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added support for DynamoDB streams and tables to the<br>service-level permissions of `AccessAnalyzerServiceRolePolicy`.                                                                                                                                                                                      | January 11, 2024  |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added support for Amazon S3 directory buckets to the service-level<br>permissions of `AccessAnalyzerServiceRolePolicy`.                                                                                                                                                                                      | December 1, 2023  |
| [IAMAccessAnalyzerReadOnlyAccess](#security-iam-awsmanpol-IAMAccessAnalyzerReadOnlyAccess "#security-iam-awsmanpol-IAMAccessAnalyzerReadOnlyAccess") – Added permissions                                                   | IAM Access Analyzer added permissions to allow you to check whether updates to<br>your policies grant additional access.<br>This permission is required by IAM Access Analyzer to perform policy checks on<br>your policies.                                                                                                     | November 26, 2023 |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added IAM actions to the service-level permissions of<br>`AccessAnalyzerServiceRolePolicy` to support the following<br>actions:<br>• Listing entities for a policy<br>• Generating service last accessed details<br>• Listing access key information                                                         | November 26, 2023 |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added support for the following resource types to the<br>service-level permissions of `AccessAnalyzerServiceRolePolicy`:<br>• Amazon EBS volume snapshots<br>• Amazon ECR repositories<br>• Amazon EFS file systems<br>• Amazon RDS DB snapshots<br>• Amazon RDS DB cluster snapshots<br>• Amazon SNS topics | October 25, 2022  |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added the `lambda:GetFunctionUrlConfig` action to<br>the service-level permissions of<br>`AccessAnalyzerServiceRolePolicy`.                                                                                                                                                                                  | April 6, 2022     |
| [AccessAnalyzerServiceRolePolicy](https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy "https://console.aws.amazon.com/iam/home#policies/AccessAnalyzerServiceRolePolicy") – Added permissions | IAM Access Analyzer added new Amazon S3 actions to analyze metadata associated with<br>multi-region access points.                                                                                                                                                                                                               | September 2, 2021 |
| [IAMAccessAnalyzerReadOnlyAccess](#security-iam-awsmanpol-IAMAccessAnalyzerReadOnlyAccess "#security-iam-awsmanpol-IAMAccessAnalyzerReadOnlyAccess") – Added permissions                                                   | IAM Access Analyzer added a new action to grant `ValidatePolicy`<br>permissions to allow you to use the policy checks for validation.<br>This permission is required by IAM Access Analyzer to perform policy checks on<br>your policies.                                                                                        | March 16, 2021    |
| IAM Access Analyzer started tracking<br>changes                                                                                                                                                                            | IAM Access Analyzer started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                    | March 1, 2021     |
