# AWS managed policies for AWS Clean Rooms

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy:

`AWSCleanRoomsReadOnlyAccess`

You can attach `AWSCleanRoomsReadOnlyAccess` to your IAM principals.

This policy grants read-only permissions to resources and
metadata in an `AWSCleanRoomsReadOnlyAccess` collaboration.

**Permissions details**

This policy includes the following permissions:

- `CleanRoomsRead` – Allows principals read-only access to the
  service.
- `ConsoleDisplayTables` – Allows principals read-only access
  to the AWS Glue metadata needed to show data about the underlying AWS Glue tables on
  the console.
- `ConsoleLogSummaryQueryLogs` – Allows principals to see the
  query logs.
- `ConsoleLogSummaryObtainLogs` – Allows principals to
  retrieve the log results.

For a JSON listing of the policy details, see [AWSCleanRoomsReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSCleanRoomsReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSCleanRoomsReadOnlyAccess.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy:

`AWSCleanRoomsFullAccess`

You can attach `AWSCleanRoomsFullAccess` to your IAM principals.

This policy grants administrative permissions that allow full access (read, write, and
update) to resources and metadata in an AWS Clean Rooms collaboration. This policy includes
access to perform queries.

**Permissions details**

This policy includes the following permissions:

- `CleanRoomsAccess` – Grants full access to all actions on
  all resources for AWS Clean Rooms.
- `PassServiceRole` – Grants access to pass a service role to
  only the service (`PassedToService` condition) that has
  "cleanrooms" in its name.
- `ListRolesToPickServiceRole` – Allows principals to list all
  their roles in order to choose a service role when using AWS Clean Rooms.
- `GetRoleAndListRolePoliciesToInspectServiceRole` – Allows
  principals to see the service role and corresponding policy in IAM.
- `ListPoliciesToInspectServiceRolePolicy` – Allows principals
  to see the service role and corresponding policy in IAM.
- `GetPolicyToInspectServiceRolePolicy` – Allows principals to
  see the service role and corresponding policy in IAM.
- `ConsoleDisplayTables` – Allows principals read-only access
  to the AWS Glue metadata needed to show data about the underlying AWS Glue tables on
  the console.
- `ConsolePickQueryResultsBucketListAll` – Allows principals
  to choose an Amazon S3 bucket from a list of all available S3 buckets into which
  their query results are written.
- `SetQueryResultsBucket` – Allows principals to choose an S3
  bucket into which their query results are written.
- `ConsoleDisplayQueryResults` – Allows principals to show the
  query results to the customer, read from the S3 bucket.
- `WriteQueryResults` – Allows principals to write the query
  results into a customer-owned S3 bucket.
- `EstablishLogDeliveries` – Allows principals to deliver
  query logs to a customer's Amazon CloudWatch Logs log group.
- `SetupLogGroupsDescribe` – Allows principals to use the
  Amazon CloudWatch Logs log group creation process.
- `SetupLogGroupsCreate` – Allows principals to create an
  Amazon CloudWatch Logs log group.
- `SetupLogGroupsResourcePolicy` – Allows principals to set up
  a resource policy on the Amazon CloudWatch Logs log group.
- `ConsoleLogSummaryQueryLogs` – Allows principals to see the
  query logs.
- `ConsoleLogSummaryObtainLogs` – Allows principals to
  retrieve the log results.

For a JSON listing of the policy details, see [AWSCleanRoomsFullAccess](../../../aws-managed-policy/latest/reference/AWSCleanRoomsFullAccess.md "../../../aws-managed-policy/latest/reference/AWSCleanRoomsFullAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy:

`AWSCleanRoomsFullAccessNoQuerying`

You can attach `AWSCleanRoomsFullAccessNoQuerying` to your IAM
principals.

This policy grants administrative permissions that allow full access (read, write, and
update) to resources and metadata in an AWS Clean Rooms collaboration. This policy excludes
access to perform queries.

**Permissions details**

This policy includes the following permissions:

- `CleanRoomsAccess` – Grants full access to all actions on
  all resources for AWS Clean Rooms, except for querying in collaborations.
- `CleanRoomsNoQuerying` – Explicitly denies
  `StartProtectedQuery` and `UpdateProtectedQuery` to
  prevent querying.
- `PassServiceRole` – Grants access to pass a service role to
  only the service (`PassedToService` condition) that has
  "cleanrooms" in its name.
- `ListRolesToPickServiceRole` – Allows principals to list all
  their roles in order to choose a service role when using AWS Clean Rooms.
- `GetRoleAndListRolePoliciesToInspectServiceRole` – Allows
  principals to see the service role and corresponding policy in IAM.
- `ListPoliciesToInspectServiceRolePolicy` – Allows principals
  to see the service role and corresponding policy in IAM.
- `GetPolicyToInspectServiceRolePolicy` – Allows principals to
  see the service role and corresponding policy in IAM.
- `ConsoleDisplayTables` – Allows principals read-only access
  to the AWS Glue metadata needed to show data about the underlying AWS Glue tables on
  the console.
- `EstablishLogDeliveries` – Allows principals to deliver
  query logs to a customer's Amazon CloudWatch Logs log group.
- `SetupLogGroupsDescribe` – Allows principals to use the
  Amazon CloudWatch Logs log group creation process.
- `SetupLogGroupsCreate` – Allows principals to create an
  Amazon CloudWatch Logs log group.
- `SetupLogGroupsResourcePolicy` – Allows principals to set up
  a resource policy on the Amazon CloudWatch Logs log group.
- `ConsoleLogSummaryQueryLogs` – Allows principals to see the
  query logs.
- `ConsoleLogSummaryObtainLogs` – Allows principals to
  retrieve the log results.
- `cleanrooms` – Manage collaborations, analysis templates,
  configured tables, memberships, and associated resources within the AWS Clean Rooms
  service. Perform various operations such as creating, updating, deleting,
  listing, and retrieving information about these resources.
- `iam` – Pass service roles with names containing
  "`cleanrooms`" to the AWS Clean Rooms service. List roles, policies, and
  inspect service roles and policies related to the AWS Clean Rooms service.
- `glue` – Retrieve information about databases, tables,
  partitions, and schemas from AWS Glue. This is required for the AWS Clean Rooms service to
  display and interact with the underlying data sources.
- `logs` – Manage log deliveries, log groups, and resource
  policies for CloudWatch Logs. Query and retrieve logs related to the AWS Clean Rooms service. These
  permissions are necessary for monitoring, auditing, and troubleshooting purposes
  within the service.

The policy also explicitly denies the actions
`cleanrooms:StartProtectedQuery` and
`cleanrooms:UpdateProtectedQuery` to prevent users from directly
executing or updating protected queries, which should be done through the AWS Clean Rooms
controlled mechanisms.

For a JSON listing of the policy details, see [AWSCleanRoomsFullAccessNoQuerying](../../../aws-managed-policy/latest/reference/AWSCleanRoomsFullAccessNoQuerying.md "../../../aws-managed-policy/latest/reference/AWSCleanRoomsFullAccessNoQuerying.md") in the _AWS
Managed Policy Reference Guide_.

## AWS managed policy:

`AWSCleanRoomsMLReadOnlyAccess`

You can attach `AWSCleanRoomsMLReadOnlyAccess` to your IAM principals.

This policy grants read-only permissions to resources and metadata in an
`AWSCleanRoomsMLReadOnlyAccess` collaboration.

This policy includes the following permissions:

- `CleanRoomsConsoleNavigation` – Grants access to view the
  screens of the AWS Clean Rooms console.
- `CleanRoomsMLRead` – Allows principals read-only access to
  the Clean Rooms ML service.
- `PassCleanRoomsResources` – Grants access to pass specified
  AWS Clean Rooms resources.

For a JSON listing of the policy details, see [AWSCleanRoomsMLReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSCleanRoomsMLReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSCleanRoomsMLReadOnlyAccess.md") in the _AWS Managed
Policy Reference Guide_.

## AWS managed policy:

`AWSCleanRoomsMLFullAccess`

You can attach `AWSCleanRoomsMLFullAcces` to your IAM principals. This
policy grants administrative permissions that allow full access (read, write, and
update) to resources and metadata needed by Clean Rooms ML.

**Permissions details**

This policy includes the following permissions:

- `CleanRoomsMLFullAccess` – Grants access to all Clean Rooms ML
  actions.
- `PassServiceRole` – Grants access to pass a service role to
  only the service (`PassedToService` condition) that has
  "cleanrooms-ml" in its name.
- `CleanRoomsConsoleNavigation` – Grants access to view the
  screens of the AWS Clean Rooms console.
- `CollaborationMembershipCheck` – When you start an audience
  generation (lookalike segment) job within a collaboration, the Clean Rooms ML service
  calls `ListMembers` to check that the collaboration is valid, the
  caller is an active member, and the configured audience model owner is an active
  member. This permission is always required; the console navigation SID is only
  required for console users.
- `PassCleanRoomsResources` – Grants access to pass specified
  AWS Clean Rooms resources.
- `AssociateModels` – Allows principals to associate a Clean Rooms ML
  model with your collaboration.
- `TagAssociations` – Allows principals to add tags to the
  association between a lookalike model and a collaboration.
- `ListRolesToPickServiceRole` – Allows principals to list all
  their roles in order to choose a service role when using AWS Clean Rooms.
- `GetRoleAndListRolePoliciesToInspectServiceRole` – Allows
  principals to see the service role and corresponding policy in IAM.
- `ListPoliciesToInspectServiceRolePolicy` – Allows principals
  to see the service role and corresponding policy in IAM.
- `GetPolicyToInspectServiceRolePolicy` – Allows principals to
  see the service role and corresponding policy in IAM.
- `ConsoleDisplayTables` – Allows principals read-only access
  to the AWS Glue metadata needed to show data about the underlying AWS Glue tables on
  the console.
- `ConsolePickOutputBucket` – Allows principals to select Amazon S3
  buckets for configured audience model outputs.
- `ConsolePickS3Location` – Allows principals to select the
  location within a bucket for configured audience model outputs.
- `ConsoleDescribeECRRepositories` – Allows principals to
  describe Amazon ECR repositories and images.

For a JSON listing of the policy details, see [AWSCleanRoomsMLFullAccess](../../../aws-managed-policy/latest/reference/AWSCleanRoomsMLFullAccess.md "../../../aws-managed-policy/latest/reference/AWSCleanRoomsMLFullAccess.md") in the _AWS Managed
Policy Reference Guide_.

## AWS Clean Rooms updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Clean Rooms since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the AWS Clean Rooms Document history page.

| Change                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                    | Date              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [AWSCleanRoomsFullAccessNoQuerying](#security-iam-awsmanpol-fullaccess-noquery "#security-iam-awsmanpol-fullaccess-noquery")–<br>Update to existing policy       | Added cleanrooms:UpdateConfiguredTableAllowedColumns and<br>cleanrooms:UpdateConfiguredTableReference to<br>CleanRoomsAccess.                                                                                                                                                                                                                                                                                                  | July<br>29, 2025  |
| [AWSCleanRoomsMLReadOnlyAccess](#ml-read-only "#ml-read-only")<br>– Update to existing policy                                                                    | Added PassCleanRoomsResources to<br>AWSCleanRoomsMLReadOnlyAccess. Added<br>PassCleanRoomsResources and<br>ConsoleDescribeECRRepositories to<br>AWSCleanRoomsMLFullAccess.                                                                                                                                                                                                                                                     | January 10, 2025  |
| [AWSCleanRoomsFullAccessNoQuerying](#security-iam-awsmanpol-fullaccess-noquery "#security-iam-awsmanpol-fullaccess-noquery")<br>– Update to existing policy      | Added cleanrooms:BatchGetSchemaAnalysisRule to<br>CleanRoomsAccess.                                                                                                                                                                                                                                                                                                                                                            | May 13, 2024      |
| [AWSCleanRoomsFullAccess](#security-iam-awsmanpol-fullaccess "#security-iam-awsmanpol-fullaccess") – Update<br>to existing policy                                | Updated the Statement ID in AWSCleanRoomsFullAccess<br>from ConsolePickQueryResultsBucket to<br>SetQueryResultsBucket in this policy to better<br>represent the permissions since the permissions are needed for setting<br>the query results bucket both with and without the console.                                                                                                                                        | March 21, 2024    |
| [AWSCleanRoomsMLReadOnlyAccess](#ml-read-only "#ml-read-only")<br>– New policy<br>[AWSCleanRoomsMLFullAccess](#ml-full-access "#ml-full-access") –<br>New policy | Added AWSCleanRoomsMLReadOnlyAccess and<br>AWSCleanRoomsMLFullAccess to support<br>AWS Clean Rooms ML.                                                                                                                                                                                                                                                                                                                         | November 29, 2023 |
| [AWSCleanRoomsFullAccessNoQuerying](#security-iam-awsmanpol-fullaccess-noquery "#security-iam-awsmanpol-fullaccess-noquery")<br>– Update to existing policy      | Added cleanrooms:CreateAnalysisTemplate,<br>cleanrooms:GetAnalysisTemplate,<br>cleanrooms:UpdateAnalysisTemplate,<br>cleanrooms:DeleteAnalysisTemplate,<br>cleanrooms:ListAnalysisTemplates,<br>cleanrooms:GetCollaborationAnalysisTemplate,<br>cleanrooms:BatchGetCollaborationAnalysisTemplate, and<br>cleanrooms:ListCollaborationAnalysisTemplates to<br>CleanRoomsAccess to enable the new analysis templates<br>feature. | July 31, 2023     |
| [AWSCleanRoomsFullAccessNoQuerying](#security-iam-awsmanpol-fullaccess-noquery "#security-iam-awsmanpol-fullaccess-noquery")<br>– Update to existing policy      | Added cleanrooms:ListTagsForResource,<br>cleanrooms:UntagResource, and<br>cleanrooms:TagResource to<br>CleanRoomsAccess to enable resource tagging.                                                                                                                                                                                                                                                                            | March 21, 2023    |
| AWS Clean Rooms started tracking changes                                                                                                                         | AWS Clean Rooms started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                      | January 12, 2023  |
