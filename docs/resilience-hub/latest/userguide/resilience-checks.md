

# Resilience Checks for AWS services
<a name="resilience-checks"></a>

This chapter provides the details of various resilience checks performed by AWS Resilience Hub for supported AWS services to ensure that the resiliency postures of applications are not affected. These checks estimate the recovery time objective (RTO) and recovery point objective (RPO) against the values defined in the resilience policy for each Application Component (AppComponent). The assessments encompass different types of disruptions, that is, Application, Infrastructure failures, AZ outages, and Regional failures. However, to run these checks you must provide relevant IAM permissions to AWS Resilience Hub for allowing it to access your resources. To learn more about the required IAM permissions to allow AWS Resilience Hub to access your resources and perform the resilience checks in this chapter, see [AWS managed policies for AWS Resilience Hub](security-iam-awsmanpol.md).

**Topics**
+ [Amazon Elastic File System](#resilience-check-efs)
+ [Amazon Relational Database Service and Amazon Aurora](#resilience-check-rds)
+ [Amazon Simple Storage Service](#resilience-check-s3)
+ [Amazon DynamoDB](#resilience-check-ddb)
+ [Amazon Elastic Compute Cloud](#resilience-checks-ec2)
+ [Amazon EBS](#resilience-checks-ebs)
+ [AWS Lambda](#resilience-checks-lambda)
+ [Amazon Elastic Kubernetes Service](#resilience-checks-eks)
+ [Amazon Simple Notification Service](#resilience-checks-sns)
+ [Amazon Simple Queue Service](#resilience-checks-sqs)
+ [Amazon Elastic Container Service](#resilience-checks-ecs)
+ [Elastic Load Balancing](#resilience-checks-elb)
+ [Amazon API Gateway](#resilience-checks-abp)
+ [Amazon DocumentDB](#resilience-checks-docdb)
+ [NAT Gateway](#resilience-checks-nat-gateway)
+ [Amazon Route 53](#resilience-checks-r53)
+ [Amazon Application Recovery Controller (ARC)](#resilience-checks-r53arc)
+ [Amazon FSx for Windows File Server](#resilience-checks-fsx)
+ [AWS Step Functions](#resilience-checks-step-func)
+ [Amazon ElastiCache (Redis OSS)](#resilience-checks-elstc-cache-srvrless)

## Amazon Elastic File System
<a name="resilience-check-efs"></a>

This section lists all the resilience checks and recommendations that are specific to Amazon Elastic File System. For more information about Amazon Elastic File System, see the [Amazon Elastic File System documentation](https://docs.aws.amazon.com/efs).

### Filesystem type
<a name="one-az-deployment"></a>

AWS Resilience Hub checks filesystem type: Regional or One Zone. The filesystem type affects its resiliency in the event of Infrastructure or AZ disruptions. For more information about filesystem types, see [Availability and durability of Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/features.html#availability-durability).

### Filesystem Backup
<a name="filesystem-backup"></a>

AWS Resilience Hub checks if an AWS Backup plan is defined for the deployed filesystem. Additionally, it verifies if the `Cross-Region` backup option is enabled, ensuring coverage for Region-level disruptions if required by your policy.

### Data Replication
<a name="data-replication"></a>

AWS Resilience Hub checks if an in-Region or cross-Region Amazon EFS data replication is defined for the deployed filesystem. Amazon EFS data replication helps to improve estimated RTO and estimated RPO at Application, Infrastructure, AZ, and Region levels. Additionally, AWS Resilience Hub checks if it is combined with an in-Region AWS Backup to enable filesystem resiliency in the event of application disruption.

## Amazon Relational Database Service and Amazon Aurora
<a name="resilience-check-rds"></a>

This section lists all the resilience checks and recommendations that are specific for Amazon Relational Database Service and Amazon Aurora. For more information about Amazon Relational Database Service and Amazon Aurora, see [Amazon Relational Database Service documentation](https://docs.aws.amazon.com/rds/).

### Single-AZ deployment
<a name="one-az-deployment-rds"></a>

AWS Resilience Hub checks if the database is deployed as a single instance and if determined, it indicates that it does not support secondary instance and read replica.

### Multi-AZ deployment
<a name="multi-az-deployment-rds"></a>

AWS Resilience Hub checks if the database is deployed either with secondary instance or read replicas. If the database is deployed with read replica, AWS Resilience Hub validates if it is deployed in a different AZ to allow failover in the event of an AZ disruption. 

### Backup
<a name="rds-bckp"></a>

AWS Resilience Hub checks if the following backup capabilities are applied on a deployed database instance.
+ AWS Backup plan with automatic backup option
+ AWS Backup plan with cross-Region backup copy if it is required by your policy
+ Manual snapshots for 3rd party backup systems

### Cross-Region failover
<a name="rds-cross-Region-failover"></a>

AWS Resilience Hub checks RTO and RPO targets that are defined in the resiliency policy to recover from Regional disruption. Additionally, AWS Resilience Hub can identify following cross-Region architectures to cover for Regional disruption:
+ An in-Region backup with a copy of a cross-Region snapshot
+ A read replica in another Region
+ An Amazon Aurora global database with a secondary cluster in another Region
+ An Amazon Aurora global database with a headless secondary cluster in another Region

### Faster in-Region failover
<a name="rds-faster-in-Region-failover"></a>

AWS Resilience Hub checks RTO and RPO targets defined in the resiliency policy during infrastructure or AZ disruptions. Additionally, AWS Resilience Hub can identify the following in-Region architectures to cover for Application, Infrastructure and AZ disruptions: 
+ An In-Region backup
+ A read replica in a different AZ
+ An Aurora cluster with a read replica in another AZ
+ A Multi-AZ instance of Amazon Relational Database Service (Amazon RDS)
+ An Amazon RDS Multi-AZ cluster
+ A single instance of Amazon RDS with a read replica in another AZ

## Amazon Simple Storage Service
<a name="resilience-check-s3"></a>

This section lists all the resilience checks and recommendations that are specific for Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see [Amazon S3 documentation](https://docs.aws.amazon.com/s3).

### Versioning
<a name="versioning-s3"></a>

AWS Resilience Hub verifies if an Amazon S3 bucket is configured with versioning enabled.

### Scheduled backup
<a name="scheduled-bckp-s3"></a>

AWS Resilience Hub checks if an AWS Backup plan is defined for the deployed Amazon Simple Storage Service (Amazon S3) bucket. Additionally, it also checks if cross-Region backup option is enabled if your policy requires coverage for Region-level disruptions.

#### Point-in-time recovery
<a name="pitr-s3"></a>

AWS Resilience Hub checks if point-in-time recovery (PITR) is required by your resiliency policy’s RPO target. However, cross-Region backup is not supported for PITR. Hence, you use an existing scheduled AWS Backup plan with cross-Region backup option enabled, or create a new one.

### Data replication
<a name="data-repilication-s3"></a>

AWS Resilience Hub checks if a Same Region Replication (SRR) and Cross Region Replication (CRR) is defined for the deployed Amazon S3 bucket. Amazon S3 data replication improves estimated workload RTO and estimated workload RPO at Application, Infrastructure, AZ, and Region level. Additionally, it also protects from physical deletion of object because deletion of an object version is not replicated to the target Amazon S3 bucket. Additionally, based on the RTO targets defined in your resiliency policy, AWS Resilience Hub checks if Amazon S3 Replication Time Control (S3 RTC) should be enabled or not. This billable feature replicates 99.99 percent of source bucket objects within 15 minutes.
+ AWS Backup plan with automatic backup option
+ AWS Backup plan with cross-Region backup copy if it is required by your policy
+ Manual snapshots for 3rd party backup systems

## Amazon DynamoDB
<a name="resilience-check-ddb"></a>

This section lists all the resilience checks and recommendations that are specific for Amazon DynamoDB. For more information about Amazon DynamoDB, see [Amazon DynamoDB documentation](https://docs.aws.amazon.com/dynamodb).

### Scheduled backup
<a name="scheduled-bckp-ddb"></a>

AWS Resilience Hub checks if a backup is already defined for the deployed table. Additionally, it also checks if cross-Region backup should be configured for your policy if it requires coverage for Region-level disruptions.

#### Point-in-time recovery
<a name="pitr-ddb"></a>

AWS Resilience Hub checks if point-in-time recovery (PITR) is required according to your resiliency policy’s RPO target. However, cross-Region backup is not supported for PITR. Hence, you use an existing scheduled AWS Backup plan with cross-Region backup option enabled, or create a new one.

### Global table
<a name="global-table-ddb"></a>

AWS Resilience Hub checks if the deployed Amazon DynamoDB table is defined as a Global Table with one or more replicas in other Regions. Setting up Global Table improves estimated workload RTO and estimated workload RPO at Region level, and also provides a capability to work in active-active or active-passive multi-Region modes. AWS Backup or Amazon DynamoDB PITR can be used in one of the Regions to handle application disruptions.

## Amazon Elastic Compute Cloud
<a name="resilience-checks-ec2"></a>

This section lists all the resilience checks and recommendations that are specific for Amazon Elastic Compute Cloud. For more information about Amazon Elastic Compute Cloud, see [Amazon Elastic Compute Cloud documentation](https://docs.aws.amazon.com/ec2).

### Stateful instance
<a name="stateful-instance-ec2"></a>

AWS Resilience Hub identifies an Amazon EC2 instance as a stateful instance if one of the following criteria is met:
+ If `DeleteOnTermination` attribute is set to false for at least one Amazon Elastic Block Store (Amazon EBS) volume that is attached to this instance.
+ If Amazon Data Lifecycle Manager or an AWS Backup plan is attached to the Amazon EC2 instance or at least one Amazon EBS volume.
+ If AWS Elastic Disaster Recovery is used to replicate your Amazon EC2 instance storage volumes.

**Note**  
If an Amazon EC2 instance doesn’t meet the any of the above criteria, AWS Resilience Hub treats it as a stateless Amazon EC2 instance.

### Auto Scaling groups
<a name="asg-ec2"></a>

AWS Resilience Hub checks for a group of stateless Amazon EC2 instances. If discovered, it is recommended to orchestrate the same using Auto Scaling groups (ASG) with Multi-AZ configuration. If an existing ASG is identified, ARH will verify if it is configured across multiple Availability Zones. If ASG is also defined using spot Amazon EC2 instances only, it is recommended to augment its capacity with on-demand Amazon EC2 instances to improve the resiliency when spot Amazon EC2 instances are unavailable.

### Amazon EC2 Fleet
<a name="fleet-ec2"></a>

AWS Resilience Hub identifies Amazon EC2 Fleet and verifies if it is defined as Multi-AZ deployment and also if it uses spot Amazon EC2 instances only. Defining an Amazon EC2 Fleet as Multi-AZ deployment will improve its resiliency in the event of an AZ disruption. Augmenting an Amazon EC2 Fleet with on-demand instances will improve its resiliency when spot instances are unavailable.

## Amazon EBS
<a name="resilience-checks-ebs"></a>

This section lists all the resilience checks and recommendations that are specific to Amazon EBS. For more information about Amazon EBS, see [Amazon EBS documentation](https://docs.aws.amazon.com/ebs/).

### Scheduled backup
<a name="scheduled-backup-ebs"></a>

AWS Resilience Hub checks if either or both the following are defined for your Amazon EBS volumes.
+  A backup rule for specific Amazon EBS volume attached to your Amazon EC2 instance. 
+  A backup rule to create Amazon EBS-backed AMI to your Amazon EC2 instance. 
+  Manual snapshots for 3rd party backup systems. 

Additionally, if your policy requires coverage for Region-level disruptions, AWS Resilience Hub checks if your backup rule has cross-Region backup option enabled.

### Data backup and replication
<a name="data-backup-replication-ebs"></a>

AWS Resilience Hub identifies an Amazon EBS volume is considered a stateful volume if one of the following criteria is met:
+  If `DeleteOnTermination` attribute is set to false for this Amazon EBS volume. 
+  If Amazon Data Lifecycle Manager or an AWS Backup plan is associated with either this Amazon EBS volume or the Amazon EC2 instance it is attached to. 
+  If AWS Elastic Disaster Recovery is used to replicate your Amazon EC2 instance storage volumes.

## AWS Lambda
<a name="resilience-checks-lambda"></a>

This section lists all the resilience checks and recommendations that are specific to AWS Lambda. For more information about AWS Lambda, see [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/).

### Customer Amazon VPC Access
<a name="customer-vpc-access-lambda"></a>

AWS Resilience Hub identifies an AWS Lambda function connected to the VPC. Connecting AWS Lambda to subnets in different AZs of your Amazon VPC allows function resiliency in case of an AZ disruption. 

### Dead-letter queue
<a name="dlq-lambda"></a>

AWS Resilience Hub checks if an AWS Lambda function has a dead-letter queue (DLQ) attached to it for storing failed requests. Attaching a DLQ to AWS Lambda function allows to prevent the data loss of requests and retry to process the failed requests at a later stage.

## Amazon Elastic Kubernetes Service
<a name="resilience-checks-eks"></a>

This section lists all the resilience checks and recommendations that are specific to Amazon Elastic Kubernetes Service (Amazon EKS). For more information about Amazon EKS, see [Amazon EKS documentation](https://docs.aws.amazon.com/eks/).

### Multi-AZ deployment
<a name="multi-az-eks"></a>

AWS Resilience Hub identifies if pod deployment is running on multiple worker nodes in multiple AZs. An additional Amazon EKS cluster in another Region is required if your resiliency policy requires coverage in the event of Regional disruption. This additional Amazon EKS cluster is also verified for pod deployments that are distributed between multiple worker nodes in multiple AZs.

### Deployment vs. ReplicaSet
<a name="deployment-replica-set-eks"></a>

AWS Resilience Hub checks if you are using ReplicaSets or pod objects instead of deployment. Replacing ReplicaSets or pod objects with deployment simplifies the pod updates to a new version of the software and includes other useful features.

### Deployment maintenance
<a name="deployment-maintenance-eks"></a>

AWS Resilience Hub checks if the following best practices are used for deployment:
+ Using Pod Disruption Budget (PDB) – Using PDB makes it possible to improve the availability by setting a limit on the number of pods in the workload that can be disrupted at any given time.
+ Replacing self-managed node groups with Amazon EKS managed node groups – This replacement simplifies worker node image updates during maintenance.
+ Supporting dynamic CPU and memory requests per deployment – These requests help Kubernetes to select a node that fits the needs of a pod.
+ Configuring liveness and readiness probes for all the containers – Configuring liveness probes help to improve the resiliency by restarting the non-functional pods. Configuring readiness probes make it possible to improve the availability by diverting the traffic away from busy pods.
+ Configuring Karpenter, Cluster Autoscaler, or AWS Fargate – These configurations allow Amazon EKS cluster’s infrastructure to grow and meet the workload demands.
+ Configuring Horizontal Pod Autoscaler – This configuration helps Amazon EKS cluster to automatically scale the workload to meet request processing demand.

## Amazon Simple Notification Service
<a name="resilience-checks-sns"></a>

This section lists all the resilience checks and recommendations that are specific to Amazon Simple Notification Service (Amazon SNS). For more information about Amazon SNS, see [Amazon SNS documentation](https://docs.aws.amazon.com/sns/).

### Topic subscriptions
<a name="topic-subscriptions-sns"></a>

AWS Resilience Hub checks if Amazon SNS topic has at least 1 subscription attached to it for ensuring that incoming messages are not lost.

## Amazon Simple Queue Service
<a name="resilience-checks-sqs"></a>

This section lists all the resilience checks and recommendations that are specific to Amazon Simple Queue Service (Amazon SQS). For more information about Amazon SQS, see [Amazon SQS documentation](https://docs.aws.amazon.com/sqs/).

### Dead-letter queue
<a name="dlq-sqs"></a>

AWS Resilience Hub checks if the Amazon SQS queue has a DLQ associated to it to handle messages that can't be delivered to subscribers successfully.

## Amazon Elastic Container Service
<a name="resilience-checks-ecs"></a>

This section lists all the resilience checks and recommendations that are specific to Amazon Elastic Container Service (Amazon ECS). For more information about Amazon ECS, see [Amazon ECS documentation](https://docs.aws.amazon.com/ecs/).

### Multi-AZ deployment
<a name="multi-az-ecs"></a>

AWS Resilience Hub checks if Amazon ECS tasks or services are running in multiple AZs based on either Amazon EC2 or AWS Fargate launch types. An additional Amazon ECS cluster in another Region is required if your policy needs coverage for Regional disruption. The additional cluster is also verified for execution of tasks or services in multiple AZs.

## Elastic Load Balancing
<a name="resilience-checks-elb"></a>

This section lists all the resilience checks and recommendations that are specific to Elastic Load Balancing. For more information about Elastic Load Balancing, see [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/).

### Multi-AZ deployment
<a name="multi-az-deployment-elb"></a>

AWS Resilience Hub checks if Elastic Load Balancing is running in multiple AZs. 

An additional Elastic Load Balancing in a different Region is required if your policy needs coverage for Regional disruption. The additional Elastic Load Balancing, located in a different Region, is also verified for its deployment in multiple AZs.

## Amazon API Gateway
<a name="resilience-checks-abp"></a>

This section lists all the resilience checks and recommendations that are specific to Amazon API Gateway. For more information about Amazon API Gateway, see [Amazon API Gateway documentation](https://docs.aws.amazon.com/apigateway).

### Cross-Region deployment
<a name="cross-region-deployment-abp"></a>

If your policy needs to consider Regional disruption, AWS Resilience Hub will check if there is an additional deployment of Amazon API Gateway API resource in a different Region.

### Private API Multi-AZ deployment
<a name="Private-api-multi-az-deployment-abp"></a>

AWS Resilience Hub checks if your API is defined as private within Amazon API Gateway. Private APIs should receive traffic through Amazon VPC interface endpoint that is deployed to multiple AZs.

## Amazon DocumentDB
<a name="resilience-checks-docdb"></a>

This section lists all the checks and recommendations that are specific to Amazon DocumentDB. For more information about Amazon DocumentDB, see [Amazon DocumentDB documentation](https://docs.aws.amazon.com/documentdb/).

### Multi-AZ deployment
<a name="multi-az-deployment-ddb"></a>

AWS Resilience Hub checks if Amazon DocumentDB cluster is deployed in multiple AZs. An additional secondary Amazon DocumentDB cluster is required in a different Region if your policy requires coverage for Regional disruption. The additional Amazon DocumentDB cluster, located in a different Region, is also verified for its execution in multiple AZs.

### Elastic cluster and Multi-AZ deployment
<a name="elastic-cluster-multi-az-deployment-ddb"></a>

AWS Resilience Hub checks if Amazon DocumentDB Elastic cluster shards are using read replicas that are deployed in different AZs.

### Elastic cluster and Manual snapshots
<a name="elastic-cluster-manual-snapshots-ddb"></a>

AWS Resilience Hub checks if manual snapshots are regularly created for an Amazon DocumentDB Elastic cluster. Manual snapshots allow longer persistence and provides flexibility in setting the snapshot frequency to suit your business needs.

## NAT Gateway
<a name="resilience-checks-nat-gateway"></a>

This section lists all the checks and recommendations that are specific to NAT Gateway. For more information about NAT Gateways, see [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html).

### Multi-AZ deployment
<a name="multi-az-deployment-nat"></a>

AWS Resilience Hub checks if NAT Gateway is deployed in multiple AZs. An additional NAT Gateway deployment is required in a different Region if your policy requires coverage for Regional disruption. The additional NAT Gateway, located in a different Region, is also verified for its deployment in multiple AZs.

## Amazon Route 53
<a name="resilience-checks-r53"></a>

This section lists all the checks and recommendations that are specific to Amazon Route 53. For more information about Amazon Route 53, see [Amazon Route 53 documentation](https://docs.aws.amazon.com/route53/).

### Multi-AZ deployment
<a name="multi-az-deployment-r53"></a>

AWS Resilience Hub checks if Amazon Route 53 hosted zone record is defined with multiple targets in the same Region and if these targets are deployed in multiple AZs. If your policy requires coverage for Regional disruption, AWS Resilience Hub checks if Amazon Route 53 hosted zone record is defined in multiple Regions with multiple targets per Region, and if these targets are deployed in multiple AZs.

## Amazon Application Recovery Controller (ARC)
<a name="resilience-checks-r53arc"></a>

This section lists all the checks and recommendations that are specific to Amazon Application Recovery Controller (ARC) (ARC). For more information about ARC, see [ARC documentation](https://docs.aws.amazon.com/amazonarc/).

### Multi-AZ deployment
<a name="multi-az-deployment-r53arc"></a>

AWS Resilience Hub checks if similar resources are deployed in multiple Regions and recommends as a best practice to define ARC readiness checks to increase their availability and readiness in the event of a Regional disruption. You will be notified that you will incur additional hourly charges.

## Amazon FSx for Windows File Server
<a name="resilience-checks-fsx"></a>

This section lists all the checks and recommendations that are specific to Amazon FSx for Windows File Server. For more information about Amazon FSx for Windows File Server, see [Amazon FSx for Windows File Server documentation](https://docs.aws.amazon.com/fsx/).

### Filesystem type
<a name="filesystem-type-fsx"></a>

AWS Resilience Hub checks the filesystem type: `Regional` or `One Zone`. Filesystem type affects its resiliency in the event of Infrastructure or AZ disruptions. For more information about filesystem types, see [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/availability-durability.html).

### Filesystem Backup
<a name="filesystem-backup-fsx"></a>

AWS Resilience Hub checks if an AWS Backup is defined for the deployed filesystem. Additionally, it also checks if `cross-Region backup` option is enabled if your policy requires coverage for Region-level disruptions. 

### Data Replication
<a name="data-replication-fsx"></a>

AWS Resilience Hub checks if an in-Region or cross-Region scheduled AWS DataSync data replication task is defined for the deployed filesystem.

AWS DataSync scheduled data replication task can improve estimated workload RTO and estimated workload RPO at Infrastructure, AZ, and Region levels. Additionally, it could be combined with an in-Region AWS Backup to recover in the event of an application disruption.

## AWS Step Functions
<a name="resilience-checks-step-func"></a>

This section lists all the checks and recommendations that are specific to AWS Step Functions. For more information about AWS Step Functions, see [AWS Step Functions documentation](https://docs.aws.amazon.com/step-functions/).

### Versioning and alias
<a name="versioning-alias-step-func"></a>

AWS Resilience Hub checks if AWS Step Functions workflow uses versioning and alias to improve the re-deployment time.

### Cross-Region deployment
<a name="cross-region-deployment-step-func"></a>

AWS Resilience Hub checks if AWS Step Functions workflow of the same workflow type is deployed in a different Region to recover in the event of a Regional disruption.

## Amazon ElastiCache (Redis OSS)
<a name="resilience-checks-elstc-cache-srvrless"></a>

This section lists all the checks and recommendations that are specific to Amazon ElastiCache (Redis OSS).

For more information about Amazon ElastiCache (Redis OSS), see [Amazon ElastiCache documentation](https://docs.aws.amazon.com/elasticache/).

### Single-AZ deployment
<a name="single-az-elstc-cache-srvrless"></a>

AWS Resilience Hub checks if Amazon ElastiCache (Redis OSS) cluster is deployed either as a single node or with all its nodes in a single Availability Zone.

### Single-AZ deployment
<a name="multi-az-elstc-cache-srvrless"></a>

AWS Resilience Hub validates if Amazon ElastiCache (Redis OSS) cluster is deployed as a replication group (for both Cluster Mode enabled and Cluster Mode Disabled clusters) across multiple Availability Zones to allow failover in the event of an Availability Zone disruption.

### Cross-Region failover
<a name="cross-region-flover-elstc-cache-srvrless"></a>

AWS Resilience Hub checks RTO and RPO targets that are defined in the resiliency policy to recover from a Regional disruption. Additionally, AWS Resilience Hub can identify Amazon ElastiCache (Redis OSS) global datastore clusters deployed in multiple Regions.

### Backup
<a name="backup-elstc-cache-srvrless"></a>

AWS Resilience Hub checks if the following backup capabilities are applied on a deployed Amazon ElastiCache (Redis OSS) or self-designed cluster:
+ Automatic backup
+ Manual backup for 3rd party backup systems

AWS Resilience Hub will not recommend backup as a recovery method if you are not using backup. However, you can reset Cache layer in the event of data inconsistency and recreate the data from the primary storage. 

### Faster in-Region failover
<a name="faster-in-region-flover-elstc-cache-srvrless"></a>

AWS Resilience Hub checks RTO and RPO targets defined in the resiliency policy during infrastructure or AZ disruptions. Additionally, AWS Resilience Hub can identify the following in-Region architectures to recover from Infrastructure and AZ disruptions: 
+ Secondary standby node instance in a different Availability Zone for Cluster Mode Disabled type of Amazon ElastiCache (Redis OSS) cluster.
+ Secondary standby node instance in a different Availability Zone per every shard for Cluster Mode Enabled type of Amazon ElastiCache (Redis OSS) cluster. 