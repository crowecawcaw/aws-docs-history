# AWS managed policies for Next generation Resilience Hub

An AWS managed policy is a standalone policy that is created and administered by AWS.
AWS managed policies are designed to provide permissions for many common use cases so that you
can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your
specific use cases because they're available for all AWS customers to use. We recommend that you
reduce permissions further by defining customer managed policies that are specific to your use
cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the
permissions defined in an AWS managed policy, the update affects all principal identities (users,
groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed
policy when a new AWS service is launched or new API operations become available for existing
services.

###### Topics

- [AWSResilienceHubV2AssessmentExecutionPolicy](#next-gen-security_iam_aws-v2-assessment-policy "#next-gen-security_iam_aws-v2-assessment-policy")
- [AWSResilienceHubResilienceTestingPolicy](#next-gen-security_iam_aws-resilience-testing-policy "#next-gen-security_iam_aws-resilience-testing-policy")
- [AWSResilienceHubServiceRolePolicy](#next-gen-security-iam-awsmanpol-slr "#next-gen-security-iam-awsmanpol-slr")
- [Next generation Resilience Hub updates to AWS managed policies](#next-gen-security-iam-awsmanpol-updates "#next-gen-security-iam-awsmanpol-updates")

## AWSResilienceHubV2AssessmentExecutionPolicy

You can attach the `AWSResilienceHubV2AssessmentExecutionPolicy` to your IAM
identities. While running an assessment, this policy grants read-only access permissions to other
AWS services for resilience discovery, assessment, and management.

### Permission details

This policy grants wildcarded read-only permissions that might include sensitive information
in the output.

This policy includes the following permissions:

- Amazon CloudWatch (CloudWatch) – Provides `Describe`, `Get`, and
  `List` permissions for CloudWatch resources that are associated with your AWS
  account.
- AWS CloudFormation – Provides `Describe`, `Get`, and `List`
  permissions for AWS CloudFormation resources that are associated with your AWS account.
- Amazon Elastic Compute Cloud (Amazon EC2) – Provides specific `Describe` permissions for Amazon EC2
  resources that are associated with your AWS account.
- Amazon Elastic Container Service (Amazon ECS) – Provides `Describe` and `List` permissions
  for Amazon ECS resources that are associated with your AWS account.
- Amazon Elastic Kubernetes Service (Amazon EKS) – Provides `Describe` and `List` permissions
  for Amazon EKS resources that are associated with your AWS account.
- Amazon Elastic Container Registry (Amazon ECR) – Provides `Describe` permissions for Amazon ECR resources
  that are associated with your AWS account.
- Amazon Elastic File System (Amazon EFS) – Provides `Describe` permissions for Amazon EFS resources
  that are associated with your AWS account.
- Amazon ElastiCache (ElastiCache) – Provides `Describe` permissions for ElastiCache resources
  that are associated with your AWS account.
- Elastic Load Balancing – Provides `Describe` permissions for Elastic Load Balancing resources that are
  associated with your AWS account.
- Amazon DynamoDB (DynamoDB) – Provides `Describe` and `List` permissions
  for DynamoDB resources that are associated with your AWS account.
- Amazon RDS – Provides `Describe` permissions for Amazon RDS resources that are
  associated with your AWS account.
- Amazon DocumentDB – Provides `Describe` and `List` permissions for
  Amazon DocumentDB resources that are associated with your AWS account.
- AWS Lambda (Lambda) – Provides specific `Get` and `List`
  permissions for Lambda resources that are associated with your AWS account.
- AWS Step Functions – Provides `Describe` and `List` permissions for
  AWS Step Functions resources that are associated with your AWS account.
- IAM – Provides specific `Get` and `List` permissions for
  IAM resources that are associated with your AWS account.
- Amazon Simple Notification Service (Amazon SNS) – Provides `Get` and `List` permissions for
  Amazon SNS resources that are associated with your AWS account.
- Amazon Simple Queue Service (Amazon SQS) – Provides `Get` and `List` permissions for
  Amazon SQS resources that are associated with your AWS account.
- Amazon Simple Storage Service (Amazon S3) – Provides `Get` and `List` permissions for
  Amazon S3 resources that are associated with your AWS account. The Amazon S3 permissions in the
  `AWSResilienceHubS3AccessStatement` are restricted to resources in the same account
  by using the `aws:ResourceAccount` condition key.
- Amazon Route 53 (Route 53) – Provides `Get` and `List` permissions for
  Route 53 resources, including Route 53 Application Recovery Controller resources, that are
  associated with your AWS account.
- Amazon EC2 Systems Manager (SSM) – Provides `Describe` and `Get` permissions
  for SSM resources that are associated with your AWS account.
- Amazon EC2 Auto Scaling – Provides `Describe` permissions for Amazon EC2 Auto Scaling resources that
  are associated with your AWS account.
- AWS Backup – Provides `Describe`, `Get`, and `List`
  permissions for AWS Backup resources that are associated with your AWS account.
- AWS Elastic Disaster Recovery (Elastic Disaster Recovery) – Provides `Describe` permissions for Elastic Disaster Recovery resources
  that are associated with your AWS account.
- AWS Fault Injection Service (AWS FIS) – Provides `Get` and `List` permissions for
  AWS FIS experiments and experiment templates that are associated with your AWS account.
- Amazon FSx for Windows File Server (Amazon FSx) – Provides `Describe` permissions for Amazon FSx
  resources that are associated with your AWS account.
- Amazon Data Lifecycle Manager – Provides `Get` permissions for Amazon Data Lifecycle Manager resources that are
  associated with your AWS account.
- AWS DataSync – Provides `Describe` and `List` permissions for
  AWS DataSync resources that are associated with your AWS account.
- AWS Resource Groups (Resource Groups) – Provides `Get` and `List` permissions for
  Resource Groups resources that are associated with your AWS account.
- AWS Service Catalog (Service Catalog) – Provides `Get` and `List` permissions for
  Service Catalog resources that are associated with your AWS account.
- Amazon API Gateway – Provides `GET` permissions scoped to specific
  resource ARN patterns for REST APIs, HTTP APIs, usage plans, and domain names.
- Amazon Kinesis – Provides `Describe` and `List` permissions
  for Kinesis resources that are associated with your AWS account.
- Amazon Kinesis Data Firehose – Provides `Describe` and `List`
  permissions for Kinesis Data Firehose resources that are associated with your AWS
  account.
- Amazon EventBridge – Provides `Describe` and `List`
  permissions for EventBridge resources that are associated with your AWS account.
- Amazon MSK – Provides `Describe`, `Get`, and `List`
  permissions for Amazon MSK and MSK Connect resources that are associated with your AWS
  account.
- Amazon MemoryDB – Provides `Describe` permissions for MemoryDB resources
  that are associated with your AWS account.
- Amazon Redshift – Provides `Describe` permissions for Redshift resources
  that are associated with your AWS account.
- AWS Global Accelerator – Provides `Describe` and `List`
  permissions for Global Accelerator resources that are associated with your AWS account.
- AWS Network Firewall – Provides `Describe` and `List`
  permissions for Network Firewall resources that are associated with your AWS account.
- AWS Shield – Provides `Describe` and `List` permissions for
  Shield resources that are associated with your AWS account.
- AWS WAF V2 – Provides `Get` and `List` permissions for WAF
  V2 resources that are associated with your AWS account.
- AWS Resource Access Manager – Provides `Get` and `List`
  permissions for RAM resources that are associated with your AWS account.
- Amazon VPC Lattice – Provides `Get` and `List` permissions for
  VPC Lattice resources that are associated with your AWS account.
- AWS Config – Provides `Describe` and `List` permissions for
  Config resources that are associated with your AWS account.
- Amazon CloudFront – Provides `Get` and `List` permissions for
  CloudFront resources that are associated with your AWS account.
- AWS Secrets Manager – Provides `Describe` and `List`
  permissions for Secrets Manager resources that are associated with your AWS account.
- AWS Directory Service – Provides `Describe` permissions for Directory
  Service resources that are associated with your AWS account.
- Amazon DSQL – Provides `Get` and `List` permissions for DSQL
  resources that are associated with your AWS account.
- Amazon QLDB – Provides `Describe` and `List` permissions for
  QLDB resources that are associated with your AWS account.
- AWS Certificate Manager – Provides `Describe`, `Get`, and
  `List` permissions for ACM resources that are associated with your AWS
  account.
- Application Auto Scaling – Provides `Describe` permissions for
  Application Auto Scaling resources that are associated with your AWS account.
- SSM Incidents – Provides `Get` and `List` permissions for SSM
  Incidents resources that are associated with your AWS account.
- Tag – Provides `GetResources` permission for querying tagged resources
  that are associated with your AWS account.

The AWS managed policy `AWSResilienceHubV2AssessmentExecutionPolicy` provides
these permissions. Attach the managed policy rather than copying the policy document so that your
permissions stay current as AWS updates it. To view the full policy document, see [AWSResilienceHubV2AssessmentExecutionPolicy](../../../aws-managed-policy/latest/reference/AWSResilienceHubV2AssessmentExecutionPolicy.md "../../../aws-managed-policy/latest/reference/AWSResilienceHubV2AssessmentExecutionPolicy.md") in the AWS Managed Policy Reference
Guide.

## AWSResilienceHubResilienceTestingPolicy

You can attach the `AWSResilienceHubResilienceTestingPolicy` to your IAM
identities. This policy grants Resilience Hub the AWS Fault Injection Service (AWS FIS) permissions needed to start
and manage experiments on your behalf during resilience testing. Experiments started by
Resilience Hub are tagged with `managedBy: resiliencehub`.

### Permission details

This policy includes the following permissions:

- AWS Fault Injection Service (AWS FIS) – Provides permissions to author and manage the experiment
  templates and experiments that Resilience Hub runs on your behalf: creating and deleting
  experiment templates, starting and stopping experiments, monitoring experiment state,
  listing the customer resources targeted by an experiment, tagging resources on create, and
  configuring multi-account targets. These actions are scoped to resources tagged with
  `managedBy: resiliencehub`.
- IAM – Provides `iam:PassRole` to pass the test execution role to
  AWS FIS, and `iam:CreateServiceLinkedRole` to allow AWS FIS to create the
  service-linked role it needs to run experiments.
- AWS Application Recovery Controller (ARC) Region switch – Provides
  `List` and `Get` permissions to monitor Region switch plan executions
  that run as part of an experiment.
- Amazon CloudWatch (CloudWatch) – Provides `DescribeAlarmHistory` to evaluate customer
  alarms as part of the post-experiment workflow during resilience testing.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AWSResilienceHubFISActionStatement",
      "Effect": "Allow",
      "Action": "fis:CreateExperimentTemplate",
      "Resource": "arn:aws:fis:*:*:action/*"
    },
    {
      "Sid": "AWSResilienceHubFISCreateExperimentTemplateStatement",
      "Effect": "Allow",
      "Action": "fis:CreateExperimentTemplate",
      "Resource": "arn:aws:fis:*:*:experiment-template/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/managedBy": "resiliencehub"
        }
      }
    },
    {
      "Sid": "AWSResilienceHubFISStartExperimentFromTemplateStatement",
      "Effect": "Allow",
      "Action": "fis:StartExperiment",
      "Resource": "arn:aws:fis:*:*:experiment-template/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/managedBy": "resiliencehub"
        }
      }
    },
    {
      "Sid": "AWSResilienceHubFISStartExperimentStatement",
      "Effect": "Allow",
      "Action": "fis:StartExperiment",
      "Resource": "arn:aws:fis:*:*:experiment/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/managedBy": "resiliencehub"
        }
      }
    },
    {
      "Sid": "AWSResilienceHubFISExperimentStatement",
      "Effect": "Allow",
      "Action": [
        "fis:GetExperiment",
        "fis:StopExperiment",
        "fis:ListExperimentResolvedTargets"
      ],
      "Resource": "arn:aws:fis:*:*:experiment/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/managedBy": "resiliencehub"
        }
      }
    },
    {
      "Sid": "AWSResilienceHubFISExperimentTemplateStatement",
      "Effect": "Allow",
      "Action": [
        "fis:CreateTargetAccountConfiguration",
        "fis:DeleteExperimentTemplate"
      ],
      "Resource": "arn:aws:fis:*:*:experiment-template/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/managedBy": "resiliencehub"
        }
      }
    },
    {
      "Sid": "AWSResilienceHubFISPassRoleStatement",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::*:role/*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "fis.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AWSResilienceHubFISTagResourceStatement",
      "Effect": "Allow",
      "Action": "fis:TagResource",
      "Resource": [
        "arn:aws:fis:*:*:experiment-template/*",
        "arn:aws:fis:*:*:experiment/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/managedBy": "resiliencehub"
        }
      }
    },
    {
      "Sid": "AWSResilienceHubRegionSwitchStatement",
      "Effect": "Allow",
      "Action": [
        "arc-region-switch:ListPlanExecutions",
        "arc-region-switch:GetPlanExecution"
      ],
      "Resource": "arn:aws:arc-region-switch::*:plan/*:*"
    },
    {
      "Sid": "AWSResilienceHubFISCreateSLRStatement",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/*",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": "fis.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AWSResilienceHubCloudWatchAlarmStatement",
      "Effect": "Allow",
      "Action": "cloudwatch:DescribeAlarmHistory",
      "Resource": "*"
    }
  ]
}
```

## AWSResilienceHubServiceRolePolicy

The `AWSResilienceHubServiceRolePolicy` is a service-linked role (SLR) policy.
You cannot attach this policy to your IAM entities. Next generation Resilience Hub automatically creates this
service-linked role when you enable AWS Organizations support for multi-account resilience
management. This role trusts the `resiliencehub.amazonaws.com` service principal.

For more information about service-linked roles for AWS Resilience Hub, see [Using service-linked
roles for AWS Resilience Hub](using-service-linked-roles.md "using-service-linked-roles.md").

### Permission details

With this policy, Next generation Resilience Hub can access read-only AWS Organizations information
for multi-account resilience management.

This policy includes the following permissions:

- AWS Organizations – Provides `Describe` and `List`
  permissions for Organizations resources. These permissions discover organization structure,
  identify delegated administrators, and verify trusted access status.

The following IAM policy provides required permissions for Next generation Resilience Hub to access AWS
Organizations resources for multi-account resilience management.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AWSResilienceHubOrganizationsReadStatement",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeAccount",
                "organizations:DescribeOrganization",
                "organizations:DescribeOrganizationalUnit",
                "organizations:ListAWSServiceAccessForOrganization",
                "organizations:ListAccounts",
                "organizations:ListAccountsForParent",
                "organizations:ListChildren",
                "organizations:ListDelegatedAdministrators",
                "organizations:ListDelegatedServicesForAccount",
                "organizations:ListOrganizationalUnitsForParent",
                "organizations:ListParents",
                "organizations:ListRoots",
                "organizations:ListTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

## Next generation Resilience Hub updates to AWS managed policies

View details about updates to AWS managed policies for Next generation Resilience Hub since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to the
RSS feed on the Next generation Resilience Hub Document history page.

| Change                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                               | Date          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [AWSResilienceHubResilienceTestingPolicy](#next-gen-security_iam_aws-resilience-testing-policy "#next-gen-security_iam_aws-resilience-testing-policy") – New<br>policy                                                 | AWS added a new policy for the next generation of Resilience Hub to grant the AWS Fault Injection Service (AWS FIS) permissions<br>needed to start and manage experiments on your behalf during resilience testing.                                                                                                       | July 31, 2026 |
| [AWSResilienceHubServiceRolePolicy](next-gen-security-iam-awsmanpol.md#next-gen-security-iam-awsmanpol-slr "next-gen-security-iam-awsmanpol.md#next-gen-security-iam-awsmanpol-slr") – Update to an existing<br>policy | Next generation Resilience Hub added read-only AWS Organizations permissions to the<br>`AWSResilienceHubServiceRolePolicy`. These permissions support multi-account<br>resilience management, including discovering organization structure, identifying delegated<br>administrators, and verifying trusted access status. | July 7, 2026  |
| [AWSResilienceHubV2AssessmentExecutionPolicy](#next-gen-security_iam_aws-v2-assessment-policy "#next-gen-security_iam_aws-v2-assessment-policy") – New policy                                                          | Next generation Resilience Hub added a new policy to grant read-only access permissions to other AWS<br>services for resilience discovery, assessment, and management.                                                                                                                                                    | June 18, 2026 |
| Next generation Resilience Hub started tracking changes                                                                                                                                                                | Next generation Resilience Hub started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                     | June 18, 2026 |
