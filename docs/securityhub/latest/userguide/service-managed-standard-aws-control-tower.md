# Service-Managed Standard: AWS Control Tower

This section provides information about Service-Managed Standard: AWS Control Tower.

## What is Service-Managed Standard: AWS Control Tower?

This standard is designed for users of AWS Security Hub CSPM and AWS Control Tower. It lets you configure the proactive controls of AWS Control Tower alongside the detective controls of Security Hub CSPM in the AWS Control Tower service.

Proactive controls help ensure that your AWS accounts maintain compliance because
they flag actions that may lead to policy violations or misconfigurations. Detective
controls detect noncompliance of resources (for example, misconfigurations) within your
AWS accounts. By enabling proactive and detective controls for your AWS environment,
you can enhance your security posture at different stages of development.

###### Tip

Service-managed standards differ from standards that AWS Security Hub CSPM manages. For
example, you must create and delete a service-managed standard in the managing service. For more
information, see [Service-managed standards in Security Hub CSPM](service-managed-standards.md "service-managed-standards.md").

In the Security Hub CSPM console and API, you can view Service-Managed Standard: AWS Control Tower alongside other Security Hub CSPM
standards.

## Creating the standard

This standard is available only if you create the standard in AWS Control Tower. AWS Control Tower
creates the standard when you first enable an applicable control by using one of the
following methods:

- AWS Control Tower console
- AWS Control Tower API (call the [`EnableControl`](../../../controltower/latest/APIReference/API_EnableControl.md "../../../controltower/latest/APIReference/API_EnableControl.md") API)
- AWS CLI (run the [`enable-control`](../../../cli/latest/reference/controltower/enable-control.md "../../../cli/latest/reference/controltower/enable-control.md") command)

Security Hub CSPM controls are identified in the AWS Control Tower console as
**SH.`ControlID`** (for example,
**SH.CodeBuild.1**).

When you create the standard, if you haven’t already enabled Security Hub CSPM, AWS Control Tower also
enables Security Hub CSPM for you.

If you haven't set up AWS Control Tower, you can't view or access this standard in the Security Hub CSPM
console, Security Hub CSPM API, or AWS CLI. Even if you have set up AWS Control Tower, you can't view or access
this standard in Security Hub CSPM without first creating the standard in AWS Control Tower using one of the
preceding methods.

This standard is only available in the [AWS Regions where AWS Control Tower is
available](../../../controltower/latest/userguide/region-how.md "../../../controltower/latest/userguide/region-how.md"), including AWS GovCloud (US).

## Enabling and disabling

controls in the standard

After you've created the standard in the AWS Control Tower console, you can view the standard
and its available controls in both services.

After you first create the standard, it doesn't have any controls that are
automatically enabled. In addition, when Security Hub CSPM adds new controls, they aren't
automatically enabled for Service-Managed Standard: AWS Control Tower. You should enable and disable controls for
the standard in AWS Control Tower by using one of the following methods:

- AWS Control Tower console
- AWS Control Tower API (call the [`EnableControl`](../../../controltower/latest/APIReference/API_EnableControl.md "../../../controltower/latest/APIReference/API_EnableControl.md") and [`DisableControl`](../../../controltower/latest/APIReference/API_DisableControl.md "../../../controltower/latest/APIReference/API_DisableControl.md") APIs)
- AWS CLI (run the [`enable-control`](../../../cli/latest/reference/controltower/enable-control.md "../../../cli/latest/reference/controltower/enable-control.md") and [`disable-control`](../../../cli/latest/reference/controltower/disable-control.md "../../../cli/latest/reference/controltower/disable-control.md") commands)

When you change the enablement status of a control in AWS Control Tower, the change is also
reflected in Security Hub CSPM.

