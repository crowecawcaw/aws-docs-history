# Review IAM permissions needed for the

AWS Glue Studio user

To use AWS Glue Studio, the user must have access to various AWS resources. The user must be
able to view and select Amazon S3 buckets, IAM policies and roles, and
AWS Glue Data Catalog objects.

## AWS Glue service permissions

AWS Glue Studio uses the actions and resources of the AWS Glue service. Your user needs
permissions on these actions and resources to effectively use AWS Glue Studio. You can grant
the AWS Glue Studio user the `AWSGlueConsoleFullAccess` managed policy, or create
a custom policy with a smaller set of permissions.

###### Important

Per security best practices, it is recommended to restrict access by
tightening policies to further restrict access to Amazon S3 bucket and
Amazon CloudWatch log groups. For an example Amazon S3 policy,
see [Writing IAM Policies: How to Grant Access to an Amazon S3
Bucket](https://aws.amazon.com/blogs/security/writing-iam-policies-how-to-grant-access-to-an-amazon-s3-bucket/ "https://aws.amazon.com/blogs/security/writing-iam-policies-how-to-grant-access-to-an-amazon-s3-bucket/").

## Creating Custom IAM Policies for AWS Glue Studio

You can create a custom policy with a smaller set of permissions for AWS Glue Studio. The
policy can grant permissions for a subset of objects or actions. Use the following
information when creating a custom policy.

To use the AWS Glue Studio APIs, include `glue:UseGlueStudio`
in the action policy
in your IAM permissions. Using `glue:UseGlueStudio` will allow you to access
all AWS Glue Studio actions even as more actions are added to the API over time.

For more information on actions defined by AWS Glue, see
[Actions defined by AWS Glue](../../../service-authorization/latest/reference/list_awsglue.md "../../../service-authorization/latest/reference/list_awsglue.md").

**Data preparation authoring Actions**

- SendRecipeAction
- GetRecipeAction

**Directed acyclic graph (DAG) Actions**

- CreateDag
- UpdateDag
- GetDag
- DeleteDag

**Job Actions**

- SaveJob
- GetJob
- CreateJob
- DeleteJob
- GetJobs
- UpdateJob

**Job run Actions**

- StartJobRun
- GetJobRuns
- BatchStopJobRun
- GetJobRun
- QueryJobRuns
- QueryJobs
- QueryJobRunsAggregated

**Schema Actions**

- GetSchema
- GetInferredSchema

**Database Actions**

- GetDatabases

**Plan Actions**

- GetPlan

**Table Actions**

- SearchTables
- GetTables
- GetTable

**Connection Actions**

- CreateConnection
- DeleteConnection
- UpdateConnection
- GetConnections
- GetConnection

**Mapping Actions**

- GetMapping

**S3 Proxy Actions**

- ListBuckets
- ListObjectsV2
- GetBucketLocation

**Security Configuration Actions**

- GetSecurityConfigurations

**Script Actions**

- CreateScript (different from API of same name in AWS Glue)

##

Accessing AWS Glue Studio APIs

To access AWS Glue Studio, add `glue:UseGlueStudio` in the actions policy list in the IAM permissions.

In the example below, `glue:UseGlueStudio` is included in the action policy,
but the AWS Glue Studio APIs are not individually identified. That is because when you include `glue:UseGlueStudio`,
you are automatically granted access to the internal APIs without having to specify the individual AWS Glue Studio
APIs in the IAM permissions.

In the example, the additional listed action policies (for example, `glue:SearchTables`) are not
AWS Glue Studio APIs, so they will need to be included in the IAM permissions as required. You may also want to
include Amazon S3 Proxy actions to specify the level of Amazon S3 access to grant. The example policy below provides access to open
AWS Glue Studio, create a visual job, and save/run it if the IAM role selected has sufficient access.

## Notebook and data preview

permissions

Data previews and notebooks allow you to see a sample of your data at any stage
of your job (reading, transforming, writing), without having to run the job. You
specify an AWS Identity and Access Management (IAM) role for AWS Glue Studio to use when accessing the
data. IAM roles are intended to be assumable and do not have standard long-term
credentials such as a password or access keys associated with it. Instead, when
AWS Glue Studio assumes the role, IAM provides it with temporary security credentials.

To ensure data previews and notebook commands work correctly, use a role that has
a name that starts with the string `AWSGlueServiceRole`. If you choose to
use a different name for your role, then you must add the `iam:passrole`
permission and configure a policy for the role in IAM. For more information, see [Create an IAM policy for roles not named
"AWSGlueServiceRole\*"](getting-started-iam-permissions.md#create-iam-policy "getting-started-iam-permissions.md#create-iam-policy").

###### Warning

If a role grants the `iam:passrole` permission for a notebook, and
you implement role chaining, a user could unintentionally gain access to the
notebook. There is currently no auditing implemented which would allow you to
monitor which users have been granted access to the notebook.

If you would like to deny an IAM identity the ability to create data preview sessions, consult the
following example [Deny an identity the ability to create data preview sessions](security_iam_id-based-policy-examples.md#deny-data-preview-sessions-per-identity "security_iam_id-based-policy-examples.md#deny-data-preview-sessions-per-identity").

## Amazon CloudWatch

permissions

You can monitor your AWS Glue Studio jobs using Amazon CloudWatch, which collects
and processes raw data from AWS Glue into readable, near-real-time metrics. By default,
AWS Glue metrics data is sent to CloudWatch automatically. For more information, see [What Is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_, and [AWS Glue Metrics](monitoring-awsglue-with-cloudwatch-metrics.md#awsglue-metrics "monitoring-awsglue-with-cloudwatch-metrics.md#awsglue-metrics") in the
_AWS Glue Developer Guide_.

To access CloudWatch dashboards, the user accessing AWS Glue Studio needs one of the
following:

- The `AdministratorAccess` policy
- The `CloudWatchFullAccess` policy
- A custom policy that includes one or more of these specific
  permissions:
  - `cloudwatch:GetDashboard` and
    `cloudwatch:ListDashboards` to view dashboards
  - `cloudwatch:PutDashboard` to create or modify
    dashboards
  - `cloudwatch:DeleteDashboards` to delete
    dashboards

For more information for changing permissions for an IAM user using policies,
see [Changing Permissions for an IAM User](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the
_IAM User Guide_.
