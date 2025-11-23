# AWS Foundational Security Best Practices standard in

Security Hub CSPM

Developed by AWS and industry professionals, the AWS Foundational Security Best Practices (FSBP) standard is a
compilation of security best practices for organizations, regardless of organization
sector or size. It provides a set of controls that detect when AWS accounts and
resources deviate from security best practices. It also provides prescriptive guidance
about how to improve and maintain your organization's security posture.

In AWS Security Hub CSPM, the AWS Foundational Security Best Practices standard includes controls that continuously evaluate
your AWS accounts and workloads, and help you identify areas that deviate from
security best practices. The controls include security best practices for resources from
multiple AWS services. Each control is assigned a category that reflects the security
function that the control applies to. For a list of categories and additional details,
see [Control categories](control-categories.md "control-categories.md").

## Controls that apply to the standard

The following list specifies which AWS Security Hub CSPM controls apply to the AWS
Foundational Security Best Practices standard (v1.0.0). To review the details of a
control, choose the control.

[[Account.1] Security contact information should be provided for an AWS account](account-controls.md#account-1 "account-controls.md#account-1")

[[ACM.1] Imported and ACM-issued certificates should be renewed after a specified time period](acm-controls.md#acm-1 "acm-controls.md#acm-1")

[[ACM.2] RSA certificates managed by ACM should use a key length of at least 2,048 bits](acm-controls.md#acm-2 "acm-controls.md#acm-2")

[[APIGateway.1] API Gateway REST and WebSocket API execution logging
should be enabled](apigateway-controls.md#apigateway-1 "apigateway-controls.md#apigateway-1")

[[APIGateway.2] API Gateway REST API stages should be configured to use
SSL certificates for backend authentication](apigateway-controls.md#apigateway-2 "apigateway-controls.md#apigateway-2")

[[APIGateway.3] API Gateway REST API stages should have AWS X-Ray
tracing enabled](apigateway-controls.md#apigateway-3 "apigateway-controls.md#apigateway-3")

[[APIGateway.4] API Gateway should be associated with a WAF Web
ACL](apigateway-controls.md#apigateway-4 "apigateway-controls.md#apigateway-4")

[[APIGateway.5] API Gateway REST API cache data should be encrypted at
rest](apigateway-controls.md#apigateway-5 "apigateway-controls.md#apigateway-5")

[[APIGateway.8] API Gateway routes should specify an authorization
type](apigateway-controls.md#apigateway-8 "apigateway-controls.md#apigateway-8")

[[APIGateway.9] Access logging should be configured for API Gateway V2
Stages](apigateway-controls.md#apigateway-9 "apigateway-controls.md#apigateway-9")

[[AppSync.1] AWS AppSync API caches should be encrypted at rest](appsync-controls.md#appsync-1 "appsync-controls.md#appsync-1")

[[AppSync.2] AWS AppSync should have field-level logging enabled](appsync-controls.md#appsync-2 "appsync-controls.md#appsync-2")

[[AppSync.5] AWS AppSync GraphQL APIs should not be authenticated with API keys](appsync-controls.md#appsync-5 "appsync-controls.md#appsync-5")

[[AppSync.6] AWS AppSync API caches should be encrypted in transit](appsync-controls.md#appsync-6 "appsync-controls.md#appsync-6")

[[Athena.4] Athena workgroups should have logging enabled](athena-controls.md#athena-4 "athena-controls.md#athena-4")

[[AutoScaling.1] Amazon EC2 Auto Scaling groups associated with a load balancer should use ELB health checks](autoscaling-controls.md#autoscaling-1 "autoscaling-controls.md#autoscaling-1")

[[AutoScaling.2] Amazon EC2 Auto Scaling group should cover multiple Availability Zones](autoscaling-controls.md#autoscaling-2 "autoscaling-controls.md#autoscaling-2")

[[AutoScaling.3] Amazon EC2 Auto Scaling group launch configurations should configure EC2 instances to require Instance Metadata Service Version 2 (IMDSv2)](autoscaling-controls.md#autoscaling-3 "autoscaling-controls.md#autoscaling-3")

[[Autoscaling.5] Amazon EC2 instances launched using Amazon EC2 Auto Scaling group launch configurations should not have Public IP addresses](autoscaling-controls.md#autoscaling-5 "autoscaling-controls.md#autoscaling-5")

[[AutoScaling.6] Amazon EC2 Auto Scaling groups should use multiple instance types in multiple Availability Zones](autoscaling-controls.md#autoscaling-6 "autoscaling-controls.md#autoscaling-6")

[[AutoScaling.9] Amazon EC2 Auto Scaling groups should use Amazon EC2 launch templates](autoscaling-controls.md#autoscaling-9 "autoscaling-controls.md#autoscaling-9")

[[Backup.1] AWS Backup recovery points should be encrypted at rest](backup-controls.md#backup-1 "backup-controls.md#backup-1")

[[CloudFront.1] CloudFront distributions should have a default
root object configured](cloudfront-controls.md#cloudfront-1 "cloudfront-controls.md#cloudfront-1")

[[CloudFront.3] CloudFront distributions should require
encryption in transit](cloudfront-controls.md#cloudfront-3 "cloudfront-controls.md#cloudfront-3")

[[CloudFront.4] CloudFront distributions should have origin
failover configured](cloudfront-controls.md#cloudfront-4 "cloudfront-controls.md#cloudfront-4")

[[CloudFront.5] CloudFront distributions should have logging
enabled](cloudfront-controls.md#cloudfront-5 "cloudfront-controls.md#cloudfront-5")

[[CloudFront.6] CloudFront distributions should have WAF
enabled](cloudfront-controls.md#cloudfront-6 "cloudfront-controls.md#cloudfront-6")

[[CloudFront.7] CloudFront distributions should use custom
SSL/TLS certificates](cloudfront-controls.md#cloudfront-7 "cloudfront-controls.md#cloudfront-7")

[[CloudFront.8] CloudFront distributions should use SNI to serve
HTTPS requests](cloudfront-controls.md#cloudfront-8 "cloudfront-controls.md#cloudfront-8")

[[CloudFront.9] CloudFront distributions should encrypt traffic
to custom origins](cloudfront-controls.md#cloudfront-9 "cloudfront-controls.md#cloudfront-9")

[[CloudFront.10] CloudFront distributions should not use
deprecated SSL protocols between edge locations and custom origins](cloudfront-controls.md#cloudfront-10 "cloudfront-controls.md#cloudfront-10")

[[CloudFront.12] CloudFront distributions should not point to
non-existent S3 origins](cloudfront-controls.md#cloudfront-12 "cloudfront-controls.md#cloudfront-12")

[[CloudFront.13] CloudFront distributions should use origin
access control](cloudfront-controls.md#cloudfront-13 "cloudfront-controls.md#cloudfront-13")

[[CloudFront.15] CloudFront distributions should use the
recommended TLS security policy](cloudfront-controls.md#cloudfront-15 "cloudfront-controls.md#cloudfront-15")

[[CloudFront.16] CloudFront distributions should use origin
access control for Lambda function URL origins](cloudfront-controls.md#cloudfront-16 "cloudfront-controls.md#cloudfront-16")

[[CloudTrail.1] CloudTrail should be enabled and configured with at least
one multi-Region trail that includes read and write management events](cloudtrail-controls.md#cloudtrail-1 "cloudtrail-controls.md#cloudtrail-1")

[[CloudTrail.2] CloudTrail should have encryption at-rest enabled](cloudtrail-controls.md#cloudtrail-2 "cloudtrail-controls.md#cloudtrail-2")

[[CloudTrail.4] CloudTrail log file validation should be enabled](cloudtrail-controls.md#cloudtrail-4 "cloudtrail-controls.md#cloudtrail-4")

[[CloudTrail.5] CloudTrail trails should be integrated with
Amazon CloudWatch Logs](cloudtrail-controls.md#cloudtrail-5 "cloudtrail-controls.md#cloudtrail-5")

[[CodeBuild.1] CodeBuild Bitbucket source repository URLs should not contain sensitive credentials](codebuild-controls.md#codebuild-1 "codebuild-controls.md#codebuild-1")

[[CodeBuild.2] CodeBuild project environment variables should not contain clear text credentials](codebuild-controls.md#codebuild-2 "codebuild-controls.md#codebuild-2")

[[CodeBuild.3] CodeBuild S3 logs should be encrypted](codebuild-controls.md#codebuild-3 "codebuild-controls.md#codebuild-3")

[[CodeBuild.4] CodeBuild project environments should have a logging AWS Configuration](codebuild-controls.md#codebuild-4 "codebuild-controls.md#codebuild-4")

[[CodeBuild.7] CodeBuild report group exports should be encrypted at rest](codebuild-controls.md#codebuild-7 "codebuild-controls.md#codebuild-7")

[[Cognito.2] Cognito identity pools should not allow
unauthenticated identities](cognito-controls.md#cognito-2 "cognito-controls.md#cognito-2")

[[Cognito.3] Password policies for Cognito user pools should
have strong configurations](cognito-controls.md#cognito-3 "cognito-controls.md#cognito-3")

[[Config.1] AWS Config should be enabled and use the service-linked role for resource recording](config-controls.md#config-1 "config-controls.md#config-1")

[[Connect.2] Amazon Connect instances should have CloudWatch logging
enabled](connect-controls.md#connect-2 "connect-controls.md#connect-2")

[[DataFirehose.1] Firehose delivery streams should be encrypted at rest](datafirehose-controls.md#datafirehose-1 "datafirehose-controls.md#datafirehose-1")

[[DataSync.1] DataSync tasks should have logging enabled](datasync-controls.md#datasync-1 "datasync-controls.md#datasync-1")

[[DMS.1] Database Migration Service replication instances should not be public](dms-controls.md#dms-1 "dms-controls.md#dms-1")

[[DMS.6] DMS replication instances should have automatic minor version upgrade enabled](dms-controls.md#dms-6 "dms-controls.md#dms-6")

[[DMS.7] DMS replication tasks for the target database should have logging enabled](dms-controls.md#dms-7 "dms-controls.md#dms-7")

[[DMS.8] DMS replication tasks for the source database should have logging enabled](dms-controls.md#dms-8 "dms-controls.md#dms-8")

[[DMS.9] DMS endpoints should use SSL](dms-controls.md#dms-9 "dms-controls.md#dms-9")

[[DMS.10] DMS endpoints for Neptune databases should have IAM authorization enabled](dms-controls.md#dms-10 "dms-controls.md#dms-10")

[[DMS.11] DMS endpoints for MongoDB should have an authentication mechanism enabled](dms-controls.md#dms-11 "dms-controls.md#dms-11")

[[DMS.12] DMS endpoints for Redis OSS should have TLS enabled](dms-controls.md#dms-12 "dms-controls.md#dms-12")

[[DMS.13] DMS replication instances should be configured to use multiple Availability Zones](dms-controls.md#dms-13 "dms-controls.md#dms-13")

[[DocumentDB.1] Amazon DocumentDB clusters should be encrypted at
rest](documentdb-controls.md#documentdb-1 "documentdb-controls.md#documentdb-1")

[[DocumentDB.2] Amazon DocumentDB clusters should have an adequate
backup retention period](documentdb-controls.md#documentdb-2 "documentdb-controls.md#documentdb-2")

[[DocumentDB.3] Amazon DocumentDB manual cluster snapshots should
not be public](documentdb-controls.md#documentdb-3 "documentdb-controls.md#documentdb-3")

[[DocumentDB.4] Amazon DocumentDB clusters should publish audit
logs to CloudWatch Logs](documentdb-controls.md#documentdb-4 "documentdb-controls.md#documentdb-4")

[[DocumentDB.5] Amazon DocumentDB clusters should have deletion
protection enabled](documentdb-controls.md#documentdb-5 "documentdb-controls.md#documentdb-5")

[[DocumentDB.6] Amazon DocumentDB clusters should be encrypted in
transit](documentdb-controls.md#documentdb-6 "documentdb-controls.md#documentdb-6")

[[DynamoDB.1] DynamoDB tables should automatically scale capacity with demand](dynamodb-controls.md#dynamodb-1 "dynamodb-controls.md#dynamodb-1")

[[DynamoDB.2] DynamoDB tables should have point-in-time recovery enabled](dynamodb-controls.md#dynamodb-2 "dynamodb-controls.md#dynamodb-2")

[[DynamoDB.3] DynamoDB Accelerator (DAX) clusters should be encrypted at rest](dynamodb-controls.md#dynamodb-3 "dynamodb-controls.md#dynamodb-3")

[[DynamoDB.6] DynamoDB tables should have deletion protection enabled](dynamodb-controls.md#dynamodb-6 "dynamodb-controls.md#dynamodb-6")

[[DynamoDB.7] DynamoDB Accelerator clusters should be encrypted in transit](dynamodb-controls.md#dynamodb-7 "dynamodb-controls.md#dynamodb-7")

[[EC2.1] Amazon EBS snapshots should not be publicly
restorable](ec2-controls.md#ec2-1 "ec2-controls.md#ec2-1")

[[EC2.2] VPC default security groups should not allow
inbound or outbound traffic](ec2-controls.md#ec2-2 "ec2-controls.md#ec2-2")

[[EC2.3] Attached Amazon EBS volumes should be encrypted
at-rest](ec2-controls.md#ec2-3 "ec2-controls.md#ec2-3")

[[EC2.4] Stopped EC2 instances should be removed
after a specified time period](ec2-controls.md#ec2-4 "ec2-controls.md#ec2-4")

[[EC2.6] VPC flow logging should be enabled in all
VPCs](ec2-controls.md#ec2-6 "ec2-controls.md#ec2-6")

[[EC2.7] EBS default encryption should be enabled](ec2-controls.md#ec2-7 "ec2-controls.md#ec2-7")

[[EC2.8] EC2 instances should use Instance Metadata
Service Version 2 (IMDSv2)](ec2-controls.md#ec2-8 "ec2-controls.md#ec2-8")

[[EC2.9] Amazon EC2 instances should not have a public IPv4
address](ec2-controls.md#ec2-9 "ec2-controls.md#ec2-9")

[[EC2.10] Amazon EC2 should be configured to use VPC endpoints
that are created for the Amazon EC2 service](ec2-controls.md#ec2-10 "ec2-controls.md#ec2-10")

[[EC2.15] Amazon EC2 subnets should not automatically assign
public IP addresses](ec2-controls.md#ec2-15 "ec2-controls.md#ec2-15")

[[EC2.16] Unused Network Access Control Lists should be
removed](ec2-controls.md#ec2-16 "ec2-controls.md#ec2-16")

[[EC2.17] Amazon EC2 instances should not use multiple
ENIs](ec2-controls.md#ec2-17 "ec2-controls.md#ec2-17")

[[EC2.18] Security groups should only allow unrestricted
incoming traffic for authorized ports](ec2-controls.md#ec2-18 "ec2-controls.md#ec2-18")

[[EC2.19] Security groups should not allow unrestricted
access to ports with high risk](ec2-controls.md#ec2-19 "ec2-controls.md#ec2-19")

[[EC2.20] Both VPN tunnels for an AWS Site-to-Site VPN
connection should be up](ec2-controls.md#ec2-20 "ec2-controls.md#ec2-20")

[[EC2.21] Network ACLs should not allow ingress from
0.0.0.0/0 to port 22 or port 3389](ec2-controls.md#ec2-21 "ec2-controls.md#ec2-21")

[[EC2.23] Amazon EC2 Transit Gateways should not automatically
accept VPC attachment requests](ec2-controls.md#ec2-23 "ec2-controls.md#ec2-23")

[[EC2.24] Amazon EC2 paravirtual instance types should not be
used](ec2-controls.md#ec2-24 "ec2-controls.md#ec2-24")

[[EC2.25] Amazon EC2 launch templates should not assign public
IPs to network interfaces](ec2-controls.md#ec2-25 "ec2-controls.md#ec2-25")

[[EC2.51] EC2 Client VPN endpoints should have client
connection logging enabled](ec2-controls.md#ec2-51 "ec2-controls.md#ec2-51")

[[EC2.55] VPCs should be configured with an interface endpoint for ECR API](ec2-controls.md#ec2-55 "ec2-controls.md#ec2-55")

[[EC2.56] VPCs should be configured with an interface endpoint for Docker Registry](ec2-controls.md#ec2-56 "ec2-controls.md#ec2-56")

[[EC2.57] VPCs should be configured with an interface endpoint for Systems Manager](ec2-controls.md#ec2-57 "ec2-controls.md#ec2-57")

[[EC2.58] VPCs should be configured with an interface endpoint for Systems Manager Incident Manager
Contacts](ec2-controls.md#ec2-58 "ec2-controls.md#ec2-58")

[[EC2.60] VPCs should be configured with an interface endpoint for Systems Manager Incident Manager](ec2-controls.md#ec2-60 "ec2-controls.md#ec2-60")

[[EC2.170] EC2 launch templates should use Instance
Metadata Service Version 2 (IMDSv2)](ec2-controls.md#ec2-170 "ec2-controls.md#ec2-170")

[[EC2.171] EC2 VPN connections should have logging
enabled](ec2-controls.md#ec2-171 "ec2-controls.md#ec2-171")

[[EC2.172] EC2 VPC Block Public Access settings should block
internet gateway traffic](ec2-controls.md#ec2-172 "ec2-controls.md#ec2-172")

[[EC2.173] EC2 Spot Fleet requests with launch
parameters should enable encryption for attached EBS volumes](ec2-controls.md#ec2-173 "ec2-controls.md#ec2-173")

[[EC2.180] EC2 network interfaces should have
source/destination checking enabled](ec2-controls.md#ec2-180 "ec2-controls.md#ec2-180")

[[EC2.181] EC2 launch templates should enable encryption
for attached EBS volumes](ec2-controls.md#ec2-181 "ec2-controls.md#ec2-181")

[[ECR.1] ECR private repositories should have image scanning configured](ecr-controls.md#ecr-1 "ecr-controls.md#ecr-1")

[[ECR.2] ECR private repositories should have tag immutability configured](ecr-controls.md#ecr-2 "ecr-controls.md#ecr-2")

[[ECR.3] ECR repositories should have at least one lifecycle policy configured](ecr-controls.md#ecr-3 "ecr-controls.md#ecr-3")

[[ECS.1] Amazon ECS task definitions should have secure networking modes and user
definitions](ecs-controls.md#ecs-1 "ecs-controls.md#ecs-1")

[[ECS.2] ECS services should not have public IP addresses assigned to them automatically](ecs-controls.md#ecs-2 "ecs-controls.md#ecs-2")

[[ECS.3] ECS task definitions should not share the host's process namespace](ecs-controls.md#ecs-3 "ecs-controls.md#ecs-3")

[[ECS.4] ECS containers should run as non-privileged](ecs-controls.md#ecs-4 "ecs-controls.md#ecs-4")

[[ECS.5] ECS containers should be limited to read-only access to root filesystems](ecs-controls.md#ecs-5 "ecs-controls.md#ecs-5")

[[ECS.8] Secrets should not be passed as container environment variables](ecs-controls.md#ecs-8 "ecs-controls.md#ecs-8")

[[ECS.9] ECS task definitions should have a logging configuration](ecs-controls.md#ecs-9 "ecs-controls.md#ecs-9")

[[ECS.10] ECS Fargate services should run on the latest Fargate platform version](ecs-controls.md#ecs-10 "ecs-controls.md#ecs-10")

[[ECS.12] ECS clusters should use Container Insights](ecs-controls.md#ecs-12 "ecs-controls.md#ecs-12")

[[ECS.16] ECS task sets should not automatically assign public IP addresses](ecs-controls.md#ecs-16 "ecs-controls.md#ecs-16")

[[EFS.1] Elastic File System should be configured to encrypt file data at-rest using AWS KMS](efs-controls.md#efs-1 "efs-controls.md#efs-1")

[[EFS.2] Amazon EFS volumes should be in backup plans](efs-controls.md#efs-2 "efs-controls.md#efs-2")

[[EFS.3] EFS access points should enforce a root directory](efs-controls.md#efs-3 "efs-controls.md#efs-3")

[[EFS.4] EFS access points should enforce a user identity](efs-controls.md#efs-4 "efs-controls.md#efs-4")

[[EFS.6] EFS mount targets should not be associated with subnets that assign
public IP addresses on launch](efs-controls.md#efs-6 "efs-controls.md#efs-6")

[[EFS.7] EFS file systems should have automatic backups enabled](efs-controls.md#efs-7 "efs-controls.md#efs-7")

[[EFS.8] EFS file systems should be encrypted at rest](efs-controls.md#efs-8 "efs-controls.md#efs-8")

[[EKS.1] EKS cluster endpoints should not be publicly accessible](eks-controls.md#eks-1 "eks-controls.md#eks-1")

[[EKS.2] EKS clusters should run on a supported Kubernetes version](eks-controls.md#eks-2 "eks-controls.md#eks-2")

[[EKS.3] EKS clusters should use encrypted Kubernetes secrets](eks-controls.md#eks-3 "eks-controls.md#eks-3")

[[EKS.8] EKS clusters should have audit logging enabled](eks-controls.md#eks-8 "eks-controls.md#eks-8")

[[ElastiCache.1] ElastiCache (Redis OSS) clusters should have
automatic backups enabled](elasticache-controls.md#elasticache-1 "elasticache-controls.md#elasticache-1")

[[ElastiCache.2] ElastiCache clusters should have automatic minor
version upgrades enabled](elasticache-controls.md#elasticache-2 "elasticache-controls.md#elasticache-2")

[[ElastiCache.3] ElastiCache replication groups should have
automatic failover enabled](elasticache-controls.md#elasticache-3 "elasticache-controls.md#elasticache-3")

[[ElastiCache.4] ElastiCache replication groups should be encrypted
at rest](elasticache-controls.md#elasticache-4 "elasticache-controls.md#elasticache-4")

[[ElastiCache.5] ElastiCache replication groups should be encrypted
in transit](elasticache-controls.md#elasticache-5 "elasticache-controls.md#elasticache-5")

[[ElastiCache.6] ElastiCache (Redis OSS) replication groups of earlier versions
should have Redis OSS AUTH enabled](elasticache-controls.md#elasticache-6 "elasticache-controls.md#elasticache-6")

[[ElastiCache.7] ElastiCache clusters should not use the default
subnet group](elasticache-controls.md#elasticache-7 "elasticache-controls.md#elasticache-7")

[[ElasticBeanstalk.1] Elastic Beanstalk environments should have enhanced health reporting enabled](elasticbeanstalk-controls.md#elasticbeanstalk-1 "elasticbeanstalk-controls.md#elasticbeanstalk-1")

[[ElasticBeanstalk.2] Elastic Beanstalk managed platform updates should be enabled](elasticbeanstalk-controls.md#elasticbeanstalk-2 "elasticbeanstalk-controls.md#elasticbeanstalk-2")

[[ElasticBeanstalk.3] Elastic Beanstalk should stream logs to CloudWatch](elasticbeanstalk-controls.md#elasticbeanstalk-3 "elasticbeanstalk-controls.md#elasticbeanstalk-3")

[[ELB.1] Application Load Balancer should be configured to redirect all HTTP requests
to HTTPS](elb-controls.md#elb-1 "elb-controls.md#elb-1")

[[ELB.2] Classic Load Balancers with SSL/HTTPS listeners should use a certificate
provided by AWS Certificate Manager](elb-controls.md#elb-2 "elb-controls.md#elb-2")

[[ELB.3] Classic Load Balancer listeners should be configured with HTTPS or TLS
termination](elb-controls.md#elb-3 "elb-controls.md#elb-3")

[[ELB.4] Application Load Balancer should be configured to drop invalid http
headers](elb-controls.md#elb-4 "elb-controls.md#elb-4")

[[ELB.5] Application and Classic Load Balancers logging should be enabled](elb-controls.md#elb-5 "elb-controls.md#elb-5")

[[ELB.6] Application, Gateway, and Network Load Balancers should have deletion
protection enabled](elb-controls.md#elb-6 "elb-controls.md#elb-6")

[[ELB.7] Classic Load Balancers should have connection draining enabled](elb-controls.md#elb-7 "elb-controls.md#elb-7")

[[ELB.8] Classic Load Balancers with SSL listeners should use a predefined
security policy that has strong AWS Configuration](elb-controls.md#elb-8 "elb-controls.md#elb-8")

[[ELB.9] Classic Load Balancers should have cross-zone load balancing
enabled](elb-controls.md#elb-9 "elb-controls.md#elb-9")

[[ELB.10] Classic Load Balancer should span multiple Availability Zones](elb-controls.md#elb-10 "elb-controls.md#elb-10")

[[ELB.12] Application Load Balancer should be configured with defensive or strictest
desync mitigation mode](elb-controls.md#elb-12 "elb-controls.md#elb-12")

[[ELB.13] Application, Network and Gateway Load Balancers should span multiple
Availability Zones](elb-controls.md#elb-13 "elb-controls.md#elb-13")

[[ELB.14] Classic Load Balancer should be configured with defensive or strictest
desync mitigation mode](elb-controls.md#elb-14 "elb-controls.md#elb-14")

[[ELB.17] Application and Network Load Balancers with listeners
should use recommended security policies](elb-controls.md#elb-17 "elb-controls.md#elb-17")

[[ELB.18] Application and Network Load Balancer listeners should
use secure protocols to encrypt data in transit](elb-controls.md#elb-18 "elb-controls.md#elb-18")

[[EMR.1] Amazon EMR cluster primary nodes should not have public IP addresses](emr-controls.md#emr-1 "emr-controls.md#emr-1")

[[EMR.2] Amazon EMR block public access setting should be enabled](emr-controls.md#emr-2 "emr-controls.md#emr-2")

[[EMR.3] Amazon EMR security configurations should be encrypted at rest](emr-controls.md#emr-3 "emr-controls.md#emr-3")

[[EMR.4] Amazon EMR security configurations should be encrypted in transit](emr-controls.md#emr-4 "emr-controls.md#emr-4")

[[ES.1] Elasticsearch domains should have encryption at-rest enabled](es-controls.md#es-1 "es-controls.md#es-1")

[[ES.2] Elasticsearch domains should not be publicly accessible](es-controls.md#es-2 "es-controls.md#es-2")

[[ES.3] Elasticsearch domains should encrypt data sent between nodes](es-controls.md#es-3 "es-controls.md#es-3")

[[ES.4] Elasticsearch domain error logging to CloudWatch Logs should be enabled](es-controls.md#es-4 "es-controls.md#es-4")

[[ES.5] Elasticsearch domains should have audit logging enabled](es-controls.md#es-5 "es-controls.md#es-5")

[[ES.6] Elasticsearch domains should have at least three data nodes](es-controls.md#es-6 "es-controls.md#es-6")

[[ES.7] Elasticsearch domains should be configured with at least three dedicated master nodes](es-controls.md#es-7 "es-controls.md#es-7")

[[ES.8] Connections to Elasticsearch domains should be encrypted using the latest TLS security policy](es-controls.md#es-8 "es-controls.md#es-8")

[[EventBridge.3] EventBridge custom event buses should have a resource-based policy attached](eventbridge-controls.md#eventbridge-3 "eventbridge-controls.md#eventbridge-3")

[[FSx.1] FSx for OpenZFS file systems should be configured to copy tags to backups and volumes](fsx-controls.md#fsx-1 "fsx-controls.md#fsx-1")

[[FSx.2] FSx for Lustre file systems should be configured to copy tags to backups](fsx-controls.md#fsx-2 "fsx-controls.md#fsx-2")

[[FSx.3] FSx for OpenZFS file systems should be configured for Multi-AZ deployment](fsx-controls.md#fsx-3 "fsx-controls.md#fsx-3")

[[FSx.4] FSx for NetApp ONTAP file systems should be configured for Multi-AZ deployment](fsx-controls.md#fsx-4 "fsx-controls.md#fsx-4")

[[FSx.5] FSx for Windows File Server file systems should be configured for Multi-AZ deployment](fsx-controls.md#fsx-5 "fsx-controls.md#fsx-5")

[[Glue.3] AWS Glue machine learning transforms should be encrypted at rest](glue-controls.md#glue-3 "glue-controls.md#glue-3")

[[Glue.4] AWS Glue Spark jobs should run on supported versions of AWS Glue](glue-controls.md#glue-4 "glue-controls.md#glue-4")

[[GuardDuty.1] GuardDuty should be enabled](guardduty-controls.md#guardduty-1 "guardduty-controls.md#guardduty-1")

[[GuardDuty.5] GuardDuty EKS Audit Log Monitoring should be enabled](guardduty-controls.md#guardduty-5 "guardduty-controls.md#guardduty-5")

[[GuardDuty.6] GuardDuty Lambda Protection should be enabled](guardduty-controls.md#guardduty-6 "guardduty-controls.md#guardduty-6")

[[GuardDuty.7] GuardDuty EKS Runtime Monitoring should be enabled](guardduty-controls.md#guardduty-7 "guardduty-controls.md#guardduty-7")

[[GuardDuty.8] GuardDuty Malware Protection for EC2 should be enabled](guardduty-controls.md#guardduty-8 "guardduty-controls.md#guardduty-8")

[[GuardDuty.9] GuardDuty RDS Protection should be enabled](guardduty-controls.md#guardduty-9 "guardduty-controls.md#guardduty-9")

[[GuardDuty.10] GuardDuty S3 Protection should be enabled](guardduty-controls.md#guardduty-10 "guardduty-controls.md#guardduty-10")

[[GuardDuty.11] GuardDuty Runtime Monitoring should be enabled](guardduty-controls.md#guardduty-11 "guardduty-controls.md#guardduty-11")

[[GuardDuty.12] GuardDuty ECS Runtime Monitoring should be enabled](guardduty-controls.md#guardduty-12 "guardduty-controls.md#guardduty-12")

[[GuardDuty.13] GuardDuty EC2 Runtime Monitoring should be
enabled](guardduty-controls.md#guardduty-13 "guardduty-controls.md#guardduty-13")

[[IAM.1] IAM policies should not allow full "\*" administrative privileges](iam-controls.md#iam-1 "iam-controls.md#iam-1")

[[IAM.2] IAM users should not have IAM policies attached](iam-controls.md#iam-2 "iam-controls.md#iam-2")

[[IAM.3] IAM users' access keys should be rotated every 90 days or less](iam-controls.md#iam-3 "iam-controls.md#iam-3")

[[IAM.4] IAM root user access key should not exist](iam-controls.md#iam-4 "iam-controls.md#iam-4")

[[IAM.5] MFA should be enabled for all IAM users that have a console password](iam-controls.md#iam-5 "iam-controls.md#iam-5")

[[IAM.6] Hardware MFA should be enabled for the root user](iam-controls.md#iam-6 "iam-controls.md#iam-6")

[[IAM.7] Password policies for IAM users should have strong configurations](iam-controls.md#iam-7 "iam-controls.md#iam-7")

[[IAM.8] Unused IAM user credentials should be removed](iam-controls.md#iam-8 "iam-controls.md#iam-8")

[[IAM.21] IAM customer managed policies that you create should not allow wildcard actions for services](iam-controls.md#iam-21 "iam-controls.md#iam-21")

[[Inspector.1] Amazon Inspector EC2 scanning should be enabled](inspector-controls.md#inspector-1 "inspector-controls.md#inspector-1")

[[Inspector.2] Amazon Inspector ECR scanning should be enabled](inspector-controls.md#inspector-2 "inspector-controls.md#inspector-2")

[[Inspector.3] Amazon Inspector Lambda code scanning should be enabled](inspector-controls.md#inspector-3 "inspector-controls.md#inspector-3")

[[Inspector.4] Amazon Inspector Lambda standard scanning should be enabled](inspector-controls.md#inspector-4 "inspector-controls.md#inspector-4")

[[Kinesis.1] Kinesis streams should be encrypted at rest](kinesis-controls.md#kinesis-1 "kinesis-controls.md#kinesis-1")

[[Kinesis.3] Kinesis streams should have an adequate data retention period](kinesis-controls.md#kinesis-3 "kinesis-controls.md#kinesis-3")

[[KMS.1] IAM customer managed policies should not allow decryption actions on all KMS keys](kms-controls.md#kms-1 "kms-controls.md#kms-1")

[[KMS.2] IAM principals should not have IAM inline policies that allow decryption actions on all KMS keys](kms-controls.md#kms-2 "kms-controls.md#kms-2")

[[KMS.3] AWS KMS keys should not be deleted unintentionally](kms-controls.md#kms-3 "kms-controls.md#kms-3")

[[KMS.5] KMS keys should not be publicly accessible](kms-controls.md#kms-5 "kms-controls.md#kms-5")

[[Lambda.1] Lambda function policies should prohibit public
access](lambda-controls.md#lambda-1 "lambda-controls.md#lambda-1")

[[Lambda.2] Lambda functions should use supported
runtimes](lambda-controls.md#lambda-2 "lambda-controls.md#lambda-2")

[[Lambda.5] VPC Lambda functions should operate in multiple
Availability Zones](lambda-controls.md#lambda-5 "lambda-controls.md#lambda-5")

[[Macie.1] Amazon Macie should be enabled](macie-controls.md#macie-1 "macie-controls.md#macie-1")

[[Macie.2] Macie automated sensitive data discovery should be enabled](macie-controls.md#macie-2 "macie-controls.md#macie-2")

[[MQ.2] ActiveMQ brokers should stream audit logs to CloudWatch](mq-controls.md#mq-2 "mq-controls.md#mq-2")

[[MQ.3] Amazon MQ brokers should have automatic minor version upgrade enabled](mq-controls.md#mq-3 "mq-controls.md#mq-3")

[[MSK.1] MSK clusters should be encrypted in transit among broker
nodes](msk-controls.md#msk-1 "msk-controls.md#msk-1")

[[MSK.3] MSK Connect connectors should be encrypted in
transit](msk-controls.md#msk-3 "msk-controls.md#msk-3")

[[MSK.4] MSK clusters should have public access disabled](msk-controls.md#msk-4 "msk-controls.md#msk-4")

[[MSK.5] MSK connectors should have logging enabled](msk-controls.md#msk-5 "msk-controls.md#msk-5")

[[MSK.6] MSK clusters should disable unauthenticated
access](msk-controls.md#msk-6 "msk-controls.md#msk-6")

[[Neptune.1] Neptune DB clusters should be encrypted at
rest](neptune-controls.md#neptune-1 "neptune-controls.md#neptune-1")

[[Neptune.2] Neptune DB clusters should publish audit
logs to CloudWatch Logs](neptune-controls.md#neptune-2 "neptune-controls.md#neptune-2")

[[Neptune.3] Neptune DB cluster snapshots should not be
public](neptune-controls.md#neptune-3 "neptune-controls.md#neptune-3")

[[Neptune.4] Neptune DB clusters should have deletion
protection enabled](neptune-controls.md#neptune-4 "neptune-controls.md#neptune-4")

[[Neptune.5] Neptune DB clusters should have automated
backups enabled](neptune-controls.md#neptune-5 "neptune-controls.md#neptune-5")

[[Neptune.6] Neptune DB cluster snapshots should be
encrypted at rest](neptune-controls.md#neptune-6 "neptune-controls.md#neptune-6")

[[Neptune.7] Neptune DB clusters should have IAM
database authentication enabled](neptune-controls.md#neptune-7 "neptune-controls.md#neptune-7")

[[Neptune.8] Neptune DB clusters should be configured to
copy tags to snapshots](neptune-controls.md#neptune-8 "neptune-controls.md#neptune-8")

[[NetworkFirewall.2] Network Firewall logging should be enabled](networkfirewall-controls.md#networkfirewall-2 "networkfirewall-controls.md#networkfirewall-2")

[[NetworkFirewall.3] Network Firewall policies should have at least one rule group associated](networkfirewall-controls.md#networkfirewall-3 "networkfirewall-controls.md#networkfirewall-3")

[[NetworkFirewall.4] The default stateless action for Network Firewall policies should be drop or forward for full packets](networkfirewall-controls.md#networkfirewall-4 "networkfirewall-controls.md#networkfirewall-4")

[[NetworkFirewall.5] The default stateless action for Network Firewall policies should be drop or forward for fragmented packets](networkfirewall-controls.md#networkfirewall-5 "networkfirewall-controls.md#networkfirewall-5")

[[NetworkFirewall.6] Stateless Network Firewall rule group should not be empty](networkfirewall-controls.md#networkfirewall-6 "networkfirewall-controls.md#networkfirewall-6")

[[NetworkFirewall.9] Network Firewall firewalls should have deletion protection enabled](networkfirewall-controls.md#networkfirewall-9 "networkfirewall-controls.md#networkfirewall-9")

[[NetworkFirewall.10] Network Firewall firewalls should have subnet change
protection enabled](networkfirewall-controls.md#networkfirewall-10 "networkfirewall-controls.md#networkfirewall-10")

[[Opensearch.1] OpenSearch domains should have encryption at rest enabled](opensearch-controls.md#opensearch-1 "opensearch-controls.md#opensearch-1")

[[Opensearch.2] OpenSearch domains should not be publicly accessible](opensearch-controls.md#opensearch-2 "opensearch-controls.md#opensearch-2")

[[Opensearch.3] OpenSearch domains should encrypt data sent between nodes](opensearch-controls.md#opensearch-3 "opensearch-controls.md#opensearch-3")

[[Opensearch.4] OpenSearch domain error logging to CloudWatch Logs should be enabled](opensearch-controls.md#opensearch-4 "opensearch-controls.md#opensearch-4")

[[Opensearch.5] OpenSearch domains should have audit logging enabled](opensearch-controls.md#opensearch-5 "opensearch-controls.md#opensearch-5")

[[Opensearch.6] OpenSearch domains should have at least three data nodes](opensearch-controls.md#opensearch-6 "opensearch-controls.md#opensearch-6")

[[Opensearch.7] OpenSearch domains should have fine-grained access control enabled](opensearch-controls.md#opensearch-7 "opensearch-controls.md#opensearch-7")

[[Opensearch.8] Connections to OpenSearch domains should be encrypted using the latest TLS security policy](opensearch-controls.md#opensearch-8 "opensearch-controls.md#opensearch-8")

[[Opensearch.10] OpenSearch domains should have the latest software update installed](opensearch-controls.md#opensearch-10 "opensearch-controls.md#opensearch-10")

[[PCA.1] AWS Private CA root certificate authority should be disabled](pca-controls.md#pca-1 "pca-controls.md#pca-1")

[[Route53.2] Route 53 public hosted zones should log DNS queries](route53-controls.md#route53-2 "route53-controls.md#route53-2")

[[RDS.1] RDS snapshot should be private](rds-controls.md#rds-1 "rds-controls.md#rds-1")

[[RDS.2] RDS DB Instances should prohibit public access, as determined by the PubliclyAccessible configuration](rds-controls.md#rds-2 "rds-controls.md#rds-2")

[[RDS.3] RDS DB instances should have encryption at-rest enabled](rds-controls.md#rds-3 "rds-controls.md#rds-3")

[[RDS.4] RDS cluster snapshots and database snapshots should be encrypted at rest](rds-controls.md#rds-4 "rds-controls.md#rds-4")

[[RDS.5] RDS DB instances should be configured with multiple Availability Zones](rds-controls.md#rds-5 "rds-controls.md#rds-5")

[[RDS.6] Enhanced monitoring should be configured for RDS DB instances](rds-controls.md#rds-6 "rds-controls.md#rds-6")

[[RDS.7] RDS clusters should have deletion protection enabled](rds-controls.md#rds-7 "rds-controls.md#rds-7")

[[RDS.8] RDS DB instances should have deletion protection enabled](rds-controls.md#rds-8 "rds-controls.md#rds-8")

[[RDS.9] RDS DB instances should publish logs to CloudWatch Logs](rds-controls.md#rds-9 "rds-controls.md#rds-9")

[[RDS.10] IAM authentication should be configured for RDS instances](rds-controls.md#rds-10 "rds-controls.md#rds-10")

[[RDS.11] RDS instances should have automatic backups enabled](rds-controls.md#rds-11 "rds-controls.md#rds-11")

[[RDS.12] IAM authentication should be configured for RDS clusters](rds-controls.md#rds-12 "rds-controls.md#rds-12")

[[RDS.13] RDS automatic minor version upgrades should be enabled](rds-controls.md#rds-13 "rds-controls.md#rds-13")

[[RDS.14] Amazon Aurora clusters should have backtracking enabled](rds-controls.md#rds-14 "rds-controls.md#rds-14")

[[RDS.15] RDS DB clusters should be configured for multiple Availability Zones](rds-controls.md#rds-15 "rds-controls.md#rds-15")

[[RDS.16] Aurora DB clusters should be configured to copy tags to DB
snapshots](rds-controls.md#rds-16 "rds-controls.md#rds-16")

[[RDS.17] RDS DB instances should be configured to copy tags to snapshots](rds-controls.md#rds-17 "rds-controls.md#rds-17")

[[RDS.19] Existing RDS event notification subscriptions should be configured for critical cluster events](rds-controls.md#rds-19 "rds-controls.md#rds-19")

[[RDS.20] Existing RDS event notification subscriptions should be configured for critical database instance events](rds-controls.md#rds-20 "rds-controls.md#rds-20")

[[RDS.21] An RDS event notifications subscription should be configured for critical database parameter group events](rds-controls.md#rds-21 "rds-controls.md#rds-21")

[[RDS.22] An RDS event notifications subscription should be configured for critical database security group events](rds-controls.md#rds-22 "rds-controls.md#rds-22")

[[RDS.23] RDS instances should not use a database engine default port](rds-controls.md#rds-23 "rds-controls.md#rds-23")

[[RDS.24] RDS Database clusters should use a custom administrator username](rds-controls.md#rds-24 "rds-controls.md#rds-24")

[[RDS.25] RDS database instances should use a custom administrator username](rds-controls.md#rds-25 "rds-controls.md#rds-25")

[[RDS.27] RDS DB clusters should be encrypted at rest](rds-controls.md#rds-27 "rds-controls.md#rds-27")

[[RDS.34] Aurora MySQL DB clusters should publish audit logs to CloudWatch Logs](rds-controls.md#rds-34 "rds-controls.md#rds-34")

[[RDS.35] RDS DB clusters should have automatic minor version upgrade enabled](rds-controls.md#rds-35 "rds-controls.md#rds-35")

[[RDS.36] RDS for PostgreSQL DB instances should publish logs to CloudWatch Logs](rds-controls.md#rds-36 "rds-controls.md#rds-36")

[[RDS.37] Aurora PostgreSQL DB clusters should publish logs to CloudWatch Logs](rds-controls.md#rds-37 "rds-controls.md#rds-37")

[[RDS.40] RDS for SQL Server DB instances should publish logs to CloudWatch Logs](rds-controls.md#rds-40 "rds-controls.md#rds-40")

[[RDS.41] RDS for SQL Server DB instances should be encrypted in transit](rds-controls.md#rds-41 "rds-controls.md#rds-41")

[[RDS.42] RDS for MariaDB DB instances should publish logs to CloudWatch Logs](rds-controls.md#rds-42 "rds-controls.md#rds-42")

[[RDS.43] RDS DB proxies should require TLS encryption for
connections](rds-controls.md#rds-43 "rds-controls.md#rds-43")

[[RDS.44] RDS for MariaDB DB instances should be encrypted in transit](rds-controls.md#rds-44 "rds-controls.md#rds-44")

[[RDS.45] Aurora MySQL DB clusters should have audit logging enabled](rds-controls.md#rds-45 "rds-controls.md#rds-45")

[[RDS.46] RDS DB instances should not be deployed in public subnets with routes to internet gateways](rds-controls.md#rds-46 "rds-controls.md#rds-46")

[[RDS.47] RDS for PostgreSQL DB clusters should be configured to copy tags to DB
snapshots](rds-controls.md#rds-47 "rds-controls.md#rds-47")

[[RDS.48] RDS for MySQL DB clusters should be configured to copy tags to DB
snapshots](rds-controls.md#rds-48 "rds-controls.md#rds-48")

[[Redshift.1] Amazon Redshift clusters should prohibit public access](redshift-controls.md#redshift-1 "redshift-controls.md#redshift-1")

[[Redshift.2] Connections to Amazon Redshift clusters should be encrypted in transit](redshift-controls.md#redshift-2 "redshift-controls.md#redshift-2")

[[Redshift.3] Amazon Redshift clusters should have automatic snapshots enabled](redshift-controls.md#redshift-3 "redshift-controls.md#redshift-3")

[[Redshift.4] Amazon Redshift clusters should have audit logging enabled](redshift-controls.md#redshift-4 "redshift-controls.md#redshift-4")

[[Redshift.6] Amazon Redshift should have automatic upgrades to major versions enabled](redshift-controls.md#redshift-6 "redshift-controls.md#redshift-6")

[[Redshift.7] Redshift clusters should use enhanced VPC routing](redshift-controls.md#redshift-7 "redshift-controls.md#redshift-7")

[[Redshift.8] Amazon Redshift clusters should not use the default Admin username](redshift-controls.md#redshift-8 "redshift-controls.md#redshift-8")

[[Redshift.10] Redshift clusters should be encrypted at rest](redshift-controls.md#redshift-10 "redshift-controls.md#redshift-10")

[[Redshift.15] Redshift security groups should allow ingress on the cluster port only from restricted origins](redshift-controls.md#redshift-15 "redshift-controls.md#redshift-15")

[[Redshift.18] Redshift clusters should have Multi-AZ
deployments enabled](redshift-controls.md#redshift-18 "redshift-controls.md#redshift-18")

[[RedshiftServerless.1] Amazon Redshift Serverless workgroups should use enhanced VPC routing](redshiftserverless-controls.md#redshiftserverless-1 "redshiftserverless-controls.md#redshiftserverless-1")

[[RedshiftServerless.2] Connections to Redshift Serverless workgroups should
be required to use SSL](redshiftserverless-controls.md#redshiftserverless-2 "redshiftserverless-controls.md#redshiftserverless-2")

[[RedshiftServerless.3] Redshift Serverless workgroups should prohibit
public access](redshiftserverless-controls.md#redshiftserverless-3 "redshiftserverless-controls.md#redshiftserverless-3")

[[RedshiftServerless.5] Redshift Serverless namespaces should not use the default admin username](redshiftserverless-controls.md#redshiftserverless-5 "redshiftserverless-controls.md#redshiftserverless-5")

[[RedshiftServerless.6] Redshift Serverless namespaces should export logs to
CloudWatch Logs](redshiftserverless-controls.md#redshiftserverless-6 "redshiftserverless-controls.md#redshiftserverless-6")

[[S3.1] S3 general purpose buckets should have block public access settings enabled](s3-controls.md#s3-1 "s3-controls.md#s3-1")

[[S3.2] S3 general purpose buckets should block public read
access](s3-controls.md#s3-2 "s3-controls.md#s3-2")

[[S3.3] S3 general purpose buckets should block public write
access](s3-controls.md#s3-3 "s3-controls.md#s3-3")

[[S3.5] S3 general purpose buckets should require requests to use SSL](s3-controls.md#s3-5 "s3-controls.md#s3-5")

[[S3.6] S3 general purpose bucket policies should restrict access to other AWS accounts](s3-controls.md#s3-6 "s3-controls.md#s3-6")

[[S3.8] S3 general purpose buckets should block public access](s3-controls.md#s3-8 "s3-controls.md#s3-8")

[[S3.9] S3 general purpose buckets should have server access logging enabled](s3-controls.md#s3-9 "s3-controls.md#s3-9")

[[S3.12] ACLs should not be used to manage user access to S3 general purpose buckets](s3-controls.md#s3-12 "s3-controls.md#s3-12")

[[S3.13] S3 general purpose buckets should have Lifecycle configurations](s3-controls.md#s3-13 "s3-controls.md#s3-13")

[[S3.19] S3 access points should have block public access settings enabled](s3-controls.md#s3-19 "s3-controls.md#s3-19")

[[S3.24] S3 Multi-Region Access Points should have block public access settings enabled](s3-controls.md#s3-24 "s3-controls.md#s3-24")

[[S3.25] S3 directory buckets should have lifecycle
configurations](s3-controls.md#s3-25 "s3-controls.md#s3-25")

[[SageMaker.1] Amazon SageMaker notebook instances should not have
direct internet access](sagemaker-controls.md#sagemaker-1 "sagemaker-controls.md#sagemaker-1")

[[SageMaker.2] SageMaker notebook instances should be launched in a
custom VPC](sagemaker-controls.md#sagemaker-2 "sagemaker-controls.md#sagemaker-2")

[[SageMaker.3] Users should not have root access to SageMaker notebook
instances](sagemaker-controls.md#sagemaker-3 "sagemaker-controls.md#sagemaker-3")

[[SageMaker.4] SageMaker endpoint production variants should have an
initial instance count greater than 1](sagemaker-controls.md#sagemaker-4 "sagemaker-controls.md#sagemaker-4")

[[SageMaker.5] SageMaker models should have network isolation enabled](sagemaker-controls.md#sagemaker-5 "sagemaker-controls.md#sagemaker-5")

[[SageMaker.8] SageMaker notebook instances should run on supported platforms](sagemaker-controls.md#sagemaker-8 "sagemaker-controls.md#sagemaker-8")

[[SecretsManager.1] Secrets Manager secrets should have automatic rotation enabled](secretsmanager-controls.md#secretsmanager-1 "secretsmanager-controls.md#secretsmanager-1")

[[SecretsManager.2] Secrets Manager secrets configured with automatic rotation should rotate successfully](secretsmanager-controls.md#secretsmanager-2 "secretsmanager-controls.md#secretsmanager-2")

[[SecretsManager.3] Remove unused Secrets Manager secrets](secretsmanager-controls.md#secretsmanager-3 "secretsmanager-controls.md#secretsmanager-3")

[[SecretsManager.4] Secrets Manager secrets should be rotated within a specified number of days](secretsmanager-controls.md#secretsmanager-4 "secretsmanager-controls.md#secretsmanager-4")

[[ServiceCatalog.1] Service Catalog portfolios should be shared within an AWS organization only](servicecatalog-controls.md#servicecatalog-1 "servicecatalog-controls.md#servicecatalog-1")

[[SNS.4] SNS topic access policies should not allow public access](sns-controls.md#sns-4 "sns-controls.md#sns-4")

[[SQS.1] Amazon SQS queues should be encrypted at rest](sqs-controls.md#sqs-1 "sqs-controls.md#sqs-1")

[[SQS.3] SQS queue access policies should not allow public access](sqs-controls.md#sqs-3 "sqs-controls.md#sqs-3")

[[SSM.1] Amazon EC2 instances should be managed by AWS Systems Manager](ssm-controls.md#ssm-1 "ssm-controls.md#ssm-1")

[[SSM.2] Amazon EC2 instances managed by Systems Manager should have a patch
compliance status of COMPLIANT after a patch installation](ssm-controls.md#ssm-2 "ssm-controls.md#ssm-2")

[[SSM.3] Amazon EC2 instances managed by Systems Manager should have an
association compliance status of COMPLIANT](ssm-controls.md#ssm-3 "ssm-controls.md#ssm-3")

[[SSM.4] SSM documents should not be public](ssm-controls.md#ssm-4 "ssm-controls.md#ssm-4")

[[SSM.6] SSM Automation should have CloudWatch logging
enabled](ssm-controls.md#ssm-6 "ssm-controls.md#ssm-6")

[[SSM.7] SSM documents should have the block public sharing
setting enabled](ssm-controls.md#ssm-7 "ssm-controls.md#ssm-7")

[[StepFunctions.1] Step Functions state machines should have
logging turned on](stepfunctions-controls.md#stepfunctions-1 "stepfunctions-controls.md#stepfunctions-1")

[[Transfer.2] Transfer Family servers should not use FTP protocol for endpoint connection](transfer-controls.md#transfer-2 "transfer-controls.md#transfer-2")

[[Transfer.3] Transfer Family connectors should have logging enabled](transfer-controls.md#transfer-3 "transfer-controls.md#transfer-3")

[[WAF.1] AWS WAF Classic Global Web ACL logging should be enabled](waf-controls.md#waf-1 "waf-controls.md#waf-1")

[[WAF.2] AWS WAF Classic Regional rules should have at least one condition](waf-controls.md#waf-2 "waf-controls.md#waf-2")

[[WAF.3] AWS WAF Classic Regional rule groups should have at least one rule](waf-controls.md#waf-3 "waf-controls.md#waf-3")

[[WAF.4] AWS WAF Classic Regional web ACLs should have at least one rule or rule group](waf-controls.md#waf-4 "waf-controls.md#waf-4")

[[WAF.6] AWS WAF Classic global rules should have at least one condition](waf-controls.md#waf-6 "waf-controls.md#waf-6")

[[WAF.7] AWS WAF Classic global rule groups should have at least one rule](waf-controls.md#waf-7 "waf-controls.md#waf-7")

[[WAF.8] AWS WAF Classic global web ACLs should have at least one rule or rule group](waf-controls.md#waf-8 "waf-controls.md#waf-8")

[[WAF.10] AWS WAF web ACLs should have at least one rule or rule group](waf-controls.md#waf-10 "waf-controls.md#waf-10")

[[WAF.12] AWS WAF rules should have CloudWatch metrics enabled](waf-controls.md#waf-12 "waf-controls.md#waf-12")

[[WorkSpaces.1] WorkSpaces user volumes should be encrypted at rest](workspaces-controls.md#workspaces-1 "workspaces-controls.md#workspaces-1")

[[WorkSpaces.2] WorkSpaces root volumes should be encrypted at rest](workspaces-controls.md#workspaces-2 "workspaces-controls.md#workspaces-2")
