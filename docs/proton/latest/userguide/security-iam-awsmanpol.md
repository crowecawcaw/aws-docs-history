End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# AWS managed policies for AWS Proton

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer managed
policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get started
quickly, you can use our AWS managed policies. These policies cover common use cases and are
available in your AWS account. For more information about AWS managed policies, see [AWS
managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities (users,
groups, and roles) where the policy is attached. Services are most likely to update an AWS
managed policy when a new feature is launched or when new operations become available. Services
do not remove permissions from an AWS managed policy, so policy updates won't break your
existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services.
For example, the **ReadOnlyAccess** AWS managed policy provides
read-only access to all AWS services and resources. When a service launches a new feature,
AWS adds read-only permissions for new operations and resources. For a list and descriptions
of job function policies, see [AWS managed policies for job
functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

AWS Proton provides managed IAM policies and trust relationships that you can attach to
users, groups, or roles that allow differing levels of control over resources and API
operations. You can apply these policies directly, or you can use them as starting points for
creating your own policies.

The following trust relationship is used for each of the AWS Proton managed policies.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "ExampleTrustRelationshipWithProtonConfusedDeputyPrevention",
 "Effect": "Allow",
 "Principal": {
 "Service": "proton.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:proton:*:`123456789012`:environment/*"
 }
 }
 }
}`

```

## AWS managed policy:

AWSProtonFullAccess

You can attach `AWSProtonFullAccess` to your IAM entities. AWS Proton also
attaches this policy to a service role that allows AWS Proton to perform actions on your behalf.

This policy grants administrative permissions that allow full access to AWS Proton actions and
limited access to other AWS service actions that AWS Proton depends on.

The policy includes the following key action namespaces:

- `proton` – Allows administrators full access to AWS Proton
  APIs.
- `iam` – Allows administrators to pass roles to AWS Proton. This is
  required so that AWS Proton can make API calls to other services on the administrator's
  behalf.
- `kms` – Allows administrators to add a grant to a customer managed
  key.
- `codeconnections` – Allows administrators to list and pass
  codeconnections so they can be used by AWS Proton.

For more information, see [AWSProtonFullAccess](../../../aws-managed-policy/latest/reference/AWSProtonFullAccess.md "../../../aws-managed-policy/latest/reference/AWSProtonFullAccess.md").

## AWS managed policy:

AWSProtonDeveloperAccess

You can attach `AWSProtonDeveloperAccess` to your IAM entities. AWS Proton also
attaches this policy to a service role that allows AWS Proton to perform actions on your
behalf.

This policy grants permissions that allow limited access to AWS Proton actions and to other
AWS actions that AWS Proton depends on. The scope of these permissions is designed to support the
role of a developer who creates and deploys AWS Proton services.

