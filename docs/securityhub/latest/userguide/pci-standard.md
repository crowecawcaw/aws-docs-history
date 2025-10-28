# PCI DSS in Security Hub CSPM

The Payment Card Industry Data Security Standard (PCI DSS) is a third-party compliance
framework that provides a set of rules and guidelines for safely handling credit and
debit card information. The PCI Security Standards Council (SSC) creates and updates
this framework.

AWS Security Hub CSPM provides a PCI DSS standard that can help you stay compliant with this
third-party framework. You can use this standard to discover security vulnerabilities in
AWS resources that handle cardholder data. We recommend enabling this standard in
AWS accounts that have resources that store, process, or transmit cardholder data or
sensitive authentication data. Assessments by the PCI SSC validated this
standard.

Security Hub CSPM offers support for both PCI DSS v3.2.1 and PCI DSS v4.0.1. We recommend using v4.0.1 to stay
current with security best practices. You can have both versions of the standard enabled
at the same time. For information about enabling standards, see [Enabling a security standard](enable-standards.md "enable-standards.md"). If you currently use
v3.2.1 but want to use only v4.0.1, enable the newer version before disabling the older
version. This prevents gaps in your security checks. If you use the Security Hub CSPM integration
with AWS Organizations and want to batch enable v4.0.1 in multiple accounts, we recommend using
[central configuration](central-configuration-intro.md "central-configuration-intro.md") to do
so.

The following sections specify which controls apply to PCI DSS v3.2.1 and PCI DSS v4.0.1.

## Controls that apply to PCI DSS v3.2.1

The following list specifies which Security Hub CSPM controls apply to PCI DSS v3.2.1. To review the
details of a control, choose the control.

