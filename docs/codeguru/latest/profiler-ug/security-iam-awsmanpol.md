# AWS managed policies for CodeGuru Profiler

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

##

AWS managed policy: AmazonCodeGuruProfilerFullAccess

You can attach the `AmazonCodeGuruProfilerFullAccess` policy to your IAM
identities.

Provides full access to CodeGuru Profiler, including permissions to create, update,
and delete profiling groups. Apply this only to administrative-level users who you want
to grant full control over CodeGuru Profiler profiling groups and related resources in your AWS account,
including the ability to delete profiling groups.

**Permissions details**

This policy includes the following permissions.

- `codeguru-profiler` – Allows principals full access to all CodeGuru Profiler actions.
- `codeguru` – Allows principals full access to all CodeGuru actions.
- `iam` – Allows principals to list roles and users from IAM

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
 "Resource": "*"
 }
 ]
 }`

```

##

AWS managed policy: AmazonCodeGuruProfilerReadOnlyAccess

You can attach the `AmazonCodeGuruProfilerReadOnlyAccess` policy to your IAM
identities.

Grants read-only access to CodeGuru Profiler and related resources in other AWS services.
Apply this policy to principals who you want to grant the ability to view profiling group visualizations,
but not make any changes to them.

**Permissions details**

This policy includes the following permissions.

- `codeguru-profiler` – Allows principals access to CodeGuru Profiler
  Describe, Get, List actions.
- `codeguru` – Allows principals access to CodeGuru Get actions.
- `iam` – Allows principals to list roles and users from IAM

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codeguru-profiler:Get*",
 "codeguru-profiler:Describe*",
 "codeguru-profiler:List*",
 "iam:ListRoles",
 "iam:ListUsers",
 "codeguru:*"
 ],
 "Resource": "*"
 }
 ]
 }`

```

##

AWS managed policy: AmazonCodeGuruProfilerAgentAccess

You can attach the `AmazonCodeGuruProfilerAgentAccess` policy to your IAM
identities.

This policy is added to the execution role of AWS Lambda functions onboarded to CodeGuru
Profiler via Lambda console's monitoring page.
It allows the Profiler agent to create a Profiling Group, refresh its configuration and submit agent profiles
to CodeGuru Profiler service.

**Permissions details**

This policy includes the following permissions.

- `codeguru-profiler` – Allows principals access to CodeGuru Profiler
  ConfigureAgent, CreateProfilingGroup and PostAgentProfile actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codeguru-profiler:ConfigureAgent",
 "codeguru-profiler:CreateProfilingGroup",
 "codeguru-profiler:PostAgentProfile"
 ],
 "Resource": "arn:aws:codeguru-profiler:*:*:profilingGroup/*"
 }
 ]
 }`

```

## CodeGuru Profiler updates to AWS managed

policies

View details about updates to AWS managed policies for CodeGuru Profiler since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the CodeGuru Profiler Document history page.

| Change                                                                                                                                                                         | Description                                                                                         | Date           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | -------------- |
| [AmazonCodeGuruProfilerAgentAccess](#security-iam-awsmanpol-amazoncodeguruprofileragentaccess "#security-iam-awsmanpol-amazoncodeguruprofileragentaccess") – Updates to policy | CodeGuru Profiler reduced resource scope in order to improve application security.                  | July 12, 2021  |
| [AmazonCodeGuruProfilerAgentAccess](#security-iam-awsmanpol-amazoncodeguruprofileragentaccess "#security-iam-awsmanpol-amazoncodeguruprofileragentaccess") – Updates to policy | CodeGuru Profiler added permissions needed for CodeGuru Profiler agent to Create a Profiling Group. | April 1, 2021  |
| CodeGuru Profiler started tracking changes                                                                                                                                     | CodeGuru Profiler started tracking changes for its AWS managed policies.                            | March 25, 2021 |