However, disabling a control in Security Hub CSPM that's enabled in AWS Control Tower results in control
drift. The control status in AWS Control Tower shows as `Drifted`. You can resolve
this drift by selecting [Re-register
OU](../../../controltower/latest/userguide/drift.md#resolving-drift "../../../controltower/latest/userguide/drift.md#resolving-drift") in the AWS Control Tower console, or by disabling and re-enabling the control in
AWS Control Tower using one of the preceding methods.

Completing enablement and disablement actions in AWS Control Tower helps you avoid control
drift.

When you enable or disable controls in AWS Control Tower, the action applies across accounts
and Regions. If you enable and disable controls in Security Hub CSPM (not recommended for this
standard), the action applies only to the current account and Region.

###### Note

[Central
configuration](central-configuration-intro.md "central-configuration-intro.md") can't be used to manage Service-Managed Standard: AWS Control Tower. If you use central configuration, you can use _only_
the AWS Control Tower service to enable and disable controls in this standard for a centrally managed account.

## Viewing enablement status

and control status

You can view the enablement status of a control by using one of the following
methods:

- Security Hub CSPM console, Security Hub CSPM API, or AWS CLI
- AWS Control Tower console
- AWS Control Tower API to see a list of enabled controls (call the [`ListEnabledControls`](../../../controltower/latest/APIReference/API_ListEnabledControls.md "../../../controltower/latest/APIReference/API_ListEnabledControls.md") API)
- AWS CLI to see a list of enabled controls (run the [`list-enabled-controls`](../../../cli/latest/reference/controltower/list-enabled-controls.md "../../../cli/latest/reference/controltower/list-enabled-controls.md") command)

A control that you disable in AWS Control Tower has an enablement status of
`Disabled` in Security Hub CSPM unless you explicitly enable that control in
Security Hub CSPM.

Security Hub CSPM calculates control status based on the workflow status and compliance status of
the control findings. For more information about enablement status and control status,
see [Reviewing the details of controls in
Security Hub CSPM](securityhub-standards-control-details.md "securityhub-standards-control-details.md").

Based on control statuses, Security Hub CSPM calculates a [security score](standards-security-score.md "standards-security-score.md") for Service-Managed Standard: AWS Control Tower. This score is only available in Security Hub CSPM.
In addition, you can only view [control
findings](controls-findings-create-update.md "controls-findings-create-update.md") in Security Hub CSPM. The standard security score and control findings aren't
available in AWS Control Tower.

###### Note

When you enable controls for Service-Managed Standard: AWS Control Tower, Security Hub CSPM may take up to 18 hours to
generate findings for controls that use an existing AWS Config service-linked rule. You
may have existing service-linked rules if you've enabled other standards and
controls in Security Hub CSPM. For more information, see [Schedule for running security checks](securityhub-standards-schedule.md "securityhub-standards-schedule.md").

## Deleting the standard

You can delete this standard in AWS Control Tower by disabling all applicable controls using
one of the following methods:

- AWS Control Tower console
- AWS Control Tower API (call the [`DisableControl`](../../../controltower/latest/APIReference/API_DisableControl.md "../../../controltower/latest/APIReference/API_DisableControl.md") API)
- AWS CLI (run the [`disable-control`](../../../cli/latest/reference/controltower/disable-control.md "../../../cli/latest/reference/controltower/disable-control.md") command)

Disabling all controls deletes the standard in all managed accounts and governed
Regions in AWS Control Tower. Deleting the standard in AWS Control Tower removes it from the
**Standards** page of the Security Hub CSPM console, and you can no longer
access it by using the Security Hub CSPM API or AWS CLI.

###### Note

Disabling all controls from the standard in Security Hub CSPM doesn't disable or delete the
standard.

Disabling the Security Hub CSPM service removes Service-Managed Standard: AWS Control Tower and any other standards that
you’ve enabled.

## Finding field format for

Service-Managed Standard: AWS Control Tower

When you create Service-Managed Standard: AWS Control Tower and enable controls for it, you'll start to receive
control findings in Security Hub CSPM. Security Hub CSPM reports control findings in the [AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").
These are the ASFF values for this standard's Amazon Resource Name (ARN) and
`GeneratorId`:

- **Standard ARN** –
  ``arn:aws:us-east-1`:securityhub:::standards/service-managed-aws-control-tower/v/1.0.0`
- **GeneratorId** –
  `service-managed-aws-control-tower/v/1.0.0/`CodeBuild.1``

For a sample finding for Service-Managed Standard: AWS Control Tower, see [Samples of control findings](sample-control-findings.md "sample-control-findings.md").

## Controls that apply to

Service-Managed Standard: AWS Control Tower

Service-Managed Standard: AWS Control Tower supports a subset of controls that are part of the AWS Foundational Security Best Practices (FSBP) standard. Choose a control to view information about it, including remediation steps for failed findings.

The following list shows available controls for Service-Managed Standard: AWS Control Tower. Regional limits on
controls match Regional limits on the corollary controls in the FSBP standard. This list
shows standard-agnostic security control IDs. In the AWS Control Tower console, control IDs are
formatted as **SH.`ControlID`** (for example
**SH.CodeBuild.1**). In Security Hub CSPM, if [consolidated control findings](controls-findings-create-update.md#consolidated-control-findings "controls-findings-create-update.md#consolidated-control-findings") is
turned off in your account, the `ProductFields.ControlId` field uses the
standard-based control ID. The standard-based control ID is formatted as
**CT.`ControlId`** (for example,
**CT.CodeBuild.1**).

- [[Account.1] Security contact information should be provided for an AWS account](account-controls.md#account-1 "account-controls.md#account-1")
- [[ACM.1] Imported and ACM-issued certificates should be renewed after a specified time period](acm-controls.md#acm-1 "acm-controls.md#acm-1")
- [[ACM.2] RSA certificates managed by ACM should use a key length of at least 2,048 bits](acm-controls.md#acm-2 "acm-controls.md#acm-2")
- [[APIGateway.1] API Gateway REST and WebSocket API execution logging
  should be enabled](apigateway-controls.md#apigateway-1 "apigateway-controls.md#apigateway-1")
- [[APIGateway.2] API Gateway REST API stages should be configured to use
  SSL certificates for backend authentication](apigateway-controls.md#apigateway-2 "apigateway-controls.md#apigateway-2")
- [[APIGateway.3] API Gateway REST API stages should have AWS X-Ray
  tracing enabled](apigateway-controls.md#apigateway-3 "apigateway-controls.md#apigateway-3")
- [[APIGateway.4] API Gateway should be associated with a WAF Web
  ACL](apigateway-controls.md#apigateway-4 "apigateway-controls.md#apigateway-4")
- [[APIGateway.5] API Gateway REST API cache data should be encrypted at
  rest](apigateway-controls.md#apigateway-5 "apigateway-controls.md#apigateway-5")
- [[APIGateway.8] API Gateway routes should specify an authorization
  type](apigateway-controls.md#apigateway-8 "apigateway-controls.md#apigateway-8")
- [[APIGateway.9] Access logging should be configured for API Gateway V2
  Stages](apigateway-controls.md#apigateway-9 "apigateway-controls.md#apigateway-9")
- [[AppSync.5] AWS AppSync GraphQL APIs should not be authenticated with API keys](appsync-controls.md#appsync-5 "appsync-controls.md#appsync-5")
- [[AutoScaling.1] Amazon EC2 Auto Scaling groups associated with a load balancer should use ELB health checks](autoscaling-controls.md#autoscaling-1 "autoscaling-controls.md#autoscaling-1")
- [[AutoScaling.2] Amazon EC2 Auto Scaling group should cover multiple Availability Zones](autoscaling-controls.md#autoscaling-2 "autoscaling-controls.md#autoscaling-2")
- [[AutoScaling.3] Amazon EC2 Auto Scaling group launch configurations should configure EC2 instances to require Instance Metadata Service Version 2 (IMDSv2)](autoscaling-controls.md#autoscaling-3 "autoscaling-controls.md#autoscaling-3")
- [[Autoscaling.5] Amazon EC2 instances launched using Amazon EC2 Auto Scaling group launch configurations should not have Public IP addresses](autoscaling-controls.md#autoscaling-5 "autoscaling-controls.md#autoscaling-5")
- [[AutoScaling.6] Amazon EC2 Auto Scaling groups should use multiple instance types in multiple Availability Zones](autoscaling-controls.md#autoscaling-6 "autoscaling-controls.md#autoscaling-6")
- [[AutoScaling.9] Amazon EC2 Auto Scaling groups should use Amazon EC2 launch templates](autoscaling-controls.md#autoscaling-9 "autoscaling-controls.md#autoscaling-9")
- [[CloudTrail.1] CloudTrail should be enabled and configured with at least
  one multi-Region trail that includes read and write management events](cloudtrail-controls.md#cloudtrail-1 "cloudtrail-controls.md#cloudtrail-1")
- [[CloudTrail.2] CloudTrail should have encryption at-rest enabled](cloudtrail-controls.md#cloudtrail-2 "cloudtrail-controls.md#cloudtrail-2")
- [[CloudTrail.4] CloudTrail log file validation should be enabled](cloudtrail-controls.md#cloudtrail-4 "cloudtrail-controls.md#cloudtrail-4")
- [[CloudTrail.5] CloudTrail trails should be integrated with
  Amazon CloudWatch Logs](cloudtrail-controls.md#cloudtrail-5 "cloudtrail-controls.md#cloudtrail-5")
- [[CloudTrail.6] Ensure the S3 bucket used to store CloudTrail logs is not
  publicly accessible](cloudtrail-controls.md#cloudtrail-6 "cloudtrail-controls.md#cloudtrail-6")
- [[CodeBuild.1] CodeBuild Bitbucket source repository URLs should not contain sensitive credentials](codebuild-controls.md#codebuild-1 "codebuild-controls.md#codebuild-1")
- [[CodeBuild.2] CodeBuild project environment variables should not contain clear text credentials](codebuild-controls.md#codebuild-2 "codebuild-controls.md#codebuild-2")
- [[CodeBuild.3] CodeBuild S3 logs should be encrypted](codebuild-controls.md#codebuild-3 "codebuild-controls.md#codebuild-3")
- [[CodeBuild.4] CodeBuild project environments should have a logging AWS Configuration](codebuild-controls.md#codebuild-4 "codebuild-controls.md#codebuild-4")
- [[DMS.1] Database Migration Service replication instances should not be public](dms-controls.md#dms-1 "dms-controls.md#dms-1")
- [[DMS.9] DMS endpoints should use SSL](dms-controls.md#dms-9 "dms-controls.md#dms-9")
- [[DocumentDB.1] Amazon DocumentDB clusters should be encrypted at
  rest](documentdb-controls.md#documentdb-1 "documentdb-controls.md#documentdb-1")
- [[DocumentDB.2] Amazon DocumentDB clusters should have an adequate
  backup retention period](documentdb-controls.md#documentdb-2 "documentdb-controls.md#documentdb-2")
- [[DocumentDB.3] Amazon DocumentDB manual cluster snapshots should
  not be public](documentdb-controls.md#documentdb-3 "documentdb-controls.md#documentdb-3")
- [[DynamoDB.1] DynamoDB tables should automatically scale capacity with demand](dynamodb-controls.md#dynamodb-1 "dynamodb-controls.md#dynamodb-1")
- [[DynamoDB.2] DynamoDB tables should have point-in-time recovery enabled](dynamodb-controls.md#dynamodb-2 "dynamodb-controls.md#dynamodb-2")
- [[DynamoDB.3] DynamoDB Accelerator (DAX) clusters should be encrypted at rest](dynamodb-controls.md#dynamodb-3 "dynamodb-controls.md#dynamodb-3")
- [[EC2.1] Amazon EBS snapshots should not be publicly
  restorable](ec2-controls.md#ec2-1 "ec2-controls.md#ec2-1")
- [[EC2.2] VPC default security groups should not allow
  inbound or outbound traffic](ec2-controls.md#ec2-2 "ec2-controls.md#ec2-2")
- [[EC2.3] Attached Amazon EBS volumes should be encrypted
  at-rest](ec2-controls.md#ec2-3 "ec2-controls.md#ec2-3")
- [[EC2.4] Stopped EC2 instances should be removed
  after a specified time period](ec2-controls.md#ec2-4 "ec2-controls.md#ec2-4")
- [[EC2.6] VPC flow logging should be enabled in all
  VPCs](ec2-controls.md#ec2-6 "ec2-controls.md#ec2-6")
- [[EC2.7] EBS default encryption should be enabled](ec2-controls.md#ec2-7 "ec2-controls.md#ec2-7")
- [[EC2.8] EC2 instances should use Instance Metadata
  Service Version 2 (IMDSv2)](ec2-controls.md#ec2-8 "ec2-controls.md#ec2-8")
- [[EC2.9] Amazon EC2 instances should not have a public IPv4
  address](ec2-controls.md#ec2-9 "ec2-controls.md#ec2-9")
- [[EC2.10] Amazon EC2 should be configured to use VPC endpoints
  that are created for the Amazon EC2 service](ec2-controls.md#ec2-10 "ec2-controls.md#ec2-10")
- [[EC2.15] Amazon EC2 subnets should not automatically assign
  public IP addresses](ec2-controls.md#ec2-15 "ec2-controls.md#ec2-15")
- [[EC2.16] Unused Network Access Control Lists should be
  removed](ec2-controls.md#ec2-16 "ec2-controls.md#ec2-16")
- [[EC2.17] Amazon EC2 instances should not use multiple
  ENIs](ec2-controls.md#ec2-17 "ec2-controls.md#ec2-17")
- [[EC2.18] Security groups should only allow unrestricted
  incoming traffic for authorized ports](ec2-controls.md#ec2-18 "ec2-controls.md#ec2-18")
- [[EC2.19] Security groups should not allow unrestricted
  access to ports with high risk](ec2-controls.md#ec2-19 "ec2-controls.md#ec2-19")
- [[EC2.20] Both VPN tunnels for an AWS Site-to-Site VPN
  connection should be up](ec2-controls.md#ec2-20 "ec2-controls.md#ec2-20")
- [[EC2.21] Network ACLs should not allow ingress from
  0.0.0.0/0 to port 22 or port 3389](ec2-controls.md#ec2-21 "ec2-controls.md#ec2-21")
- [[EC2.22] Unused Amazon EC2 security groups should be
  removed](ec2-controls.md#ec2-22 "ec2-controls.md#ec2-22")
- [[EC2.23] Amazon EC2 Transit Gateways should not automatically
  accept VPC attachment requests](ec2-controls.md#ec2-23 "ec2-controls.md#ec2-23")
- [[EC2.25] Amazon EC2 launch templates should not assign public
  IPs to network interfaces](ec2-controls.md#ec2-25 "ec2-controls.md#ec2-25")
- [[ECR.1] ECR private repositories should have image scanning configured](ecr-controls.md#ecr-1 "ecr-controls.md#ecr-1")
- [[ECR.2] ECR private repositories should have tag immutability configured](ecr-controls.md#ecr-2 "ecr-controls.md#ecr-2")
- [[ECR.3] ECR repositories should have at least one lifecycle policy configured](ecr-controls.md#ecr-3 "ecr-controls.md#ecr-3")
- [[ECS.1] Amazon ECS task definitions should have secure networking modes and user
  definitions](ecs-controls.md#ecs-1 "ecs-controls.md#ecs-1")
- [[ECS.2] ECS services should not have public IP addresses assigned to them automatically](ecs-controls.md#ecs-2 "ecs-controls.md#ecs-2")
- [[ECS.3] ECS task definitions should not share the host's process namespace](ecs-controls.md#ecs-3 "ecs-controls.md#ecs-3")
- [[ECS.4] ECS containers should run as non-privileged](ecs-controls.md#ecs-4 "ecs-controls.md#ecs-4")
- [[ECS.5] ECS containers should be limited to read-only access to root filesystems](ecs-controls.md#ecs-5 "ecs-controls.md#ecs-5")
- [[ECS.8] Secrets should not be passed as container environment variables](ecs-controls.md#ecs-8 "ecs-controls.md#ecs-8")
- [[ECS.10] ECS Fargate services should run on the latest Fargate platform version](ecs-controls.md#ecs-10 "ecs-controls.md#ecs-10")
- [[ECS.12] ECS clusters should use Container Insights](ecs-controls.md#ecs-12 "ecs-controls.md#ecs-12")
- [[EFS.1] Elastic File System should be configured to encrypt file data at-rest using AWS KMS](efs-controls.md#efs-1 "efs-controls.md#efs-1")
- [[EFS.2] Amazon EFS volumes should be in backup plans](efs-controls.md#efs-2 "efs-controls.md#efs-2")
- [[EFS.3] EFS access points should enforce a root directory](efs-controls.md#efs-3 "efs-controls.md#efs-3")
- [[EFS.4] EFS access points should enforce a user identity](efs-controls.md#efs-4 "efs-controls.md#efs-4")
- [[EKS.1] EKS cluster endpoints should not be publicly accessible](eks-controls.md#eks-1 "eks-controls.md#eks-1")
- [[EKS.2] EKS clusters should run on a supported Kubernetes version](eks-controls.md#eks-2 "eks-controls.md#eks-2")
- [[ElastiCache.3] ElastiCache replication groups should have
  automatic failover enabled](elasticache-controls.md#elasticache-3 "elasticache-controls.md#elasticache-3")
- [[ElastiCache.4] ElastiCache replication groups should be encrypted
  at rest](elasticache-controls.md#elasticache-4 "elasticache-controls.md#elasticache-4")
- [[ElastiCache.5] ElastiCache replication groups should be encrypted
  in transit](elasticache-controls.md#elasticache-5 "elasticache-controls.md#elasticache-5")
- [[ElastiCache.6] ElastiCache (Redis OSS) replication groups of earlier versions
  should have Redis OSS AUTH enabled](elasticache-controls.md#elasticache-6 "elasticache-controls.md#elasticache-6")
- [[ElasticBeanstalk.1] Elastic Beanstalk environments should have enhanced health reporting enabled](elasticbeanstalk-controls.md#elasticbeanstalk-1 "elasticbeanstalk-controls.md#elasticbeanstalk-1")
- [[ElasticBeanstalk.2] Elastic Beanstalk managed platform updates should be enabled](elasticbeanstalk-controls.md#elasticbeanstalk-2 "elasticbeanstalk-controls.md#elasticbeanstalk-2")
- [[ELB.1] Application Load Balancer should be configured to redirect all HTTP requests
  to HTTPS](elb-controls.md#elb-1 "elb-controls.md#elb-1")
- [[ELB.2] Classic Load Balancers with SSL/HTTPS listeners should use a certificate
  provided by AWS Certificate Manager](elb-controls.md#elb-2 "elb-controls.md#elb-2")
- [[ELB.3] Classic Load Balancer listeners should be configured with HTTPS or TLS
  termination](elb-controls.md#elb-3 "elb-controls.md#elb-3")
- [[ELB.4] Application Load Balancer should be configured to drop invalid http
  headers](elb-controls.md#elb-4 "elb-controls.md#elb-4")
- [[ELB.5] Application and Classic Load Balancers logging should be enabled](elb-controls.md#elb-5 "elb-controls.md#elb-5")
- [[ELB.6] Application, Gateway, and Network Load Balancers should have deletion
  protection enabled](elb-controls.md#elb-6 "elb-controls.md#elb-6")
- [[ELB.7] Classic Load Balancers should have connection draining enabled](elb-controls.md#elb-7 "elb-controls.md#elb-7")
- [[ELB.8] Classic Load Balancers with SSL listeners should use a predefined
  security policy that has strong AWS Configuration](elb-controls.md#elb-8 "elb-controls.md#elb-8")
- [[ELB.9] Classic Load Balancers should have cross-zone load balancing
  enabled](elb-controls.md#elb-9 "elb-controls.md#elb-9")
- [[ELB.10] Classic Load Balancer should span multiple Availability Zones](elb-controls.md#elb-10 "elb-controls.md#elb-10")
- [[ELB.12] Application Load Balancer should be configured with defensive or strictest
  desync mitigation mode](elb-controls.md#elb-12 "elb-controls.md#elb-12")
- [[ELB.13] Application, Network and Gateway Load Balancers should span multiple
  Availability Zones](elb-controls.md#elb-13 "elb-controls.md#elb-13")
- [[ELB.14] Classic Load Balancer should be configured with defensive or strictest
  desync mitigation mode](elb-controls.md#elb-14 "elb-controls.md#elb-14")
- [[EMR.1] Amazon EMR cluster primary nodes should not have public IP addresses](emr-controls.md#emr-1 "emr-controls.md#emr-1")
- [[ES.1] Elasticsearch domains should have encryption at-rest enabled](es-controls.md#es-1 "es-controls.md#es-1")
- [[ES.2] Elasticsearch domains should not be publicly accessible](es-controls.md#es-2 "es-controls.md#es-2")
- [[ES.3] Elasticsearch domains should encrypt data sent between nodes](es-controls.md#es-3 "es-controls.md#es-3")
- [[ES.4] Elasticsearch domain error logging to CloudWatch Logs should be enabled](es-controls.md#es-4 "es-controls.md#es-4")
- [[ES.5] Elasticsearch domains should have audit logging enabled](es-controls.md#es-5 "es-controls.md#es-5")
- [[ES.6] Elasticsearch domains should have at least three data nodes](es-controls.md#es-6 "es-controls.md#es-6")
- [[ES.7] Elasticsearch domains should be configured with at least three dedicated master nodes](es-controls.md#es-7 "es-controls.md#es-7")
- [[ES.8] Connections to Elasticsearch domains should be encrypted using the latest TLS security policy](es-controls.md#es-8 "es-controls.md#es-8")
- [[EventBridge.3] EventBridge custom event buses should have a resource-based policy attached](eventbridge-controls.md#eventbridge-3 "eventbridge-controls.md#eventbridge-3")
- [[GuardDuty.1] GuardDuty should be enabled](guardduty-controls.md#guardduty-1 "guardduty-controls.md#guardduty-1")
- [[IAM.1] IAM policies should not allow full "\*" administrative privileges](iam-controls.md#iam-1 "iam-controls.md#iam-1")
- [[IAM.2] IAM users should not have IAM policies attached](iam-controls.md#iam-2 "iam-controls.md#iam-2")
- [[IAM.3] IAM users' access keys should be rotated every 90 days or less](iam-controls.md#iam-3 "iam-controls.md#iam-3")
- [[IAM.4] IAM root user access key should not exist](iam-controls.md#iam-4 "iam-controls.md#iam-4")
- [[IAM.5] MFA should be enabled for all IAM users that have a console password](iam-controls.md#iam-5 "iam-controls.md#iam-5")
- [[IAM.6] Hardware MFA should be enabled for the root user](iam-controls.md#iam-6 "iam-controls.md#iam-6")
- [[IAM.7] Password policies for IAM users should have strong configurations](iam-controls.md#iam-7 "iam-controls.md#iam-7")
- [[IAM.8] Unused IAM user credentials should be removed](iam-controls.md#iam-8 "iam-controls.md#iam-8")
- [[IAM.21] IAM customer managed policies that you create should not allow wildcard actions for services](iam-controls.md#iam-21 "iam-controls.md#iam-21")
- [[Kinesis.1] Kinesis streams should be encrypted at rest](kinesis-controls.md#kinesis-1 "kinesis-controls.md#kinesis-1")
- [[KMS.1] IAM customer managed policies should not allow decryption actions on all KMS keys](kms-controls.md#kms-1 "kms-controls.md#kms-1")
- [[KMS.2] IAM principals should not have IAM inline policies that allow decryption actions on all KMS keys](kms-controls.md#kms-2 "kms-controls.md#kms-2")
- [[KMS.3] AWS KMS keys should not be deleted unintentionally](kms-controls.md#kms-3 "kms-controls.md#kms-3")
- [[KMS.4] AWS KMS key rotation should be enabled](kms-controls.md#kms-4 "kms-controls.md#kms-4")
- [[Lambda.1] Lambda function policies should prohibit public
  access](lambda-controls.md#lambda-1 "lambda-controls.md#lambda-1")
- [[Lambda.2] Lambda functions should use supported
  runtimes](lambda-controls.md#lambda-2 "lambda-controls.md#lambda-2")
- [[Lambda.3] Lambda functions should be in a VPC](lambda-controls.md#lambda-3 "lambda-controls.md#lambda-3")
- [[Lambda.5] VPC Lambda functions should operate in multiple
  Availability Zones](lambda-controls.md#lambda-5 "lambda-controls.md#lambda-5")
- [[MSK.1] MSK clusters should be encrypted in transit among broker
  nodes](msk-controls.md#msk-1 "msk-controls.md#msk-1")
- [[MQ.5] ActiveMQ brokers should use active/standby deployment mode](mq-controls.md#mq-5 "mq-controls.md#mq-5")
- [[MQ.6] RabbitMQ brokers should use cluster deployment mode](mq-controls.md#mq-6 "mq-controls.md#mq-6")
- [[Neptune.1] Neptune DB clusters should be encrypted at
  rest](neptune-controls.md#neptune-1 "neptune-controls.md#neptune-1")
- [[Neptune.2] Neptune DB clusters should publish audit
  logs to CloudWatch Logs](neptune-controls.md#neptune-2 "neptune-controls.md#neptune-2")
- [[Neptune.3] Neptune DB cluster snapshots should not be
  public](neptune-controls.md#neptune-3 "neptune-controls.md#neptune-3")
- [[Neptune.4] Neptune DB clusters should have deletion
  protection enabled](neptune-controls.md#neptune-4 "neptune-controls.md#neptune-4")
- [[Neptune.5] Neptune DB clusters should have automated
  backups enabled](neptune-controls.md#neptune-5 "neptune-controls.md#neptune-5")
- [[Neptune.6] Neptune DB cluster snapshots should be
  encrypted at rest](neptune-controls.md#neptune-6 "neptune-controls.md#neptune-6")
- [[Neptune.7] Neptune DB clusters should have IAM
  database authentication enabled](neptune-controls.md#neptune-7 "neptune-controls.md#neptune-7")
- [[Neptune.8] Neptune DB clusters should be configured to
  copy tags to snapshots](neptune-controls.md#neptune-8 "neptune-controls.md#neptune-8")
- [[NetworkFirewall.3] Network Firewall policies should have at least one rule group associated](networkfirewall-controls.md#networkfirewall-3 "networkfirewall-controls.md#networkfirewall-3")
- [[NetworkFirewall.4] The default stateless action for Network Firewall policies should be drop or forward for full packets](networkfirewall-controls.md#networkfirewall-4 "networkfirewall-controls.md#networkfirewall-4")
- [[NetworkFirewall.5] The default stateless action for Network Firewall policies should be drop or forward for fragmented packets](networkfirewall-controls.md#networkfirewall-5 "networkfirewall-controls.md#networkfirewall-5")
- [[NetworkFirewall.6] Stateless Network Firewall rule group should not be empty](networkfirewall-controls.md#networkfirewall-6 "networkfirewall-controls.md#networkfirewall-6")
- [[Opensearch.1] OpenSearch domains should have encryption at rest enabled](opensearch-controls.md#opensearch-1 "opensearch-controls.md#opensearch-1")
- [[Opensearch.2] OpenSearch domains should not be publicly accessible](opensearch-controls.md#opensearch-2 "opensearch-controls.md#opensearch-2")
- [[Opensearch.3] OpenSearch domains should encrypt data sent between nodes](opensearch-controls.md#opensearch-3 "opensearch-controls.md#opensearch-3")
- [[Opensearch.4] OpenSearch domain error logging to CloudWatch Logs should be enabled](opensearch-controls.md#opensearch-4 "opensearch-controls.md#opensearch-4")
- [[Opensearch.5] OpenSearch domains should have audit logging enabled](opensearch-controls.md#opensearch-5 "opensearch-controls.md#opensearch-5")
- [[Opensearch.6] OpenSearch domains should have at least three data nodes](opensearch-controls.md#opensearch-6 "opensearch-controls.md#opensearch-6")
- [[Opensearch.7] OpenSearch domains should have fine-grained access control enabled](opensearch-controls.md#opensearch-7 "opensearch-controls.md#opensearch-7")
- [[Opensearch.8] Connections to OpenSearch domains should be encrypted using the latest TLS security policy](opensearch-controls.md#opensearch-8 "opensearch-controls.md#opensearch-8")
- [[RDS.1] RDS snapshot should be private](rds-controls.md#rds-1 "rds-controls.md#rds-1")
- [[RDS.2] RDS DB Instances should prohibit public access, as determined by the PubliclyAccessible configuration](rds-controls.md#rds-2 "rds-controls.md#rds-2")
- [[RDS.3] RDS DB instances should have encryption at-rest enabled](rds-controls.md#rds-3 "rds-controls.md#rds-3")
- [[RDS.4] RDS cluster snapshots and database snapshots should be encrypted at rest](rds-controls.md#rds-4 "rds-controls.md#rds-4")
- [[RDS.5] RDS DB instances should be configured with multiple Availability Zones](rds-controls.md#rds-5 "rds-controls.md#rds-5")
- [[RDS.6] Enhanced monitoring should be configured for RDS DB instances](rds-controls.md#rds-6 "rds-controls.md#rds-6")
- [[RDS.8] RDS DB instances should have deletion protection enabled](rds-controls.md#rds-8 "rds-controls.md#rds-8")
- [[RDS.9] RDS DB instances should publish logs to CloudWatch Logs](rds-controls.md#rds-9 "rds-controls.md#rds-9")
- [[RDS.10] IAM authentication should be configured for RDS instances](rds-controls.md#rds-10 "rds-controls.md#rds-10")
- [[RDS.11] RDS instances should have automatic backups enabled](rds-controls.md#rds-11 "rds-controls.md#rds-11")
- [[RDS.12] IAM authentication should be configured for RDS clusters](rds-controls.md#rds-12 "rds-controls.md#rds-12")
- [[RDS.13] RDS automatic minor version upgrades should be enabled](rds-controls.md#rds-13 "rds-controls.md#rds-13")
- [[RDS.15] RDS DB clusters should be configured for multiple Availability Zones](rds-controls.md#rds-15 "rds-controls.md#rds-15")
- [[RDS.17] RDS DB instances should be configured to copy tags to snapshots](rds-controls.md#rds-17 "rds-controls.md#rds-17")
- [[RDS.18] RDS instances should be deployed in a VPC](rds-controls.md#rds-18 "rds-controls.md#rds-18")
- [[RDS.19] Existing RDS event notification subscriptions should be configured for critical cluster events](rds-controls.md#rds-19 "rds-controls.md#rds-19")
- [[RDS.20] Existing RDS event notification subscriptions should be configured for critical database instance events](rds-controls.md#rds-20 "rds-controls.md#rds-20")
- [[RDS.21] An RDS event notifications subscription should be configured for critical database parameter group events](rds-controls.md#rds-21 "rds-controls.md#rds-21")
- [[RDS.22] An RDS event notifications subscription should be configured for critical database security group events](rds-controls.md#rds-22 "rds-controls.md#rds-22")
- [[RDS.23] RDS instances should not use a database engine default port](rds-controls.md#rds-23 "rds-controls.md#rds-23")
- [[RDS.25] RDS database instances should use a custom administrator username](rds-controls.md#rds-25 "rds-controls.md#rds-25")
- [[RDS.27] RDS DB clusters should be encrypted at rest](rds-controls.md#rds-27 "rds-controls.md#rds-27")
- [[Redshift.1] Amazon Redshift clusters should prohibit public access](redshift-controls.md#redshift-1 "redshift-controls.md#redshift-1")
- [[Redshift.2] Connections to Amazon Redshift clusters should be encrypted in transit](redshift-controls.md#redshift-2 "redshift-controls.md#redshift-2")
- [[Redshift.4] Amazon Redshift clusters should have audit logging enabled](redshift-controls.md#redshift-4 "redshift-controls.md#redshift-4")
- [[Redshift.6] Amazon Redshift should have automatic upgrades to major versions enabled](redshift-controls.md#redshift-6 "redshift-controls.md#redshift-6")
- [[Redshift.7] Redshift clusters should use enhanced VPC routing](redshift-controls.md#redshift-7 "redshift-controls.md#redshift-7")
- [[Redshift.8] Amazon Redshift clusters should not use the default Admin username](redshift-controls.md#redshift-8 "redshift-controls.md#redshift-8")
- [[Redshift.10] Redshift clusters should be encrypted at rest](redshift-controls.md#redshift-10 "redshift-controls.md#redshift-10")
- [[S3.1] S3 general purpose buckets should have block public access settings enabled](s3-controls.md#s3-1 "s3-controls.md#s3-1")
- [[S3.2] S3 general purpose buckets should block public read
  access](s3-controls.md#s3-2 "s3-controls.md#s3-2")
- [[S3.3] S3 general purpose buckets should block public write
  access](s3-controls.md#s3-3 "s3-controls.md#s3-3")
- [[S3.5] S3 general purpose buckets should require requests to use SSL](s3-controls.md#s3-5 "s3-controls.md#s3-5")
- [[S3.6] S3 general purpose bucket policies should restrict access to other AWS accounts](s3-controls.md#s3-6 "s3-controls.md#s3-6")
- [[S3.8] S3 general purpose buckets should block public access](s3-controls.md#s3-8 "s3-controls.md#s3-8")
- [[S3.9] S3 general purpose buckets should have server access logging enabled](s3-controls.md#s3-9 "s3-controls.md#s3-9")
- [[S3.12] ACLs should not be used to manage user access to S3 general purpose buckets](s3-controls.md#s3-12 "s3-controls.md#s3-12")
- [[S3.13] S3 general purpose buckets should have Lifecycle configurations](s3-controls.md#s3-13 "s3-controls.md#s3-13")
- [[S3.17] S3 general purpose buckets should be encrypted at rest with AWS KMS keys](s3-controls.md#s3-17 "s3-controls.md#s3-17")
- [[SageMaker.1] Amazon SageMaker notebook instances should not have
  direct internet access](sagemaker-controls.md#sagemaker-1 "sagemaker-controls.md#sagemaker-1")
- [[SageMaker.2] SageMaker notebook instances should be launched in a
  custom VPC](sagemaker-controls.md#sagemaker-2 "sagemaker-controls.md#sagemaker-2")
- [[SageMaker.3] Users should not have root access to SageMaker notebook
  instances](sagemaker-controls.md#sagemaker-3 "sagemaker-controls.md#sagemaker-3")
- [[SecretsManager.1] Secrets Manager secrets should have automatic rotation enabled](secretsmanager-controls.md#secretsmanager-1 "secretsmanager-controls.md#secretsmanager-1")
- [[SecretsManager.2] Secrets Manager secrets configured with automatic rotation should rotate successfully](secretsmanager-controls.md#secretsmanager-2 "secretsmanager-controls.md#secretsmanager-2")
- [[SecretsManager.3] Remove unused Secrets Manager secrets](secretsmanager-controls.md#secretsmanager-3 "secretsmanager-controls.md#secretsmanager-3")
- [[SecretsManager.4] Secrets Manager secrets should be rotated within a specified number of days](secretsmanager-controls.md#secretsmanager-4 "secretsmanager-controls.md#secretsmanager-4")
- [[SQS.1] Amazon SQS queues should be encrypted at rest](sqs-controls.md#sqs-1 "sqs-controls.md#sqs-1")
- [[SSM.1] Amazon EC2 instances should be managed by AWS Systems Manager](ssm-controls.md#ssm-1 "ssm-controls.md#ssm-1")
- [[SSM.2] Amazon EC2 instances managed by Systems Manager should have a patch
  compliance status of COMPLIANT after a patch installation](ssm-controls.md#ssm-2 "ssm-controls.md#ssm-2")
- [[SSM.3] Amazon EC2 instances managed by Systems Manager should have an
  association compliance status of COMPLIANT](ssm-controls.md#ssm-3 "ssm-controls.md#ssm-3")
- [[SSM.4] SSM documents should not be public](ssm-controls.md#ssm-4 "ssm-controls.md#ssm-4")
- [[WAF.2] AWS WAF Classic Regional rules should have at least one condition](waf-controls.md#waf-2 "waf-controls.md#waf-2")
- [[WAF.3] AWS WAF Classic Regional rule groups should have at least one rule](waf-controls.md#waf-3 "waf-controls.md#waf-3")
- [[WAF.4] AWS WAF Classic Regional web ACLs should have at least one rule or rule group](waf-controls.md#waf-4 "waf-controls.md#waf-4")
- [[WAF.10] AWS WAF web ACLs should have at least one rule or rule group](waf-controls.md#waf-10 "waf-controls.md#waf-10")

For more information about this standard, see [Security Hub CSPM
controls](../../../controltower/latest/userguide/security-hub-controls.md "../../../controltower/latest/userguide/security-hub-controls.md") in the _AWS Control Tower User Guide_.
