# Using

identity-based policies for CodeGuru Profiler

By default, IAM users and roles don't have permission to create or modify
CodeGuru Profiler resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions. To learn how to attach policies to an IAM user or group, see [Adding and removing IAM
identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

To learn how to create an IAM identity-based policy using example JSON policy
documents, see [Creating policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Permissions required to use the CodeGuru Profiler
  console](#console-permissions "#console-permissions")
- [Permissions required by the CodeGuru Profiler profiling
  agent](#agent-policies "#agent-policies")
- [Permissions required to access CodeGuru Profiler data](#view-policies "#view-policies")
- [AWS managed (predefined) policies for
  CodeGuru Profiler](#managed-policies "#managed-policies")
- [Customer managed policy
  examples](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete CodeGuru Profiler resources in your
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

## Permissions required to use the CodeGuru Profiler

console

A user who uses the CodeGuru Profiler console must have a minimum set of permissions that allows
them to describe other AWS resources for the AWS account. You must have permissions
from the following services:

- CodeGuru Profiler
- [`ListUsers`](../../../IAM/latest/APIReference/API_ListUsers.md "../../../IAM/latest/APIReference/API_ListUsers.md") and [`ListRoles`](../../../IAM/latest/APIReference/API_ListRoles.md "../../../IAM/latest/APIReference/API_ListRoles.md")
  from the IAM service

If you create an IAM policy that is more restrictive than the minimum required
permissions, the console won't function as intended.

## Permissions required by the CodeGuru Profiler profiling

agent

The CodeGuru Profiler profiling agent is imported into your profiled application. When your
application runs, the agent starts in a different thread to profile your application.
The following permissions are required to submit data to CodeGuru Profiler:

- `codeguru-profiler:ConfigureAgent`
- `codeguru-profiler:PostAgentProfile`

For more information, see [Enabling the agent with code](enabling-the-agent-with-code.md "enabling-the-agent-with-code.md").

The following example policy grants the current AWS user permission to write to a
single profiling group in the current AWS Region.

```
`{
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "codeguru-profiler:ConfigureAgent",
 "codeguru-profiler:PostAgentProfile"
 ],
 "Resource": "arn:aws:codeguru-profiler:`region-id`:`aws-account-id`:profilingGroup/`profilingGroupName`"
 }]
}`
```

## Permissions required to access CodeGuru Profiler data

Data collected and submitted to CodeGuru Profiler by an agent is used to create application
profiles for visualizations:

- `codeguru-profiler:GetProfile`
- `codeguru-profiler:DescribeProfilingGroup`

For more information, see [Working with visualizations](working-with-visualizations.md "working-with-visualizations.md").

The following is an example.

```
`{
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "codeguru-profiler:GetProfile",
 "codeguru-profiler:DescribeProfilingGroup"
 ],
 "Resource": "arn:aws:codeguru-profiler:`region-id`:`aws-account-id`:profilingGroup/profilingGroupName"
 }]
}`
```

For the CodeGuru Profiler console, it can be useful to have an additional policy statement
providing `ListProfilingGroups` permissions to allow users to see the list of
`ProfilingGroups`. For example, the following allows users to see a list
of all profiling groups in their AWS account and Region.

```
`{
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "codeguru-profiler:ListProfilingGroups"
 ],
 "Resource": "*"
 }]
}`
```

For more information, see [`ConfigureAgent`](../profiler-api/API_ConfigureAgent.md "../profiler-api/API_ConfigureAgent.md"), [`PostAgentProfile`](../profiler-api/API_PostAgentProfile.md "../profiler-api/API_PostAgentProfile.md"), [`GetProfile`](../profiler-api/API_GetProfile.md "../profiler-api/API_GetProfile.md"), [`DescribeProfilingGroup`](../profiler-api/API_DescribeProfilingGroup.md "../profiler-api/API_DescribeProfilingGroup.md"), and [`ListProfilingGroups`](../profiler-api/API_ListProfilingGroups.md "../profiler-api/API_ListProfilingGroups.md") in the _Amazon CodeGuru Profiler API
Reference_.

## AWS managed (predefined) policies for

CodeGuru Profiler

