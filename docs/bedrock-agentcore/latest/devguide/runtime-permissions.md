# IAM Permissions for AgentCore Runtime

The following are IAM permissions you need to create an agent in an AgentCore Runtime and the
execution role permissions that an agent needs to run in an AgentCore Runtime

###### Topics

- [Use Amazon Bedrock AgentCore](#runtime-permissions-use-agentcore "#runtime-permissions-use-agentcore")
- [Use the starter toolkit](#runtime-permissions-starter-toolkit "#runtime-permissions-starter-toolkit")
- [Execution role for running an
  agent in AgentCore Runtime](#runtime-permissions-execution "#runtime-permissions-execution")

## Use Amazon Bedrock AgentCore

To use Amazon Bedrock AgentCore, you can attach the [BedrockAgentCoreFullAccess](../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md "../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md") AWS managed policy to your IAM user or
IAM. role. This AWS managed policy grants broad permissions. We recommend creating a
custom policy with only the permissions your application requires by copying the
relevant statements and restricting the resources to your specific use case. To use the
starter toolkit, you need [additional](#runtime-permissions-starter-toolkit "#runtime-permissions-starter-toolkit") permissions.

## Use the starter toolkit

To use the Amazon Bedrock AgentCore starter toolkit, attach the following IAM policy to your
IAM user or role. To change IAM permissions, see [Change permissions for an IAM
user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IAMRoleManagement",
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:GetRole",
 "iam:PutRolePolicy",
 "iam:DeleteRolePolicy",
 "iam:AttachRolePolicy",
 "iam:DetachRolePolicy",
 "iam:TagRole",
 "iam:ListRolePolicies",
 "iam:ListAttachedRolePolicies"
 ],
 "Resource": [
 "arn:aws:iam::*:role/*BedrockAgentCore*",
 "arn:aws:iam::*:role/service-role/*BedrockAgentCore*"
 ]
 },
 {
 "Sid": "CodeBuildProjectAccess",
 "Effect": "Allow",
 "Action": [
 "codebuild:StartBuild",
 "codebuild:BatchGetBuilds",
 "codebuild:ListBuildsForProject",
 "codebuild:CreateProject",
 "codebuild:UpdateProject",
 "codebuild:BatchGetProjects"
 ],
 "Resource": [
 "arn:aws:codebuild:*:*:project/bedrock-agentcore-*",
 "arn:aws:codebuild:*:*:build/bedrock-agentcore-*"
 ]
 },
 {
 "Sid": "CodeBuildListAccess",
 "Effect": "Allow",
 "Action": [
 "codebuild:ListProjects"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMPassRoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AmazonBedrockAgentCore*",
 "arn:aws:iam::*:role/service-role/AmazonBedrockAgentCore*"
 ]
 },
 {
 "Sid": "CloudWatchLogsAccess",
 "Effect": "Allow",
 "Action": [
 "logs:GetLogEvents",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/bedrock-agentcore/*",
 "arn:aws:logs:*:*:log-group:/aws/codebuild/*"
 ]
 },
 {
 "Sid": "S3Access",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListBucket",
 "s3:CreateBucket",
 "s3:PutLifecycleConfiguration"
 ],
 "Resource": [
 "arn:aws:s3:::bedrock-agentcore-*",
 "arn:aws:s3:::bedrock-agentcore-*/*"
 ]
 },
 {
 "Sid": "ECRRepositoryAccess",
 "Effect": "Allow",
 "Action": [
 "ecr:CreateRepository",
 "ecr:DescribeRepositories",
 "ecr:GetRepositoryPolicy",
 "ecr:InitiateLayerUpload",
 "ecr:CompleteLayerUpload",
 "ecr:PutImage",
 "ecr:UploadLayerPart",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "ecr:ListImages",
 "ecr:TagResource"
 ],
 "Resource": [
 "arn:aws:ecr:*:*:repository/bedrock-agentcore-*"
 ]
 },
 {
 "Sid": "ECRAuthorizationAccess",
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Execution role for running an

agent in AgentCore Runtime

To run agent or tool in AgentCore Runtime you need an AWS Identity and Access Management execution role. For
information about creating an IAM role, see [IAM role creation](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md").

### AgentCore Runtime execution role

The AgentCore Runtime execution role is an IAM role that AgentCore Runtime assumes to run
an agent. Replace the following:

- `us-east-1` with the AWS Region that you are
  using
- `123456789012` with your AWS account ID
- `agentName` with the name of your agent. You'll need to
  decide the agent name before creating the role and AgentCore Runtime.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ECRImageAccess",
 "Effect": "Allow",
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": [
 "arn:aws:ecr:`us-east-1`:`123456789012`:repository/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/bedrock-agentcore/runtimes/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/bedrock-agentcore/runtimes/*:log-stream:*"
 ]
 },
 {
 "Sid": "ECRTokenAccess",
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "xray:PutTraceSegments",
 "xray:PutTelemetryRecords",
 "xray:GetSamplingRules",
 "xray:GetSamplingTargets"
 ],
 "Resource": [ "*" ]
 },
 {
 "Effect": "Allow",
 "Resource": "*",
 "Action": "cloudwatch:PutMetricData",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "bedrock-agentcore"
 }
 }
 },
 {
 "Sid": "GetAgentAccessToken",
 "Effect": "Allow",
 "Action": [
 "bedrock-agentcore:GetWorkloadAccessToken",
 "bedrock-agentcore:GetWorkloadAccessTokenForJWT",
 "bedrock-agentcore:GetWorkloadAccessTokenForUserId"
 ],
 "Resource": [
 "arn:aws:bedrock-agentcore:`us-east-1`:`123456789012`:workload-identity-directory/default",
 "arn:aws:bedrock-agentcore:`us-east-1`:`123456789012`:workload-identity-directory/default/workload-identity/`agentName`-*"
 ]
 },
 {"Sid": "BedrockModelInvocation",
 "Effect": "Allow",
 "Action": [
 "bedrock:InvokeModel",
 "bedrock:InvokeModelWithResponseStream"
 ],
 "Resource": [
 "arn:aws:bedrock:*::foundation-model/*",
 "arn:aws:bedrock:`us-east-1`:`123456789012`:*"
 ]
 }
 ]
}`

```

### AgentCore Runtime trust policy

The trust relationship for the AgentCore Runtime execution role should allow
AgentCore Runtime to assume the role:

Replace the following:

- `us-east-1` with the AWS Region that you are
  using
- `123456789012` with your AWS account ID

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AssumeRolePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "bedrock-agentcore.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:bedrock-agentcore:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```
