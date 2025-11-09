AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Replatform applications to Amazon ECS template

You can use the _Replatform applications to Amazon ECS_ template in Migration Hub Orchestrator to
replatform your .NET and Java applications to containers. The applications can be sourced
from EC2 instances or application artifacts that are uploaded to Amazon S3. You can deploy
containerized applications on Amazon Elastic Container Service (Amazon ECS) on AWS Fargate using one application per
container or with multiple applications in a single container.

###### Topics

- [Prerequisites](#replatform-to-ecs-prerequisites "#replatform-to-ecs-prerequisites")
- [Configuring a
  workflow](#replatform-to-ecs-configure-workflow "#replatform-to-ecs-configure-workflow")
- [Running a workflow](#replatform-to-ecs-run-workflow "#replatform-to-ecs-run-workflow")
- [Combining multiple
  applications in one container](replatform-to-ecs-combining-applications.md "replatform-to-ecs-combining-applications.md")
- [Completing the required
  steps](#replatform-to-ecs-complete-steps "#replatform-to-ecs-complete-steps")

## Prerequisites

The prerequisites required to use this template depend on the source type that you
will specify in the workflow. Your application source can be one or more Amazon EC2
instances or application artifacts that you uploaded to Amazon S3.

The following prerequisites must be met to successfully replatform your applications
with this template.

The following prerequisites apply when you specify the source type of Amazon EC2
while using this template.

###### Topics

- [Application support
  and compatibility](#replatform-to-ecs-prerequisites-setup "#replatform-to-ecs-prerequisites-setup")
- [SSM
  agent](#replatform-to-ecs-prerequisites-ssm-agent "#replatform-to-ecs-prerequisites-ssm-agent")
- [IAM
  instance profile for EC2 instances](#replatform-to-ecs-prerequisites-permissions-instances "#replatform-to-ecs-prerequisites-permissions-instances")

#### Application support

and compatibility

Before using this template on Amazon EC2 instances, ensure that your servers
and applications are supported for App2Container. For more information, see [App2Container
compatibility](../../../app2container/latest/UserGuide/compatibility-a2c.md "../../../app2container/latest/UserGuide/compatibility-a2c.md") and [Applications you can containerize using AWS App2Container](../../../app2container/latest/UserGuide/supported-applications.md "../../../app2container/latest/UserGuide/supported-applications.md") in the
_AWS App2Container User Guide_.

###### Note

You don't need to install Docker on your application server to use
this template.

#### SSM

agent

To use this template with Amazon EC2 instances, they must be managed nodes in
AWS Systems Manager (Systems Manager). The SSM agent is required for your instances to become
managed nodes. Some AMIs have the SSM agent preinstalled, while others
require manual installation. For more information on verifying if the SSM
agent is installed, and how to manually install it if required, see [Amazon Machine Images (AMIs) with SSM Agent preinstalled](../../../systems-manager/latest/userguide/ami-preinstalled-agent.md "../../../systems-manager/latest/userguide/ami-preinstalled-agent.md") in the
_AWS Systems Manager User Guide_.

#### IAM

instance profile for EC2 instances

This template requires that your EC2 instances have an instance profile
role with the necessary permissions attached. The permissions provided by an
instance profile are used by your EC2 instances. You can create a new IAM
instance profile with the required permissions, or add them to an existing
role used by the instance. An instance profile can only contain one IAM
role. The IAM role can contain one or more policies. For more information,
see [Instance profiles](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#ec2-instance-profile "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#ec2-instance-profile") and [Work with IAM roles](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#working-with-iam-roles "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#working-with-iam-roles") in the _Amazon Elastic Compute Cloud User
Guide_.

To configure the required Systems Manager core functionality for your EC2 instances,
you can attach the AWS managed policy
`AmazonSSMManagedInstanceCore` to your instance profile. For
more information about instance permissions for Systems Manager, see [Step 1: Configure instance permissions for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-permissions.md "../../../systems-manager/latest/userguide/setup-instance-permissions.md") in the
_AWS Systems Manager User Guide_.

The following permissions must also be added to the IAM role used by
your instance profile. You can create a new policy with the following JSON
policy document and then attach the policy to your instance profile role.
For more information, see [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _AWS Identity and Access Management User
Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3BucketAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Sid": "S3ObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::*/application-transformation*"
 ]
 },
 {
 "Sid": "KmsAccess",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:*:*:key/*"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "s3.*.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "TelemetryAccess",
 "Effect": "Allow",
 "Action": [
 "application-transformation:PutMetricData",
 "application-transformation:PutLogData"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

[Show moreShow less](# "#")

The following prerequisites apply when you specify the source type of Amazon S3
while using this template.

###### Topics

- [Amazon S3
  buckets](#replatform-to-ecs-prerequisites-s3-bucket "#replatform-to-ecs-prerequisites-s3-bucket")
- [Application artifacts](#replatform-to-ecs-prerequisites-application-artifacts "#replatform-to-ecs-prerequisites-application-artifacts")

#### Amazon S3

buckets

This template requires that you have an Amazon S3 bucket for the S3 input path
and the Amazon S3 output path. You can create different buckets for the input and
output S3 locations. The workflow requires that the application artifacts be
uploaded to an Amazon S3 bucket beginning with the following prefix:

```
S3://`bucket-name`/application-transformation
```

For more information on creating an Amazon S3 bucket, see [Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_.

#### Application artifacts

This template requires that you have application artifacts available in an
Amazon S3 bucket in the bucket prefix mentioned previously in order to replatform
the application. App2Container has the
`AWSApp2Container-ReplatformApplications` AWS Systems Manager
Automation runbook for use on Amazon EC2 instances which generates the required
application artifacts. For more information, see [App2Container
Automation runbook](../../../app2container/latest/UserGuide/automation-runbook.md "../../../app2container/latest/UserGuide/automation-runbook.md") in the _AWS App2Container User
Guide_.

When using Amazon S3 as the source type, you must upload these artifacts to the
S3 bucket you created with the required application artifact files. The
following files are required:

- `replatform-definition.json`
- `analysis.json`
- `ContainerFiles.tar` or
  `ContainerFiles.zip`

The `replatform-definition.json` file should resemble
the following:

```
{
    "version": "1.0",
    "workloads": [
        {
            "containers": [
                {
                    "applications": [
                        {
                            "applicationOverrideS3Uri": "s3://`bucket-name`/application-transformation/`path-to-application-artifacts`/"
                        }
                    ]
                }
            ]
        }
    ]
}
```

### Required IAM

resources

Multiple resources must have the required permissions in order to use this
template. Ensure that you have the following required policies and roles
created.

###### Topics

- [IAM policy for users and roles](#replatform-to-ecs-prerequisites-permissions-users-roles "#replatform-to-ecs-prerequisites-permissions-users-roles")
- [IAM
  policies and roles for Amazon ECS](#replatform-to-ecs-prerequisites-permissions-ecs "#replatform-to-ecs-prerequisites-permissions-ecs")
- [(Optional) KMS key policy](#replatform-to-ecs-prerequisites-permissions-kms "#replatform-to-ecs-prerequisites-permissions-kms")

#### IAM policy for users and roles

Your user or role must have the required permissions to use this template. You
can add this policy inline, or create and add this policy to your user, group,
or role. For more information, see [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") and [Choosing between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the
_AWS Identity and Access Management User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ApplicationTransformationAccess",
 "Effect": "Allow",
 "Action": [
 "application-transformation:StartRuntimeAssessment",
 "application-transformation:GetRuntimeAssessment",
 "application-transformation:PutLogData",
 "application-transformation:PutMetricData",
 "application-transformation:StartContainerization",
 "application-transformation:GetContainerization",
 "application-transformation:StartDeployment",
 "application-transformation:GetDeployment"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AssessmentEc2ReadAccess",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AssessmentIAMRoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:GetInstanceProfile",
 "iam:GetRole"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AsssessmentSSMSendCommandAccess",
 "Effect": "Allow",
 "Action": [
 "ssm:SendCommand"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:instance/*",
 "arn:aws:ssm:*::document/AWS-RunRemoteScript"
 ]
 },
 {
 "Sid": "AsssessmentSSMDescribeAccess",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeInstanceInformation",
 "ssm:ListCommandInvocations",
 "ssm:GetCommandInvocation"
 ],
 "Resource": [
 "arn:aws:ssm:*:*:*"
 ]
 },
 {
 "Sid": "S3ObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::*/application-transformation*"
 ]
 },
 {
 "Sid": "S3ListAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Sid": "KmsAccess",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:*::*"
 },
 {
 "Sid": "EcrAccess",
 "Effect": "Allow",
 "Action": [
 "ecr:CreateRepository",
 "ecr:GetLifecyclePolicy",
 "ecr:GetRepositoryPolicy",
 "ecr:ListImages",
 "ecr:ListTagsForResource",
 "ecr:TagResource",
 "ecr:UntagResource"
 ],
 "Resource": "arn:*:ecr:*:*:repository/*"
 },
 {
 "Sid": "EcrPushAccess",
 "Effect": "Allow",
 "Action": [
 "ecr:InitiateLayerUpload",
 "ecr:PutImage",
 "ecr:UploadLayerPart",
 "ecr:CompleteLayerUpload",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "arn:*:ecr:*:*:repository/*"
 },
 {
 "Sid": "EcrAuthAccess",
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ContainerizeKmsCreateGrantAccess",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant"
 ],
 "Resource": "arn:aws:kms:*::*",
 "Condition": {
 "Bool": {
 "kms:GrantIsForAWSResource": true
 }
 }
 },
 {
 "Sid": "CloudformationExecutionAccess",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:UpdateStack"
 ],
 "Resource": [
 "arn:*:cloudformation:*:*:stack/application-transformation-*"
 ]
 },
 {
 "Sid": "GetECSSLR",
 "Effect": "Allow",
 "Action": "iam:GetRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS"
 },
 {
 "Sid": "CreateEcsServiceLinkedRoleAccess",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "ecs.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CreateElbServiceLinkedRoleAccess",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CreateSecurityGroupAccess",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateSecurityGroup"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Ec2CreateAccess",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateInternetGateway",
 "ec2:CreateKeyPair",
 "ec2:CreateRoute",
 "ec2:CreateRouteTable",
 "ec2:CreateSubnet",
 "ec2:CreateTags",
 "ec2:CreateVpc"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Ec2ModifyAccess",
 "Effect": "Allow",
 "Action": [
 "ec2:AssociateRouteTable",
 "ec2:AttachInternetGateway",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:DeleteTags",
 "ec2:ModifySubnetAttribute",
 "ec2:ModifyVpcAttribute",
 "ec2:RevokeSecurityGroupIngress"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMPassRoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`123456789012`:role/`my-role`"
 },
 {
 "Sid": "EcsCreateAccess",
 "Effect": "Allow",
 "Action": [
 "ecs:CreateCluster",
 "ecs:CreateService",
 "ecs:RegisterTaskDefinition"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EcsModifyAccess",
 "Effect": "Allow",
 "Action": [
 "ecs:TagResource",
 "ecs:UntagResource",
 "ecs:UpdateService"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EcsReadTaskDefinitionAccess",
 "Effect": "Allow",
 "Action": [
 "ecs:DescribeTaskDefinition"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "cloudformation.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudwatchCreateAccess",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:TagResource",
 "logs:PutRetentionPolicy"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/ecs/containerinsights/*:*",
 "arn:aws:logs:*:*:log-group:/aws/ecs/container-logs/*:*"
 ]
 },
 {
 "Sid": "CloudwatchGetAccess",
 "Effect": "Allow",
 "Action": [
 "logs:GetLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/ecs/containerinsights/*:*",
 "arn:aws:logs:*:*:log-group:/aws/ecs/container-logs/*:*"
 ]
 },
 {
 "Sid": "ReadOnlyAccess",
 "Effect": "Allow",
 "Action": [
 "cloudformation:DescribeStacks",
 "cloudformation:ListStacks",
 "clouddirectory:ListDirectories",
 "ds:DescribeDirectories",
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeImages",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeKeyPairs",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ecr:DescribeImages",
 "ecr:DescribeRepositories",
 "ecs:DescribeClusters",
 "ecs:DescribeServices",
 "ecs:DescribeTasks",
 "ecs:ListTagsForResource",
 "ecs:ListTasks",
 "iam:ListRoles",
 "s3:GetBucketLocation",
 "s3:GetBucketVersioning",
 "s3:ListAllMyBuckets",
 "secretsmanager:ListSecrets",
 "acm:DescribeCertificate",
 "acm:GetCertificate",
 "ssm:GetParameters"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ElasticLoadBalancingCreateAccess",
 "Effect": "Allow",
 "Action": [
 "elasticloadbalancing:CreateListener",
 "elasticloadbalancing:CreateLoadBalancer",
 "elasticloadbalancing:CreateTargetGroup",
 "elasticloadbalancing:CreateRule"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ElasticLoadBalancingModifyAccess",
 "Effect": "Allow",
 "Action": [
 "elasticloadbalancing:AddTags",
 "elasticloadbalancing:ModifyTargetGroup",
 "elasticloadbalancing:ModifyTargetGroupAttributes"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ElasticLoadBalancingGetAccess",
 "Effect": "Allow",
 "Action": [
 "elasticloadbalancing:DescribeLoadBalancerAttributes",
 "elasticloadbalancing:DescribeTags",
 "elasticloadbalancing:DescribeTargetGroups",
 "elasticloadbalancing:DescribeRules",
 "elasticloadbalancing:DescribeListeners",
 "elasticloadbalancing:DescribeLoadBalancers"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Route53CreateAccess",
 "Effect": "Allow",
 "Action": [
 "route53:CreateHostedZone"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Route53ModifyAccess",
 "Effect": "Allow",
 "Action": [
 "route53:ChangeTagsForResource",
 "route53:ChangeResourceRecordSets",
 "route53:GetChange",
 "route53:GetHostedZone",
 "route53:ListResourceRecordSets",
 "route53:CreateHostedZone",
 "route53:ListHostedZonesByVPC"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SsmMessagesAccess",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeSessions",
 "ssmmessages:CreateControlChannel",
 "ssmmessages:CreateDataChannel",
 "ssmmessages:OpenControlChannel",
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ServiceDiscoveryCreateAccess",
 "Effect": "Allow",
 "Action": [
 "servicediscovery:CreateService",
 "servicediscovery:CreatePrivateDnsNamespace",
 "servicediscovery:UpdatePrivateDnsNamespace",
 "servicediscovery:TagResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ServiceDiscoveryGetAccess",
 "Effect": "Allow",
 "Action": [
 "servicediscovery:GetNamespace",
 "servicediscovery:GetOperation",
 "servicediscovery:GetService",
 "servicediscovery:ListTagsForResource"
 ],
 "Resource": "*"
 }
 ]
}`

```

[Show moreShow less](# "#")

#### IAM

policies and roles for Amazon ECS

To deploy your containerized applications on Amazon ECS, you must create IAM
policies and roles in your Amazon ECS tasks. For more information about these IAM
resources for Amazon ECS and how to create them, see [Task
execution IAM role](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") and [Task IAM
role](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md") in the _Amazon Elastic Container Service Developer Guide_.

#### (Optional) KMS key policy

You can use AWS KMS to encrypt resources used by this template. If you create a
KMS key to use with this template, we recommend that you use the following
least-privilege permissions for your key policy. For more information, see
[Key policies in
AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

```
{
    "Sid": "KmsAccess",
    "Effect": "Allow",
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": [
        "arn:aws:kms:*:*:key/*"
    ],
    "Condition": {
        "StringLike": {
            "kms:ViaService": [
                "s3.*.amazonaws.com"
            ]
        }
    }
}
```

[Show moreShow less](# "#")

## Configuring a

workflow

You must configure the workflow for the template in order to replatform your
application.

###### To create a workflow using the template

1. Access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Create workflow**.
3. On the **Choose a workflow template** page, choose the
   **Replatform applications to Amazon ECS** template.
4. On the **Configure your workflow** page, enter values for the
   following:
   1. For **Workflow details**, enter values for the
      following:
      1. For **Name**, enter a name for your migration
         workflow.
      2. (Optional) For **Description**, enter a
         description for the workflow you are creating.

   2. For **Source environment configuration**, specify the
      following:
      1. For **Source Region**, choose the Region from
         the dropdown list in which you have EC2 instances hosting
         applications you want to replatform or the S3 bucket containing
         your application artifacts.
      2. For **Source type**, choose **EC2
         instances** if your applications you want to
         replatform are in EC2 instances, or **S3
         location** if your application artifacts are in an
         S3 bucket.
         1. If you chose **EC2 instances**, under
            **Select from EC2 instances**,
            select the instances which have the applications you
            want to replatform.
         2. If you chose **S3 location**, under
            **Specify input path in
            `Region`**,
            enter the path to your
            `replatform-definition.json` file
            in the S3 bucket. Your other required application
            artifacts should also be in this bucket. You can also
            choose **Browse S3** to specify the
            path by navigating to it in the console. The path should
            resemble the following:

         ```
         S3://`bucket-name`/application-transformation/replatform-definition.json
         ```

   3. For **Specify S3 output path**, enter the path of
      your S3 bucket using `S3://` syntax. You can also choose
      **Browse S3** to specify the path by navigating to
      it in the console. The path should resemble the following
      example:

   ```
   S3://`bucket-name`/application-transformation
   ```

   4. (Optional) For **Tags**, choose **Add new
      tag** and enter any desired key-value pairs for your
      resources that are created by this workflow.
   5. Choose **Next**.
   6. On the Review and submit page, ensure the provided details for the
      workflow are correct, then choose **Create**.

Creating a migration workflow doesn't take action on your resources. You will need to
run the workflow as detailed in the following section.

###### Note

You can customize the migration workflow once it has been created. For more information, see
[Migration workflows for Migration Hub Orchestrator](migration-workflows.md "migration-workflows.md").

## Running a workflow

With the workflow created, you can now run it to replatform your applications.

###### To run a workflow

1. Access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, choose your workflow and then
   choose **View details**.
4. Choose **Run** to run the workflow.

###### Important

Some steps might require additional action to complete. All steps must be
completed in order to replatform your application. The following section
details this process.

## Completing the required

steps

The workflow will require additional input for certain steps in order to complete
them. The workflow might take some time to reach this status before you can take action
on the steps.

###### To complete steps for a workflow

1. Access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, choose your workflow and then
   choose **View details**.
4. In the **Steps** tab, choose **Expand all**.
   Steps with a **Status** of **User attention
   required** need additional input to complete the step.
5. Choose the step which requires further input, choose
   **Actions**, **Change status**, and then
   choose **Completed**.
   1. The **Analyze** step requires the following
      input:
      1. For **Applications**, from the dropdown list,
         select the applications that you want to replatform.
      2. For **Containerization options**, choose
         either **One application per container** to
         provision one application per container, or **Combine
         applications in one container** to provision all
         applications in one container. For more information on the
         requirements to combine applications in one container, see [Combining multiple
         applications in one container](replatform-to-ecs-combining-applications.md "replatform-to-ecs-combining-applications.md").
      3. Choose **Confirm** to complete the
         step.

   2. The **Deploy** step requires the following
      input:
      1. For **VPC ID**, enter the ID of the VPC to
         use for deployment.
      2. For **ECS task execution IAM role ARN**,
         choose the ARN of the ECS task execution IAM role used to make
         AWS API calls on your behalf.
      3. (Optional) For **Task role ARN**, choose the
         ARN of the role to be assumed by Amazon ECS tasks.
      4. (Optional) For **Cluster name**, enter a name
         to use for the ECS cluster.
      5. (Optional) For **CPU**, choose the number of
         CPU units the Amazon ECS container agent should reserve for the
         container.
      6. (Optional) For **Memory**, enter amount of
         memory to allocate to the container, specified in GB.

   3. Choose **Confirm** to complete the step.

6. On the **Workflows** page, under **Migration
   workflows**, verify that the overall status of the workflow is
   **Complete**.
