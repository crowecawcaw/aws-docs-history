

# Fault tolerance
<a name="fault-tolerance-checks"></a>

You can use the following checks for the fault tolerance category.

**Contents**
+ [ALB Multi-AZ](#alb-multi-az)
+ [Amazon Aurora MySQL cluster backtracking not enabled](#amazon-aurora-mysql-cluster-backtracking-not-enabled)
+ [Amazon Aurora DB Instance Accessibility](#amazon-aurora-db-instance-accessibility)
+ [Amazon CloudFront Origin Failover](#amazon-cloudfront-origin-failover)
+ [Amazon Comprehend Endpoint Access Risk](#amazon-comprehend-endpoint-access-risk)
+ [Amazon DocumentDB Single AZ Clusters](#amazon-documentdb-single-az-clusters)
+ [Amazon DynamoDB Point-in-time Recovery](#amazon-dynamodb-table-point-in-time-recovery)
+ [Amazon DynamoDB Table Not Included in Backup Plan](#amazon-dynamodb-table-not-in-backup-plan)
+ [Amazon EBS Not Included in AWS Backup Plan](#amazon-ebs-not-in-backup-plan)
+ [Amazon EBS Snapshots](#amazon-ebs-snapshots)
+ [Amazon EC2 Auto Scaling does not have ELB Health Check Enabled](#amazon-ec2-auto-scaling-group-no-elb-health-check)
+ [Amazon EC2 Auto Scaling Group has Capacity Rebalancing Enabled](#amazon-ec2-auto-scaling-group-capacity-rebalance-enabled)
+ [Amazon EC2 Auto Scaling is not deployed in multiple AZs or does not meet the minimum number of AZs](#amazon-ec2-auto-scaling-group-multiple-az)
+ [Amazon EC2 Availability Zone Balance](#amazon-ec2-availability-zone-balance)
+ [Amazon EC2 detailed monitoring not enabled](#amazon-ec2-detailed-monitoring-not-enabled)
+ [Amazon ECS AWSLogs driver in blocking mode](#amazon-ecs-awslogs-driver-blockingmode)
+ [Amazon ECS service using a single AZ](#amazon-ecs-service-single-az)
+ [Amazon ECS Multi-AZ placement strategy](#amazon-ecs-multi-az-placement-strategy)
+ [Amazon EFS no mount target redundancy](#amazon-efs-no-mount-target-redundancy)
+ [Amazon EFS not in AWS Backup plan](#amazon-efs-not-in-backup-plan)
+ [Amazon ElastiCache Multi-AZ clusters](#amazon-elasticache-multi-az-clusters)
+ [ElastiCache (Redis OSS) Clusters Automatic Backup](#amazon-elasticache-redis-clusters-auto-backup)
+ [Amazon MemoryDB Multi-AZ clusters](#amazon-memorydb-multi-az-clusters)
+ [Amazon MSK brokers hosting too many partitions](#amazon-msk-brokers-hosting-too-many-partitions)
+ [Amazon MSK Cluster Multi-AZ](#amazon-msk-cluster-multi-az)
+ [Amazon OpenSearch Service domains with less than three data nodes](#amazon-opensearch-service-domains-less-than-three-nodes)
+ [Amazon RDS Backups](#amazon-rds-backups)
+ [Amazon RDS Continuous Backup Not Enabled](#amazon-rds-cont-backups)
+ [Amazon RDS DB clusters have one DB instance](#amazon-rds-db-clusters-one-db-instance)
+ [Amazon RDS DB clusters with all instances in the same Availability Zone](#amazon-rds-db-clusters-same-az)
+ [Amazon RDS DB clusters with all reader instances in the same Availability Zone](#amazon-rds-reader-instances-same-az)
+ [Amazon RDS DB Instance Enhanced Monitoring not enabled](#amazon-rds-db-instance-enhanced-monitoring-not-enabled)
+ [Amazon RDS DB instances have storage autoscaling turned off](#amazon-rds-db-instance-storage-autoscaling-off)
+ [Amazon RDS DB instances not using Multi-AZ deployment](#amazon-rds-db-instances-not-using-multi)
+ [Amazon RDS DiskQueueDepth](#Amazon-RDS-DiskQueueDepth)
+ [Amazon RDS FreeStorageSpace](#Amazon-RDS-FreeStorageSpace)
+ [Amazon RDS log\_output parameter is set to table](#amazon-rds-log-parameter-set-to-table)
+ [Amazon RDS innodb\_default\_row\_format parameter setting is unsafe](#rds-innodb-default-row-format-unsafe)
+ [Amazon RDS innodb\_flush\_log\_at\_trx\_commit parameter is not 1](#rds-innodb-flush-log-at-trx-parameter-off)
+ [Amazon RDS max\_user\_connections parameter is low](#rds-max-user-connections-parameter-low)
+ [Amazon RDS Multi-AZ](#amazon-rds-multi-az)
+ [Amazon RDS Not In AWS Backup Plan](#amazon-rds-not-in-backup-plan)
+ [Amazon RDS Read Replicas are open in writable mode](#rds-read-replicas-writable)
+ [Amazon RDS resource automated backups is turned off](#amazon-rds-auto-backup-off)
+ [Amazon RDS sync\_binlog parameter is turned off](#rds-sync-binlog-parameter-off)
+ [RDS DB Cluster has no Multi-AZ replication enabled](#rds-db-cluster-multi-zone-replication-not-enabled)
+ [RDS Multi-AZ Standby Instance Not Enabled](#rds-multi-az-standby-instance)
+ [Amazon RDS ReplicaLag](#Amazon-RDS-ReplicaLag)
+ [Amazon RDS synchronous\_commit parameter is turned off](#rds-synchronous-commit-parameter-off)
+ [Amazon Redshift cluster automated snapshots](#amazon-redshift-cluster-automated-snapshots)
+ [Amazon Route 53 Deleted Health Checks](#amazon-route-53-deleted-health-checks)
+ [Amazon Route 53 Failover Resource Record Sets](#amazon-route-53-failover-resource-record-sets)
+ [Amazon Route 53 High TTL Resource Record Sets](#amazon-route-53-high-ttl-resource-record-sets)
+ [Amazon Route 53 Name Server Delegations](#amazon-route-53-name-server-delegations)
+ [Amazon Route 53 Resolver Endpoint Availability Zone Redundancy](#amazon-route53-resolver-endpoint-availability-zone-redundancy)
+ [Amazon S3 Bucket Replication Not Enabled](#amazon-s3-bucket-replication-not-enabled)
+ [Amazon S3 Bucket Versioning](#amazon-s3-bucket-versioning)
+ [Application, Network, and Gateway Load Balancers Not Spanning Multiple Availability Zones](#application-network-load-balancers-not-span-multi-az)
+ [Auto Scaling available IPs in Subnets](#auto-scaling-available-ips-in-subnets)
+ [Auto Scaling Group Health Check](#auto-scaling-group-health-check)
+ [Auto Scaling Group Resources](#auto-scaling-group-resources)
+ [AWS CloudHSM clusters running HSM instances in a single AZ](#aws-cloudhsm-clusters-running-hsm-instances-in-a-single-az)
+ [Direct Connect Location Resiliency](#amazon-direct-connect-location-resiliency)
+ [AWS Lambda functions without a dead-letter queue configured](#aws-lambda-functions-without-dlq)
+ [AWS Lambda On Failure Event Destinations](#AWS-Lambda-On-Failure-Event-Destinations)
+ [AWS Lambda VPC-enabled Functions without Multi-AZ Redundancy](#aws-lambda-vpc-enabled-functions-without-multi-az-redundancy)
+ [AWS Outposts Single Rack deployment](#aws-outposts-single-rack-deployment)
+ [AWS Resilience Hub Application Component check](#amazon-resilience-hub-application-component-check)
+ [AWS Resilience Hub policy breached](#aws-resilience-hub-policy-breached)
+ [AWS Resilience Hub resilience scores](#aws-resilience-hub-resilience-scores)
+ [AWS Resilience Hub assessment age](#aws-resilience-hub-assessment-age)
+ [AWS Site-to-Site VPN has at least one tunnel in DOWN status](#aws-site-to-site-vpn-tunnel-in-down-status)
+ [AWS STS global endpoint usage across AWS Regions](#sts-global-endpoint)
+ [AWS Well-Architected high risk issues for reliability](#well-architected-high-risk-issues-reliability)
+ [Classic Load Balancer has no multiple AZs configured](#classic-load-balancewr-no-multi-azs)
+ [CLB Connection Draining](#elb-connection-draining)
+ [ELB Target Imbalance](#elb-target-imbalance)
+ [GWLB - endpoint AZ independence](#gwlb-endpoint-az-independence)
+ [Load Balancer Optimization](#load-balancer-optimization)
+ [NAT Gateway AZ Independence](#nat-gateway-az-independence)
+ [Network Firewall endpoint AZ Independence](#network-firewall-endpoint-az-independence)
+ [Network Firewall Multi-AZ](#network-firewall-multi-az)
+ [Network Load Balancers Cross Load Balancing](#network-load-balancers-cross-load-balancing)
+ [NLB - Internet-facing resource in private subnet](#nlb-internet-facing-resources-private-subnet)
+ [NLB Multi-AZ](#nlb-multi-az)
+ [Number of AWS Regions in an Incident Manager replication set](#number-of-aws-regions-in-an-incident-manager-replication-set)
+ [Single AZ Application Check](#single-az-application-check)
+ [VPC interface endpoint network interfaces in multiple AZs](#vpc-interface-endpoint-network-interface-multi-az)
+ [VPN Tunnel Redundancy](#vpn-tunnel-redundancy)
+ [ActiveMQ Availability Zone Redundancy](#activemq-availability-zone-redundancy)
+ [RabbitMQ Availability Zone Redundancy](#rabbitmq-availability-zone-redundancy)

## ALB Multi-AZ
<a name="alb-multi-az"></a>

**Description**  
Checks if your Application Load Balancers are configured to use more than one Availability Zone (AZ). An AZ is a distinct location that is insulated from failures in other zones. Configure your load balancer in multiple AZs in the same Region to help improve your workload availability.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dfprch08`

**Alert Criteria**  
Yellow: ALB is in a single AZ.  
Green: ALB has two or more AZs.

**Recommended Action**  
Make sure that your load balancer is configured with at least two Availability Zones.   
For more information, see [Availability Zones for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html).

**Additional Resources**  
For more information, see the following documentation:  
+ [How Elastic Load Balancing works](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#AZ-Region)
+ [Regions, Availability Zones, and Local Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html)

**Report columns**  
+ Status
+ Region
+ ALB Name
+ ALB Rule
+ ALB ARN
+ Number of AZs
+ Last Updated Time

## Amazon Aurora MySQL cluster backtracking not enabled
<a name="amazon-aurora-mysql-cluster-backtracking-not-enabled"></a>

**Description**  
Checks if an Amazon Aurora MySQL cluster has backtracking enabled.  
Amazon Aurora MySQL cluster backtracking is a feature that allows you to restore an Aurora DB cluster to a previous point in time without creating a new cluster. It enables you to roll back your database to a specific point in time within a retention period, without the need to restore from a snapshot.  
You can adjust the backtracking time window (hours) in the **BacktrackWindowInHours** parameter of the AWS Config rules.  
For more information, see [Backtracking an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz131`

**Source**  
`AWS Config Managed Rule: aurora-mysql-backtracking-enabled`

**Alert Criteria**  
Yellow: Amazon Aurora MySQL clusters backtracking is not enabled.

**Recommended Action**  
Turn on backtracking for your Amazon Aurora MySQL cluster.  
For more information, see [Backtracking an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html).

**Additional Resources**  
[Backtracking an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon Aurora DB Instance Accessibility
<a name="amazon-aurora-db-instance-accessibility"></a>

**Description**  
Checks for cases where an Amazon Aurora DB cluster has both private and public instances.   
When your primary instance fails, a replica can be promoted to a primary instance. If that replica is private, users who have only public access would no longer be able to connect to the database after failover. We recommend that all the DB instances in a cluster have the same accessibility.

**Check ID**  
`xuy7H1avtl`

**Alert Criteria**  
Yellow: The instances in an Aurora DB cluster have different accessibility (a mix of public and private).

**Recommended Action**  
Modify the `Publicly Accessible` setting of the instances in the DB cluster so that they are all either public or private. For details, see the instructions for MySQL instances at [Modifying a DB Instance Running the MySQL Database Engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.MySQL.html).

**Additional Resources**  
[Fault Tolerance for an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Managing.html#Aurora.Managing.FaultTolerance)

**Report columns**  
+ Status
+ Region
+ Cluster
+ Public DB Instances
+ Private DB Instances
+ Reason

## Amazon CloudFront Origin Failover
<a name="amazon-cloudfront-origin-failover"></a>

**Description**  
Checks that an origin group is configured for distributions that include two origins in Amazon CloudFront.  
For more information, see [Optimizing high availability with CloudFront origin failover](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz112`

**Source**  
`AWS Config Managed Rule: cloudfront-origin-failover-enabled`

**Alert Criteria**  
Yellow: Amazon CloudFront origin failover is not enabled.

**Recommended Action**  
Make sure that you turn on the origin failover feature for your CloudFront distributions to help ensure high availability of your content delivery to end users. When you turn on this feature, traffic is automatically routed to the backup origin server if the primary origin server is unavailable. This minimizes potential downtime and ensures continuous availability of your content.

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon Comprehend Endpoint Access Risk
<a name="amazon-comprehend-endpoint-access-risk"></a>

**Description**  
Checks the AWS Key Management Service (AWS KMS) key permissions for an endpoint where the underlying model was encrypted by using customer managed keys. If the customer managed key is disabled, or the key policy was changed to alter the allowed permissions for Amazon Comprehend, the endpoint availability might be affected.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Cm24dfsM13`

**Alert Criteria**  
Red: The customer managed key is disabled or the key policy was changed to alter the allowed permissions for Amazon Comprehend access.

**Recommended Action**  
If the customer managed key was disabled, we recommend that you enable it. For more information, see [Enabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html). If the key policy was altered and you want to keep using the endpoint, we recommend that you update the AWS KMS key policy. For more information, see [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html).

**Additional Resources**  
[AWS KMS Permissions](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html)

**Report columns**  
+ Status
+ Region
+ Endpoint ARN
+ Model ARN
+ KMS KeyId
+ Last Updated Time

## Amazon DocumentDB Single AZ Clusters
<a name="amazon-documentdb-single-az-clusters"></a>

**Description**  
Checks if there are Amazon DocumentDB clusters configured as Single-AZ.  
 Running Amazon DocumentDB workloads in a Single-AZ architecture is not sufficient for highly critical workloads and it can take up to 10 minutes to recover from a component failure. Customers should deploy replica instances in additional availability zones to ensure availability during maintenance, instance failures, component failures, or availability zone failures.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c15vnddn2x`

**Alert Criteria**  
Yellow: Amazon DocumentDB cluster has instances in less than three availability zones.  
 Green: Amazon DocumentDB cluster has instances in three availability zones.

**Recommended Action**  
If your application requires high availability, modify your DB instance to enable Multi-AZ using replica instances. See [Amazon DocumentDB High Availability and Replication](https://docs.aws.amazon.com/documentdb/latest/developerguide/replication.html)

**Additional Resources**  
[Understanding Amazon DocumentDB Cluster Fault Tolerance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-fault-tolerance.html)  
[Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html)

**Report columns**  
+ Status
+ Region
+ Availability Zone
+ DB Cluster Identifier
+ DB Cluster ARN
+ Last Updated Time

## Amazon DynamoDB Point-in-time Recovery
<a name="amazon-dynamodb-table-point-in-time-recovery"></a>

**Description**  
Checks if point-in time-recovery is enabled for your Amazon DynamoDB tables.  
Point-in time-recovery helps protect your DynamoDB tables from accidental write or delete operations. With point-in time-recovery, you don't have to worry about creating, maintaining, or scheduling on-demand backups. Point-in time-recovery restores tables to any point in time during the last 35 days. DynamoDB maintains incremental backups of your table.  
For more information, see [Point-in-time recovery for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz138`

**Source**  
`AWS Config Managed Rule: dynamodb-pitr-enabled`

**Alert Criteria**  
Yellow: Point-in-time recovery is not enabled for your DynamoDB tables.

**Recommended Action**  
Turn on point-in-time recovery in Amazon DynamoDB to continuously back up your table data.  
For more information, see [Point-in-time recovery: How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html).

**Additional Resources**  
[Point-in-time recovery for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon DynamoDB Table Not Included in Backup Plan
<a name="amazon-dynamodb-table-not-in-backup-plan"></a>

**Description**  
Checks if Amazon DynamoDB tables are part of an AWS Backup plan.  
AWS Backup provides incremental backups for DynamoDB tables that capture changes made since the last backup. Including DynamoDB tables in an AWS Backup plan helps protect your data from accidental data loss scenarios and automates the backup process. This provides a reliable and scalable backup solution for your DynamoDB tables, helping to ensure that your valuable data is protected and available for recovery as needed.  
For more information, see [Creating backups of DynamoDB tables with AWS Backup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CreateBackupAWS.html)  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz107`

**Source**  
`AWS Config Managed Rule: dynamodb-in-backup-plan`

**Alert Criteria**  
Yellow: Amazon DynamoDB table is not included in AWS Backup plan.

**Recommended Action**  
Ensure that your Amazon DynamoDB tables are part of an AWS Backup plan.

**Additional Resources**  
[Scheduled backups](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CreateBackupAWS.html#CreateBackupAWS_scheduled)  
[What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)  
[Creating backup plans using the AWS Backup console](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html#create-backup-plan-console)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EBS Not Included in AWS Backup Plan
<a name="amazon-ebs-not-in-backup-plan"></a>

**Description**  
Checks if Amazon EBS volumes are present in backup plans for AWS Backup.   
Include Amazon EBS volumes in an AWS Backup plan to automate regular backups for the data stored on those volumes. This protects you against data loss, makes data management easier, and allows for data restoration when needed. A backup plan helps to ensure that your data is safe and that you're able to meet recovery time and point objectives (RTO/RPO) for your application and services.  
For more information, see [Creating a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz106`

**Source**  
`AWS Config Managed Rule: ebs-in-backup-plan`

**Alert Criteria**  
Yellow: Amazon EBS volume is not included in AWS Backup plan.

**Recommended Action**  
Make sure that your Amazon EBS volumes are part of an AWS Backup plan.

**Additional Resources**  
[Creating backup plans using the AWS Backup console](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html#create-backup-plan-console)  
[What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)  
[Getting started 3: Create a scheduled backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-a-scheduled-backup.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EBS Snapshots
<a name="amazon-ebs-snapshots"></a>

**Description**  
Checks the age of the snapshots for your Amazon EBS volumes (either available or in-use). Failures can occur even if Amazon EBS volumes are replicated. Snapshots are persisted to Amazon S3 for durable storage and point-in-time recovery.

**Check ID**  
`H7IgTzjTYb`

**Alert Criteria**  
+ Yellow: The most recent volume snapshot is between 7 and 30 days old.
+ Red: The most recent volume snapshot is more than 30 days old.
+ Red: The volume does not have a snapshot.

**Recommended Action**  
Create weekly or monthly snapshots of your volumes. For more information, see [Creating an Amazon EBS Snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html).  
To automate the creation of EBS snapshots, you can consider using [AWS Backup](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/new-ebs-volume-backups.html#aws-backup-volume) or [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/new-ebs-volume-backups.html#amazon-dlm).

**Additional Resources**  
[Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)  
[Amazon EBS Snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)  
[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)  
[Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)

**Report columns**  
+ Status
+ Region
+ Volume ID
+ Volume Name
+ Snapshot ID
+ Snapshot Name
+ Snapshot Age
+ Volume Attachment
+ Reason

## Amazon EC2 Auto Scaling does not have ELB Health Check Enabled
<a name="amazon-ec2-auto-scaling-group-no-elb-health-check"></a>

**Description**  
Checks if your Amazon EC2 Auto Scaling groups that are associated with a Classic Load Balancer are using Elastic Load Balancing health checks. The default health checks for an Auto Scaling group are Amazon EC2 status checks only. If an instance fails these status checks, it is marked unhealthy and is terminated. Amazon EC2 Auto Scaling launches a new replacement instance. The Elastic Load Balancing health check periodically monitors Amazon EC2 instances to detect and terminate unhealthy instances and then launch new instances.  
For more information, see [Add Elastic Load Balancing health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-elb-healthcheck.html#as-add-elb-healthcheck-console).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz104`

**Source**  
`AWS Config Managed Rule: autoscaling-group-elb-healthcheck-required` 

**Alert Criteria**  
Yellow: Amazon EC2 Auto Scaling group attached to Classic Load Balancer has not enabled Elastic Load Balancing health checks.

**Recommended Action**  
Ensure that your Auto Scaling groups that are associated with a Classic Load Balancer use Elastic Load Balancing health checks.   
Elastic Load Balancing health checks report if the load balancer is healthy and available to handle requests. This ensures high availability for your application.  
For more information, see [Add Elastic Load Balancing health checks to an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-elb-healthcheck.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EC2 Auto Scaling Group has Capacity Rebalancing Enabled
<a name="amazon-ec2-auto-scaling-group-capacity-rebalance-enabled"></a>

**Description**  
Checks if Capacity Rebalancing is enabled for Amazon EC2 Auto Scaling groups that use multiple instance types.  
Configuring Amazon EC2 Auto Scaling groups with capacity rebalancing helps ensure that Amazon EC2 instances are evenly distributed across Availability Zones, regardless of instance types and purchasing options. It uses a target tracking policy associated with the group, such as CPU utilization or network traffic.   
For more information, see [Auto Scaling groups with multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html#as-mixed-instance-types.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`AWS Config c18d2gz103`

**Source**  
AWS Config Managed Rule: autoscaling-capacity-rebalancing 

**Alert Criteria**  
Yellow: Amazon EC2 Auto Scaling group capacity rebalancing is not enabled.

**Recommended Action**  
Ensure that capacity rebalancing is enabled for your Amazon EC2 Auto Scaling groups that use multiple instance types.  
For more information, see [Enable Capacity Rebalancing (console)](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html#enable-capacity-rebalancing-console.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EC2 Auto Scaling is not deployed in multiple AZs or does not meet the minimum number of AZs
<a name="amazon-ec2-auto-scaling-group-multiple-az"></a>

**Description**  
Checks if the Amazon EC2 Auto Scaling group is deployed in multiple Availability Zones, or the minimum number of Availability Zones specified. Deploy Amazon EC2 instances in multiple Availability Zones to ensure high availability.  
You can adjust the minimum number of Availability Zones using the **minAvailibilityZones** parameter in your AWS Config rules.  
For more information, see [Auto Scaling groups with multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html).

**Check ID**  
`c18d2gz101`

**Source**  
`AWS Config Managed Rule: autoscaling-multiple-az`

**Alert Criteria**  
Red: The Amazon EC2 Auto Scaling group doesn't have multiple AZs configured, or doesn't meet the minimum number of AZs specified.

**Recommended Action**  
Make sure that your Amazon EC2 Auto Scaling group is configured with multiple AZs. Deploy Amazon EC2 instances in multiple Availability Zones to ensure high availability.

**Additional Resources**  
[Create an Auto Scaling group using a launch template](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html)  
[Create an Auto Scaling group using a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-configuration.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EC2 Availability Zone Balance
<a name="amazon-ec2-availability-zone-balance"></a>

**Description**  
Checks the distribution of Amazon Elastic Compute Cloud (Amazon EC2) instances across Availability Zones in a Region.   
Availability Zones are distinct locations that are insulated from failures in other Availability Zones. This allows inexpensive, low-latency network connectivity between Availability Zones in the same Region. By launching instances in multiple Availability Zones in the same Region, you can help protect your applications from a single point of failure.

**Check ID**  
`wuy7G1zxql`

**Alert Criteria**  
+  Yellow: The Region has instances in multiple zones, but the distribution is uneven (the difference between the highest and lowest instance counts in utilized Availability Zones is greater than 20%).
+  Red: The Region has instances only in a single Availability Zone.

**Recommended Action**  
Balance your Amazon EC2 instances evenly across multiple Availability Zones. You can do this by launching instances manually or by using Auto Scaling to do it automatically. For more information, see [Launch Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html) and [Load Balance Your Auto Scaling Group](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/US_SetUpASLBApp.html).

**Additional Resources**  
+ [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/)
+ [Placement groups for your Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
+ [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)

**Report columns**  
+ Status
+ Region
+ Zone a Instances
+ Zone b Instances
+ Zone c Instances
+ Zone e Instances
+ Zone f Instances
+ Reason

## Amazon EC2 detailed monitoring not enabled
<a name="amazon-ec2-detailed-monitoring-not-enabled"></a>

**Description**  
Checks if detailed monitoring is enabled for yourAmazon EC2 instances.  
Amazon EC2 detailed monitoring provides more frequent metrics, published at one-minute intervals, instead of the five-minute intervals used in Amazon EC2 basic monitoring. Enabling detailed monitoring for Amazon EC2 helps you better manage your Amazon EC2 resources, so that you can find trends and take action faster.  
For more information, see [Basic monitoring and detailed monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`AWS Config c18d2gz144`

**Source**  
AWS Config Managed Rule: ec2-instance-detailed-monitoring-enabled 

**Alert criteria**  
Yellow: Detailed monitoring is not enabled for Amazon EC2 instances.

**Recommended action**  
Turn on detailed monitoring for your Amazon EC2 instances to increase the frequency at which Amazon EC2 metric data is published to Amazon CloudWatch (from 5-minute to 1-minute intervals).

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon ECS AWSLogs driver in blocking mode
<a name="amazon-ecs-awslogs-driver-blockingmode"></a>

**Description**  
Checks for Amazon ECS task definitions configured with the AWSLogs logging driver in blocking mode. A driver configured in the blocking mode risks system availability.  
This check does not consider account-level driver configuration settings.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dvkm4z6b`

**Alert criteria**  
Yellow: The awslogs driver logging configuration parameter mode is set to blocking.  
Green: Amazon ECS task definition is not using the awslogs driver or the awslogs driver is configured in non-blocking mode.

**Recommended action**  
To mitigate the availability risk, consider changing the task definition AWSLogs driver configuration from blocking to non-blocking. With non-blocking mode, you will have to set a value for the max-buffer-size parameter. For more information and guidance on configuration parameters, see [Preventing log loss with non-blocking mode in the AWSLogs container log driver](https://aws.amazon.com/blogs/containers/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/).

**Additional resources**  
[Using the AWS logs log driver](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html)  
[Choosing container logging options to avoid backpressure](https://aws.amazon.com/blogs/containers/choosing-container-logging-options-to-avoid-backpressure/)  
[Preventing log loss with non-blocking mode in the AWSLogs container log driver](https://aws.amazon.com/blogs/containers/preventing-log-loss-with-non-blocking-mode-in-the-awslogs-container-log-driver/)

**Report columns**  
+ Status
+ Region
+ Task Definition ARN
+ Container Definition Names
+ Last Updated Time

## Amazon ECS service using a single AZ
<a name="amazon-ecs-service-single-az"></a>

**Description**  
Checks that your service configuration uses a single Availability Zone (AZ).  
An AZ is a distinct location that is insulated from failures in other zones. This supports inexpensive, low-latency network connectivity between AZs in the same AWS Region. By launching instances in multiple AZs in the same Region, you can help protect your applications from a single point of failure.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7dfpz01`

**Alert criteria**  
+ Yellow: An Amazon ECS service is running all tasks in a single AZ.
+ Green: An Amazon ECS service is running tasks in at least two different AZs.

**Recommended action**  
Create at least one more task for the service in a different AZ.

**Additional resources**  
[ Amazon ECS capacity and availability](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/capacity-availability.html)

**Report columns**  
+ Status
+ Region
+ ECS Cluster Name/ECS Service Name
+ Number of Availability Zones
+ Last Updated Time

## Amazon ECS Multi-AZ placement strategy
<a name="amazon-ecs-multi-az-placement-strategy"></a>

**Description**  
Checks that your Amazon ECS service uses the spread placement strategy based on Availability Zone (AZ). This strategy distributes tasks across Availability Zones in the same AWS Region and can help protect your applications from a single point of failure.  
For tasks that run as part of an Amazon ECS service, spread is the default task placement strategy.  
This check also verifies that spread is the first or only strategy in your list of enabled placement strategies.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7dfpz02`

**Alert criteria**  
+ Yellow: Spread by availability zone is disabled or isn't the first strategy in your list of enabled placement strategies for your Amazon ECS service.
+ Green: Spread by availability zone is the first strategy in your list of enabled placement strategies or the only placement strategy enabled for your Amazon ECS service.

**Recommended action**  
Enable the spread task placement strategy to distribute tasks across multiple AZs. Verify that spread by availability zone is the first strategy for all enabled task placement strategies or the only strategy used. If you choose to manage AZ placement, you can use a mirrored service in another AZ to mitigate these risks.

**Additional resources**  
[ Amazon ECS task placement strategies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html)

**Report columns**  
+ Status
+ Region
+ ECS Cluster Name/ECS Service Name
+ Spread Task Placement Strategy Enabled and Applied Correctly
+ Last Updated Time

## Amazon EFS no mount target redundancy
<a name="amazon-efs-no-mount-target-redundancy"></a>

**Description**  
Checks if mount targets exist in multiple Availability Zones for an Amazon EFS file system.  
An Availability Zone is a distinct location that is insulated from failures in other zones. By creating mount targets in multiple geographically separated Availability Zones within an AWS Region, you can achieve the highest levels of availability and durability for your Amazon EFS file systems.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dfprch01`

**Alert criteria**  
+ Yellow: File system has 1 mount target created in a single Availability Zone.

  Green: File system has 2 or more mount targets created in multiple Availability Zones.

**Recommended action**  
For EFS file systems using One Zone storage classes, we recommend you create new file systems that use Standard storage classes by restoring a backup to a new file system. Then create mount targets in multiple Availability Zones.  
For EFS file systems using Standard storage classes, we recommend you create mount targets in multiple Availability Zones.

**Additional resources**  
+ [Managing mount targets using the Amazon EFS console](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)
+ [Amazon EFS Quotas and Limits](https://docs.aws.amazon.com/efs/latest/ug/limits.html)

**Report columns**  
+ Status
+ Region
+ EFS File System ID
+ Number of mount targets
+ Number of AZs
+ Last Updated Time

## Amazon EFS not in AWS Backup plan
<a name="amazon-efs-not-in-backup-plan"></a>

**Description**  
Checks if Amazon EFS file systems are included in backup plans with AWS Backup.   
AWS Backup is a unified backup service designed to simplify the creation, migration, restoration, and deletion of backups, while providing improved reporting and auditing.  
 For more information, see [Backing up your Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html).

**Check ID**  
`c18d2gz117`

**Source**  
`AWS Config Managed Rule: EFS_IN_BACKUP_PLAN`

**Alert criteria**  
Red: Amazon EFS file systems aren't included in AWS Backup plan.

**Recommended action**  
Make sure that your Amazon EFS file systems are included in your AWS Backup plan to protect against accidental data loss or data corruption.

**Additional resources**  
[Backing up your Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html)  
[Amazon EFS Backup and Restore using AWS Backup](https://aws.amazon.com/getting-started/hands-on/amazon-efs-backup-and-restore-using-aws-backup/).

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon ElastiCache Multi-AZ clusters
<a name="amazon-elasticache-multi-az-clusters"></a>

**Description**  
Checks for ElastiCache clusters that deploy in a single Availability Zone (AZ). This check alerts you if Multi-AZ is inactive in a cluster.  
Deployments in multiple AZs enhance ElastiCache cluster availability by asynchronously replicating to read-only replicas in a different AZ. When planned cluster maintenance occurs, or a primary node is unavailable, ElastiCache automatically promotes a replica to primary. This failover allows cluster write operations to resume, and doesn't require an administrator to intervene.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`ECHdfsQ402`

**Alert criteria**  
+ Green: Multi-AZ is active in the cluster.
+ Yellow: Multi-AZ is inactive in the cluster.

**Recommended action**  
Create at least one replica per shard, in an AZ that is different than the primary.

**Additional resources**  
For more information, see [Minimizing downtime in ElastiCache (Redis OSS) with Multi-AZ](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/AutoFailover.html).

**Report columns**  
+ Status
+ Region
+ Cluster Name
+ Last Updated Time

## ElastiCache (Redis OSS) Clusters Automatic Backup
<a name="amazon-elasticache-redis-clusters-auto-backup"></a>

**Description**  
Checks if the Amazon ElastiCache (Redis OSS) clusters have automatic backup turned on and if the snapshot retention period is above the specified or 15 day default limit. When automatic backups are enabled, ElastiCache creates a backup of the cluster on a daily basis.  
You can specify your desired snapshot retention limit using the **snapshotRetentionPeriod** parameters of your AWS Config rules.  
For more information, see [Backup and restore for ElastiCache (Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz178`

**Source**  
`AWS Config Managed Rule: elasticache-redis-cluster-automatic-backup-check`

**Alert Criteria**  
Red: Amazon ElastiCache (Redis OSS) clusters do not have automatic backup turned on or the snapshot retention period is below the limit.

**Recommended Action**  
Make sure that Amazon ElastiCache (Redis OSS) clusters have automatic backup turned on and the snapshot retention period is above the specified or 15 day default limit. Automatic backups can help guard against data loss. In the event of a failure, you can create a new cluster, restoring your data from the most recent backup.  
For more information, see [Backup and restore for ElastiCache (Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups.html).

**Additional Resources**  
For more information, see [Scheduling automatic backups](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-automatic.html).

**Report columns**  
+ Status
+ Region
+ Cluster Name
+ Last Updated Time

## Amazon MemoryDB Multi-AZ clusters
<a name="amazon-memorydb-multi-az-clusters"></a>

**Description**  
Checks for MemoryDB clusters that deploy in a single Availability Zone (AZ). This check alerts you if Multi-AZ is inactive in a cluster.  
Deployments in multiple AZs enhance MemoryDB cluster availability by asynchronously replicating to read-only replicas in a different AZ. When planned cluster maintenance occurs, or a primary node is unavailable, MemoryDB automatically promotes a replica to primary. This failover allows cluster write operations to resume, and doesn't require an administrator to intervene.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`MDBdfsQ401`

**Alert Criteria**  
+ Green: Multi-AZ is active in the cluster.
+ Yellow: Multi-AZ is inactive in the cluster.

**Recommended Action**  
Create at least one replica per shard, in an AZ that is different than the primary.

**Additional Resources**  
For more information, see [Minimizing downtime in MemoryDB with Multi-AZ](https://docs.aws.amazon.com/memorydb/latest/devguide/autofailover.html).

**Report columns**  
+ Status
+ Region
+ Cluster Name
+ Last Updated Time

## Amazon MSK brokers hosting too many partitions
<a name="amazon-msk-brokers-hosting-too-many-partitions"></a>

**Description**  
 Checks that the brokers of a Managed Streaming for Kafka (MSK) Cluster do not have more than the recommended number of partitions assigned.

**Check ID**  
`Cmsvnj8vf1`

**Alert Criteria**  
+ Red: Your MSK broker has reached or exceeded 100% of the recommended maximum partition limit
+ Yellow: Your MSK has reached 80% of the recommended maximum partition limit

**Recommended Action**  
Follow the MSK [recommended best practices ](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html) to scale your MSK Cluster or delete any unused partitions.

**Additional Resources**  
+ [Right-sizing your Cluster](https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-your-apache-kafka-clusters-to-optimize-performance-and-cost/)

**Report columns**  
+ Status
+ Region
+ Cluster ARN
+ Broker ID
+ Partition Count

## Amazon MSK Cluster Multi-AZ
<a name="amazon-msk-cluster-multi-az"></a>

**Description**  
Checks the number of Availability Zones (AZs) for your Amazon MSK provisioned cluster. The Amazon MSK cluster is formed of several brokers that work together and distribute the data and load. Production might be interrupted during maintenance or broker issues in a 2-AZ cluster.

**Check ID**  
`90046ff5b5`

**Alert Criteria**  
+ Yellow: The Amazon MSK cluster is provisioned with brokers in only two AZs
+ Green: The Amazon MSK cluster is provisioned with brokers across three or more AZs

**Recommended Action**  
To increase availability of the cluster, you can create another cluster in a 3 AZs setup. Then migrate the existing cluster to the new cluster that you created. You can use Amazon MSK replication for this migration.

**Additional Resources**  
[Amazon MSK high availability](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html#ensure-high-availability)  
[Amazon MSK migration](https://docs.aws.amazon.com/msk/latest/developerguide/migration.html)

**Report columns**  
+ Status
+ Region
+ MSK Cluster ARN
+ Number of AZs
+ Last Updated Time

## Amazon OpenSearch Service domains with less than three data nodes
<a name="amazon-opensearch-service-domains-less-than-three-nodes"></a>

**Description**  
Checks if Amazon OpenSearch Service domains are configured with at least three data nodes and ZoneAwarenessEnabled is true. With ZoneAwarenessEnabled enabled, Amazon OpenSearch Service ensures that each primary shard and its corresponding replica are allocated in different Availability Zones.  
For more information, see [Configuring a multi-AZ domain in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz183`

**Source**  
`AWS Config Managed Rule: opensearch-data-node-fault-tolerance`

**Alert Criteria**  
Yellow: Amazon OpenSearch Service domains are configured with less than three data nodes.

**Recommended Action**  
Make sure that Amazon OpenSearch Service domains are configured with a minimum of three data nodes. Configure a multi-AZ domain to enhance the availability of the Amazon OpenSearch Service cluster by allocating nodes and replicating data across three Availability Zones within the same Region. This prevents data loss and minimizes downtime in the event of node or data center (AZ) failure.  
For more information, see [Increase availability for Amazon OpenSearch Service by deploying in three Availability Zones](https://aws.amazon.com/blogs/big-data/increase-availability-for-amazon-opensearch-service-by-deploying-in-three-availability-zones/).

**Additional Resources**  
+ [Increase availability for Amazon OpenSearch Service by deploying in three Availability Zones](https://aws.amazon.com/blogs/big-data/increase-availability-for-amazon-opensearch-service-by-deploying-in-three-availability-zones/)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon RDS Backups
<a name="amazon-rds-backups"></a>

**Description**  
Checks for automated backups of Amazon RDS DB instances.   
By default, backups are enabled with a retention period of one day. Backups reduce the risk of unexpected data loss and allow for point-in-time recovery.   
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`opQPADkZvH`

**Alert Criteria**  
Red: A DB instance has the backup retention period set to 0 days.

**Recommended Action**  
Set the retention period for the automated DB instance backup to 1 to 35 days as appropriate to the requirements of your application. See [Working With Automated Backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html).

**Additional Resources**  
[Getting Started with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)

**Report columns**  
+ Status
+ Region/AZ
+ DB Instance
+ VPC ID
+ Backup Retention Period

## Amazon RDS Continuous Backup Not Enabled
<a name="amazon-rds-cont-backups"></a>

**Description**  
Checks if an Amazon RDS instance is enabled with automated backups using Amazon RDS or with continuous backups of AWS Backup. Continuous backups reduce the risk of unexpected data loss and allow for point-in-time recovery.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`44fde09ab5`

**Alert Criteria**  
+ Red: The instance doesn't have automated backup enabled in Amazon RDS or continuous backup in AWS Backup.
+ Red: MySQL versions below 5.6 don't support automated or continuous backup. To provide resiliency, first upgrade the database version and then enable automated or continuous backup.
+ Green: The instance has automated backup enabled in Amazon RDS.
+ Green: The instance has continuous backup enabled in AWS Backup.

**Recommended Action**  
Make sure that Amazon RDS instances have automated backup configured either by setting a retention period greater than 0 in Amazon RDS or by creating a continuous backup plan using AWS Backup.

**Additional Resources**  
+ [Getting Started with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)
+ [Managing automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.html)
+ [Introduction to backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
+ [Continuous backups and point-in-time restore (PITR)](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html)
+ [AWS Backup feature availability](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html)

**Report columns**  
+ Status
+ Region
+ DB Instance Identifier
+ DB Instance ARN
+ Deployment Type
+ Backup Type
+ Reason
+ Last Updated Time

## Amazon RDS DB clusters have one DB instance
<a name="amazon-rds-db-clusters-one-db-instance"></a>

**Description**  
Add at least another DB instance to the DB cluster to improve availability and performance.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt011`

**Alert Criteria**  
Yellow: DB clusters have only one DB instance.

**Recommended Action**  
Add a reader DB instance to the DB cluster.

**Additional Resources**  
In the current configuration, one DB instance is used for both read and write operations. You can add another DB instance to allow read redistribution and a failover option.   
For more information, see [High availability for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ Engine Name
+ DB Instance Class
+ Last Updated Time

## Amazon RDS DB clusters with all instances in the same Availability Zone
<a name="amazon-rds-db-clusters-same-az"></a>

**Description**  
The DB clusters are currently in a single Availability Zone. Use multiple Availability Zones to improve the availability.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt007`

**Alert Criteria**  
Yellow: DB clusters have all the instances in the same Availability Zone.

**Recommended Action**  
Add the DB instances to multiple Availability Zones in your DB cluster.

**Additional Resources**  
We recommend that you add the DB instances to multiple Availability Zones in a DB cluster. Adding DB instances to multiple Availability Zones improvesthe availability of your DB cluster.  
For more information, see [High availability for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ Engine Name
+ Last Updated Time

## Amazon RDS DB clusters with all reader instances in the same Availability Zone
<a name="amazon-rds-reader-instances-same-az"></a>

**Description**  
Your DB cluster has all the reader instances in the same Availability Zone. We recommend that you distribute the Reader instances across multiple Availability Zones in your DB cluster.  
Distribution increases the availability of the database, and improves the response time by reducing network latency between clients and the database.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt018`

**Alert Criteria**  
Red: DB clusters have the reader instances in the same Availability Zone.

**Recommended Action**  
Distribute the reader instances across multiple Availability Zones.

**Additional Resources**  
Availability Zones (AZs) are locations that are distinct from each other to provide isolation in case of outages within each AWS Region. We recommend that you distribute the primary instance and reader instances in your DB cluster across multiple AZs to improve the availability of your DB cluster. You can create a Multi-AZ cluster using the AWS Management Console, AWS CLI, or Amazon RDS API when you create the cluster. You can modify the existing Aurora cluster to a Multi-AZ cluster by adding a new reader instance and specifying a different AZ.  
For more information, see [High availability for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ Engine Name
+ Last Updated Time

## Amazon RDS DB Instance Enhanced Monitoring not enabled
<a name="amazon-rds-db-instance-enhanced-monitoring-not-enabled"></a>

**Description**  
Checks if your Amazon RDS DB instances have Enhanced Monitoring enabled.  
Amazon RDS Enhanced Monitoring provides metrics in real time for the operating system (OS) that your DB instance runs on. All system metrics and process information for your Amazon RDS DB instances can be view on the Amazon RDS console. And, you can customize the dashboard. With Enhanced Monitoring, you have visibility of your Amazon RDS instance operation status in near real time, allowing you to respond to operational issues faster.  
You can specify your desired monitoring interval using the **monitoringInterval** parameter of your AWS Config rules.  
For more information, see [Overview of Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.overview.html) and [OS metrics in Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring-Available-OS-Metrics.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz158`

**Source**  
`AWS Config Managed Rule: rds-enhanced-monitoring-enabled`

**Alert Criteria**  
Yellow: Your Amazon RDS DB instances don't have Enhanced Monitoring enabled or are not configured with the desired interval.

**Recommended Action**  
Enable Enhanced Monitoring for your Amazon RDS DB instances to improve the visibility of your Amazon RDS instance operation status.  
For more information, see [Monitoring OS metrics with Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html).

**Additional Resources**  
[OS metrics in Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring-Available-OS-Metrics.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon RDS DB instances have storage autoscaling turned off
<a name="amazon-rds-db-instance-storage-autoscaling-off"></a>

**Description**  
Amazon RDS storage autoscaling isn't turned on for your DB instance. When there is an increase in the database workload, RDS Storage autoscaling automatically scales the storage capacity with zero downtime.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt013`

**Alert Criteria**  
Red: DB instances don't have storage autoscaling turned on.

**Recommended Action**  
Turn on Amazon RDS storage autoscaling with a specified maximum storage threshold.

**Additional Resources**  
Amazon RDS storage autoscaling automatically scales storage capacity with zero downtime when the database workload increases. Storage autoscaling monitors the storage usage and automatically scales up the capacity when the usage is close to the provisioned storage capacity. You can specify a maximum limit on the storage that Amazon RDS can allocate to the DB instance. There is no additional cost for storage autoscaling. You pay only for the Amazon RDS resources that are allocated to your DB instance. We recommend that you turn on Amazon RDS storage autoscaling.  
For more information, see [Managing capacity automatically with Amazon RDS storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling).

**Report columns**  
+ Status
+ Region
+ Resource
+ Recommended Value
+ Engine Name
+ Last Updated Time

## Amazon RDS DB instances not using Multi-AZ deployment
<a name="amazon-rds-db-instances-not-using-multi"></a>

**Description**  
We recommend that you use Multi-AZ deployment. The Multi-AZ deployments enhance the availability and durability of the DB instance.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt019`

**Alert Criteria**  
Yellow: DB instances aren't using Multi-AZ deployment.

**Recommended Action**  
Set up Multi-AZ for the impacted DB instances.

**Additional Resources**  
In an Amazon RDS Multi-AZ deployment, Amazon RDS automatically creates a primary database instance and replicates the data to an instance in a different availability zone. When it detects a failure, Amazon RDS automatically fails over to a standby instance without manual intervention.   
For more information, see [Pricing](https://aws.amazon.com/rds/features/multi-az/#Pricing).

**Report columns**  
+ Status
+ Region
+ Resource
+ Engine Name
+ Last Updated Time

## Amazon RDS DiskQueueDepth
<a name="Amazon-RDS-DiskQueueDepth"></a>

**Description**  
Checks to see if the CloudWatch metric DiskQueueDepth shows that number of queued writes to the RDS Instance database storage has grown to a level where an operational investigation should be suggested.

**Check ID**  
`Cmsvnj8db3`

**Alert Criteria**  
+ Red: DiskQueueDepth CloudWatch metric has exceeded 10
+ Yellow: DiskQueueDepth CloudWatch metric is greater than 5 but less than or equal to 10
+ Green: DiskQueueDepth CloudWatch metric is less than or equal to 5

**Recommended Action**  
Consider moving to instances and storage volumes that support the read/write characteristics.

**Report columns**  
+ Status
+ Region
+ DB Instance ARN
+ DiskQueueDepth Metric

## Amazon RDS FreeStorageSpace
<a name="Amazon-RDS-FreeStorageSpace"></a>

**Description**  
Checks to see if the FreeStorageSpace CloudWatch metric for an RDS database instance has decreased below an operationally reasonable threshold.

**Check ID**  
`Cmsvnj8db2`

**Alert Criteria**  
+ Red: FreeStorageSpace has less than 10% of total capacity
+ Yellow: FreeStorageSpace is between 10% and 20% of total capacity
+ Green: FreeStorageSpace is more than 20% of total capacity

**Recommended Action**  
Scale up the storage space for the RDS database instance that is running low on free storage using the Amazon RDS Management Console, Amazon RDS API or AWS Command Line Interface.

**Report columns**  
+ Status
+ Region
+ DB Instance ARN
+ FreeStorageSpace Metric (MB)
+ DB Instance Allocated Storage (MB)
+ DB Instance Storage Used Percent

## Amazon RDS log\_output parameter is set to table
<a name="amazon-rds-log-parameter-set-to-table"></a>

**Description**  
When **log\_output** is set to **TABLE**, more storage is used than when **log\_output** is set to **FILE**. We recommend that you set the parameter to **FILE**, to avoid reaching the storage size limit.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt023`

**Alert Criteria**  
Yellow: DB parameter groups have **log\_output** parameter set to **TABLE**.

**Recommended Action**  
Set the **log\_output** parameter value to **FILE** in your DB parameter groups.

**Additional Resources**  
For more information, see [MySQL database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.MySQL.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS innodb\_default\_row\_format parameter setting is unsafe
<a name="rds-innodb-default-row-format-unsafe"></a>

**Description**  
Your DB instance encounters a known issue: A table created in a MySQL version lower than 8.0.26 with the **row\_format** set to **COMPACT** or **REDUNDANT** is inaccessible and unrecoverable when the index exceeds 767 bytes.  
We recommend that you set the **innodb\_default\_row\_format** parameter value to **DYNAMIC**.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt036`

**Alert Criteria**  
Red: DB parameter groups have an unsafe setting for the **innodb\_default\_row\_format** parameter.

**Recommended Action**  
Set the **innodb\_default\_row\_format** parameter to **DYNAMIC**.

**Additional Resources**  
When a table is created with MySQL version lower than 8.0.26 with **row\_format** set to **COMPACT** or **REDUNDANT**, creating indexes with a key prefix shorter than 767 bytes isn't enforced. After the database restarts, these tables can't be accessed or recovered.  
For more information, see [Changes in MySQL 8.0.26 (2021-07-20, General Availability)n](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-26.html#mysqld-8-0-26-bug%60) on the MySQL documentation website.

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS innodb\_flush\_log\_at\_trx\_commit parameter is not 1
<a name="rds-innodb-flush-log-at-trx-parameter-off"></a>

**Description**  
The value of the **innodb\_flush\_log\_at\_trx\_commit** parameter of your DB instance isn't a safe value. This parameter controls the persistence of commit operations to disk.  
We recommend that you set the **innodb\_flush\_log\_at\_trx\_commit** parameter to 1.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt030`

**Alert Criteria**  
Yellow: DB parameter groups have **innodb\_flush\_log\_at\_trx\_commit** set to other than 1.

**Recommended Action**  
Set the **innodb\_flush\_log\_at\_trx\_commit** parameter value to 1

**Additional Resources**  
The database transaction is durable when the log buffer is saved to the durable storage. However, saving to the disk impacts performance. Depending on the value set for **innodb\_flush\_log\_at\_trx\_commit** parameter, the behavior of how logs are written and saved to the disk can vary.  
+ When the parameter value is 1, the logs are written and saved to the disk after each committed transaction.
+  When the parameter value is 0, the logs are written and saved to the disk once per second.
+ When the parameter value is 2, the logs are written after each transaction is committed and saved to the disk once per second. The data moves from the InnoDB memory buffer to the operating system's cache which is also in the memory.
When the parameter value is not 1, InnoDB doesn't assure ACID properties. The recent transactions for the last second may be lost when the database crashes.
For more information, see [Best practices for configuring parameters for Amazon RDS for MySQL, part 1: Parameters related to performance](https://aws.amazon.com/blogs/database/best-practices-for-configuring-parameters-for-amazon-rds-for-mysql-part-1-parameters-related-to-performance/).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS max\_user\_connections parameter is low
<a name="rds-max-user-connections-parameter-low"></a>

**Description**  
Your DB instance has a low value for the maximum number of simultaneous connections for each database account.  
We recommend setting the **max\_user\_connections** parameter to a number greater than **5**.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt034`

**Alert Criteria**  
Yellow: DB parameter groups have **max\_user\_connections** misconfigured.

**Recommended Action**  
Increase the value of the **max\_user\_connections** parameter to a number greater than **5**.

**Additional Resources**  
The **max\_user\_connections** setting controls the maximum number of simultaneous connections allowed for a MySQL user account. Reaching this connection limit cause failures in the Amazon RDS instance administration operations, such as backup, patching, and parameters changes.  
For more information, see [Setting Account Resource Limits](https://dev.mysql.com/doc/refman/8.0/en/user-resources.html) on the MySQL documentation website.

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS Multi-AZ
<a name="amazon-rds-multi-az"></a>

**Description**  
Checks for DB instances that are deployed in a single Availability Zone (AZ).   
Multi-AZ deployments enhance database availability by synchronously replicating to a standby instance in a different Availability Zone. During planned database maintenance, or the failure of a DB instance or Availability Zone, Amazon RDS automatically fails over to the standby. This failover allows database operations to resume quickly without administrative intervention. Because Amazon RDS does not support Multi-AZ deployment for Microsoft SQL Server, this check does not examine SQL Server instances.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`f2iK5R6Dep`

**Alert Criteria**  
Yellow: A DB instance is deployed in a single Availability Zone.

**Recommended Action**  
If your application requires high availability, modify your DB instance to enable Multi-AZ deployment. See [High Availability (Multi-AZ)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).

**Additional Resources**  
[Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html)

**Report columns**  
+ Status
+ Region/AZ
+ DB Instance
+ VPC ID
+ Multi-AZ

## Amazon RDS Not In AWS Backup Plan
<a name="amazon-rds-not-in-backup-plan"></a>

**Description**  
Checks if your Amazon RDS DB instances are included in a backup plan in AWS Backup.  
AWS Backup is a fully managed backup service that makes it easy to centralize and automate backing up data across AWS services.  
Including your Amazon RDS DB instance in a backup plan is important for regulatory compliance obligations, disaster recovery, business policies for data protection, and business continuity goals.  
For more information, see [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz159`

**Source**  
`AWS Config Managed Rule: rds-in-backup-plan`

**Alert Criteria**  
Yellow: An Amazon RDS DB instance is not included in a backup plan with AWS Backup.

**Recommended Action**  
Include your Amazon RDS DB instances in a backup plan with AWS Backup.  
For more information, see [Amazon RDS Backup and Restore Using AWS Backup](https://aws.amazon.com/getting-started/hands-on/amazon-rds-backup-restore-using-aws-backup/).

**Additional Resources**  
[Assigning resources to a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon RDS Read Replicas are open in writable mode
<a name="rds-read-replicas-writable"></a>

**Description**  
Your DB instance has a read replica in writable mode, which allows updates from clients.  
We recommend that you set the the **read\_only** parameter to **TrueIfReplica** so that the read replicas isn't in writable mode.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt035`

**Alert Criteria**  
Yellow: DB parameter groups turn on writable mode for the read replicas.

**Recommended Action**  
Set the **read\_only** parameter value to **TrueIfReplica**.

**Additional Resources**  
The **read\_only** parameter controls the write permission from the clients to a database instance. The default value for this parameter is **TrueIfReplica**. For a replica instance, **TrueIfReplica** sets the **read\_only** value to ON (1) and disables any write activity from the clients. For a master/writer instance, **TrueIfReplica** sets the value to OFF (0) and enables the write activity from the clients for the instance. When the read replica is opened in writable mode, the data stored in this instance may diverge from the primary instance which causes replication errors.  
For more information, see [Best practices for configuring parameters for Amazon RDS for MySQL, part 2: Parameters related to replication](https://aws.amazon.com/blogs/database/best-practices-for-configuring-parameters-for-amazon-rds-for-mysql-part-2-parameters-related-to-replication/) on the MySQL documentation website.

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS resource automated backups is turned off
<a name="amazon-rds-auto-backup-off"></a>

**Description**  
Automated backups are disabled on your DB resources. Automated backups enable point-in-time recovery of your DB instance.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt001`

**Alert Criteria**  
Red: Amazon RDS resources don't have automated backups turned on

**Recommended Action**  
Turn on automated backups with a retention period of up to 14 days.

**Additional Resources**  
Automated backups enable point-in-time recovery of your DB instances. We recommend turning on automated backups. When you turn on automated backups for a DB instance, Amazon RDS automatically performs a full backup of your data daily during your preferred backup window. The backup captures transaction logs when there are updates to your DB instance. You get backup storage up to the storage size of your DB instance at no additional cost.  
For more information, see the following resources:  
+ [Enabling automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.Enabling)
+ [Demystifying Amazon RDS backup storage costs](https://aws.amazon.com/blogs/database/demystifying-amazon-rds-backup-storage-costs/)

**Report columns**  
+ Status
+ Region
+ Resource
+ Recommended Value
+ Engine Name
+ Last Updated Time

## Amazon RDS sync\_binlog parameter is turned off
<a name="rds-sync-binlog-parameter-off"></a>

**Description**  
The synchronization of the binary log to disk isn't enforced before the transaction commits are acknowledged in your DB instance.  
We recommend that you set the **sync\_binlog** parameter value to **1**.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt031`

**Alert Criteria**  
Yellow: DB parameter groups have synchronous binary logging turned off.

**Recommended Action**  
Set the **sync\_binlog** parameter to **1**.

**Additional Resources**  
The **sync\_binlog** parameter controls how MySQL pushes the binary log to disk. When the value of this parameter is set to **1**, it turns on binary log synchronization to disk before transactions are committed. When the value of this parameter is set to **0**, it turns off the binary log synchronization to the disk. Typically, MySQL server depends on the operating system to push the binary log to disk regularly similar to other files. The **sync\_binlog** parameter value set to **0** can enhance the performance. However, during a power failure or an operating system crash, the server loses all the committed transactions that weren't synchronized to the binary logs.  
For more information, see [Best practices for configuring parameters for Amazon RDS for MySQL, part 2: Parameters related to replication](https://aws.amazon.com/blogs/database/best-practices-for-configuring-parameters-for-amazon-rds-for-mysql-part-2-parameters-related-to-replication/).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## RDS DB Cluster has no Multi-AZ replication enabled
<a name="rds-db-cluster-multi-zone-replication-not-enabled"></a>

**Description**  
Checks if your Amazon RDS DB clusters have Multi-AZ replication enabled.  
A Multi-AZ DB cluster has a writer DB instance and two reader DB instances in three separate Availability Zones. Multi-AZ DB clusters provide high availability, increased capacity for read workloads, and lower latency when compared to Multi-AZ deployments.  
For more information, see [Creating a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz161`

**Source**  
`AWS Config Managed Rule: rds-cluster-multi-az-enabled`

**Alert Criteria**  
Yellow: Your Amazon RDS DB cluster does not have Multi-AZ replication configured

**Recommended Action**  
Turn on Multi-AZ DB cluster deployment when you create an Amazon RDS DB cluster.  
For more information, see [Creating a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html).

**Additional Resources**  
[Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## RDS Multi-AZ Standby Instance Not Enabled
<a name="rds-multi-az-standby-instance"></a>

**Description**  
Checks if your Amazon RDS DB instances have a Multi-AZ standby replica configured.  
Amazon RDS Multi-AZ provides high availability and durabiliy for database instances by replicating data to a standby replica in a different Availability Zone. This provides automatic failover, improve performance, and enhances data durability. In a Multi-AZ DB instance deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. The primary DB instance is synchronously replicated across Availability Zones to a standby replica to provide data redundancy and minimize latency spikes during system backups. Running a DB instance with high availability enhances availability during planned system maintenance. It can also help protect your databases against DB instance failure and Availability Zone disruption.  
For more information, see [Multi-AZ DB instance deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz156`

**Source**  
`AWS Config Managed Rule: rds-multi-az-support`

**Alert Criteria**  
Yellow: An Amazon RDS DB instance does not have a Multi-AZ replica configured.

**Recommended Action**  
Turn on Multi-AZ deployment when you create an Amazon RDS DB instance.  
This check can't be excluded from view in the Trusted Advisor console.

**Additional Resources**  
[Multi-AZ DB instance deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon RDS ReplicaLag
<a name="Amazon-RDS-ReplicaLag"></a>

**Description**  
Checks to see if the ReplicaLag CloudWatch metric for an RDS database instance has increased above an operationally reasonable threshold over the past week.  
ReplicaLag metric measures the number of seconds a read replica is behind the primary instance. Replication lag occurs when the asynchronous updates made to the read replica cannot keep up with the updates happening on the primary database instance. In the event of a failure to the primary instance, data could be missing from the read replica if the ReplicaLag is above an operationally reasonable threshold.

**Check ID**  
`Cmsvnj8db1`

**Alert Criteria**  
+ Red: ReplicaLag metric exceeded 60 seconds at least once during the week.
+ Yellow: ReplicaLag metric exceeded 10 seconds at least once during the week.
+ Green: ReplicaLag is less than 10 seconds.

**Recommended Action**  
There are several possible causes for ReplicaLag to increase beyond operationally safe levels. For example, it can be caused by recently replaced/launched replica instances from older backups and these replicas requiring substantial time to “catch-up” to the primary database instance and live transactions. This ReplicaLag may dwindle over time as catch-up occurs. Another example could be that the transaction velocity able to be achieved on the primary database instance is higher than the replication process or replica infrastructure is able to match. This ReplicaLag may grow over time as replication fails to keep pace with the primary database performance. Finally, the workload may be bursty throughout different periods of the day/month/etc. that result in occasional ReplicaLag to fall behind. Your team should investigate which possible root cause has contributed to high ReplicaLag for the database, and possibly change the database instance type or other characteristics of the workload to ensure data continuity on the replica matches your requirements.

**Additional Resources**  
+ [Working with read replicas for Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.html)
+ [Working with MySQL replication in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.html)
+ [Working with MySQL read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.html)

**Report columns**  
+ Status
+ Region
+ DB Instance ARN
+ ReplicaLag Metric

## Amazon RDS synchronous\_commit parameter is turned off
<a name="rds-synchronous-commit-parameter-off"></a>

**Description**  
When the **synchronous\_commit** parameter is turned off, data can be lost in a database crash. The durability of the database is at risk.  
We recommend that you turn on the **synchronous\_commit** parameter.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt026`

**Alert Criteria**  
Red: DB parameter groups have **synchronous\_commit** parameter turned off.

**Recommended Action**  
Turn on **synchronous\_commit** parameter in your DB parameter groups.

**Additional Resources**  
The **synchronous\_commit** parameter defines the Write-Ahead Logging (WAL) process completion before the database server sends a successful notification to the client. This commit is called as an asynchronous commit because the client acknowledges the commit before WAL saves the transaction in the disk. If the **synchronous\_commit** parameter is turned off, then the transactions can be lost, DB instance durability might be compromised, and data might be lost when a database crashes.  
For more information, see [MySQL database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.MySQL.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon Redshift cluster automated snapshots
<a name="amazon-redshift-cluster-automated-snapshots"></a>

**Description**  
Checks if automated snapshots are enabled for your Amazon Redshift clusters.  
Amazon Redshift automatically takes incremental snapshots that track changes to the cluster since the previous automated snapshot. Automated snapshots retain all of the data required to restore a cluster from a snapshot. To disable automated snapshots, set the retention period to zero. You can't disable automated snapshots for RA3 node types.  
You can specify your desired minimum and maximum retention period using the **MinRetentionPeriod** and **MaxRetentionPeriod** parameter of your AWS Config rules.  
[Amazon Redshift snapshots and backups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz135`

**Source**  
`AWS Config Managed Rule: redshift-backup-enabled`

**Alert Criteria**  
Red: Amazon Redshift does not have automated snapshots configured within the desired retention period.

**Recommended Action**  
Make sure that automated snapshots are enabled for your Amazon Redshift clusters.  
For more information, see [Managing snapshots using the console](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-snapshots-console.html).

**Additional Resources**  
[Amazon Redshift snapshots and backups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)  
For more information, see [Working with backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon Route 53 Deleted Health Checks
<a name="amazon-route-53-deleted-health-checks"></a>

**Description**  
Checks for resource record sets that are associated with health checks that have been deleted.  
Route 53 does not prevent you from deleting a health check that is associated with one or more resource record sets. If you delete a health check without updating the associated resource record sets, the routing of DNS queries for your DNS failover configuration will not work as intended.   
Hosted zones created by AWS services won't appear in your check results.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`Cb877eB72b`

**Alert Criteria**  
Yellow: A resource record set is associated with a health check that has been deleted.

**Recommended Action**  
Create a new health check and associate it with the resource record set. See [Creating, Updating, and Deleting Health Checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html) and [Adding Health Checks to Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-adding-to-rrsets.html). 

**Additional Resources**  
+ [Amazon Route 53 Health Checks and DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
+ [How Health Checks Work in Simple Amazon Route 53 Configurations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-simple-configs.html)

**Report columns**  
+ Hosted Zone Name
+ Hosted Zone ID
+ Resource Record Set Name
+ Resource Record Set Type
+ Resource Record Set Identifier

## Amazon Route 53 Failover Resource Record Sets
<a name="amazon-route-53-failover-resource-record-sets"></a>

**Description**  
Checks for Amazon Route 53 failover resource record sets that have a misconfiguration.   
When Amazon Route 53 health checks determine that the primary resource is unhealthy, Amazon Route 53 responds to queries with a secondary, backup resource record set. You must create correctly configured primary and secondary resource record sets for failover to work.   
Hosted zones created by AWS services won't appear in your check results.   
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`b73EEdD790`

**Alert Criteria**  
+ Yellow: A primary failover resource record set does not have a corresponding secondary resource record set.
+ Yellow: A secondary failover resource record set does not have a corresponding primary resource record set.
+ Yellow: Primary and secondary resource record sets that have the same name are associated with the same health check. 

**Recommended Action**  
 If a failover resource set is missing, create the corresponding resource record set. See [Creating Failover Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/creating-failover-rrsets.html).  
If your resource record sets are associated with the same health check, create separate health checks for each one. See [Creating, Updating, and Deleting Health Checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html). 

**Additional Resources**  
[Amazon Route 53 Health Checks and DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)

**Report columns**  
+ Hosted Zone Name
+ Hosted Zone ID
+ Resource Record Set Name
+ Resource Record Set Type
+ Reason

## Amazon Route 53 High TTL Resource Record Sets
<a name="amazon-route-53-high-ttl-resource-record-sets"></a>

**Description**  
Checks for resource record sets that can benefit from having a lower time-to-live (TTL) value.   
TTL is the number of seconds that a resource record set is cached by DNS resolvers. When you specify a long TTL, DNS resolvers take longer to request updated DNS records, which can cause unnecessary delay in rerouting traffic (for example, when DNS Failover detects and responds to a failure of one of your endpoints). This check looks only at records with a policy of Failover, or if there is an associated health check.   
Hosted zones created by AWS services won’t appear in your check results.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`C056F80cR3`

**Alert Criteria**  
+ Yellow: A resource record set whose routing policy is Failover has a TTL greater than 60 seconds.
+ Green: A resource record either has no failover policy, or has a failover policy with a TTL less than 60.

**Recommended Action**  
Enter a TTL value of 60 seconds for the listed resource record sets. For more information, see [Working with Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrsets-working-with.html).

**Additional Resources**  
[Amazon Route 53 Health Checks and DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)

**Report columns**  
+ Status
+ Hosted Zone Name
+ Hosted Zone ID
+ Resource Record Set Name
+ Resource Record Set Type
+ Resource Record Set ID
+ TTL

## Amazon Route 53 Name Server Delegations
<a name="amazon-route-53-name-server-delegations"></a>

**Description**  
Checks for Amazon Route 53 hosted zones for which your domain registrar or DNS is not using the correct Route 53 name servers.   
When you create a hosted zone, Route 53 assigns a delegation set of four name servers. The names of these servers are ns-{{\#\#\#}}.awsdns-{{\#\#}}.com, .net, .org, and .co.uk, where {{\#\#\#}} and {{\#\#}} typically represent different numbers. Before Route 53 can route DNS queries for your domain, you must update your registrar's name server configuration to remove the name servers that the registrar assigned. Then, you must add all four name servers in the Route 53 delegation set. For maximum availability, you must add all four Route 53 name servers.  
Hosted zones created by AWS services won't appear in your check results.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`cF171Db240`

**Alert Criteria**  
Yellow: A hosted zone for which the registrar for your domain does not use all four of the Route 53 name servers in the delegation set.

**Recommended Action**  
Add or update name server records with your registrar or with the current DNS service for your domain to include all four of the name servers in your Route 53 delegation set. To find these values, see [Getting the Name Servers for a Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/GetInfoAboutHostedZone.html). For information about adding or updating name server records, see [Creating and Migrating Domains and Subdomains to Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/creating-migrating.html).

**Additional Resources**  
[Working with Hosted Zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html)

**Report columns**  
+ Hosted Zone Name
+ Hosted Zone ID
+ Number of Name Server Delegations Used

## Amazon Route 53 Resolver Endpoint Availability Zone Redundancy
<a name="amazon-route53-resolver-endpoint-availability-zone-redundancy"></a>

**Description**  
Checks to see if your service configuration has IP addresses specified in at least two Availability Zones (AZs) for redundancy. An AZ is a distinct location that is insulated from failures in other zones. By specifying IP addresses in multiple AZs in the same Region, you can help protect your applications from a single point of failure.

**Check ID**  
`Chrv231ch1`

**Alert Criteria**  
+ Yellow: IP addresses are specified only in one AZ
+ Green: IP addresses are specified in at least two AZs

**Recommended Action**  
Specify IP addresses in at least two Availability Zones for redundancy.

**Additional Resources**  
+ If you require more than one elastic network interface endpoint to be available at all times, we recommend that you create at least one more network interface than you need, to make sure you have additional capacity available for handling possible traffic surges. The additional network interface also ensures availability during service operations like maintenance or upgrades.
+ [High availability for Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-high-availability.html)

**Report columns**  
+ Status
+ Region
+ Resource ARN
+ Number of AZs

## Amazon S3 Bucket Replication Not Enabled
<a name="amazon-s3-bucket-replication-not-enabled"></a>

**Description**  
Checks if your Amazon S3 buckets have replication rules enabled for Cross-Region Replication, Same-Region Replication, or both.  
Replication is the automatic, asynchronous copying of objects across buckets in the same or different AWS Regions. Replication copies newly created objects and object updates from a source bucket to a destination bucket or buckets. Use Amazon S3 bucket replication to help improve the resilience and compliance of your applications and data storage.  
For more information, see [Replicating objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz119`

**Source**  
`AWS Config Managed Rule: s3-bucket-replication-enabled`

**Alert Criteria**  
Yellow: Amazon S3 bucket replication rules are not enabled for Cross-Region Replication, Same-Region Replication, or both.

**Recommended Action**  
Turn on Amazon S3 bucket replication rules to improve the resiliency and compliance of your applications and data storage.  
For more information, see [View your backup jobs and recovery points](https://docs.aws.amazon.com/aws-backup/latest/devguide/view-protected-resources.html) and [Setting up replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-how-setup.html).

**Additional Resources**  
[Walkthroughs: Examples for configuring replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-example-walkthroughs.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon S3 Bucket Versioning
<a name="amazon-s3-bucket-versioning"></a>

**Description**  
Checks for Amazon Simple Storage Service buckets that do not have versioning enabled, or that have versioning suspended.   
When versioning is enabled, you can easily recover from both unintended user actions and application failures. Versioning allows you to preserve, retrieve, and restore any version of any object stored in a bucket. You can use lifecycle rules to manage all versions of your objects, as well as their associated costs, by automatically archiving objects to the Glacier storage class. Rules can also be configured to remove versions of your objects after a specified period of time. You can also require multi-factor authentication (MFA) for any object deletions or configuration changes to your buckets.   
Versioning can't be deactivated after it has been enabled. However, it can be suspended, which prevents new versions of objects from being created. Using versioning can increase your costs for Amazon S3, because you pay for storage of multiple versions of an object.

**Check ID**  
`R365s2Qddf`

**Alert Criteria**  
+ Green: Versioning is enabled for the bucket.
+ Yellow: Versioning is not enabled for the bucket.
+ Yellow: Versioning is suspended for the bucket.
+ Yellow: Trusted Advisor doesn't have access to validate versioning.

**Recommended Action**  
Enable bucket versioning on most buckets to prevent accidental deletion or overwriting. See [Using Versioning](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html) and [Enabling Versioning Programmatically](https://docs.aws.amazon.com/AmazonS3/latest/dev/manage-versioning-examples.html).  
If bucket versioning is suspended, consider re-enabling versioning. For information on working with objects in a versioning-suspended bucket, see [Managing Objects in a Versioning-Suspended Bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/VersionSuspendedBehavior.html).  
When versioning is enabled or suspended, you can define lifecycle configuration rules to mark certain object versions as expired or to permanently remove unneeded object versions. For more information, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).  
MFA Delete requires additional authentication when the versioning status of the bucket is changed or when versions of an object are deleted. It requires the user to enter credentials and a code from an approved authentication device. For more information, see [MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html#MultiFactorAuthenticationDelete).

**Additional Resources**  
[Working with Buckets](https://docs.aws.amazon.com/AmazonS3/latest/UG/BucketOperations.html)

**Report columns**  
+ Status
+ Region
+ Bucket Name
+ Versioning
+ MFA Delete Enabled

## Application, Network, and Gateway Load Balancers Not Spanning Multiple Availability Zones
<a name="application-network-load-balancers-not-span-multi-az"></a>

**Description**  
Checks If your load balancers (Application, Network, and Gateway Load Balancer) are configured with subnets across multiple Availability Zones.  
You can specify your desired minimum Availability Zones in the **minAvailabilityZones** parameters of your AWS Config rules.  
For more information, see [Availability Zones for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html), [Availability Zones - Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#availability-zones), and [Create a Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/create-load-balancer.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz169`

**Source**  
`AWS Config Managed Rule: elbv2-multiple-az`

**Alert Criteria**  
Yellow: Application, Network, or Gateway Load Balancers configured with subnets in less than two Availability Zones.

**Recommended Action**  
 Configure your Application, Network, and Gateway Load Balancers with subnets across multiple Availability Zones.

**Additional Resources**  
[Availability Zones for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html)  
[Availability Zones (Elastic Load Balancing)](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#availability-zones)  
[Create a Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/create-load-balancer.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Auto Scaling available IPs in Subnets
<a name="auto-scaling-available-ips-in-subnets"></a>

**Description**  
 Checks that sufficient available IPs remain among targeted Subnets.Having sufficient IPs available for use would help when Auto Scaling Group reaches its maximum size and needs to launch additional instances.

**Check ID**  
`Cjxm268ch1`

**Alert Criteria**  
+ Red: The maximum number of instances and IP addresses that could be created by an ASG exceed the number of IP addresses remaining in the configured subnets.
+ Green: There are sufficient IP addresses available for the remaining scale possible in the ASG.

**Recommended Action**  
Increase the number of available IP addresses 

**Report columns**  
+ Status
+ Region
+ Resource ARN
+ Maximum instances that can be created
+ Number of available instances

## Auto Scaling Group Health Check
<a name="auto-scaling-group-health-check"></a>

**Description**  
Examines the health check configuration for Auto Scaling groups.   
If Elastic Load Balancing is being used for an Auto Scaling group, the recommended configuration is to enable an Elastic Load Balancing health check. If an Elastic Load Balancing health check is not used, Auto Scaling can only act upon the health of the Amazon Elastic Compute Cloud (Amazon EC2) instance. Auto Scaling will not act on the application running on the instance.

**Check ID**  
`CLOG40CDO8`

**Alert Criteria**  
+ Yellow: An Auto Scaling group has an associated load balancer, but the Elastic Load Balancing health check is not enabled.
+ Yellow: An Auto Scaling group does not have an associated load balancer, but the Elastic Load Balancing health check is enabled.

**Recommended Action**  
If the Auto Scaling group has an associated load balancer, but the Elastic Load Balancing health check is not enabled, see [Add an Elastic Load Balancing Health Check to your Auto Scaling Group](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-add-elb-healthcheck.html).  
If the Elastic Load Balancing health check is enabled, but no load balancer is associated with the Auto Scaling group, see [Set Up an Auto-Scaled and Load-Balanced Application](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-register-lbs-with-asg.html).

**Additional Resources**  
[Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/)

**Report columns**  
+ Status
+ Region
+ Auto Scaling Group Name
+ Load Balancer Associated
+ Health Check

## Auto Scaling Group Resources
<a name="auto-scaling-group-resources"></a>

**Description**  
Checks the availability of resources associated with your launch configurations, launch templates, and your Auto Scaling groups.   
Auto Scaling groups that point to unavailable resources cannot launch new Amazon Elastic Compute Cloud (Amazon EC2) instances. When properly configured, Auto Scaling causes the number of Amazon EC2 instances to increase seamlessly during demand spikes, and decrease automatically during demand lulls. Auto Scaling groups and launch configurations/launch templates that point to unavailable resources do not operate as intended.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`8CNsSllI5v`

**Alert Criteria**  
+ Red: An Auto Scaling group is associated with a deleted load balancer.
+ Red: A launch configuration is associated with a deleted Amazon Machine Image (AMI).
+ Red: A launch template is associated with a deleted Amazon Machine Image (AMI).

**Recommended Action**  
If the load balancer has been deleted, either create a new load balancer or target group and then associate it to the Auto Scaling group. or create a new Auto Scaling group without the load balancer. For information about creating a new Auto Scaling group with a new load balancer, see [Set Up an Auto-Scaled and Load-Balanced Application](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-register-lbs-with-asg.html). For information about creating a new Auto Scaling group without a load balancer, see Create Auto Scaling Group in [Getting Started With Auto Scaling Using the Console](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/USBasicSetup-Console.html).  
If the AMI has been deleted, then create a new launch configuration or launch template version using a valid AMI and associate it with an Auto Scaling group. For information on how to create a new launch configuration, see [Create a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html) in the *Amazon EC2 Auto Scaling User Guide*. For information on how to create a launch template, see [Create a launch template for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*.  
For security reasons, the check results don’t include any resources referenced using AWS Systems Manager parameters in the launch template.
If your launch templates include an AWS Systems Manager parameter that include an Amazon Machine Image (AMI) ID , then review the launch template to make sure that the parameters reference a valid AMI ID, or make the appropriate changes in the AWS Systems Manager parameter store. For more information, see [Use AWS Systems Manager parameters instead of AMI IDs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/using-systems-manager-parameters.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Additional Resources**  
+ [Troubleshooting Auto Scaling: Amazon EC2 AMIs](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/ts-as-ami.html)
+ [Troubleshooting Auto Scaling: Load Balancer Configuration](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/ts-as-loadbalancer.html)
+ [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/latest/userguide/)
+ [Use AWS Systems Manager parameters instead of AMI IDs](https://docs.aws.amazon.com/autoscaling/ec2/userguide/using-systems-manager-parameters.html)

**Report columns**  
+ Status
+ Region
+ Auto Scaling Group Name
+ Launch Type
+ Resource Type
+ Resource Name

## AWS CloudHSM clusters running HSM instances in a single AZ
<a name="aws-cloudhsm-clusters-running-hsm-instances-in-a-single-az"></a>

**Description**  
Checks your clusters that run HSM instances in a single Availability Zone (AZ). This check alerts you if your clusters are at risk of not having the most recent backup.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`hc0dfs7601`

**Alert Criteria**  
+ Yellow: A CloudHSM cluster is running all HSM instances in a single Availability Zone for more than 1 hour.
+ Green: A CloudHSM cluster is running all HSM instances in at least two different Availability Zones.

**Recommended Action**  
Create at least one more instance for the cluster in a different Availability Zone.

**Additional Resources**  
[Best practices for AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/best-practices.html)

**Report columns**  
+ Status
+ Region
+ Cluster ID
+ Number of HSM Instances
+ Last Updated Time

## Direct Connect Location Resiliency
<a name="amazon-direct-connect-location-resiliency"></a>

**Description**  
Checks the resilience of the Direct Connect used to connect your on-premises to each Direct Connect gateway or virtual private gateway.  
This check alerts you if any Direct Connect gateway or virtual private gateway isn't configured with virtual interfaces across at least two distinct Direct Connect locations. Lack of location resiliency can result in unexpected downtime during maintenance, a fiber cut, a device failure, or a complete location failure.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.
Direct Connect is implemented with Transit Gateway using Direct Connect gateway.

**Check ID**  
`c1dfpnchv2`

**Alert Criteria**  
Red: The Direct Connect gateway or virtual private gateway is configured with one or more virtual interfaces on a single Direct Connect device.  
Yellow: The Direct Connect gateway or virtual private gateway is configured with virtual interfaces across multiple Direct Connect devices in a single Direct Connect location.  
Green: The Direct Connect gateway or virtual private gateway is configured with virtual interfaces across two or more distinct Direct Connect locations.

**Recommended Action**  
To build Direct Connect location resiliency, you can configure the Direct Connect gateway or virtual private gateway to connect to at least two distinct Direct Connect locations. For more information, see [Direct Connect Resiliency Recommendation](https://aws.amazon.com/directconnect/resiliency-recommendation/).

**Additional Resources**  
[Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)  
[Direct Connect Failover Test](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_failover.html)

**Report columns**  
+ Status
+ Region
+ Last Updated Time
+ Resiliency Status 
+ Location
+ Connection ID
+ Gateway ID

## AWS Lambda functions without a dead-letter queue configured
<a name="aws-lambda-functions-without-dlq"></a>

**Description**  
Checks if an AWS Lambda function is configured with a dead-letter queue.  
A dead-letter queue is a feature of AWS Lambda that allows you to capture and analyze failed events, providing a way to handle those events accordingly. Your code might raise an exception, time out, or run out of memory, resulting in failed asynchronous executions of your Lambda function. A dead-letter queue stores messages from failed invocations, providing a way to handle the messages and troubleshoot the failures.  
You can specify the dead-letter queue resource that you want to check using the **dlqArns** parameter in your AWS Config rules.  
For more information, see [Dead-letter queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz182`

**Source**  
`AWS Config Managed Rule: lambda-dlq-check`

**Alert Criteria**  
Yellow: AWS Lambda function has no dead-letter queue configured.

**Recommended Action**  
Make sure that your AWS Lambda functions have a dead-letter queue configured to control message handling for all failed asynchronous invocations.  
For more information, see [Dead-letter queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq).

**Additional Resources**  
+ [Robust Serverless Application Design with AWS Lambda Dead Letter Queues](https://aws.amazon.com/blogs/compute/robust-serverless-application-design-with-aws-lambda-dlq/)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## AWS Lambda On Failure Event Destinations
<a name="AWS-Lambda-On-Failure-Event-Destinations"></a>

**Description**  
 Checks that Lambda functions in your account have On Failure event destination or Dead Letter Queue (DLQ) configured for asynchronous invocations, so that records from failed invocations can be routed to a destination for further investigation or processing.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dfprch05`

**Alert Criteria**  
+ Yellow: Function does not have any On Failure event destination or DLQ configured.

**Recommended Action**  
Please set up On Failure event destination or DLQ for your Lambda functions to send failed invocations along with other details to one of the available destination AWS services for further debugging or processing.

**Additional Resources**  
+ [Asynchronous Invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)
+ [AWS Lambda On Failure Event Destinations](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-destinations/)

**Report columns**  
+ Status
+ Region
+ The function with version which is flagged.
+ Current day async requests dropped percentage
+ Current day async requests
+ Average daily async requests dropped percentage
+ Average daily async requests
+ Last Updated Time

## AWS Lambda VPC-enabled Functions without Multi-AZ Redundancy
<a name="aws-lambda-vpc-enabled-functions-without-multi-az-redundancy"></a>

**Description**  
Checks the $LATEST version of VPC-enabled Lambda functions that are vulnerable to service interruption in a single Availability Zone. It’s a best practice that VPC-enabled functions are connected to multiple Availability Zones for high availability.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`L4dfs2Q4C6`

**Alert Criteria**  
Yellow: The $LATEST version of a VPC-enabled Lambda function is connected to subnets in a single Availability Zone.

**Recommended Action**  
When configuring functions for access to your VPC, choose subnets in multiple Availability Zones to ensure high availability.

**Additional Resources**  
+ [Configuring a Lambda function to access resources in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)
+ [Resilience in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-resilience.html)

**Report columns**  
+ Status
+ Region
+ Function ARN
+ VPC ID
+ Average daily Invokes
+ Last Updated Time

## AWS Outposts Single Rack deployment
<a name="aws-outposts-single-rack-deployment"></a>

**Description**  
Checks for Outposts Racks balance. This evaluates if a customers Outposts instances are deployed across multiple Outposts Racks or to a single Outpost Rack. A single Outposts rack creates a single point of failure for issues that involve a single Rack (for example, environmental failures). These scenarios can be mitigated by deploying outposts across multiple Racks.

**Check ID**  
`c243hjzrhn`

**Alert Criteria**  
+ Yellow: Your Outpost is deployed on single Rack
+ Green: Your Outpost is deployed across multiple Racks.

**Recommended Action**  
If you are running production workloads on AWS Outposts, then its a best practice to use the following resilient architecture. A single AWS Outposts rack creates a single point of failure. Consider adding a second AWS Outposts rack to that location with enough capacity for a failover event, and then distribute workloads across racks.

**Additional Resources**  
[Failure mode 4: Racks or data centers](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/thinking-in-terms-of-failure-modes.html#failure-mode-4-racks-or-data-centers)

**Report columns**  
+ Status
+ Resource ARN
+ AZ
+ Number of Racks
+ Last Updated Time

## AWS Resilience Hub Application Component check
<a name="amazon-resilience-hub-application-component-check"></a>

**Description**  
Checks if an Application Component (AppComponent) in your application is unrecoverable. If an AppComponent doesn't recover in the case of a disruption event, you might experience unknown data loss and system downtime.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.

**Check ID**  
`RH23stmM04`

**Alert Criteria**  
Red: AppComponent is unrecoverable.

**Recommended Action**  
To ensure that your AppComponent is recoverable, review and implement the resiliency recommendations, and then run a new assessment. For more information about reviewing the resiliency recommendations, see Additional Resources.

**Additional Resources**  
[Reviewing resiliency recommendations](https://docs.aws.amazon.com/resilience-hub/latest/userguide/resil-recs.html)  
[AWS Resilience Hub concepts](https://docs.aws.amazon.com/resilience-hub/latest/userguide/concepts-terms.html)  
[AWS Resilience Hub User Guide](https://docs.aws.amazon.com/resilience-hub/latest/userguide/concepts-terms.html)

**Report columns**  
+ Status
+ Region
+ Application Name
+ AppComponent Name
+ Last Updated Time

## AWS Resilience Hub policy breached
<a name="aws-resilience-hub-policy-breached"></a>

**Description**  
Checks Resilience Hub for applications that don't meet the recovery time objective (RTO) and recovery point objective (RPO) that the policy defines. The check alerts you if your application doesn't meet the RTO and RPO objectives you've set for an application in Resilience Hub.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`RH23stmM02`

**Alert Criteria**  
+ Green: The application has a policy and meets the RTO and RPO objectives.
+ Yellow: The application hasn't been assessed yet.
+ Red: The application has a policy but doesn’t meet the RTO and RPO objectives.

**Recommended Action**  
Sign in to the Resilience Hub console and review the recommendations so that your application meets the RTO and RPO objectives.

**Additional Resources**  
[Resilience Hub concepts](https://docs.aws.amazon.com/resilience-hub/latest/userguide/concepts-terms.html)

**Report columns**  
+ Status
+ Region
+ Application Name
+ Last Updated Time

## AWS Resilience Hub resilience scores
<a name="aws-resilience-hub-resilience-scores"></a>

**Description**  
Checks if you have run an assessment for your applications in Resilience Hub. This check alerts you if your resilience scores are below a specific value.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`RH23stmM01`

**Alert Criteria**  
+ Green: Your application has a resilience score of 70 or greater.
+ Yellow: Your application has a resilience score of 40 through 69.
+ Yellow: The application hasn't been assessed yet.
+ Red: Your application has a resilience score of less than 40.

**Recommended Action**  
Sign in to the Resilience Hub console and run an assessment for your application. Review the recommendations to improve the resilience score.

**Additional Resources**  
[Resilience Hub concepts](https://docs.aws.amazon.com/resilience-hub/latest/userguide/concepts-terms.html)

**Report columns**  
+ Status
+ Region
+ Application Name
+ Application Resilience Score
+ Last Updated Time

## AWS Resilience Hub assessment age
<a name="aws-resilience-hub-assessment-age"></a>

**Description**  
Checks how long since you last ran an application assessment. This check alerts you if you haven’t run an application assessment for a specified number of days.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`RH23stmM03`

**Alert Criteria**  
+ Green: Your application assessment ran in the last 30 days.
+ Yellow: Your application assessment hasn't run in the last 30 days.

**Recommended Action**  
Sign in to the Resilience Hub console and run an assessment for your application.

**Additional Resources**  
[Resilience Hub concepts](https://docs.aws.amazon.com/resilience-hub/latest/userguide/concepts-terms.html)

**Report columns**  
+ Status
+ Region
+ Application Name
+ Days Since the Last Assessment Ran
+ Last Assessment Run Time
+ Last Updated Time

## AWS Site-to-Site VPN has at least one tunnel in DOWN status
<a name="aws-site-to-site-vpn-tunnel-in-down-status"></a>

**Description**  
Checks the number of tunnels that are active for each of your AWS Site-to-Site VPNs.  
A VPN should have two tunnels configured at all times. This provides redundancy in case of outage or planned maintenance of the devices at the AWS endpoint. For some hardware, only one tunnel is active at a time. If a VPN has no active tunnels, charges for the VPN might still apply.  
For more information, see [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz123`

**Source**  
`AWS Config Managed Rule: vpc-vpn-2-tunnels-up`

**Alert Criteria**  
Yellow: A Site-to-Site VPN has at least one tunnel DOWN.

**Recommended Action**  
Make sure that two tunnels are configured for VPN connections. And, if your hardware supports it, then make sure that both tunnels are active. If you no longer need a VPN connection, then delete it to avoid charges.  
For more information, see [Your customer gateway device](https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html) and the content available on the [AWS Knowledge Center.](https://repost.aws/knowledge-center#AWS_Virtual_Private_Network)

**Additional Resources**  
+ [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+ [Adding a Virtual Private Gateway to Your VPC](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-target-gateway)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## AWS STS global endpoint usage across AWS Regions
<a name="sts-global-endpoint"></a>

**Description**  
This check identifies a resiliency risk when AWS workloads make cross-region calls to the STS global endpoint in the US East (N. Virginia) Region. AWS workloads that make cross-region requests to the STS global endpoint in US East (N. Virginia) might be adversely impacted if connectivity to the US East (N. Virginia) STS endpoint is impacted.  
In April 2025, AWS enhanced the global endpoint to automatically serve the STS global endpoint calls in the same Region as your workloads running in AWS, for all AWS Regions enabled by default. However, some workloads, such as those running in opt-in Regions, or those not using Amazon DNS servers, do not benefit from the reduced latency and [fault isolation](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) offered as part of this enhancement. For these workloads, STS global endpoint requests are served in the US East (N. Virginia) Region, posing a resiliency risk to your application, and increasing latency of STS requests.  
Results for this check are automatically refreshed several times daily, each time covering the past 15 days. Refresh requests are not allowed. So, it might take up to 15 days for changes to appear in the Trusted Advisor check results.  
For Business, Enterprise On-Ramp, or Enterprise Support customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c15m0mgld3`

**Alert criteria**  
Red: Workloads are making cross-region calls to the AWS STS global endpoint in the US East (N. Virginia) Region.

**Recommended action**  
To improve the resiliency and performance of your workloads, we recommend that you migrate from the STS global endpoint to the STS Regional endpoint. By using a Regional endpoint, you can use AWS STS in the same Region as your workloads.   
The following is a list of AWS Identity and Access Management (IAM) Principals making cross-region calls to the AWS STS global endpoint in the US East (N. Virginia) Region. By following the steps in the blog post [How to use Regional AWS STS endpoints](https://aws.amazon.com/blogs/security/how-to-use-regional-aws-sts-endpoints/), you can reconfigure your workloads to use the Regional STS endpoint.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html)

**Additional resources**  
+ [Manage AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html)
+ [AWS STS Regional endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html)

**Report columns**  
+ Status
+ Principal Arn
+ Action
+ Principal Type
+ Originating Region
+ Last Updated Time

## AWS Well-Architected high risk issues for reliability
<a name="well-architected-high-risk-issues-reliability"></a>

**Description**  
Checks for high risk issues (HRIs) for your workloads in the reliability pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Wxdfp4B1L4`

**Alert Criteria**  
+ Red: At least one active high risk issue was identified in the reliability pillar for AWS Well-Architected.
+ Green: No active high risk issues were detected in the reliability pillar for AWS Well-Architected.

**Recommended Action**  
AWS Well-Architected detected high risk issues during your workload evaluation. These issues present opportunities to reduce risk and save money. Sign in to the [AWS Well-Architected](https://console.aws.amazon.com/wellarchitected) tool to review your answers and take action to resolve your active issues.

**Report columns**  
+ Status
+ Region
+ Workload ARN
+ Workload Name
+ Reviewer Name
+ Workload Type
+ Workload Started Date
+ Workload Last Modified Date
+ Number of identified HRIs for Reliability
+ Number of HRIs resolved for Reliability
+ Number of questions answered for Reliability
+ Total number of questions in Reliability pillar
+ Last Updated Time

## Classic Load Balancer has no multiple AZs configured
<a name="classic-load-balancewr-no-multi-azs"></a>

**Description**  
 Checks if Classic Load Balancer spans multiple Availability Zones (AZs).  
A load balancer distributes incoming application traffic across multiple Amazon EC2 instances in multiple Availability Zones. By default, the load balancer distributes traffic evenly across the Availability Zones that you enable for your load balancer. If one Availability Zone experiences an outage, then load balancer nodes automatically forward requests to the healthy registered instances in one or more Availability Zones.  
You can adjust the minimum number of Availability Zones using the **minAvailabilityZones** parameter in your AWS Config rules  
For more information, see [What is a Classic Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/introduction.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz154`

**Source**  
`AWS Config Managed Rule: clb-multiple-az`

**Alert Criteria**  
Yellow: Classic Load Balancer does not have Multi-AZ configured or does not meet the minimum number of AZs specified.

**Recommended Action**  
Make sure that your Classic Load Balancers have multiple Availability Zones configured. Span your load balancer across multiple AZs to make sure that you have high availability of your application.  
For more information, see [Tutorial: Create a Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## CLB Connection Draining
<a name="elb-connection-draining"></a>

**Description**  
Checks for Classic load balancers that do not have connection draining enabled.   
When connection draining is not enabled and you deregister an Amazon EC2 instance from a Classic load balancer, the Classic load balancer stops routing traffic to that instance and closes the connection. When connection draining is enabled, the Classic load balancer stops sending new requests to the deregistered instance but keeps the connection open to serve active requests.

**Check ID**  
`7qGXsKIUw`

**Alert Criteria**  
+ Yellow: Connection draining is not enabled for a Classic load balancer.
+ Green: Connection draining is enabled for Classic load balancer. .

**Recommended Action**  
Enable connection draining for the Classic load balancer. For more information, see [Connection Draining](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain) and [Enable or Disable Connection Draining for Your Load Balancer](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/config-conn-drain.html).

**Additional Resources**  
[Elastic Load Balancing Concepts](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html)

**Report columns**  
+ Status
+ Region
+ Load Balancer Name
+ Reason

## ELB Target Imbalance
<a name="elb-target-imbalance"></a>

**Description**  
Checks the target groups’ target distribution across Availability Zones (AZs) for Application Load Balancer (ALB), Network Load Balancer (NLB), and Gateway Load Balancer (GWLB).  
This check excludes the following:  
+ Load balancers configured with a single Availability Zone (AZ).
+ Load balancers where the difference in the number of targets between the most and least populated AZs is equal to or less than 1.
+ Target groups with IP-based targets where the AvailabilityZone attribute is set to 'all'.

**Check ID**  
`b92b83d667`

**Alert Criteria**  
+ Red: A single AZ represents more than 66% of the load balancer capacity.
+ Yellow: A single AZ represents more than 50% of the load balancer capacity.
+ Green: No AZs represents more than 50% of the load balancer capacity.

**Recommended Action**  
For better resilience, make sure that your targets groups have same number of targets across AZs.

**Additional Resources**  
[Target groups for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)  
[Register targets with your Application Load Balancer target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-register-targets.html)

**Report columns**  
+ Status
+ Region
+ Load Balancer Name
+ Load Balancer Type
+ Target Group ARN (arn)
+ Difference in registered targets across AZs
+ Last Updated Time

## GWLB - endpoint AZ independence
<a name="gwlb-endpoint-az-independence"></a>

**Description**  
Checks if your Gateway Load Balancer (GWLB) endpoints are configured as route destination from another Availability Zone (AZ).  
Gateway Load Balancer endpoints forward network traffic to firewall appliances behind a Gateway Load Balancer for inspection. Each Gateway Load Balancer endpoint operates within a designated AZ and is built with redundancy in only that AZ. So any resources in a particular AZ must use a Gateway Load Balancer endpoint in the same AZ. This makes sure that any potential outage of a Gateway Load Balancer endpoint or its AZ doesn’t impact your resources in another AZ. 

**Check ID**  
`528d6f5ee7`

**Alert Criteria**  
+ Yellow: Traffic from your subnet in one AZ is being routed through a Gateway Load Balancer endpoint in a different AZ.
+ Green: Traffic from your subnet in one AZ is being routed through a Gateway Load Balancer endpoint in the same AZ.

**Recommended Action**  
Check the AZ of your subnet and configure its route table to route traffic through a Gateway Load Balancer endpoint in the same AZ.  
If there is no Gateway Load Balancer endpoint in the AZ, then create a new one and then route your subnet traffic through it.  
If you have the same route table associated across subnets in different AZs, then keep this route table associated to the subnets that reside in the same AZ as the Gateway Load Balancer endpoint. For subnets in the other AZ, you can then associate a separate route table with a route to a Gateway Load Balancer endpoint in the this AZ.  
It’s a best practice to choose a maintenance window for architecture changes in your Amazon VPC. 

**Additional Resources**  
+ [Availability Zone Independence](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/availability-zone-independence.html)
+ [Configure Routing for Gateway Load Balancer endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-load-balancer-endpoints.html#configure-routing-gateway-load-balancer-endpoint)
+ [AWS Well-Architected Tool - Use bulkhead architectures to limit scope of impact](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_use_bulkhead.html)

**Report columns**  
+ Status
+ Region
+ Cross AZ Subnet Id List
+ Gateway Load Balancer Endpoint Id
+ Gateway Load Balancer Endpoint Subnet Id
+ VPC Endpoint Subnet AZ
+ Last Updated Time

## Load Balancer Optimization
<a name="load-balancer-optimization"></a>

**Description**  
Checks your load balancer configuration.   
To help increase the level of fault tolerance in Amazon Elastic Compute Cloud (Amazon EC2) when using Elastic Load Balancing , we recommend running an equal number of instances across multiple Availability Zones in a Region. A load balancer that is configured accrues charges, so this is a cost-optimization check as well.

**Check ID**  
`iqdCTZKCUp`

**Alert Criteria**  
+ Yellow: A load balancer is enabled for a single Availability Zone.
+ Yellow: A load balancer is enabled for an Availability Zone that has no active instances.
+ Yellow: The Amazon EC2 instances that are registered with a load balancer are unevenly distributed across Availability Zones. (The difference between the highest and lowest instance counts in utilized Availability Zones is more than 1, and the difference is more than 20% of the highest count.)

**Recommended Action**  
Ensure that your load balancer points to active and healthy instances in at least two Availability Zones. For more information, see [Add Availability Zone](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/enable-disable-az.html#US_AddLBAvailabilityZone).  
If your load balancer is configured for an Availability Zone with no healthy instances, or if there is an imbalance of instances across the Availability Zones, determine if all the Availability Zones are necessary. Omit any unnecessary Availability Zones and ensure there is a balanced distribution of instances across the remaining Availability Zones. For more information, see [Remove Availability Zone](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/enable-disable-az.html#US_ShrinkLBApp04).

**Additional Resources**  
+ [Availability Zones and Regions](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#AZ-Region)
+ [Managing Load Balancers](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/UserScenarios.html)
+ [Best Practices in Evaluating Elastic Load Balancing](https://aws.amazon.com/articles/1636185810492479)

**Report columns**  
+ Status
+ Region
+ Load Balancer Name
+ \# of Zones
+ Zone a Instances
+ Zone b Instances
+ Zone c Instances
+ Zone d Instances
+ Zone e Instances
+ Zone f Instances
+ Reason

## NAT Gateway AZ Independence
<a name="nat-gateway-az-independence"></a>

**Description**  
Checks if your NAT Gateways are configured with Availability Zone (AZ) independence.  
A NAT Gateway enables resources in your private subnet to securely connect to services outside the subnet using the NAT Gateway’s IP addresses and drops any unsolicited inbound traffic. Each NAT Gateway operates within a designated Availability Zone (AZ) and is built with redundancy in that AZ only. Therefore, your resources in a particular AZ should use a NAT Gateway in the same AZ so that any potential outage of a NAT Gateway or its AZ does not impact your resources in another AZ.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dfptbg10`

**Alert Criteria**  
+ Red: Traffic from your subnet in one AZ is being routed through a NATGW in a different AZ.
+ Green: Traffic from your subnet in one AZ is being routed through a NATGW in the same AZ.

**Recommended Action**  
Please check the AZ of your subnet and route traffic through a NAT Gateway in the same AZ.  
If there is no NATGW in the AZ, please create one and then route your subnet traffic through it.  
If you have the same route table associated across subnets in different AZs, keep this route table associated to the subnets that reside in the same AZ as the NAT Gateway and for subnets in the other AZ, please associate a separate route table with a route to a NAT Gateway in this other AZ.  
We recommend choosing a maintenance window for architecture changes in your Amazon VPC.

**Additional Resources**  
+ [How to create a NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-working-with)
+ [How to configure routes for different NAT Gateway use cases](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-scenarios.html)

**Report columns**  
+ Status
+ Region
+ NAT Availability Zone
+ NAT ID
+ Subnet Availability Zone
+ Subnet ID
+ Route Table ID
+ NAT ARN
+ Last Updated Time

## Network Firewall endpoint AZ Independence
<a name="network-firewall-endpoint-az-independence"></a>

**Description**  
Checks if your AWS Network Firewall endpoints are configured as a route destination from another Availability Zone (AZ).  
Network Firewall endpoints forward network traffic to a Network Firewall for inspection. Each Network Firewall endpoint operates within a designated AZ and is built with redundancy only in that AZ. Your resources in a particular AZ should use a Network Firewall endpoint in the same AZ. This makes sure that any potential outage of a Network Firewall endpoint or its AZ doesn’t impact your resources in another AZ. Network traffic that originates in a different AZ for traffic inspection incurs cross-AZ data transfer charges. It’s a best practice to make sure that all resources in a specific AZ use a Network Firewall in the same AZ to avoid cross-AZ data charges.

**Check ID**  
`7040ea389a`

**Alert Criteria**  
+ Yellow: Traffic from a subnet in one AZ is being routed through a Network Firewall endpoint in a different AZ.
+ Green: Traffic from a subnet in one AZ is being routed through a Network Firewall endpoint in the same AZ.

**Recommended Action**  
Check the AZ of your subnet and route traffic through a Network Firewall endpoint in the same AZ.  
If there is no Network Firewall endpoint in the AZ, then create a new Network Firewall and route your subnet traffic through it.  
If the same route table is associated across multiple subnets in different AZs, then keep this route table associated to the subnets that reside in the same AZ as the Network Firewall endpoint. For subnets in other AZs, associate a separate route table with a route to a Network Firewall endpoint in that AZ.  
It’s a best practice to choose a maintenance window for architecture changes in your Amazon VPC.

**Additional Resources**  
[Data Transfer within the same AWS Region](https://aws.amazon.com/ec2/pricing/on-demand/)  
[Understanding data transfer charges](https://docs.aws.amazon.com/cur/latest/userguide/cur-data-transfers-charges.html)  
[Availability Zone Independence](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/availability-zone-independence.html)  
[High Level steps for implementing a firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-high-level-steps.html)  
[Creating a firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-creating.html)  
[AWS Well-Architected Tool - Use bulkhead architectures to limit scope of impact](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_use_bulkhead.html)

**Report columns**  
+ Status
+ Region
+ Network Firewall Endpoint Id
+ Network Firewall Arn
+ Network Firewall Endpoint Subnet
+ Network Firewall Endpoint AZ
+ Cross AZ Subnets List
+ Last Updated Time

## Network Firewall Multi-AZ
<a name="network-firewall-multi-az"></a>

**Description**  
Checks if your Network Firewalls are configured to use more than one Availability Zone (AZ) for firewall endpoints.   
An AZ is a distinct location that’s insulated from failures in other zones. If the Network Firewall endpoint is deployed in only 1 AZ, then it can be a single point of failure and can impair workloads from other AZs using the Network Firewall for traffic inspection. It’s a best practice to configure your Network Firewalls in multiple AZs in the same Region to mprove your workload availability.

**Check ID**  
`c2vlfg0gqd`

**Alert Criteria**  
+ Yellow: Network Firewall endpoint is deployed in 1 AZ.
+ Green: Network Firewall endpoints is deployed in at least two AZs.

**Recommended Action**  
Make sure that your Network Firewall is configured with at least two AZs for production workloads.

**Additional Resources**  
[VPC subnet configuration forAWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config.html#vpc-config-subnets)  
[Creating a firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-creating.html)  
[Availability Zone](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#availability-zones)  
[AWS Well-Architected Tool - Deploy the workload to multiple locations](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)  
[Appliance in a shared services VPC](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html#transit-gateway-appliance-overview)

**Report columns**  
+ Status
+ Region
+ Network Firewall Arn
+ VPC Id
+ Network Firewall Subnets
+ Network Firewall Subnets AZs
+ Last Updated Time

## Network Load Balancers Cross Load Balancing
<a name="network-load-balancers-cross-load-balancing"></a>

**Description**  
Checks if cross-zone load balancing is enabled on Network Load Balancers.  
Cross-zone load balancing helps maintain even distribution of incoming traffic across instances in different Availability Zones. This prevents the load balancer from routing all traffic to instances in the same Availability Zone, which can cause uneven traffic distribution and potential overloading. The feature also helps application reliability by automatically routing traffic to healthy instances in other Availability Zones in the event of a single Availability Zone failure.  
For more information, see [Cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#cross-zone-load-balancing).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz105`

**Source**  
`AWS Config Managed Rule: nlb-cross-zone-load-balancing-enabled`

**Alert Criteria**  
+ Yellow: Network Load Balancer does not have cross-zone load balancing enabled.

**Recommended Action**  
Ensure that cross-zone load balancing is enabled on Network Load Balancers.

**Additional Resources**  
[Cross-zone load balancing (Network Load Balancers)](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#cross-zone-load-balancing)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## NLB - Internet-facing resource in private subnet
<a name="nlb-internet-facing-resources-private-subnet"></a>

**Description**  
Checks if an internet-facing Network Load Balancer (NLB) is configured with a private subnet. An internet-facing Network Load Balancer (NLB) must be configured in public subnets in order to receive traffic. A public subnet is defined as a subnet that has a direct route to an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html). If the subnet is configured as private, then it’s Availability Zone (AZ) doesn’t receive traffic, which can cause availability issues.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dfpnchv4`

**Alert Criteria**  
Red: NLB is configured with one or more private subnets  
Green: No private subnet is configured for internet-facing NLB

**Recommended Action**  
Confirm that the subnets configured in an internet-facing load balancer are public. A public subnet is defined as a subnet that has a direct route to an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html). Use one of following options:  
+ Create a new load balancer and select a different subnet with a direct route to an internet gateway.
+ Change the subnet that’s currently attached to the load balancer from private to public. To do this, change its route table and [associate an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#associate-route-table-gateway).

**Additional Resources**  
+ [Configure a load balancer and a listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html#configure-load-balancer)
+ [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
+ [Associate a gateway with a route table](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#associate-route-table-gateway)

**Report columns**  
+ Status
+ Region
+ NLB Arn
+ NLB Name
+ Subnet ID
+ NLB Scheme
+ Subnet Type
+ Last Updated Time

## NLB Multi-AZ
<a name="nlb-multi-az"></a>

**Description**  
Checks if your Network Load Balancers are configured to use more than one Availability Zone (AZ). An AZ is a distinct location that is insulated from failures in other zones. Configure your load balancer in multiple AZs in the same Region to help improve your workload availability.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dfprch09`

**Alert Criteria**  
Yellow: NLB is in a single AZ.  
Green: NLB has two or more AZs.

**Recommended Action**  
Make sure that your load balancer is configured with at least two Availability Zones.

**Additional Resources**  
For more information, see the following documentation:  
+ [Availability Zones](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#availability-zones)
+ [AWS Well-Architected - Deploy the workload to multiple locations](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)
+ [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

**Report columns**  
+ Status
+ Region
+ Number of AZs
+ NLB ARN
+ NLB Name
+ Last Updated Time

## Number of AWS Regions in an Incident Manager replication set
<a name="number-of-aws-regions-in-an-incident-manager-replication-set"></a>

**Description**  
Checks that an Incident Manager replication set’s configuration uses more than one AWS Region to support regional failover and response. For incidents created by CloudWatch alarms or EventBridge events, Incident Manager creates an incident in the same AWS Region as the alarm or event rule. If Incident Manager is temporarily unavailable in that Region, the system attempts to create an incident in another Region in the replication set. If the replication set includes only one Region, the system fails to create an incident record while Incident Manager is unavailable.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`cIdfp1js9r`

**Alert Criteria**  
+ Green: The replication set contains more than one Region.
+ Yellow: The replication set contains one Region.

**Recommended Action**  
Add at least one more Region to the replication set.

**Additional Resources**  
For more information, see [Cross-region Incident management](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-cross-account-cross-region.html#incident-manager-cross-region.html).

**Report columns**  
+ Status
+ Multi-region
+ Replication Set
+ Last Updated Time

## Single AZ Application Check
<a name="single-az-application-check"></a>

**Description**  
Checks through network patterns if your egress network traffic is routing through a single Availability Zone (AZ).  
An AZ is a distinct location that is insulated from any impact in other zones. By spreading your service across multiple AZs, you limit the blast radius of an AZ failure.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dfptbg11`

**Alert Criteria**  
+ Yellow: Your application may be deployed in only one AZ based on observed egress network patterns. If this is true and your application expects high availability, we recommend that you provision your application resources and implement your network flows to utilize multiple Availability Zones.

**Recommended Action**  
If your application requires high availability, consider implementing a multi-AZ architecture for higher availability.

**Report columns**  
+ Status
+ Region
+ VPC ID
+ Last Updated Time

## VPC interface endpoint network interfaces in multiple AZs
<a name="vpc-interface-endpoint-network-interface-multi-az"></a>

**Description**  
Checks if your AWS PrivateLink VPC interface endpoints are configured to use more than one Availability Zone (AZ). An AZ is a distinct location that is insulated from failures in other zones. This supports inexpensive, low-latency network connectivity between AZs in the same AWS Region. Select subnets in multiple AZs when you create interface endpoints to help protect your applications from a single point of failure.  
This check currently includes only interface endpoints.
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1dfprch10`

**Alert Criteria**  
Yellow: VPC endpoint is in a single AZ.  
Green: VPC endpoint is in at least two AZs.

**Recommended Action**  
Make sure that your VPC interface endpoint is configured with at least two Availability Zones.

**Additional Resources**  
For more information, see the following documentation:  
+ [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html)
+ [Private IP address of the endpoint network interface](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/creating-highly-available-endpoint-services.html#private-ip-address-of-the-endpoint-network-interface)
+ [AWS PrivateLink concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)
+ [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

**Report columns**  
+ Status
+ Region
+ VPC Endpoint ID
+ Is Multi AZ
+ Last Updated Time

## VPN Tunnel Redundancy
<a name="vpn-tunnel-redundancy"></a>

**Description**  
Checks the number of tunnels that are active for each of your Site-to-Site VPNs.  
A VPN should have two tunnels configured at all times. This provides redundancy in case of outage or planned maintenance of the devices at the AWS endpoint. For some hardware, only one tunnel is active at a time. If a VPN has no active tunnels, charges for the VPN might still apply. For more information, see [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).

**Check ID**  
`S45wrEXrLz`

**Alert Criteria**  
+ Yellow: A VPN has one active tunnel (this is normal for some hardware).
+ Yellow: A VPN has no active tunnels.

**Recommended Action**  
Be sure that two tunnels are configured for your VPN connection, and that both are active if your hardware supports it. If you no longer need a VPN connection, you can delete it to avoid charges. For more information, see [Your customer gateway device](https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html) or [Delete a Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-vpn.html).

**Additional Resources**  
+ [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+ [Create a target gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-target-gateway)

**Report columns**  
+ Status
+ Region
+ VPN ID
+ VPC
+ Virtual Private Gateway
+ Customer Gateway
+ Active Tunnels
+ Reason

## ActiveMQ Availability Zone Redundancy
<a name="activemq-availability-zone-redundancy"></a>

**Description**  
Checks that Amazon MQ for ActiveMQ brokers are configured for high availability with an active/standby broker in multiple Availability Zones.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1t3k8mqv1`

**Alert Criteria**  
+ Yellow: An Amazon MQ for ActiveMQ broker is configured in a single Availability Zone.

  Green: An Amazon MQ for ActiveMQ broker is configured in at least two Availability Zones.

**Recommended Action**  
Create a new broker with active/standby deployment mode.

**Additional Resources**  
+ [Creating an ActiveMQ broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/getting-started-activemq.html)

**Report columns**  
+ Status
+ Region
+ ActiveMQ Broker ID
+ Broker Engine Type
+ Deployment Mode
+ Last Updated Time

## RabbitMQ Availability Zone Redundancy
<a name="rabbitmq-availability-zone-redundancy"></a>

**Description**  
Checks that Amazon MQ for RabbitMQ brokers are configured for high availability with cluster instances in multiple Availability Zones.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1t3k8mqv2`

**Alert Criteria**  
+ Yellow: An Amazon MQ for RabbitMQ broker is configured in a single Availability Zone.

  Green: An Amazon MQ for RabbitMQ broker is configured in multiple Availability Zones.

**Recommended Action**  
Create a new broker with the cluster deployment mode.

**Additional Resources**  
+ [Creating a RabbitMQ broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/getting-started-rabbitmq.html)

**Report columns**  
+ Status
+ Region
+ RabbitMQ Broker ID
+ Broker Engine Type
+ Deployment Mode
+ Last Updated Time