This policy doesn't provide access to AWS Proton template and environment _create,
delete and update_ APIs. If developers need even more limited permissions than
what this policy provides, we recommend creating a custom policy that is scoped down to grant
the [least
privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege").

The policy includes the following key action namespaces:

- `proton` – Allows contributors access to a limited set of AWS Proton
  APIs.
- `codeconnections` – Allows contributors to list and pass
  codeconnections so they can be used by AWS Proton.

For more information, see [AWSProtonDeveloperAccess](../../../aws-managed-policy/latest/reference/AWSProtonDeveloperAccess.md "../../../aws-managed-policy/latest/reference/AWSProtonDeveloperAccess.md").

## AWS managed policy:

AWSProtonReadOnlyAccess

You can attach `AWSProtonReadOnlyAccess` to your IAM entities. AWS Proton also
attaches this policy to a service role that allows AWS Proton to perform actions on your behalf.

This policy grants permissions that allow read-only access to AWS Proton actions and limited
read-only access to other AWS service actions that AWS Proton depends on.

The policy includes the following key action namespaces:

- `proton` – Allows contributors read-only access to AWS Proton
  APIs.

For more information, see [AWSProtonReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSProtonReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSProtonReadOnlyAccess.md").

## AWS managed policy:

AWSProtonSyncServiceRolePolicy

AWS Proton attaches this policy to the [AWSServiceRoleForProtonSync](using-service-linked-roles-sync.md "using-service-linked-roles-sync.md") service-linked role that allows AWS Proton to perform
template sync.

This policy grants permissions that allow limited access to AWS Proton actions and to other
AWS service actions that AWS Proton depends on.

The policy includes the following key action namespaces:

- `proton` – Allows AWS Proton sync limited access to AWS Proton
  APIs.
- `codeconnections` – Allows AWS Proton sync limited access to CodeConnections
  APIs.

For more information, see [AWSProtonSyncServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSProtonSyncServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSProtonSyncServiceRolePolicy.md").

## AWS

managed policy: AWSProtonCodeBuildProvisioningBasicAccess

Permissions CodeBuild needs to run a build for AWS Proton CodeBuild Provisioning. You can attach
`AWSProtonCodeBuildProvisioningBasicAccess` to your CodeBuild Provisioning Role.

This policy grants the minimum permissions for AWS Proton CodeBuild Provisioning to function. It
grants permissions that allow CodeBuild to generate build logs. It also grants permission for
Proton to make Infrastructure as Code (IaC) outputs available to AWS Proton users. It does not
provide permissions needed by IaC tools to manage infrastructure.

The policy includes the following key action namespaces:

- `logs` ‐ Allows CodeBuild to generate build logs. Without this permission,
  CodeBuild will fail to start.
- `proton` ‐ Allows a CodeBuild Provisioning command to call `aws
proton notify-resource-deployment-status-change` for updating the IaaC outputs for
  a given AWS Proton resource.

For more information, see [AWSProtonCodeBuildProvisioningBasicAccess](../../../aws-managed-policy/latest/reference/AWSProtonCodeBuildProvisioningBasicAccess.md "../../../aws-managed-policy/latest/reference/AWSProtonCodeBuildProvisioningBasicAccess.md").

## AWS

managed policy: AWSProtonCodeBuildProvisioningServiceRolePolicy

AWS Proton attaches this policy to the [AWSServiceRoleForProtonCodeBuildProvisioning](using-service-linked-roles-codebuild.md "using-service-linked-roles-codebuild.md") service-linked role that allows AWS Proton to perform CodeBuild-based
provisioning.

This policy grants permissions that allow limited access to AWS service actions that
AWS Proton depends on.

The policy includes the following key action namespaces:

- `cloudformation` – Allows AWS Proton CodeBuild-based provisioning limited
  access to AWS CloudFormation APIs.
- `codebuild` – Allows AWS Proton CodeBuild-based provisioning limited access
  to CodeBuild APIs.
- `iam` – Allows administrators to pass roles to AWS Proton. This is
  required so that AWS Proton can make API calls to other services on the administrator's
  behalf.
- `servicequotas` – Allows AWS Proton to check the CodeBuild concurrent build
  limit, which ensures proper build queuing.

For more information, see [AWSProtonCodeBuildProvisioningServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSProtonCodeBuildProvisioningServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSProtonCodeBuildProvisioningServiceRolePolicy.md").

## AWS

managed policy: AWSProtonServiceGitSyncServiceRolePolicy

AWS Proton attaches this policy to the [AWSServiceRoleForProtonServiceSync](using-service-linked-roles-sync.md "using-service-linked-roles-sync.md") service-linked role that allows AWS Proton to perform
service sync.

This policy grants permissions that allow limited access to AWS Proton actions and to other
AWS service actions that AWS Proton depends on.

The policy includes the following key action namespaces:

- `proton` – Allows AWS Proton sync limited access to AWS Proton APIs.

For more information, see [AWSProtonServiceGitSyncServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSProtonServiceGitSyncServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSProtonServiceGitSyncServiceRolePolicy.md").

## AWS Proton updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Proton since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS Proton Document history page.

| Change                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Date               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSProtonCodeBuildProvisioningServiceRolePolicy](#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningServiceRolePolicy "#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningServiceRolePolicy") – Update to an existing policy | The managed policy for the service-linked role that allows AWS Proton to perform<br>CodeBuild-based provisioning now grants permissions to call the CloudFormation<br>`TagResource` and `UntagResource` API actions. These<br>permissions are required to perform tagging operations on resources.                                                                                                                                                                                                                     | June 15, 2024      |
| [AWSProtonFullAccess](#security-iam-awsmanpol-AWSProtonFullAccess "#security-iam-awsmanpol-AWSProtonFullAccess") – Update<br>to an existing policy                                                                                  | The managed policy for the service-linked role to use Git sync with Git<br>repositories has been updated for resources with both service prefixes. For more<br>information, see [Using service-linked roles<br>for AWS CodeConnections](../../../dtconsole/latest/userguide/what-is-dtconsole.md "../../../dtconsole/latest/userguide/what-is-dtconsole.md") and [Managed<br>policies](../../../dtconsole/latest/userguide/security-iam-awsmanpol.md "../../../dtconsole/latest/userguide/security-iam-awsmanpol.md"). | April 25, 2024     |
| [AWSProtonDeveloperAccess](#security-iam-awsmanpol-AWSProtonDeveloperAccess "#security-iam-awsmanpol-AWSProtonDeveloperAccess") –<br>Update to an existing policy                                                                   | The managed policy for the service-linked role to use Git sync with Git<br>repositories has been updated for resources with both service prefixes. For more<br>information, see [Using service-linked roles<br>for AWS CodeConnections](../../../dtconsole/latest/userguide/what-is-dtconsole.md "../../../dtconsole/latest/userguide/what-is-dtconsole.md") and [Managed<br>policies](../../../dtconsole/latest/userguide/security-iam-awsmanpol.md "../../../dtconsole/latest/userguide/security-iam-awsmanpol.md"). | April 25, 2024     |
| [AWSProtonSyncServiceRolePolicy](#security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy "#security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy")<br>– Update to an existing policy                                                 | The managed policy for the service-linked role to use Git sync with Git<br>repositories has been updated for resources with both service prefixes. For more<br>information, see [Using service-linked roles<br>for AWS CodeConnections](../../../dtconsole/latest/userguide/what-is-dtconsole.md "../../../dtconsole/latest/userguide/what-is-dtconsole.md") and [Managed<br>policies](../../../dtconsole/latest/userguide/security-iam-awsmanpol.md "../../../dtconsole/latest/userguide/security-iam-awsmanpol.md"). | April 25, 2024     |
| [AWSProtonCodeBuildProvisioningServiceRolePolicy](#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningServiceRolePolicy "#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningServiceRolePolicy") – Update to an existing policy | AWS Proton updated this policy to add permissions to ensure accounts have the<br>necessary CodeBuild concurrent build limit in order to use CodeBuild Provisioning.                                                                                                                                                                                                                                                                                                                                                    | May 12, 2023       |
| [AWSProtonServiceGitSyncServiceRolePolicy](#security-iam-awsmanpol-AwsProtonServiceGitSyncServiceRolePolicy "#security-iam-awsmanpol-AwsProtonServiceGitSyncServiceRolePolicy") – New policy                                        | AWS Proton added a new policy to allow AWS Proton to perform service syncing. The<br>policy is used in the [AWSServiceRoleForProtonServiceSync](using-service-linked-roles-sync.md#service-linked-role-permissions-sync "using-service-linked-roles-sync.md#service-linked-role-permissions-sync") service-linked role.                                                                                                                                                                                                | March 31, 2023     |
| [AWSProtonDeveloperAccess](#security-iam-awsmanpol-AWSProtonDeveloperAccess "#security-iam-awsmanpol-AWSProtonDeveloperAccess") –<br>Update to an existing policy                                                                   | AWS Proton added a new `GetResourcesSummary` action that allows you to<br>view a summary of your templates, deployed template resources, and out of date<br>resources.                                                                                                                                                                                                                                                                                                                                                 | November 18, 2022  |
| [AWSProtonReadOnlyAccess](#security-iam-awsmanpol-AWSProtonReadOnlyAccess "#security-iam-awsmanpol-AWSProtonReadOnlyAccess") –<br>Update to an existing policy                                                                      | AWS Proton added a new `GetResourcesSummary` action that allows you to<br>view a summary of your templates, deployed template resources, and out of date<br>resources.                                                                                                                                                                                                                                                                                                                                                 | November 18, 2022  |
| [AWSProtonCodeBuildProvisioningBasicAccess](#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningBasicAccess "#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningBasicAccess") – New policy                                     | AWS Proton added a new policy that gives CodeBuild the permissions it needs to run a<br>build for AWS Proton CodeBuild Provisioning.                                                                                                                                                                                                                                                                                                                                                                                   | November 16, 2022  |
| [AWSProtonSyncServiceRolePolicy](#security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy "#security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy")<br>– New policy                                                                   | AWS Proton added a new policy to allow AWS Proton to perform operations related to<br>CodeBuild-based provisioning. The policy is used in the [AWSServiceRoleForProtonCodeBuildProvisioning](using-service-linked-roles-codebuild.md "using-service-linked-roles-codebuild.md")<br>service-linked role.                                                                                                                                                                                                                | September 02, 2022 |
| [AWSProtonFullAccess](#security-iam-awsmanpol-AWSProtonFullAccess "#security-iam-awsmanpol-AWSProtonFullAccess") – Update<br>to an existing policy                                                                                  | AWS Proton updated this policy to provide access to new AWS Proton API operations and<br>to fix permission issues for some AWS Proton console operations.                                                                                                                                                                                                                                                                                                                                                              | March 30, 2022     |
| [AWSProtonDeveloperAccess](#security-iam-awsmanpol-AWSProtonDeveloperAccess "#security-iam-awsmanpol-AWSProtonDeveloperAccess") –<br>Update to an existing policy                                                                   | AWS Proton update this policy to provide access to new AWS Proton API operations and<br>to fix permission issues for some AWS Proton console operations.                                                                                                                                                                                                                                                                                                                                                               | March 30, 2022     |
| [AWSProtonReadOnlyAccess](#security-iam-awsmanpol-AWSProtonReadOnlyAccess "#security-iam-awsmanpol-AWSProtonReadOnlyAccess") –<br>Update to an existing policy                                                                      | AWS Proton update this policy to provide access to new AWS Proton API operations and<br>to fix permission issues for some AWS Proton console operations.                                                                                                                                                                                                                                                                                                                                                               | March 30, 2022     |
| [AWSProtonSyncServiceRolePolicy](#security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy "#security-iam-awsmanpol-AWSProtonSyncServiceRolePolicy")<br>– New policy                                                                   | AWS Proton added a new policy to allow AWS Proton to perform operations related to<br>template sync. The policy is used in the [AWSServiceRoleForProtonSync](using-service-linked-roles.md "using-service-linked-roles.md") service-linked role.                                                                                                                                                                                                                                                                       | November 23, 2021  |
| [AWSProtonFullAccess](#security-iam-awsmanpol-AWSProtonFullAccess "#security-iam-awsmanpol-AWSProtonFullAccess") – New<br>policy                                                                                                    | AWS Proton added a new policy to provide administrative role access to AWS Proton API<br>operations and to the AWS Proton console.                                                                                                                                                                                                                                                                                                                                                                                     | June 09, 2021      |
| [AWSProtonDeveloperAccess](#security-iam-awsmanpol-AWSProtonDeveloperAccess "#security-iam-awsmanpol-AWSProtonDeveloperAccess") –<br>New policy                                                                                     | AWS Proton added a new policy to provide developer role access to AWS Proton API<br>operations and to the AWS Proton console.                                                                                                                                                                                                                                                                                                                                                                                          | June 09, 2021      |
| [AWSProtonReadOnlyAccess](#security-iam-awsmanpol-AWSProtonReadOnlyAccess "#security-iam-awsmanpol-AWSProtonReadOnlyAccess") –<br>New policy                                                                                        | AWS Proton added a new policy to provide read-only access to AWS Proton API operations<br>and to the AWS Proton console.                                                                                                                                                                                                                                                                                                                                                                                               | June 09, 2021      |
| AWS Proton started tracking changes.                                                                                                                                                                                                | AWS Proton started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | June 09, 2021      |
