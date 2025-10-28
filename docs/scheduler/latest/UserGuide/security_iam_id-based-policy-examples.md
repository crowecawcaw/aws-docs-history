# Using identity-based policies in EventBridge Scheduler

By default, users and roles don't have permission to create or modify EventBridge Scheduler
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by EventBridge Scheduler, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon EventBridge Scheduler](../../../service-authorization/latest/reference/list_amazoneventbridgescheduler.md "../../../service-authorization/latest/reference/list_amazoneventbridgescheduler.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_id-based-policies-best-practices "#security_iam_id-based-policies-best-practices")
- [EventBridge Scheduler permissions](#security_iam_id-based-policies-permissions "#security_iam_id-based-policies-permissions")
- [AWS managed policies for EventBridge Scheduler](#security_iam_id-based-policies-managed-policies "#security_iam_id-based-policies-managed-policies")
- [Customer managed policies for EventBridge Scheduler](#security_iam_id-based-policies-customer-managed-policies "#security_iam_id-based-policies-customer-managed-policies")
- [AWS managed policy updates](#security_iam_id-based-policies-updates "#security_iam_id-based-policies-updates")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete EventBridge Scheduler resources in your
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
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
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

## EventBridge Scheduler permissions

In order for an IAM principal (user, group, or role) to create schedules in EventBridge Scheduler and access EventBridge Scheduler resources via the console or the API,
the principal must have a set of permissions added to their permission policy. You can configure these permissions depending on the principal's
job function. For example, a user, or role, that only uses the EventBridge Scheduler console to view a list of existing schedules does not need to have the permissions
required to call the `CreateSchedule` API operation. We recommend tailoring your identity-based permissions to provide only the least privileged access.

The following list shows EventBridge Scheduler's resources, and their corresponding supported actions.

- **Schedule**
  - `scheduler:ListSchedules`
  - `scheduler:GetSchedule`
  - `scheduler:CreateSchedule`
  - `scheduler:UpdateSchedule`
  - `scheduler:DeleteSchedule`

- **Schedule group**
  - `scheduler:ListScheduleGroups`
  - `scheduler:GetScheduleGroup`
  - `scheduler:CreateScheduleGroup`
  - `scheduler:DeleteScheduleGroup`
  - `scheduler:ListTagsForResource`
  - `scheduler:TagResource`
  - `scheduler:UntagResource`

You can use EventBridge Scheduler permissions to create your own customer managed policies to use with EventBridge Scheduler. You can also use the AWS managed policies described in the following section to grant the necessary permissions
for common use cases without having to manage your own policies.

## AWS managed policies for EventBridge Scheduler

AWS addresses many common use cases by providing standalone IAM policies that AWS creates, and administers. _Managed_, or predefined, policies grant the necessary permissions for common use cases,
so you don't need to investigate what permissions are needed. For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies")
in the _IAM User Guide_.

The following AWS managed policies that you can attach to users in your account are specific to EventBridge Scheduler:

- **AmazonEventBridgeSchedulerFullAccess**

Grants permissions to use all EventBridge Scheduler actions for schedules, and schedule groups.

To view the permissions for this policy, see [AmazonEventBridgeSchedulerFullAccess](../../../aws-managed-policy/latest/reference/AmazonEventBridgeSchedulerFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonEventBridgeSchedulerFullAccess.md") in the _AWS Managed Policy Reference_.

- **AmazonEventBridgeSchedulerReadOnlyAccess**

Grants read-only permissions to view details about your schedules and schedule groups.

To view the permissions for this policy, see [AmazonEventBridgeSchedulerReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonEventBridgeSchedulerReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonEventBridgeSchedulerReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

## Customer managed policies for EventBridge Scheduler

Use the following examples to create your own customer managed policies for EventBridge Scheduler. [Customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies")
give let you grant permissions only for the actions and resources required for applications and users in your team according to a principal's job function.

###### Topics

- [Example: CreateSchedule](#security_iam_id-based-policies-customer-managed-policies-create-schedule "#security_iam_id-based-policies-customer-managed-policies-create-schedule")
- [Example: GetSchedule](#security_iam_id-based-policies-customer-managed-policies-get-schedule "#security_iam_id-based-policies-customer-managed-policies-get-schedule")
- [Example: UpdateSchedule](#security_iam_id-based-policies-customer-managed-policies-update-schedule "#security_iam_id-based-policies-customer-managed-policies-update-schedule")
- [Example: DeleteScheduleGroup](#security_iam_id-based-policies-customer-managed-policies-delete-schedule-group "#security_iam_id-based-policies-customer-managed-policies-delete-schedule-group")

### Example: `CreateSchedule`

When you create a new schedule, you choose whether to encrypt your data on EventBridge Scheduler using an
[AWS owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk"),
or a [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk").

The following policy allows a principal to create a schedule and apply encryption using an AWS owned key. With an AWS owned key, AWS manages resources on
AWS Key Management Service (AWS KMS) for you so you don't need additional permissions to interact with AWS KMS.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Action":
 [
 "scheduler:CreateSchedule"
 ],
 "Effect": "Allow",
 "Resource":
 [
 "arn:aws:scheduler:us-west-2:123456789012:schedule/`my-group`/`my-schedule-name`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::123456789012:role/*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "scheduler.amazonaws.com"
 }
 }
 }
 ]
}`

```

Use the following policy to allow a principal create a schedule and use a AWS KMS customer managed key for encryption. To use a customer managed key, a principal must have permission to access the AWS KMS resources in your account.
This policy grants access to a single specified KMS key to be used to encrypt data on EventBridge Scheduler. Alternatively, you can use a wildcard (`*`) character to grant access to all keys in an account, or a subset that matches a given name pattern.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Action":
 [
 "scheduler:CreateSchedule"
 ],
 "Effect": "Allow",
 "Resource":
 [
 "arn:aws:scheduler:us-east-1:123456789012:schedule/`my-group`/`my-schedule-name`"
 ]
 },
 {
 "Action":
 [
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Effect": "Allow",
 "Resource":
 [
 "arn:aws:kms:us-west-2:123456789012:key/my-key-id"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": "scheduler.us-east-1.amazonaws.com",
 "kms:EncryptionContext:aws:scheduler:schedule:arn": "arn:aws:scheduler:us-west-2:123456789012:schedule/`my-group`/`my-schedule-name`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::123456789012:role/*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "scheduler.amazonaws.com"
 }
 }
 }
 ]
}`

```

### Example: `GetSchedule`

Use the following policy to allow a principal to get information about a schedule.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Action":
 [
 "scheduler:GetSchedule"
 ],
 "Effect": "Allow",
 "Resource":
 [
 "arn:aws:scheduler:us-west-2:123456789012:schedule/`my-group`/`my-schedule-name`"
 ]
 }
 ]
}`

```

### Example: `UpdateSchedule`

Use the following policies to allow a principal to update a schedule by calling the `scheduler:UpdateSchedule` action. Similar to `CreateSchedule`, the policy depends on whether the schedule uses a AWS KMS AWS owned key or a customer managed key for encryption.
For a schedule configured with an AWS owned key, use the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Action":
 [
 "scheduler:UpdateSchedule"
 ],
 "Effect": "Allow",
 "Resource":
 [
 "arn:aws:scheduler:us-west-2:123456789012:schedule/`my-group`/`my-schedule-name`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::123456789012:role/*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "scheduler.amazonaws.com"
 }
 }
 }
 ]
}`

```