[[AutoScaling.1] Auto Scaling groups associated with a load balancer should use ELB health checks](autoscaling-controls.md#autoscaling-1 "autoscaling-controls.md#autoscaling-1")

[[CloudTrail.2] CloudTrail should have encryption at-rest enabled](cloudtrail-controls.md#cloudtrail-2 "cloudtrail-controls.md#cloudtrail-2")

[[CloudTrail.3] At least one CloudTrail trail should be enabled](cloudtrail-controls.md#cloudtrail-3 "cloudtrail-controls.md#cloudtrail-3")

[[CloudTrail.4] CloudTrail log file validation should be enabled](cloudtrail-controls.md#cloudtrail-4 "cloudtrail-controls.md#cloudtrail-4")

[[CloudTrail.5] CloudTrail trails should be integrated with
Amazon CloudWatch Logs](cloudtrail-controls.md#cloudtrail-5 "cloudtrail-controls.md#cloudtrail-5")

[[CloudWatch.1] A log metric filter and alarm should exist for usage of the "root" user](cloudwatch-controls.md#cloudwatch-1 "cloudwatch-controls.md#cloudwatch-1")

[[CodeBuild.1] CodeBuild Bitbucket source repository URLs should not contain sensitive credentials](codebuild-controls.md#codebuild-1 "codebuild-controls.md#codebuild-1")

[[CodeBuild.2] CodeBuild project environment variables should not contain clear text credentials](codebuild-controls.md#codebuild-2 "codebuild-controls.md#codebuild-2")

[[Config.1] AWS Config should be enabled and use the service-linked role for resource recording](config-controls.md#config-1 "config-controls.md#config-1")

[[DMS.1] Database Migration Service replication instances should not be public](dms-controls.md#dms-1 "dms-controls.md#dms-1")

[[EC2.1] Amazon EBS snapshots should not be publicly
restorable](ec2-controls.md#ec2-1 "ec2-controls.md#ec2-1")

[[EC2.2] VPC default security groups should not allow
inbound or outbound traffic](ec2-controls.md#ec2-2 "ec2-controls.md#ec2-2")

[[EC2.6] VPC flow logging should be enabled in all
VPCs](ec2-controls.md#ec2-6 "ec2-controls.md#ec2-6")

[[EC2.12] Unused Amazon EC2 EIPs should be removed](ec2-controls.md#ec2-12 "ec2-controls.md#ec2-12")

[[EC2.13] Security groups should not allow ingress from
0.0.0.0/0 or ::/0 to port 22](ec2-controls.md#ec2-13 "ec2-controls.md#ec2-13")

[[ELB.1] Application Load Balancer should be configured to redirect all HTTP requests
to HTTPS](elb-controls.md#elb-1 "elb-controls.md#elb-1")

[[ES.1] Elasticsearch domains should have encryption at-rest enabled](es-controls.md#es-1 "es-controls.md#es-1")

[[ES.2] Elasticsearch domains should not be publicly accessible](es-controls.md#es-2 "es-controls.md#es-2")

[[GuardDuty.1] GuardDuty should be enabled](guardduty-controls.md#guardduty-1 "guardduty-controls.md#guardduty-1")

[[IAM.1] IAM policies should not allow full "\*" administrative privileges](iam-controls.md#iam-1 "iam-controls.md#iam-1")

[[IAM.2] IAM users should not have IAM policies attached](iam-controls.md#iam-2 "iam-controls.md#iam-2")

[[IAM.4] IAM root user access key should not exist](iam-controls.md#iam-4 "iam-controls.md#iam-4")

[[IAM.6] Hardware MFA should be enabled for the root user](iam-controls.md#iam-6 "iam-controls.md#iam-6")

[[IAM.8] Unused IAM user credentials should be removed](iam-controls.md#iam-8 "iam-controls.md#iam-8")

[[IAM.9] MFA should be enabled for the root user](iam-controls.md#iam-9 "iam-controls.md#iam-9")

[[IAM.10] Password policies for IAM users should have strong
configurations](iam-controls.md#iam-10 "iam-controls.md#iam-10")

[[IAM.19] MFA should be enabled for all IAM users](iam-controls.md#iam-19 "iam-controls.md#iam-19")

[[KMS.4] AWS KMS key rotation should be enabled](kms-controls.md#kms-4 "kms-controls.md#kms-4")

[[Lambda.1] Lambda function policies should prohibit public
access](lambda-controls.md#lambda-1 "lambda-controls.md#lambda-1")

[[Lambda.3] Lambda functions should be in a VPC](lambda-controls.md#lambda-3 "lambda-controls.md#lambda-3")

[[Opensearch.1] OpenSearch domains should have encryption at rest enabled](opensearch-controls.md#opensearch-1 "opensearch-controls.md#opensearch-1")

[[Opensearch.2] OpenSearch domains should not be publicly accessible](opensearch-controls.md#opensearch-2 "opensearch-controls.md#opensearch-2")

[[RDS.1] RDS snapshot should be private](rds-controls.md#rds-1 "rds-controls.md#rds-1")

[[RDS.2] RDS DB Instances should prohibit public access, as determined by the PubliclyAccessible configuration](rds-controls.md#rds-2 "rds-controls.md#rds-2")

[[Redshift.1] Amazon Redshift clusters should prohibit public access](redshift-controls.md#redshift-1 "redshift-controls.md#redshift-1")

[[S3.1] S3 general purpose buckets should have block public access settings enabled](s3-controls.md#s3-1 "s3-controls.md#s3-1")

[[S3.2] S3 general purpose buckets should block public read
access](s3-controls.md#s3-2 "s3-controls.md#s3-2")

[[S3.3] S3 general purpose buckets should block public write
access](s3-controls.md#s3-3 "s3-controls.md#s3-3")

[[S3.5] S3 general purpose buckets should require requests to use SSL](s3-controls.md#s3-5 "s3-controls.md#s3-5")

[[S3.7] S3 general purpose buckets should use cross-Region replication](s3-controls.md#s3-7 "s3-controls.md#s3-7")

[[SageMaker.1] Amazon SageMaker notebook instances should not have
direct internet access](sagemaker-controls.md#sagemaker-1 "sagemaker-controls.md#sagemaker-1")

[[SSM.1] Amazon EC2 instances should be managed by AWS Systems Manager](ssm-controls.md#ssm-1 "ssm-controls.md#ssm-1")

[[SSM.2] Amazon EC2 instances managed by Systems Manager should have a patch
compliance status of COMPLIANT after a patch installation](ssm-controls.md#ssm-2 "ssm-controls.md#ssm-2")

[[SSM.3] Amazon EC2 instances managed by Systems Manager should have an
association compliance status of COMPLIANT](ssm-controls.md#ssm-3 "ssm-controls.md#ssm-3")

## Controls that apply to PCI DSS v4.0.1

The following list specifies which Security Hub CSPM controls apply to PCI DSS v4.0.1. To review the
details of a control, choose the control.

[[ACM.1] Imported and ACM-issued certificates should be renewed after a specified time period](acm-controls.md#acm-1 "acm-controls.md#acm-1")

[[ACM.2] RSA certificates managed by ACM should use a key length of at least 2,048 bits](acm-controls.md#acm-2 "acm-controls.md#acm-2")

[[APIGateway.9] Access logging should be configured for API Gateway V2
Stages](apigateway-controls.md#apigateway-9 "apigateway-controls.md#apigateway-9")

[[AppSync.2] AWS AppSync should have field-level logging enabled](appsync-controls.md#appsync-2 "appsync-controls.md#appsync-2")

[[AutoScaling.3] Auto Scaling group launch configurations should configure EC2 instances to require Instance Metadata Service Version 2 (IMDSv2)](autoscaling-controls.md#autoscaling-3 "autoscaling-controls.md#autoscaling-3")

[[Autoscaling.5] Amazon EC2 instances launched using Auto Scaling group launch configurations should not have Public IP addresses](autoscaling-controls.md#autoscaling-5 "autoscaling-controls.md#autoscaling-5")

[[CloudFront.1] CloudFront distributions should have a default
root object configured](cloudfront-controls.md#cloudfront-1 "cloudfront-controls.md#cloudfront-1")

[[CloudFront.10] CloudFront distributions should not use
deprecated SSL protocols between edge locations and custom origins](cloudfront-controls.md#cloudfront-10 "cloudfront-controls.md#cloudfront-10")

[[CloudFront.12] CloudFront distributions should not point to
non-existent S3 origins](cloudfront-controls.md#cloudfront-12 "cloudfront-controls.md#cloudfront-12")

[[CloudFront.3] CloudFront distributions should require
encryption in transit](cloudfront-controls.md#cloudfront-3 "cloudfront-controls.md#cloudfront-3")

[[CloudFront.5] CloudFront distributions should have logging
enabled](cloudfront-controls.md#cloudfront-5 "cloudfront-controls.md#cloudfront-5")

[[CloudFront.6] CloudFront distributions should have WAF
enabled](cloudfront-controls.md#cloudfront-6 "cloudfront-controls.md#cloudfront-6")

[[CloudFront.9] CloudFront distributions should encrypt traffic
to custom origins](cloudfront-controls.md#cloudfront-9 "cloudfront-controls.md#cloudfront-9")

[[CloudTrail.2] CloudTrail should have encryption at-rest enabled](cloudtrail-controls.md#cloudtrail-2 "cloudtrail-controls.md#cloudtrail-2")

[[CloudTrail.3] At least one CloudTrail trail should be enabled](cloudtrail-controls.md#cloudtrail-3 "cloudtrail-controls.md#cloudtrail-3")

[[CloudTrail.4] CloudTrail log file validation should be enabled](cloudtrail-controls.md#cloudtrail-4 "cloudtrail-controls.md#cloudtrail-4")

[[CloudTrail.6] Ensure the S3 bucket used to store CloudTrail logs is not
publicly accessible](cloudtrail-controls.md#cloudtrail-6 "cloudtrail-controls.md#cloudtrail-6")

[[CloudTrail.7] Ensure S3 bucket access logging is enabled on the CloudTrail
S3 bucket](cloudtrail-controls.md#cloudtrail-7 "cloudtrail-controls.md#cloudtrail-7")

[[CodeBuild.1] CodeBuild Bitbucket source repository URLs should not contain sensitive credentials](codebuild-controls.md#codebuild-1 "codebuild-controls.md#codebuild-1")

[[CodeBuild.2] CodeBuild project environment variables should not contain clear text credentials](codebuild-controls.md#codebuild-2 "codebuild-controls.md#codebuild-2")

[[CodeBuild.3] CodeBuild S3 logs should be encrypted](codebuild-controls.md#codebuild-3 "codebuild-controls.md#codebuild-3")

[[DMS.1] Database Migration Service replication instances should not be public](dms-controls.md#dms-1 "dms-controls.md#dms-1")

[[DMS.10] DMS endpoints for Neptune databases should have IAM authorization enabled](dms-controls.md#dms-10 "dms-controls.md#dms-10")

[[DMS.11] DMS endpoints for MongoDB should have an authentication mechanism enabled](dms-controls.md#dms-11 "dms-controls.md#dms-11")

[[DMS.12] DMS endpoints for Redis OSS should have TLS enabled](dms-controls.md#dms-12 "dms-controls.md#dms-12")

[[DMS.6] DMS replication instances should have automatic minor version upgrade enabled](dms-controls.md#dms-6 "dms-controls.md#dms-6")

[[DMS.7] DMS replication tasks for the target database should have logging enabled](dms-controls.md#dms-7 "dms-controls.md#dms-7")

[[DMS.8] DMS replication tasks for the source database should have logging enabled](dms-controls.md#dms-8 "dms-controls.md#dms-8")

[[DMS.9] DMS endpoints should use SSL](dms-controls.md#dms-9 "dms-controls.md#dms-9")

[[DocumentDB.2] Amazon DocumentDB clusters should have an adequate
backup retention period](documentdb-controls.md#documentdb-2 "documentdb-controls.md#documentdb-2")

[[DocumentDB.3] Amazon DocumentDB manual cluster snapshots should
not be public](documentdb-controls.md#documentdb-3 "documentdb-controls.md#documentdb-3")

[[DocumentDB.4] Amazon DocumentDB clusters should publish audit
logs to CloudWatch Logs](documentdb-controls.md#documentdb-4 "documentdb-controls.md#documentdb-4")

[[DynamoDB.7] DynamoDB Accelerator clusters should be encrypted in transit](dynamodb-controls.md#dynamodb-7 "dynamodb-controls.md#dynamodb-7")

[[EC2.13] Security groups should not allow ingress from
0.0.0.0/0 or ::/0 to port 22](ec2-controls.md#ec2-13 "ec2-controls.md#ec2-13")

[[EC2.14] Security groups should not allow ingress from
0.0.0.0/0 or ::/0 to port 3389](ec2-controls.md#ec2-14 "ec2-controls.md#ec2-14")

[[EC2.15] Amazon EC2 subnets should not automatically assign
public IP addresses](ec2-controls.md#ec2-15 "ec2-controls.md#ec2-15")

[[EC2.16] Unused Network Access Control Lists should be
removed](ec2-controls.md#ec2-16 "ec2-controls.md#ec2-16")

[[EC2.170] EC2 launch templates should use Instance
Metadata Service Version 2 (IMDSv2)](ec2-controls.md#ec2-170 "ec2-controls.md#ec2-170")

[[EC2.171] EC2 VPN connections should have logging
enabled](ec2-controls.md#ec2-171 "ec2-controls.md#ec2-171")

[[EC2.21] Network ACLs should not allow ingress from
0.0.0.0/0 to port 22 or port 3389](ec2-controls.md#ec2-21 "ec2-controls.md#ec2-21")

[[EC2.25] Amazon EC2 launch templates should not assign public
IPs to network interfaces](ec2-controls.md#ec2-25 "ec2-controls.md#ec2-25")

[[EC2.51] EC2 Client VPN endpoints should have client
connection logging enabled](ec2-controls.md#ec2-51 "ec2-controls.md#ec2-51")

[[EC2.53] EC2 security groups should not allow
ingress from 0.0.0.0/0 to remote server administration ports](ec2-controls.md#ec2-53 "ec2-controls.md#ec2-53")

[[EC2.54] EC2 security groups should not allow
ingress from ::/0 to remote server administration ports](ec2-controls.md#ec2-54 "ec2-controls.md#ec2-54")

[[EC2.8] EC2 instances should use Instance Metadata
Service Version 2 (IMDSv2)](ec2-controls.md#ec2-8 "ec2-controls.md#ec2-8")

[[ECR.1] ECR private repositories should have image scanning configured](ecr-controls.md#ecr-1 "ecr-controls.md#ecr-1")

[[ECS.10] ECS Fargate services should run on the latest Fargate platform version](ecs-controls.md#ecs-10 "ecs-controls.md#ecs-10")

[[ECS.16] ECS task sets should not automatically assign public IP addresses](ecs-controls.md#ecs-16 "ecs-controls.md#ecs-16")

[[ECS.2] ECS services should not have public IP addresses assigned to them automatically](ecs-controls.md#ecs-2 "ecs-controls.md#ecs-2")

[[ECS.8] Secrets should not be passed as container environment variables](ecs-controls.md#ecs-8 "ecs-controls.md#ecs-8")

[[EFS.4] EFS access points should enforce a user identity](efs-controls.md#efs-4 "efs-controls.md#efs-4")

[[EKS.1] EKS cluster endpoints should not be publicly accessible](eks-controls.md#eks-1 "eks-controls.md#eks-1")

[[EKS.2] EKS clusters should run on a supported Kubernetes version](eks-controls.md#eks-2 "eks-controls.md#eks-2")

[[EKS.3] EKS clusters should use encrypted Kubernetes secrets](eks-controls.md#eks-3 "eks-controls.md#eks-3")

[[EKS.8] EKS clusters should have audit logging enabled](eks-controls.md#eks-8 "eks-controls.md#eks-8")

[[ElastiCache.2] ElastiCache clusters should have automatic minor
version upgrades enabled](elasticache-controls.md#elasticache-2 "elasticache-controls.md#elasticache-2")

[[ElastiCache.5] ElastiCache replication groups should be encrypted
in transit](elasticache-controls.md#elasticache-5 "elasticache-controls.md#elasticache-5")

[[ElastiCache.6] ElastiCache (Redis OSS) replication groups of earlier versions
should have Redis OSS AUTH enabled](elasticache-controls.md#elasticache-6 "elasticache-controls.md#elasticache-6")

[[ElasticBeanstalk.2] Elastic Beanstalk managed platform updates should be enabled](elasticbeanstalk-controls.md#elasticbeanstalk-2 "elasticbeanstalk-controls.md#elasticbeanstalk-2")

[[ElasticBeanstalk.3] Elastic Beanstalk should stream logs to CloudWatch](elasticbeanstalk-controls.md#elasticbeanstalk-3 "elasticbeanstalk-controls.md#elasticbeanstalk-3")

[[ELB.12] Application Load Balancer should be configured with defensive or strictest
desync mitigation mode](elb-controls.md#elb-12 "elb-controls.md#elb-12")

[[ELB.14] Classic Load Balancer should be configured with defensive or strictest
desync mitigation mode](elb-controls.md#elb-14 "elb-controls.md#elb-14")

[[ELB.3] Classic Load Balancer listeners should be configured with HTTPS or TLS
termination](elb-controls.md#elb-3 "elb-controls.md#elb-3")

[[ELB.4] Application Load Balancer should be configured to drop invalid http
headers](elb-controls.md#elb-4 "elb-controls.md#elb-4")

[[ELB.8] Classic Load Balancers with SSL listeners should use a predefined
security policy that has strong AWS Configuration](elb-controls.md#elb-8 "elb-controls.md#elb-8")

[[EMR.1] Amazon EMR cluster primary nodes should not have public IP addresses](emr-controls.md#emr-1 "emr-controls.md#emr-1")

[[EMR.2] Amazon EMR block public access setting should be enabled](emr-controls.md#emr-2 "emr-controls.md#emr-2")

[[ES.2] Elasticsearch domains should not be publicly accessible](es-controls.md#es-2 "es-controls.md#es-2")

[[ES.3] Elasticsearch domains should encrypt data sent between nodes](es-controls.md#es-3 "es-controls.md#es-3")

[[ES.5] Elasticsearch domains should have audit logging enabled](es-controls.md#es-5 "es-controls.md#es-5")

[[ES.8] Connections to Elasticsearch domains should be encrypted using the latest TLS security policy](es-controls.md#es-8 "es-controls.md#es-8")

[[EventBridge.3] EventBridge custom event buses should have a resource-based policy attached](eventbridge-controls.md#eventbridge-3 "eventbridge-controls.md#eventbridge-3")

[[GuardDuty.1] GuardDuty should be enabled](guardduty-controls.md#guardduty-1 "guardduty-controls.md#guardduty-1")

[[GuardDuty.10] GuardDuty S3 Protection should be enabled](guardduty-controls.md#guardduty-10 "guardduty-controls.md#guardduty-10")

[[GuardDuty.6] GuardDuty Lambda Protection should be enabled](guardduty-controls.md#guardduty-6 "guardduty-controls.md#guardduty-6")

[[GuardDuty.7] GuardDuty EKS Runtime Monitoring should be enabled](guardduty-controls.md#guardduty-7 "guardduty-controls.md#guardduty-7")

[[GuardDuty.9] GuardDuty RDS Protection should be enabled](guardduty-controls.md#guardduty-9 "guardduty-controls.md#guardduty-9")

[[IAM.3] IAM users' access keys should be rotated every 90 days or less](iam-controls.md#iam-3 "iam-controls.md#iam-3")

[[IAM.5] MFA should be enabled for all IAM users that have a console password](iam-controls.md#iam-5 "iam-controls.md#iam-5")

[[IAM.6] Hardware MFA should be enabled for the root user](iam-controls.md#iam-6 "iam-controls.md#iam-6")

[[IAM.7] Password policies for IAM users should have strong configurations](iam-controls.md#iam-7 "iam-controls.md#iam-7")

[[IAM.8] Unused IAM user credentials should be removed](iam-controls.md#iam-8 "iam-controls.md#iam-8")

[[IAM.9] MFA should be enabled for the root user](iam-controls.md#iam-9 "iam-controls.md#iam-9")

[[IAM.11] Ensure IAM password policy requires at least one uppercase letter](iam-controls.md#iam-11 "iam-controls.md#iam-11")

[[IAM.12] Ensure IAM password policy requires at least one lowercase letter](iam-controls.md#iam-12 "iam-controls.md#iam-12")

[[IAM.14] Ensure IAM password policy requires at least one number](iam-controls.md#iam-14 "iam-controls.md#iam-14")

[[IAM.16] Ensure IAM password policy prevents password reuse](iam-controls.md#iam-16 "iam-controls.md#iam-16")

[[IAM.17] Ensure IAM password policy expires passwords within 90 days or less](iam-controls.md#iam-17 "iam-controls.md#iam-17")

[[IAM.18] Ensure a support role has been created to manage incidents with
AWS Support](iam-controls.md#iam-18 "iam-controls.md#iam-18")

[[IAM.19] MFA should be enabled for all IAM users](iam-controls.md#iam-19 "iam-controls.md#iam-19")

[[Inspector.1] Amazon Inspector EC2 scanning should be enabled](inspector-controls.md#inspector-1 "inspector-controls.md#inspector-1")

[[Inspector.2] Amazon Inspector ECR scanning should be enabled](inspector-controls.md#inspector-2 "inspector-controls.md#inspector-2")

[[Inspector.3] Amazon Inspector Lambda code scanning should be enabled](inspector-controls.md#inspector-3 "inspector-controls.md#inspector-3")

[[Inspector.4] Amazon Inspector Lambda standard scanning should be enabled](inspector-controls.md#inspector-4 "inspector-controls.md#inspector-4")

[[KMS.4] AWS KMS key rotation should be enabled](kms-controls.md#kms-4 "kms-controls.md#kms-4")

[[Lambda.1] Lambda function policies should prohibit public
access](lambda-controls.md#lambda-1 "lambda-controls.md#lambda-1")

[[Lambda.2] Lambda functions should use supported
runtimes](lambda-controls.md#lambda-2 "lambda-controls.md#lambda-2")

[[MQ.2] ActiveMQ brokers should stream audit logs to CloudWatch](mq-controls.md#mq-2 "mq-controls.md#mq-2")

[[MQ.3] Amazon MQ brokers should have automatic minor version upgrade enabled](mq-controls.md#mq-3 "mq-controls.md#mq-3")

[[MSK.1] MSK clusters should be encrypted in transit among broker
nodes](msk-controls.md#msk-1 "msk-controls.md#msk-1")

[[MSK.3] MSK Connect connectors should be encrypted in
transit](msk-controls.md#msk-3 "msk-controls.md#msk-3")

[[Neptune.2] Neptune DB clusters should publish audit
logs to CloudWatch Logs](neptune-controls.md#neptune-2 "neptune-controls.md#neptune-2")

[[Neptune.3] Neptune DB cluster snapshots should not be
public](neptune-controls.md#neptune-3 "neptune-controls.md#neptune-3")

[[Opensearch.10] OpenSearch domains should have the latest software update installed](opensearch-controls.md#opensearch-10 "opensearch-controls.md#opensearch-10")

[[Opensearch.5] OpenSearch domains should have audit logging enabled](opensearch-controls.md#opensearch-5 "opensearch-controls.md#opensearch-5")

[[RDS.13] RDS automatic minor version upgrades should be enabled](rds-controls.md#rds-13 "rds-controls.md#rds-13")

[[RDS.2] RDS DB Instances should prohibit public access, as determined by the PubliclyAccessible configuration](rds-controls.md#rds-2 "rds-controls.md#rds-2")

[[RDS.20] Existing RDS event notification subscriptions should be configured for critical database instance events](rds-controls.md#rds-20 "rds-controls.md#rds-20")

[[RDS.21] An RDS event notifications subscription should be configured for critical database parameter group events](rds-controls.md#rds-21 "rds-controls.md#rds-21")

[[RDS.22] An RDS event notifications subscription should be configured for critical database security group events](rds-controls.md#rds-22 "rds-controls.md#rds-22")

[[RDS.24] RDS Database clusters should use a custom administrator username](rds-controls.md#rds-24 "rds-controls.md#rds-24")

[[RDS.25] RDS database instances should use a custom administrator username](rds-controls.md#rds-25 "rds-controls.md#rds-25")

[[RDS.34] Aurora MySQL DB clusters should publish audit logs to CloudWatch Logs](rds-controls.md#rds-34 "rds-controls.md#rds-34")

[[RDS.35] RDS DB clusters should have automatic minor version upgrade enabled](rds-controls.md#rds-35 "rds-controls.md#rds-35")

[[RDS.36] RDS for PostgreSQL DB instances should publish logs to CloudWatch Logs](rds-controls.md#rds-36 "rds-controls.md#rds-36")

[[RDS.37] Aurora PostgreSQL DB clusters should publish logs to CloudWatch Logs](rds-controls.md#rds-37 "rds-controls.md#rds-37")

[[RDS.9] RDS DB instances should publish logs to CloudWatch Logs](rds-controls.md#rds-9 "rds-controls.md#rds-9")

[[Redshift.1] Amazon Redshift clusters should prohibit public access](redshift-controls.md#redshift-1 "redshift-controls.md#redshift-1")

[[Redshift.15] Redshift security groups should allow ingress on the cluster port only from restricted origins](redshift-controls.md#redshift-15 "redshift-controls.md#redshift-15")

[[Redshift.2] Connections to Amazon Redshift clusters should be encrypted in transit](redshift-controls.md#redshift-2 "redshift-controls.md#redshift-2")

[[Redshift.4] Amazon Redshift clusters should have audit logging enabled](redshift-controls.md#redshift-4 "redshift-controls.md#redshift-4")

[[Route53.2] Route 53 public hosted zones should log DNS queries](route53-controls.md#route53-2 "route53-controls.md#route53-2")

[[S3.1] S3 general purpose buckets should have block public access settings enabled](s3-controls.md#s3-1 "s3-controls.md#s3-1")

[[S3.15] S3 general purpose buckets should have Object Lock enabled](s3-controls.md#s3-15 "s3-controls.md#s3-15")

[[S3.17] S3 general purpose buckets should be encrypted at rest with AWS KMS keys](s3-controls.md#s3-17 "s3-controls.md#s3-17")

[[S3.19] S3 access points should have block public access settings enabled](s3-controls.md#s3-19 "s3-controls.md#s3-19")

[[S3.22] S3 general purpose buckets should log object-level write events](s3-controls.md#s3-22 "s3-controls.md#s3-22")

[[S3.23] S3 general purpose buckets should log object-level read events](s3-controls.md#s3-23 "s3-controls.md#s3-23")

[[S3.24] S3 Multi-Region Access Points should have block public access settings enabled](s3-controls.md#s3-24 "s3-controls.md#s3-24")

[[S3.5] S3 general purpose buckets should require requests to use SSL](s3-controls.md#s3-5 "s3-controls.md#s3-5")

[[S3.8] S3 general purpose buckets should block public access](s3-controls.md#s3-8 "s3-controls.md#s3-8")

[[S3.9] S3 general purpose buckets should have server access logging enabled](s3-controls.md#s3-9 "s3-controls.md#s3-9")

[[SageMaker.1] Amazon SageMaker notebook instances should not have
direct internet access](sagemaker-controls.md#sagemaker-1 "sagemaker-controls.md#sagemaker-1")

[[SecretsManager.1] Secrets Manager secrets should have automatic rotation enabled](secretsmanager-controls.md#secretsmanager-1 "secretsmanager-controls.md#secretsmanager-1")

[[SecretsManager.2] Secrets Manager secrets configured with automatic rotation should rotate successfully](secretsmanager-controls.md#secretsmanager-2 "secretsmanager-controls.md#secretsmanager-2")

[[SecretsManager.4] Secrets Manager secrets should be rotated within a specified number of days](secretsmanager-controls.md#secretsmanager-4 "secretsmanager-controls.md#secretsmanager-4")

[[SSM.2] Amazon EC2 instances managed by Systems Manager should have a patch
compliance status of COMPLIANT after a patch installation](ssm-controls.md#ssm-2 "ssm-controls.md#ssm-2")

[[SSM.3] Amazon EC2 instances managed by Systems Manager should have an
association compliance status of COMPLIANT](ssm-controls.md#ssm-3 "ssm-controls.md#ssm-3")

[[StepFunctions.1] Step Functions state machines should have
logging turned on](stepfunctions-controls.md#stepfunctions-1 "stepfunctions-controls.md#stepfunctions-1")

[[Transfer.2] Transfer Family servers should not use FTP protocol for endpoint connection](transfer-controls.md#transfer-2 "transfer-controls.md#transfer-2")

[[WAF.1] AWS WAF Classic Global Web ACL logging should be enabled](waf-controls.md#waf-1 "waf-controls.md#waf-1")

[[WAF.11] AWS WAF web ACL logging should be enabled](waf-controls.md#waf-11 "waf-controls.md#waf-11")