AWS addresses many common use cases by providing standalone IAM policies that are
created and administered by AWS. These AWS managed policies grant necessary
permissions for common use cases so you can avoid having to investigate what permissions
are needed. For more information, see [AWS
Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

To create and manage CodeGuru Profiler service roles, you must also attach the AWS managed
policy named `IAMFullAccess`.

You can also create your own custom IAM policies to allow permissions for CodeGuru Profiler
actions and resources. You can attach these custom policies to the IAM users or groups
that require those permissions.

The following AWS managed policies, which you can attach to users in your account,
are specific to CodeGuru Profiler.

###### Topics

- [AmazonCodeGuruProfilerFullAccess](#managed-full-access "#managed-full-access")
- [AmazonCodeGuruProfilerReadOnlyAccess](#managed-read-only-access "#managed-read-only-access")
- [AmazonCodeGuruProfilerAgentAccess](#managed-agent-access "#managed-agent-access")

### AmazonCodeGuruProfilerFullAccess

`AmazonCodeGuruProfilerFullAccess` – Provides full access to CodeGuru Profiler,
including permissions to create, update, and delete profiling groups. Apply this only
to administrative-level users who you want to grant full control over CodeGuru Profiler profiling
groups and related resources in your AWS account, including the ability to delete
profiling groups.

The `AmazonCodeGuruProfilerFullAccess` policy contains the following
statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeguru-profiler:*",
 "iam:ListRoles",
 "iam:ListUsers",
 "codeguru:*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

### AmazonCodeGuruProfilerReadOnlyAccess

`AmazonCodeGuruProfilerReadOnlyAccess` – Grants read-only access to
CodeGuru Profiler and related resources in other AWS services. Apply this policy to users who
you want to grant the ability to view profiling group visualizations, but not make
any changes to them.

The `AmazonCodeGuruProfilerReadOnlyAccess` policy contains the following
statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeguru-profiler:Get*",
 "codeguru-profiler:Describe*",
 "codeguru-profiler:List*",
 "iam:ListRoles",
 "iam:ListUsers",
 "codeguru:Get*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

### AmazonCodeGuruProfilerAgentAccess

`AmazonCodeGuruProfilerAgentAccess` – Provides access to CodeGuru Profiler
agent to create a Profiling Group, refresh its configuration and submit profiles to the
CodeGuru Profiler service.

The `AmazonCodeGuruProfilerAgentAccess` policy contains the following
statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeguru-profiler:ConfigureAgent",
 "codeguru-profiler:CreateProfilingGroup",
 "codeguru-profiler:PostAgentProfile"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Customer managed policy

examples

You can create your own custom IAM policies to allow permissions for CodeGuru Profiler actions
and resources. You can attach these custom policies to the IAM users, roles, or groups
that require those permissions. You can also create your own custom IAM policies for
integration between CodeGuru Profiler and other AWS services.

The following example IAM policies grant permissions for various CodeGuru Profiler actions.
Use them to limit CodeGuru Profiler access for your IAM users and roles. These policies control
the ability to perform actions by using the CodeGuru Profiler console, API, AWS SDKs, or the
AWS CLI.

###### Note

All examples use the US East (Ohio) Region (us-east-2) and contain fictitious account
IDs.

**Examples**

- [Example 1: Allow a user to see
  all profiling groups and the visualizations of only one profiling group](#identity-based-policies-example-1 "#identity-based-policies-example-1")
- [Example 2: Allow a user to
  perform CodeGuru Profiler operations in a single Region](#identity-based-policies-example-2 "#identity-based-policies-example-2")
- [Example 3: Allow a user
  connecting from a specified IP address range access to a profiling group](#identity-based-policies-example-3 "#identity-based-policies-example-3")

### Example 1: Allow a user to see

all profiling groups and the visualizations of only one profiling group

The following example policy grants permissions for the AWS user with account
ID `123456789012` to see a list of all profiling groups in their
AWS account and Region. That user can see visualizations for only one profiling
group named `my-profiling-group`.

```
{
   "Statement": [
      {
         "Effect": "Allow",
         "Action": [
            "codeguru-profiler:GetProfile",
            "codeguru-profiler:DescribeProfilingGroup"
         ],
         "Resource": "arn:aws:codeguru-profiler:`us-east-2`:`123456789012`:profilingGroup/`my-profiling-group`"
      },
      {
         "Effect": "Allow",
         "Action": [
            "codeguru-profiler:ListProfilingGroups"
         ],
         "Resource": "*"
      }
   ]
}
```

### Example 2: Allow a user to

perform CodeGuru Profiler operations in a single Region

The following permissions policy uses a wildcard character
(`"codeguru-profiler:*"`) to allow users to perform all CodeGuru Profiler actions in the
us-east-2 Region and not from other AWS Regions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "codeguru-profiler:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "us-east-1"
 }
 }
 }
 ]
}`

```

### Example 3: Allow a user

connecting from a specified IP address range access to a profiling group

You can create a policy that allows users to view a CodeGuru Profiler profiling group only if
their IP address is within a certain IP address range. Because the
`GetFindingsReportAccountSummary` and `ListProfilingGroups`
actions don't support resource-level permissions, their resource is specified as
wildcard character (`*`) in a separate statement. For more information,
see the [Amazon CodeGuru Profiler permissions
reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codeguru-profiler:*",
 "iam:ListRoles",
 "iam:ListUsers",
 "codeguru:*"
 ],
 "Resource": "arn:aws:codeguru-profiler:us-east-1:123456789012:profilingGroup/DemoProfilingGroup",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": "203.0.113.0/24"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "codeguru-profiler:GetFindingsReportAccountSummary",
 "codeguru-profiler:ListProfilingGroups"
 ],
 "Resource": "*",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": "203.0.113.0/24"
 }
 }
 }
 ]
}`

```