For a schedule configured with a customer managed key, use the following policy. This policy includes additional permissions that allow a principal to access AWS KMS resources in your account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Action":
 [
 "scheduler:UpdateSchedule"
 ],
 "Effect": "Allow",
 "Resource":
 [
 "arn:aws:scheduler:us-east-1:123456789012:schedule/`my-group`/`my-schedule-name`"
 ]
 },
 {
 "Action":
 [
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Effect": "Allow",
 "Resource":
 [
 "arn:aws:kms:us-west-2:123456789012:key/`my-key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": "scheduler.us-east-1.amazonaws.com",
 "kms:EncryptionContext:aws:scheduler:schedule:arn": "arn:aws:scheduler:us-east-1:123456789012:schedule/`my-group`/`my-schedule-name`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::123456789012:role/*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "scheduler.amazonaws.com"
 }
 }
 }
 ]
}`

```

### Example: `DeleteScheduleGroup`

Use the following policy to allow a principal to delete a schedule group. When you delete a group, you also delete the schedules associated with that group. The principal that deletes the group must have permission to also delete the schedules associated with that group.
This policy grants a principal permission to call the `scheduler:DeleteScheduleGroup` action on the specified schedule groups, as well as all the schedules in the group:

###### Note

EventBridge Scheduler does not support specifying resource level permissions for individual schedules. For example, the following statement is invalid and should not be included in your policy:

`"Resource": "arn:aws:scheduler:us-west-2:123456789012:schedule/`my-group`/`my-schedule-name`"`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "scheduler:DeleteSchedule",
 "Resource": "arn:aws:scheduler:us-west-2:123456789012:schedule/`my-group`/*"
 },
 {
 "Effect": "Allow",
 "Action": "scheduler:DeleteScheduleGroup",
 "Resource": "arn:aws:scheduler:us-west-2:123456789012:schedule/`my-group`/*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::123456789012:role/*",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "scheduler.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AWS managed policy updates

| Change                                                                                                                                                               | Description                                                                                                                                                | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonEventBridgeSchedulerFullAccess](#security_iam_id-based-policies-managed-policies "#security_iam_id-based-policies-managed-policies") – New managed policy     | EventBridge Scheduler adds support for a new managed policy that grants users full access to all resources, including schedules, and schedule groups.      | November 10, 2022 |
| [AmazonEventBridgeSchedulerReadOnlyAccess](#security_iam_id-based-policies-managed-policies "#security_iam_id-based-policies-managed-policies") – New managed policy | EventBridge Scheduler adds support for a new managed policy that grants users read-only access to all resources, including schedules, and schedule groups. | November 10, 2022 |
| EventBridge Scheduler started tracking changes                                                                                                                       | EventBridge Scheduler started tracking changes for its AWS managed policies.                                                                               | November 10, 2022 |
