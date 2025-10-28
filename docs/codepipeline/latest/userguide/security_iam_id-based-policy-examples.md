# AWS CodePipeline

identity-based policy examples

By default, IAM users and roles don't have permission to create or modify
CodePipeline resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

To learn how to create a pipeline that uses resources from another account, and for
the related example policies, see [Create a pipeline in CodePipeline that uses resources
from another AWS account](pipelines-create-cross-account.md "pipelines-create-cross-account.md").

###### Topics

- [Policy best
  practices](security_iam_service-with-iam-policy-best-practices.md "security_iam_service-with-iam-policy-best-practices.md")
- [Viewing resources in the
  console](security-iam-resources-console.md "security-iam-resources-console.md")
- [Allow
  users to view their own permissions](security_iam_id-based-policy-examples-view-own-permissions.md "security_iam_id-based-policy-examples-view-own-permissions.md")
- [Identity-based policies (IAM)
  examples](security-iam-id-policies-examples.md "security-iam-id-policies-examples.md")
- [Using tags to control access to CodePipeline
  resources](tag-based-access-control.md "tag-based-access-control.md")
- [Permissions required to use the
  CodePipeline console](security-iam-permissions-console.md "security-iam-permissions-console.md")
- [Permissions required to view
  compute logs in the CodePipeline console](security-iam-permissions-console-logs.md "security-iam-permissions-console-logs.md")
- [AWS managed policies for AWS CodePipeline](managed-policies.md "managed-policies.md")
- [Customer managed policy examples](#customer-managed-policies "#customer-managed-policies")

## Customer managed policy examples

In this section, you can find example user policies that grant permissions for
various CodePipeline actions. These policies work when you are using the
CodePipeline API, AWS SDKs, or the AWS CLI. When you are using the console, you
must grant additional permissions specific to the console. For more information, see
[Permissions required to use the
CodePipeline console](security-iam-permissions-console.md "security-iam-permissions-console.md").

###### Note

All examples use the US West (Oregon) Region (`us-west-2`) and contain
fictitious account IDs.

**Examples**

- [Example 1: Grant permissions
  to get the state of a pipeline](#identity-based-policies-example-1 "#identity-based-policies-example-1")
- [Example 2: Grant permissions
  to enable and disable transitions between stages](#identity-based-policies-example-2 "#identity-based-policies-example-2")
- [Example 3: Grant permissions
  to get a list of all available action types](#identity-based-policies-example-3 "#identity-based-policies-example-3")
- [Example 4: Grant permissions
  to approve or reject manual approval actions](#identity-based-policies-example-4 "#identity-based-policies-example-4")
- [Example 5: Grant permissions
  to poll for jobs for a custom action](#identity-based-policies-example-5 "#identity-based-policies-example-5")
- [Example 6: Attach or edit a
  policy for Jenkins integration with AWS CodePipeline](#identity-based-policies-example-6 "#identity-based-policies-example-6")
- [Example 7: Configure
  cross-account access to a pipeline](#identity-based-policies-example-7 "#identity-based-policies-example-7")

### Example 1: Grant permissions

to get the state of a pipeline

The following example grants permissions to get the state of the pipeline
named `MyFirstPipeline`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codepipeline:GetPipelineState"
 ],
 "Resource": "arn:aws:codepipeline:us-west-2:111222333444:MyFirstPipeline"
 }
 ]
}`

```

### Example 2: Grant permissions

to enable and disable transitions between stages

The following example grants permissions to disable and enable transitions
between all stages in the pipeline named
`MyFirstPipeline`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codepipeline:DisableStageTransition",
 "codepipeline:EnableStageTransition"
 ],
 "Resource": "arn:aws:codepipeline:us-west-2:111222333444:MyFirstPipeline/*"
 }
 ]
}`

```

To allow the user to disable and enable transitions for a single stage in a
pipeline, you must specify the stage. For example, to allow the user to enable
and disable transitions for a stage named `Staging` in a pipeline
named `MyFirstPipeline`:

```
"Resource": "arn:aws:codepipeline:us-west-2:111222333444:MyFirstPipeline/Staging"
```

### Example 3: Grant permissions

to get a list of all available action types

