# Amazon SageMaker AI

identity-based policy examples

By default, IAM users and roles don't have permission to create or modify
SageMaker AI resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions. To learn how to attach policies to an IAM user or group, see [Adding and Removing
IAM Identity Permissions](../../../service-authorization/latest/reference/access_policies_manage-attach-detach.md "../../../service-authorization/latest/reference/access_policies_manage-attach-detach.md") in the _Service Authorization Reference_.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../service-authorization/latest/reference/access_policies_create.md#access_policies_create-json-editor "../../../service-authorization/latest/reference/access_policies_create.md#access_policies_create-json-editor").

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the
  SageMaker AI console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow
  users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Control creation of SageMaker AI resources
  with condition keys](#sagemaker-condition-examples "#sagemaker-condition-examples")
- [Control access to the SageMaker AI API by using
  identity-based policies](#api-access-policy "#api-access-policy")
- [Limit access to SageMaker AI API and runtime calls by IP
  address](#api-ip-filter "#api-ip-filter")
- [Limit access to a notebook instance by IP
  address](#nbi-ip-filter "#nbi-ip-filter")
- [Control access to SageMaker AI resources by using
  tags](#access-tag-policy "#access-tag-policy")
- [Provide permissions for tagging SageMaker AI
  resources](#grant-tagging-permissions "#grant-tagging-permissions")
- [Limit access to searchable
  resources with visibility conditions](#limit-access-to-searchable-resources "#limit-access-to-searchable-resources")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete SageMaker AI resources in your
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

## Using the

SageMaker AI console

To access the Amazon SageMaker AI console, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
SageMaker AI resources in your AWS account. If you create an identity-based
policy more restrictive than the minimum required permissions, the console won't
function properly for entities with that policy. This include users or roles with
that policy.

To ensure that those entities can still use the SageMaker AI console, you must
also attach the following AWS managed policy to the entities. For more
information, see [Adding Permissions to a User](../../../service-authorization/latest/reference/id_users_change-permissions.md#users_change_permissions-add-console "../../../service-authorization/latest/reference/id_users_change-permissions.md#users_change_permissions-add-console") in the
_Service Authorization Reference_:

You don't need to allow minimum console permissions for users that are making
calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions
that match the API operation that you're trying to perform.

###### Topics

- [Permissions required to use the Amazon SageMaker AI
  console](#console-permissions "#console-permissions")
- [Permissions required to use the
  Amazon SageMaker Ground Truth console](#groundtruth-console-policy "#groundtruth-console-policy")
- [Permissions required to use
  the Amazon Augmented AI (Preview) console](#amazon-augmented-ai-console-policy "#amazon-augmented-ai-console-policy")

### Permissions required to use the Amazon SageMaker AI

console

The permissions reference table lists the Amazon SageMaker AI API operations and shows
the required permissions for each operation. For more information about Amazon SageMaker AI
API operations, see [Amazon SageMaker AI API Permissions: Actions,
Permissions, and Resources Reference](api-permissions-reference.md "api-permissions-reference.md").

To use the Amazon SageMaker AI console, you need to grant permissions for additional
actions. Specifically, the console needs permissions that allow the
`ec2` actions to display subnets, VPCs, and security groups.
Optionally, the console needs permission to create _execution
roles_ for tasks such as `CreateNotebook`,
`CreateTrainingJob`, and `CreateModel`. Grant these
permissions with the following permissions policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SageMakerApis",
 "Effect": "Allow",
 "Action": [
 "sagemaker:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VpcConfigurationForCreateForms",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": "*"
 },
 {
 "Sid":"KmsKeysForCreateForms",
 "Effect":"Allow",
 "Action":[
 "kms:DescribeKey",
 "kms:ListAliases"
 ],
 "Resource":"*"
 },
 {
 "Sid": "AccessAwsMarketplaceSubscriptions",
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:ViewSubscriptions"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:BatchGetRepositories",
 "codecommit:CreateRepository",
 "codecommit:GetRepository",
 "codecommit:ListRepositories",
 "codecommit:ListBranches",
 "secretsmanager:CreateSecret",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecrets"
 ],
 "Resource": "*"
 },
 {
 "Sid":"ListAndCreateExecutionRoles",
 "Effect":"Allow",
 "Action":[
 "iam:ListRoles",
 "iam:CreateRole",
 "iam:CreatePolicy",
 "iam:AttachRolePolicy"
 ],
 "Resource":"*"
 },
 {
 "Sid": "DescribeECRMetaData",
 "Effect": "Allow",
 "Action": [
 "ecr:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "PassRoleForExecutionRoles",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 }
 ]
}`

```

### Permissions required to use the

Amazon SageMaker Ground Truth console

To use the Amazon SageMaker Ground Truth console, you need to grant permissions for additional
resources. Specifically, the console needs permissions for:

- the AWS Marketplace to view subscriptions,
- Amazon Cognito operations to manage your private workforce
- Amazon S3 actions for access to your input and output files
- AWS Lambda actions to list and invoke functions

Grant these permissions with the following permissions policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GroundTruthConsole",
 "Effect": "Allow",
 "Action": [
 "aws-marketplace:ViewSubscriptions",

 "cognito-idp:AdminAddUserToGroup",
 "cognito-idp:AdminCreateUser",
 "cognito-idp:AdminDeleteUser",
 "cognito-idp:AdminDisableUser",
 "cognito-idp:AdminEnableUser",
 "cognito-idp:AdminRemoveUserFromGroup",
 "cognito-idp:CreateGroup",
 "cognito-idp:CreateUserPool",
 "cognito-idp:CreateUserPoolClient",
 "cognito-idp:CreateUserPoolDomain",
 "cognito-idp:DescribeUserPool",
 "cognito-idp:DescribeUserPoolClient",
 "cognito-idp:ListGroups",
 "cognito-idp:ListIdentityProviders",
 "cognito-idp:ListUsers",
 "cognito-idp:ListUsersInGroup",
 "cognito-idp:ListUserPoolClients",
 "cognito-idp:ListUserPools",
 "cognito-idp:UpdateUserPool",
 "cognito-idp:UpdateUserPoolClient",

 "groundtruthlabeling:DescribeConsoleJob",
 "groundtruthlabeling:ListDatasetObjects",
 "groundtruthlabeling:RunGenerateManifestByCrawlingJob",

 "lambda:InvokeFunction",
 "lambda:ListFunctions",

 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Permissions required to use

the Amazon Augmented AI (Preview) console

To use the Augmented AI console, you need to grant permissions for additional
resources. Grant these permissions with the following permissions policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:*Algorithm",
 "sagemaker:*Algorithms",
 "sagemaker:*App",
 "sagemaker:*Apps",
 "sagemaker:*AutoMLJob",
 "sagemaker:*AutoMLJobs",
 "sagemaker:*CodeRepositories",
 "sagemaker:*CodeRepository",
 "sagemaker:*CompilationJob",
 "sagemaker:*CompilationJobs",
 "sagemaker:*Endpoint",
 "sagemaker:*EndpointConfig",
 "sagemaker:*EndpointConfigs",
 "sagemaker:*EndpointWeightsAndCapacities",
 "sagemaker:*Endpoints",
 "sagemaker:*Experiment",
 "sagemaker:*Experiments",
 "sagemaker:*FlowDefinitions",
 "sagemaker:*HumanLoop",
 "sagemaker:*HumanLoops",
 "sagemaker:*HumanTaskUi",
 "sagemaker:*HumanTaskUis",
 "sagemaker:*HyperParameterTuningJob",
 "sagemaker:*HyperParameterTuningJobs",
 "sagemaker:*LabelingJob",
 "sagemaker:*LabelingJobs",
 "sagemaker:*Metrics",
 "sagemaker:*Model",
 "sagemaker:*ModelPackage",
 "sagemaker:*ModelPackages",
 "sagemaker:*Models",
 "sagemaker:*MonitoringExecutions",
 "sagemaker:*MonitoringSchedule",
 "sagemaker:*MonitoringSchedules",
 "sagemaker:*NotebookInstance",
 "sagemaker:*NotebookInstanceLifecycleConfig",
 "sagemaker:*NotebookInstanceLifecycleConfigs",
 "sagemaker:*NotebookInstanceUrl",
 "sagemaker:*NotebookInstances",
 "sagemaker:*ProcessingJob",
 "sagemaker:*ProcessingJobs",
 "sagemaker:*RenderUiTemplate",
 "sagemaker:*Search",
 "sagemaker:*SearchSuggestions",
 "sagemaker:*Tags",
 "sagemaker:*TrainingJob",
 "sagemaker:*TrainingJobs",
 "sagemaker:*TransformJob",
 "sagemaker:*TransformJobs",
 "sagemaker:*Trial",
 "sagemaker:*TrialComponent",
 "sagemaker:*TrialComponents",
 "sagemaker:*Trials",
 "sagemaker:*Workteam",
 "sagemaker:*Workteams"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:*FlowDefinition"
 ],
 "Resource": "*",
 "Condition": {
 "StringEqualsIfExists": {
 "sagemaker:WorkteamType": [
 "private-crowd",
 "vendor-crowd"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "application-autoscaling:DeleteScalingPolicy",
 "application-autoscaling:DeleteScheduledAction",
 "application-autoscaling:DeregisterScalableTarget",
 "application-autoscaling:DescribeScalableTargets",
 "application-autoscaling:DescribeScalingActivities",
 "application-autoscaling:DescribeScalingPolicies",
 "application-autoscaling:DescribeScheduledActions",
 "application-autoscaling:PutScalingPolicy",
 "application-autoscaling:PutScheduledAction",
 "application-autoscaling:RegisterScalableTarget",
 "aws-marketplace:ViewSubscriptions",
 "cloudwatch:DeleteAlarms",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:GetMetricData",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics",
 "cloudwatch:PutMetricAlarm",
 "cloudwatch:PutMetricData",
 "codecommit:BatchGetRepositories",
 "codecommit:CreateRepository",
 "codecommit:GetRepository",
 "codecommit:ListBranches",
 "codecommit:ListRepositories",
 "cognito-idp:AdminAddUserToGroup",
 "cognito-idp:AdminCreateUser",
 "cognito-idp:AdminDeleteUser",
 "cognito-idp:AdminDisableUser",
 "cognito-idp:AdminEnableUser",
 "cognito-idp:AdminRemoveUserFromGroup",
 "cognito-idp:CreateGroup",
 "cognito-idp:CreateUserPool",
 "cognito-idp:CreateUserPoolClient",
 "cognito-idp:CreateUserPoolDomain",
 "cognito-idp:DescribeUserPool",
 "cognito-idp:DescribeUserPoolClient",
 "cognito-idp:ListGroups",
 "cognito-idp:ListIdentityProviders",
 "cognito-idp:ListUserPoolClients",
 "cognito-idp:ListUserPools",
 "cognito-idp:ListUsers",
 "cognito-idp:ListUsersInGroup",
 "cognito-idp:UpdateUserPool",
 "cognito-idp:UpdateUserPoolClient",
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:CreateVpcEndpoint",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcs",
 "ecr:BatchCheckLayerAvailability",
 "ecr:BatchGetImage",
 "ecr:CreateRepository",
 "ecr:Describe*",
 "ecr:GetAuthorizationToken",
 "ecr:GetDownloadUrlForLayer",
 "elasticfilesystem:DescribeFileSystems",
 "elasticfilesystem:DescribeMountTargets",
 "fsx:DescribeFileSystems",
 "glue:CreateJob",
 "glue:DeleteJob",
 "glue:GetJob",
 "glue:GetJobRun",
 "glue:GetJobRuns",
 "glue:GetJobs",
 "glue:ResetJobBookmark",
 "glue:StartJobRun",
 "glue:UpdateJob",
 "groundtruthlabeling:*",
 "iam:ListRoles",
 "kms:DescribeKey",
 "kms:ListAliases",
 "lambda:ListFunctions",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:GetLogEvents",
 "logs:PutLogEvents",
 "sns:ListTopics"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:DescribeResourcePolicies",
 "logs:GetLogDelivery",
 "logs:ListLogDeliveries",
 "logs:PutResourcePolicy",
 "logs:UpdateLogDelivery"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:SetRepositoryPolicy",
 "ecr:CompleteLayerUpload",
 "ecr:BatchDeleteImage",
 "ecr:UploadLayerPart",
 "ecr:DeleteRepositoryPolicy",
 "ecr:InitiateLayerUpload",
 "ecr:DeleteRepository",
 "ecr:PutImage"
 ],
 "Resource": "arn:aws:ecr:*:*:repository/*sagemaker*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:GitPull",
 "codecommit:GitPush"
 ],
 "Resource": [
 "arn:aws:codecommit:*:*:*sagemaker*",
 "arn:aws:codecommit:*:*:*SageMaker*",
 "arn:aws:codecommit:*:*:*Sagemaker*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:ListSecrets"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:DescribeSecret",
 "secretsmanager:GetSecretValue",
 "secretsmanager:CreateSecret"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:AmazonSageMaker-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:DescribeSecret",
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "secretsmanager:ResourceTag/SageMaker": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "robomaker:CreateSimulationApplication",
 "robomaker:DescribeSimulationApplication",
 "robomaker:DeleteSimulationApplication"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "robomaker:CreateSimulationJob",
 "robomaker:DescribeSimulationJob",
 "robomaker:CancelSimulationJob"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:AbortMultipartUpload",
 "s3:GetBucketCors",
 "s3:PutBucketCors"
 ],
 "Resource": [
 "arn:aws:s3:::*SageMaker*",
 "arn:aws:s3:::*Sagemaker*",
 "arn:aws:s3:::*sagemaker*",
 "arn:aws:s3:::*aws-glue*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": "*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "s3:ExistingObjectTag/SageMaker": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": [
 "arn:aws:lambda:*:*:function:*SageMaker*",
 "arn:aws:lambda:*:*:function:*sagemaker*",
 "arn:aws:lambda:*:*:function:*Sagemaker*",
 "arn:aws:lambda:*:*:function:*LabelingFunction*"
 ]
 },
 {
 "Action": "iam:CreateServiceLinkedRole",
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/aws-service-role/sagemaker.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_SageMakerEndpoint",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "sagemaker.application-autoscaling.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "robomaker.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "sns:Subscribe",
 "sns:CreateTopic"
 ],
 "Resource": [
 "arn:aws:sns:*:*:*SageMaker*",
 "arn:aws:sns:*:*:*Sagemaker*",
 "arn:aws:sns:*:*:*sagemaker*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "sagemaker.amazonaws.com",
 "glue.amazonaws.com",
 "robomaker.amazonaws.com",
 "states.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## Allow

users to view their own permissions

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

## Control creation of SageMaker AI resources

with condition keys

Control fine-grained access to allow the creation of SageMaker AI resources by using
SageMaker AI-specific condition keys. For information about using condition keys in IAM
policies, see [IAM JSON Policy Elements: Condition](../../../service-authorization/latest/reference/reference_policies_elements_condition.md "../../../service-authorization/latest/reference/reference_policies_elements_condition.md") in the _IAM User
Guide_.

The condition keys, related API actions, and links to relevant documentation are
listed in [Condition Keys for SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-policy-keys "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-policy-keys") in the
_Service Authorization Reference_.

The following examples show how to use the SageMaker AI condition keys to control
access.

###### Topics

- [Control access to SageMaker AI resources by
  using file system condition keys](#access-fs-condition-keys "#access-fs-condition-keys")
- [Restrict training to a specific
  VPC](#sagemaker-condition-vpc "#sagemaker-condition-vpc")
- [Restrict access to workforce
  types for Ground Truth labeling jobs and Amazon A2I Human Review workflows](#sagemaker-condition-keys-labeling "#sagemaker-condition-keys-labeling")
- [Enforce encryption of input
  data](#sagemaker-condition-kms "#sagemaker-condition-kms")
- [Enforce network isolation for
  training jobs](#sagemaker-condition-isolation "#sagemaker-condition-isolation")
- [Enforce a specific instance type
  for training jobs](#sagemaker-condition-instance "#sagemaker-condition-instance")
- [Enforce disabling internet
  access and root access for creating notebook instances](#sagemaker-condition-nbi-lockdown "#sagemaker-condition-nbi-lockdown")

### Control access to SageMaker AI resources by

using file system condition keys

SageMaker AI training provides a secure infrastructure for the training algorithm to
run in, but for some cases you may want increased defense in depth. For example,
you minimize the risk of running untrusted code in your algorithm, or you have
specific security mandates in your organization. For these scenarios, you can
use the service-specific condition keys in the Condition element of an IAM
policy to scope down the user to:

- specific file systems
- directories
- access modes (read-write, read-only)
- security groups

###### Topics

- [Restrict an IAM user to
  specific directories and access modes](#access-fs-condition-keys-ex-dirs "#access-fs-condition-keys-ex-dirs")
- [Restrict a user to a
  specific file system](#access-fs-condition-keys-ex-fs "#access-fs-condition-keys-ex-fs")

#### Restrict an IAM user to

specific directories and access modes

The following policy restricts a user to the
`/sagemaker/xgboost-dm/train` and
`/sagemaker/xgboost-dm/validation` directories of an
EFS file system to `ro` (read-only) AccessMode:

###### Note

When a directory is allowed, all of its subdirectories are also
accessible by the training algorithm. POSIX permissions are
ignored.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessToElasticFileSystem",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateHyperParameterTuningJob"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sagemaker:FileSystemId": "fs-12345678",
 "sagemaker:FileSystemAccessMode": "ro",
 "sagemaker:FileSystemType": "EFS",
 "sagemaker:FileSystemDirectoryPath": "/sagemaker/xgboost-dm/train"
 }
 }
 },
 {
 "Sid": "AccessToElasticFileSystemValidation",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateHyperParameterTuningJob"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sagemaker:FileSystemId": "fs-12345678",
 "sagemaker:FileSystemAccessMode": "ro",
 "sagemaker:FileSystemType": "EFS",
 "sagemaker:FileSystemDirectoryPath": "/sagemaker/xgboost-dm/validation"
 }
 }
 }
 ]
}`

```

#### Restrict a user to a

specific file system

To prevent a malicious algorithm using a user space client from accessing
any file system directly in your account, you can restrict networking
traffic. To restrict this traffic, allow ingress only from a specific
security group. In the following example, the user can only use the
specified security group to access the file system:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessToLustreFileSystem",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateHyperParameterTuningJob"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sagemaker:FileSystemId": "fs-12345678",
 "sagemaker:FileSystemAccessMode": "ro",
 "sagemaker:FileSystemType": "FSxLustre",
 "sagemaker:FileSystemDirectoryPath": "/fsx/sagemaker/xgboost/train"
 },
 "ForAllValues:StringEquals": {
 "sagemaker:VpcSecurityGroupIds": [
 "sg-12345678"
 ]
 }
 }
 }
 ]
}`

```

This example can restrict an algorithm to a specific file system. However,
it does not prevent an algorithm from accessing any directory within that
file system using the user space client. To mitigate this, you can:

- Ensure that the file system only contains data that you trust your
  users to access
- Create an IAM role that restricts your users to launching
  training jobs with algorithms from approved ECR repositories

For more information on how to use roles with SageMaker AI, see [SageMaker AI Roles](sagemaker-roles.md "sagemaker-roles.md").

### Restrict training to a specific

VPC

Restrict an AWS user to creating training jobs from within a Amazon VPC. When a
training job is created within a VPC, use VPC flow logs to monitor all traffic
to and from the training cluster. For information about using VPC flow logs, see
[VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") in the
_Amazon Virtual Private Cloud User Guide_.

The following policy enforces that a training job is created by a user calling
[`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") from within a VPC:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowFromVpc",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateHyperParameterTuningJob"
 ],
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "sagemaker:VpcSubnets": ["subnet-a1234"],
 "sagemaker:VpcSecurityGroupIds": ["sg12345", "sg-67890"]
 },
 "Null": {
 "sagemaker:VpcSubnets": "false",
 "sagemaker:VpcSecurityGroupIds": "false"
 }
 }
 }

 ]
}`

```

### Restrict access to workforce

types for Ground Truth labeling jobs and Amazon A2I Human Review workflows

Amazon SageMaker Ground Truth and Amazon Augmented AI work teams fall into one of three [workforce types](sms-workforce-management.md "sms-workforce-management.md"):

- public (with Amazon Mechanical Turk)
- private
- vendor

You can restrict user access to a specific work team using one of these types
or the work team ARN. To do so, use the `sagemaker:WorkteamType`
and/or the `sagemaker:WorkteamArn` condition keys. For the
`sagemaker:WorkteamType` condition key, use [string condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String"). For the
`sagemaker:WorkteamArn` condition key, use [Amazon Resource Name (ARN) condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN"). If the user
attempts to create a labeling job with a restricted work team, SageMaker AI returns an
access denied error.

The following policies show different ways to use the
`sagemaker:WorkteamType` and `sagemaker:WorkteamArn`
condition keys with appropriate condition operators and valid condition values.

The following example uses the `sagemaker:WorkteamType` condition
key with the `StringEquals` condition operator to restrict access to
a public work team. It accepts condition values in the following format:
``workforcetype`-crowd`, where
 `workforcetype`can equal`public`,
 `private`, or `vendor`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RestrictWorkteamType",
 "Effect": "Deny",
 "Action": "sagemaker:CreateLabelingJob",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sagemaker:WorkteamType": "`public-crowd`"
 }
 }
 }
 ]
}`

```

The following policies show how to restrict access to a public work team using
the `sagemaker:WorkteamArn` condition key. The first shows how to use
it with a valid IAM regex-variant of the work team ARN and the
`ArnLike` condition operator. The second shows how to use it with
the `ArnEquals` condition operator and the work team ARN.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RestrictWorkteamType",
 "Effect": "Deny",
 "Action": "sagemaker:CreateLabelingJob",
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "sagemaker:WorkteamArn": "arn:aws:sagemaker:*:*:workteam/public-crowd/*"
 }
 }
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RestrictWorkteamType",
 "Effect": "Deny",
 "Action": "sagemaker:CreateLabelingJob",
 "Resource": "*",
 "Condition": {
 "ArnEquals": {
 "sagemaker:WorkteamArn": "`arn:aws:sagemaker:us-west-2:394669845002:workteam/public-crowd/default`"
 }
 }
 }
 ]
}`

```

### Enforce encryption of input

data

The following policy restricts a user to specify a AWS KMS key to encrypt input
data using the `sagemaker:VolumeKmsKey` condition key when
creating:

- training
- hyperparameter tuning
- labeling jobs

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnforceEncryption",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateHyperParameterTuningJob",
 "sagemaker:CreateLabelingJob",
 "sagemaker:CreateFlowDefinition"
 ],
 "Resource": "*",
 "Condition": {
 "ArnEquals": {
 "sagemaker:VolumeKmsKey": "arn:aws:kms:`us-east-1`:`111122223333`:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 }
 }
 }

 ]
}`

```

### Enforce network isolation for

training jobs

The following policy restricts a user to enable network isolation when
creating training jobs by using the `sagemaker:NetworkIsolation`
condition key:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnforceIsolation",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateHyperParameterTuningJob"
 ],
 "Resource": "*",
 "Condition": {
 "Bool": {
 "sagemaker:NetworkIsolation": "true"
 }
 }
 }
 ]
}`

```

### Enforce a specific instance type

for training jobs

The following policy restricts a user to use a specific instance type when
creating training jobs by using the `sagemaker:InstanceTypes`
condition key:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnforceInstanceType",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateHyperParameterTuningJob"
 ],
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringLike": {
 "sagemaker:InstanceTypes": ["ml.c5.*"]
 }
 }
 }

 ]
}`

```

### Enforce disabling internet

access and root access for creating notebook instances

You can disable both internet access and root access to notebook instances to
help make them more secure. For information about controlling root access to a
notebook instance, see [Control root access to a SageMaker notebook instance](nbi-root-access.md "nbi-root-access.md"). For information about disabling internet
access for a notebook instance, see [Connect a Notebook Instance in a
VPC to External Resources](appendix-notebook-and-internet-access.md "appendix-notebook-and-internet-access.md").

The following policy requires a user to disable network access when creating
instance, and disable root access when creating or updating a notebook instance.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LockDownCreateNotebookInstance",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateNotebookInstance"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sagemaker:DirectInternetAccess": "Disabled",
 "sagemaker:RootAccess": "Disabled"
 },
 "Null": {
 "sagemaker:VpcSubnets": "false",
 "sagemaker:VpcSecurityGroupIds": "false"
 }
 }
 },
 {
 "Sid": "LockDownUpdateNotebookInstance",
 "Effect": "Allow",
 "Action": [
 "sagemaker:UpdateNotebookInstance"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sagemaker:RootAccess": "Disabled"
 }
 }
 }
 ]
}`

```

## Control access to the SageMaker AI API by using

identity-based policies

To control access to SageMaker AI API calls and calls to SageMaker AI hosted endpoints, use
identity-based IAM policies.

###### Topics

- [Restrict access to SageMaker AI API and runtime
  to calls from within your VPC](#api-access-policy-vpc "#api-access-policy-vpc")

### Restrict access to SageMaker AI API and runtime

to calls from within your VPC

If you set up an interface endpoint in your VPC, individuals outside the VPC
can connect to the SageMaker AI API and runtime over the internet. To prevent this,
attach an IAM policy that restricts access to calls coming from within the
VPC. These calls must be restricted to all users and groups that have access to
your SageMaker AI resources. For information about creating a VPC interface endpoint for
the SageMaker AI API and runtime, see [Connect to SageMaker AI Within your VPC](interface-vpc-endpoint.md "interface-vpc-endpoint.md").

###### Important

If you apply an IAM policy similar to one of the following, users can't
access the specified SageMaker AI APIs through the console.

To restrict access to only connections made from within your VPC, create an
AWS Identity and Access Management policy that restricts access. This access must be restricted to only
calls that come from within your VPC. Then add that policy to every AWS Identity and Access Management
user, group, or role used to access the SageMaker AI API or runtime.

###### Note

This policy allows connections only to callers within a subnet where you
created an interface endpoint.

JSON

```
`{
 "Id": "api-example-1",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableAPIAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker:*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceVpc": "vpc-111bbaaa"
 }
 }
 }
 ]
}`

```

To restrict access to the API to only calls made using the interface endpoint,
use the `aws:SourceVpce` condition key instead of
`aws:SourceVpc`:

JSON

```
`{
 "Id": "api-example-1",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableAPIAccess",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreatePresignedNotebookInstanceUrl"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:sourceVpce": [
 "vpce-111bbccc",
 "vpce-111bbddd"
 ]
 }
 }
 }
 ]
}`

```

## Limit access to SageMaker AI API and runtime calls by IP

address

You can allow access to SageMaker AI API calls and runtime invocations only from IP
addresses in a list that you specify. To do so, create an IAM policy that denies
access to the API unless the call comes from an IP address in the list. Then attach
that policy to every AWS Identity and Access Management user, group, or role used to access the API or
runtime. For information about creating IAM policies, see [Creating
IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _AWS Identity and Access Management User Guide_.

To specify the list of IP addresses that have access to the API call, use
the:

- `IpAddress` condition operator
- `aws:SourceIP` condition context key

For information about IAM condition operators, see [IAM JSON Policy Elements: Condition Operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") in the
_AWS Identity and Access Management User Guide_. For information about IAM condition
context keys, see [AWS Global Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").

For example, the following policy allows access to the [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") only from IP addresses in the ranges
`192.0.2.0`-`192.0.2.255` and
`203.0.113.0`-`203.0.113.255`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [

 {
 "Effect": "Allow",
 "Action": "sagemaker:CreateTrainingJob",
 "Resource": "*",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "192.0.2.0/24",
 "203.0.113.0/24"
 ]
 }
 }
 }
 ]
}`

```

## Limit access to a notebook instance by IP

address

You can allow access to a notebook instance only from IP addresses in a list that
you specify. To do so, create an IAM policy that denies access to [`CreatePresignedNotebookInstanceUrl`](../APIReference/API_CreatePresignedNotebookInstanceUrl.md "../APIReference/API_CreatePresignedNotebookInstanceUrl.md") unless the call comes
from an IP address in the list. Then, attach this policy to every AWS Identity and Access Management user,
group, or role used to access the notebook instance. For information about creating
IAM policies, see [Creating
IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _AWS Identity and Access Management User Guide_.

To specify the list of IP addresses that you want to have access to the notebook
instance, use the:

- `IpAddress` condition operator
- `aws:SourceIP` condition context key

For information about IAM condition operators, see [IAM JSON Policy Elements: Condition Operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") in the
_AWS Identity and Access Management User Guide_. For information about IAM condition
context keys, see [AWS Global Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").

For example, the following policy allows access to a notebook instance only from
IP addresses in the ranges `192.0.2.0`-`192.0.2.255` and
`203.0.113.0`-`203.0.113.255`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [

 {
 "Effect": "Allow",
 "Action": "sagemaker:CreatePresignedNotebookInstanceUrl",
 "Resource": "*",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "192.0.2.0/24",
 "203.0.113.0/24"
 ]
 }
 }
 }
 ]
}`

```

The policy restricts access to both the call to
`CreatePresignedNotebookInstanceUrl` and to the URL that the call
returns. The policy also restricts access to opening a notebook instance in the
console. It is enforced for every HTTP request and WebSocket frame that attempts to
connect to the notebook instance.

###### Note

Using this method to filter by IP address is incompatible when [connecting to SageMaker AI through a VPC interface endpoint.](interface-vpc-endpoint.md "interface-vpc-endpoint.md"). For
information about restricting access to a notebook instance when connecting
through a VPC interface endpoint, see [Connect to a Notebook Instance Through a
VPC Interface Endpoint](notebook-interface-endpoint.md "notebook-interface-endpoint.md").

## Control access to SageMaker AI resources by using

tags

Specify tags within an IAM policy to control access to groups of SageMaker AI resources.
Use tags to implement attribute based access control (ABAC). Using tags helps you
partition access to resources to specific groups of users. You can have one team
with access to one group of resources and a different team with access to another
set of resources. You can provide `ResourceTag` conditions in IAM
policies to provide access for each group.

###### Note

Tag-based policies don't work to restrict the following API calls:

- DeleteImageVersion
- DescribeImageVersion
- ListAlgorithms
- ListCodeRepositories
- ListCompilationJobs
- ListEndpointConfigs
- ListEndpoints
- ListFlowDefinitions
- ListHumanTaskUis
- ListHyperparameterTuningJobs
- ListLabelingJobs
- ListLabelingJobsForWorkteam
- ListModelPackages
- ListModels
- ListNotebookInstanceLifecycleConfigs
- ListNotebookInstances
- ListSubscribedWorkteams
- ListTags
- ListProcessingJobs
- ListTrainingJobs
- ListTrainingJobsForHyperParameterTuningJob
- ListTransformJobs
- ListWorkteams
- Search

A simple example can help you understand how you can use tags to partition
resources. Suppose that you've defined two different IAM groups, named
`DevTeam1` and `DevTeam2`, in your AWS account. You've
created 10 notebook instances as well. You're using 5 of the notebook instances for
one project. You're using the other 5 for a second project. You can provide
`DevTeam1` with permissions to make API calls on the notebook
instances that you're using for the first project. You can provide
`DevTeam2` to make API calls on notebook instances used for the
second project.

The following procedure provides a simple example that helps you understand the
concept of adding tags. You can use it to implement the solution described in the
preceding paragraph.

###### To control access to API calls (example)

1. Add a tag with the key `Project` and value `A` to
   the notebook instances used for the first project. For information about
   adding tags to SageMaker AI resources, see [`AddTags`](../APIReference/API_AddTags.md "../APIReference/API_AddTags.md").
2. Add a tag with the key `Project` and value `B` to
   the notebook instances used for the second project.
3. Create an IAM policy with a `ResourceTag` condition that
   denies access to the notebook instances used for the second project. Then,
   attach that policy to `DevTeam1`. The following example policy
   denies all API calls on any notebook instance with a tag with a key of
   `Project` and a value of `B`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sagemaker:*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "sagemaker:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sagemaker:ResourceTag/Project": "B"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "sagemaker:AddTags",
 "sagemaker:DeleteTags"
 ],
 "Resource": "*"
 }
 ]
}`

```

For information about creating IAM policies and attaching them to
identities, see [Controlling Access Using Policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md") in the _AWS Identity and Access Management
User Guide_. 4. Create an IAM policy with a `ResourceTag` condition that
denies access to the notebook instances used for the first project. Then,
attach that policy to `DevTeam2`. The following example policy
denies all API calls on any notebook instance with a tag with a key of
`Project` and a value of `A`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sagemaker:*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "sagemaker:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "sagemaker:ResourceTag/Project": "A"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "sagemaker:AddTags",
 "sagemaker:DeleteTags"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Provide permissions for tagging SageMaker AI

resources

[Tags](../../../whitepapers/latest/tagging-best-practices/what-are-tags.md "../../../whitepapers/latest/tagging-best-practices/what-are-tags.md")
are metadata labels that you can attach to certain AWS resources. A tag consists
of a key-value pair that provides a flexible way to annotate resources with metadata
attributes for various [tagging
use cases](../../../whitepapers/latest/tagging-best-practices/tagging-use-cases.md "../../../whitepapers/latest/tagging-best-practices/tagging-use-cases.md") including:

- search
- security
- [cost attribution](../../../whitepapers/latest/sagemaker-studio-admin-best-practices/cost-attribution.md "../../../whitepapers/latest/sagemaker-studio-admin-best-practices/cost-attribution.md")
- access control
- automation

They can be used in permissions and policies, service quotas, and integrations
with other AWS services. Tags can be user-defined or AWS generated when creating
resources. This depends on whether a user manually specifies custom tags or an AWS
service automatically generates a tag.

- _User-defined tags_ in SageMaker AI: Users can
  add tags when they create SageMaker AI resources using SageMaker SDKs, the AWS CLI CLI,
  SageMaker APIs, SageMaker AI Console, or AWS CloudFormation templates.

###### Note

User-defined tags can be overridden if a resource is later updated and
the tag value is changed or replaced. For example, a training job
created with {Team: A} could be improperly updated and retagged as
{Team: B}. As a result, the allowed permissions may be improperly
assigned. Therefore, care should be given when allowing users or groups
to add tags, as they may be able to override existing tag values. It's
best practice to tightly scope tag permissions and use IAM conditions
to control tagging abilities.

- _AWS generated tags_ in SageMaker AI: SageMaker AI
  automatically tags certain resources it creates. For example, Studio
  and Studio Classic automatically assign the `sagemaker:domain-arn`
  tag to SageMaker AI resources that they create. Tagging new resources with the
  domain ARN provides traceability into how SageMaker AI resources such as
  training jobs, models, and endpoints originate. For finer control and
  tracking, new resources receive additional tags such as:
  - `sagemaker:user-profile-arn` - The ARN of the user
    profile that created the resource. This allows tracking resources
    created by specific users.
  - `sagemaker:space-arn` - The ARN of the space in which
    the resource was created. This allows grouping and isolating
    resources per space.

###### Note

AWS generated tags cannot be changed by users.

For general information on tagging AWS resources and best practices, see [Tagging your
AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md"). For information on the main tagging use cases, see
[Tagging
use cases](../../../whitepapers/latest/tagging-best-practices/tagging-use-cases.md "../../../whitepapers/latest/tagging-best-practices/tagging-use-cases.md").

### Grant permission to add

tags when creating SageMaker AI resources

You can allow users (_User-defined tags_) or
Studio and Studio Classic (_AWS generated
tags_) to add tags on new SageMaker AI resources at creation time. To do
so, their IAM permissions must include both:

- The base SageMaker AI create permission for that resource type.
- The `sagemaker:AddTags` permission.

For example, allowing a user to create a SageMaker training job and tag it would
require granting permissions for `sagemaker:CreateTrainingJob` and
`sagemaker:AddTags`.

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to
create Amazon SageMaker AI resources must also grant permissions to add tags to those
resources. The permission to add tags to resources is required because
Studio and Studio Classic automatically tag any resources they create. If
an IAM policy allows Studio and Studio Classic to create resources but
does not allow tagging, "AccessDenied" errors can occur when trying to
create resources.

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md") that give permissions to create
SageMaker AI resources already include permissions to add tags while creating those
resources.

Administrators attach these IAM permissions to either:

- AWS IAM roles assigned to the user for user-defined tags
- the execution role used by Studio or Studio Classic for AWS
  generated tags

For instructions on creating and applying custom IAM policies, see [Creating
IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md").

###### Note

The list of SageMaker AI resource create operations can be found in the [SageMaker API documentation](../APIReference/API_Operations_Amazon_SageMaker_Service.md "../APIReference/API_Operations_Amazon_SageMaker_Service.md") by searching for actions beginning with
`Create`. These create actions, such as
`CreateTrainingJob` and `CreateEndpoint`, are the
operations that create new SageMaker AI resources.

**Add tag permissions to certain create actions**

You grant the `sagemaker:AddTags` permission with constraints by
attaching an additional IAM policy to the original resource creation policy.
The following example policy allows `sagemaker:AddTags`, but
restricts it to only certain SageMaker AI resource create actions such as
`CreateTrainingJob`.

```
{
  "Sid": "AllowAddTagsForCreateOperations",
  "Effect": "Allow",
  "Action": [
    "sagemaker:AddTags"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "sagemaker:TaggingAction": "CreateTrainingJob"
    }
  }
}
```

The policy condition limits `sagemaker:AddTags` to being used
alongside specific create actions. In this approach, the create permission
policy remains intact while an extra policy provides restricted
`sagemaker:AddTags` access. The condition prevents blanket
`sagemaker:AddTags` permission by scoping it narrowly to creation
actions that need tagging. This implements least privilege for
`sagemaker:AddTags` by only permitting it for specific SageMaker AI
resource creation use cases.

**Example: Allow tag permission globally and restrict
create actions to a domain**

In this example of a custom IAM policy, the first two statements illustrate
using tags to track resource creation. It allows the
`sagemaker:CreateModel` action on all resources and tagging of
those resources when that action is used. The third statement demonstrates how
tag values can be used to control operations on resources. In this case, it
prevents creating any SageMaker AI resources tagged with a specific domain ARN,
restricting access based on the tag value.

In particular:

- The first statement allows the `CreateModel` action on any
  resource (`*`).
- The second statement allows the `sagemaker:AddTags` action,
  but only when the `sagemaker:TaggingAction` condition key
  equals `CreateModel`. This restricts the
  `sagemaker:AddTags` action to only when it's being used
  to tag a newly created model.
- The third statement denies any SageMaker AI create action
  (`Create*`) on any resource (`*`), but only
  when the resource has a tag `sagemaker:domain-arn` equal to a
  specific domain ARN,
  `domain-arn`.

```
{
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "sagemaker:CreateModel"
         ],
         "Resource":"*"
      },
      {
         "Effect":"Allow",
         "Action":[
            "sagemaker:AddTags"
         ],
         "Resource":"*",
         "Condition":{
            "String":{
               "sagemaker:TaggingAction":[
                  "CreateModel"
               ]
            }
         }
      },
      {
         "Sid":"IsolateDomain",
         "Effect":"Deny",
         "Resource":"*",
         "Action":[
            "sagemaker:Create*"
         ],
         "Condition":{
            "StringEquals":{
               "aws:ResourceTag/sagemaker:domain-arn":"`domain-arn`"
            }
         }
      }
   ]
}
```

## Limit access to searchable

resources with visibility conditions

Use visibility conditions to limit the access of your users to specific tagged
resources within an AWS account. Your users can access only those resources for
which they have permissions. When your users are searching through their resources,
they can limit the search results to specific resources.

You might want your users to only see and interact with the resources associated
with specific Amazon SageMaker Studio or Amazon SageMaker Studio Classic domains. You can use visibility
conditions to limit their access to a single domain or multiple
domains.

```

{
    "Sid": "SageMakerApis",
    "Effect": "Allow",
    "Action": "sagemaker:Search",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "sagemaker:SearchVisibilityCondition/Tags.sagemaker:`example-domain-arn`/EqualsIfExists": "arn:aws:sagemaker:`AWS Region`:`111122223333`:domain/`example-domain-1`",
            "sagemaker:SearchVisibilityCondition/Tags.sagemaker:`example-domain-arn`/EqualsIfExists": "arn:aws:sagemaker:`AWS Region`:`111122223333`:domain/`example-domain-2`"
        }
    }
}

```

The general format of a visibility condition is
`"sagemaker:SearchVisibilityCondition/Tags.key": "value"`. You can
provide the key-value pair for any tagged resource.

```

{
   "MaxResults": number,
   "NextToken": "string",
   "Resource": "string", # Required Parameter
   "SearchExpression": {
      "Filters": [
         {
            "Name": "string",
            "Operator": "string",
            "Value": "string"
         }
      ],
      "NestedFilters": [
         {
            "Filters": [
               {
                  "Name": "string",
                  "Operator": "string",
                  "Value": "string"
               }
            ],
            "NestedPropertyName": "string"
         }
      ],
      "Operator": "string",
      "SubExpressions": [
         "SearchExpression"
      ]
   },
   "IsCrossAccount": "string",
   "VisibilityConditions" : [ List of conditions for visibility
         {"Key": "Tags.sagemaker:`example-domain-arn`", "Value": "arn:aws:sagemaker:`AWS Region`:`111122223333`:domain/`example-domain-1`"},
         {"Key": "Tags.sagemaker:`example-domain-arn`", "Value": "arn:aws:sagemaker:`AWS Region`:111122223333:domain/`example-domain-2`"}
]
   ],
   "SortBy": "string",
   "SortOrder": "string"
}

```

The visibility condition within uses the same
`"sagemaker:SearchVisibilityCondition/Tags.key": "value"` formatting
specified in the policy. Your users can specify the key-value pairs used for any
tagged resource.

If a user includes the `VisibilityConditions` parameter in their [Search](../APIReference/API_Search.md "../APIReference/API_Search.md") request, but the access policy that applies to that user doesn't
contain any matching conditions keys that were specified in
`VisibilityConditions`, the `Search` request is still
allowed and will run.

If a `VisibilityConditions` parameter is not specified in the user's
[Search](../APIReference/API_Search.md "../APIReference/API_Search.md") API request, but the access policy that applies to that user
contains condition keys related to `VisibilityConditions`, that user's
`Search` request is denied.