The following example grants permissions to get a list of all available action
types available for pipelines in the `us-west-2` Region:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codepipeline:ListActionTypes"
 ],
 "Resource": "arn:aws:codepipeline:us-west-2:111222333444:actiontype:*"
 }
 ]
}`

```

### Example 4: Grant permissions

to approve or reject manual approval actions

The following example grants permissions to approve or reject manual approval
actions in a stage named `Staging` in a pipeline named
`MyFirstPipeline`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codepipeline:PutApprovalResult"
 ],
 "Resource": "arn:aws:codepipeline:us-west-2:111222333444:MyFirstPipeline/Staging/*"
 }
 ]
}`

```

### Example 5: Grant permissions

to poll for jobs for a custom action

The following example grants permissions to poll for jobs for the custom
action named `TestProvider`, which is a `Test` action type
in its first version, across all pipelines:

###### Note

The job worker for a custom action might be configured under a different
AWS account or require a specific IAM role in order to function.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codepipeline:PollForJobs"
 ],
 "Resource": [
 "arn:aws:codepipeline:us-west-2:111222333444:actionType:`Custom`/`Test`/`TestProvider`/`1`"
 ]
 }
 ]
}`

```

### Example 6: Attach or edit a

policy for Jenkins integration with AWS CodePipeline

If you configure a pipeline to use Jenkins for build or test, create a
separate identity for that integration and attach an IAM policy that has the
minimum permissions required for integration between Jenkins and CodePipeline.
This policy is the same as the `AWSCodePipelineCustomActionAccess` managed policy. The following
example shows a policy for Jenkins integration:

JSON

```
`{
 "Version":"2012-10-17",

 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codepipeline:AcknowledgeJob",
 "codepipeline:GetJobDetails",
 "codepipeline:PollForJobs",
 "codepipeline:PutJobFailureResult",
 "codepipeline:PutJobSuccessResult"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Example 7: Configure

cross-account access to a pipeline

You can configure access to pipelines for users and groups in another AWS
account. The recommended way is to create a role in the account where the
pipeline was created. The role should allow users from the other AWS account
to assume that role and access the pipeline. For more information, see [Walkthrough:
Cross-Account Access Using Roles](../../../IAM/latest/UserGuide/walkthru_cross-account-with-roles.md "../../../IAM/latest/UserGuide/walkthru_cross-account-with-roles.md").

The following example shows a policy in the 80398EXAMPLE account that
allows users to view, but not change, the pipeline named
`MyFirstPipeline` in the CodePipeline console. This
policy is based on the `AWSCodePipeline_ReadOnlyAccess` managed policy, but because it is
specific to the `MyFirstPipeline` pipeline, it cannot use the
managed policy directly. If you do not want to restrict the policy to a specific
pipeline, consider using one of the managed policies created and maintained by
CodePipeline. For more information, see [Working with Managed
Policies](../../../IAM/latest/UserGuide/access_policies_managed-using.md "../../../IAM/latest/UserGuide/access_policies_managed-using.md"). You must attach this policy to an IAM role you create
for access, for example, a role named
`CrossAccountPipelineViewers`:

JSON

```
`{
 "Version":"2012-10-17",

 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codepipeline:GetPipeline",
 "codepipeline:GetPipelineState",
 "codepipeline:ListActionTypes",
 "codepipeline:ListPipelines",
 "iam:ListRoles",
 "s3:GetBucketPolicy",
 "s3:GetObject",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "codedeploy:GetApplication",
 "codedeploy:GetDeploymentGroup",
 "codedeploy:ListApplications",
 "codedeploy:ListDeploymentGroups",
 "elasticbeanstalk:DescribeApplications",
 "elasticbeanstalk:DescribeEnvironments",
 "lambda:GetFunctionConfiguration",
 "lambda:ListFunctions"
 ],
 "Resource": "arn:aws:codepipeline:us-east-2:`111122223333`:MyFirstPipeline"
 }
 ]
}`

```

After you create this policy, create the IAM role in the
80398EXAMPLE account and attach the policy to that role. In the role's
trust relationships, you must add the AWS account that assumes this
role.

The following example shows a policy created in the
`111111111111` AWS account that allows users to
assume the role named `CrossAccountPipelineViewers` in the
80398EXAMPLE account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`CrossAccountPipelineViewers`"
 }
 ]
}`

```
