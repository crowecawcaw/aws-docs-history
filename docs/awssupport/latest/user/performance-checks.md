

# Performance
<a name="performance-checks"></a>

Improve the performance of your service by checking your service quotas (formerly referred to as limits), so that you can take advantage of provisioned throughput, monitor for overutilized instances, and detect any unused resources.

You can use the following checks for the performance category.

**Contents**
+ [Amazon Aurora DB cluster under-provisioned for read workload](#amazon-aurora-db-cluster-under-provisioned)
+ [Amazon DynamoDB Auto Scaling Not Enabled](#dynamodb-auto-scaling-not-enabled)
+ [Amazon EBS Optimization Not Enabled](#ebs-optimization-not-enabled)
+ [Amazon EBS Provisioned IOPS (SSD) Volume Attachment Configuration](#EBS-ProvisionedIOPSRule)
+ [Amazon EBS under-provisioned volumes](#amazon-ebs-under-provisioned-volumes)
+ [Amazon EC2 Auto Scaling Group is not Associated with a Launch Template](#ec2-auto-scaling-no-launch-template)
+ [Amazon EC2 to EBS Throughput Optimization](#ebs-throughput-optimization)
+ [EC2 Virtualization Type is Paravirtual](#ec2-virtualization-type-is-paravirtual)
+ [Amazon ECS Memory Hard Limit](#ecs-memory-hard-limit)
+ [Amazon EFS Throughput Mode Optimization](#amazon-efs-throughput-mode-optimization)
+ [Amazon RDS autovacuum parameter is turned off](#rds-autovacuum-off)
+ [Amazon RDS DB clusters support only up to 64 TiB volume](#rds-db-clusters-64-tib-volume)
+ [Amazon RDS DB instances in the clusters with heterogeneous instance classes](#rds-db-instances-heterogeneous-class)
+ [Amazon RDS DB instances in the clusters with heterogeneous instance sizes](#rds-db-instances-heterogeneous-size)
+ [Amazon RDS DB memory parameters are diverging from default](#rds-db-memory-parameters-diverging)
+ [Amazon RDS enable\_indexonlyscan parameter is turned off](#rds-enable-indexonlyscan-parameter-off)
+ [Amazon RDS enable\_indexscan parameter is turned off](#rds-enable-indexscan-parameter-off)
+ [Amazon RDS general\_logging parameter is turned on](#rds-general-logging-on)
+ [Amazon RDS InnoDB\_Change\_Buffering parameter using less than optimum value](#rds-innodb-parameter-less-than-optimal)
+ [Amazon RDS innodb\_open\_files parameter is low](#rds-innodb-open-files-parameter-low)
+ [Amazon RDS innodb\_stats\_persistent parameter is turned off](#rds-innodb-stats-persistent-parameter-off)
+ [Amazon RDS instance under-provisioned for system capacity](#amazon-rds-under-provisioned-system-capacity)
+ [Amazon RDS magnetic volume is in use](#rds-magentic-volume-in-use)
+ [Amazon RDS parameter groups not using huge pages](#rds--parameter-groups-no-huge-pages)
+ [Amazon RDS query cache parameter is turned on](#rds-cache-parameter-on)
+ [Amazon RDS resources instance class update is required](#rds-resources-instance-class-update)
+ [Amazon RDS resources major versions update is required](#rds-resources-major-version-update)
+ [Amazon RDS resources using end of support engine edition under license-included](#rds-resources-using-eos-engine)
+ [Amazon Route 53 Alias Resource Record Sets](#r53-record-sets-alias)
+ [AWS Lambda under-provisioned functions for memory size](#aws-lambda-under-provisioned-functions-memory-size)
+ [AWS Lambda Functions without Concurrency Limit Configured](#lambda-functions-without-concurrency-limit)
+ [AWS Well-Architected high risk issues for performance](#well-architected-high-risk-issues-performance)
+ [CloudFront Alternate Domain Names](#cloudfront-domain-name-check)
+ [CloudFront Content Delivery Optimization](#cloudfront-content-delivery-optimization)
+ [CloudFront Header Forwarding and Cache Hit Ratio](#cloudfront-forwarded-headers)
+ [High CPU Utilization Amazon EC2 Instances](#high-utilization-amazon-ec2-instances)

## Amazon Aurora DB cluster under-provisioned for read workload
<a name="amazon-aurora-db-cluster-under-provisioned"></a>

**Description**  
Checks whether Amazon Aurora DB cluster has the resources to support a read workload.

**Check ID**  
` c1qf5bt038`

**Alert Criteria**  
Yellow:  
Increased database reads: The database load was high and the database was reading more rows than writing or updating the rows.

**Recommended Action**  
We recommend that you tune your queries to decrease the database load or add a reader DB instance to your DB cluster with the same instance class and size as the writer DB instance in the cluster. The current configuration has at least one DB instance with a continuously high database load caused mostly by read operations. Distribute these operations by adding another DB instance to the cluster and directing the read workload to the DB cluster read-only endpoint.

**Additional Resources**  
  
An Aurora DB cluster has one reader endpoint for read-only connections. This endpoint uses load balancing to manage the queries contributing the most to database load in your DB cluster. The reader endpoint directs these statements to the Aurora Read Replicas and reduces the load on the primary instance. The reader endpoint also scales the capacity to handle concurrent SELECT queries with the number of Aurora Read Replicas in the cluster.  
For more information, see [Adding Aurora Replicas to a DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-replicas-adding.html) and [Managing performance and scaling for Aurora DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Performance.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ Increased database read (count)
+ Last detection period
+ Last Updated Time

## Amazon DynamoDB Auto Scaling Not Enabled
<a name="dynamodb-auto-scaling-not-enabled"></a>

**Description**  
Checks if your Amazon DynamoDB tables and global secondary indexes have auto scaling or on-demand enabled.  
Amazon DynamoDB auto scaling uses the Application Auto Scaling service to dynamically adjust provisioned throughput capacity on your behalf in response to actual traffic patterns. This enables a table or a global secondary index to increase its provisioned read and write capacity to handle sudden increases in traffic, without throttling. When the workload decreases, Application Auto Scaling decreases the throughput so that you don't pay for unused provisioned capacity.  
You can adjust the check configuration using the parameters in your AWS Config rules.  
For more information, see [Managing throughput capacity automatically with DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz136`

**Source**  
AWS Config Managed Rule: dynamodb-autoscaling-enabled

**Alert Criteria**  
Yellow: Auto scaling is not enabled for your DynamoDB tables and/or global secondary indexes.

**Recommended Action**  
Unless you already have a mechanism to automatically scale the provisioned throughput of your DynamoDB table and/or the global secondary indexes based on your workload requirement, consider turning on auto scaling for your Amazon DynamoDB tables.   
For more information, see [Using the AWS Management Console with DynamoDB auto scalingp](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.Console.html).

**Additional Resources**  
[Managing throughput capacity automatically with DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EBS Optimization Not Enabled
<a name="ebs-optimization-not-enabled"></a>

**Description**  
Checks if Amazon EBS optimization is enabled for your Amazon EC2 instances.  
An Amazon EBS–optimized instance uses an optimized configuration stack and provides additional, dedicated capacity for Amazon EBS I/O. This optimization provides the best performance for your Amazon EBS volumes by minimizing contention between Amazon EBS I/O and other traffic from your instance..  
For more information, see [Amazon EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz142`

**Source**  
AWS Config Managed Rule: ebs-optimized-instance

**Alert Criteria**  
Yellow: Amazon EBS optimization is not enabled on supported Amazon EC2 instances.

**Recommended Action**  
Turn on Amazon EBS optimization on supported instances.  
For more information, see [Enable EBS optimization at launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#enable-ebs-optimization).

**Additional Resources**  
[Amazon EBS–optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EBS Provisioned IOPS (SSD) Volume Attachment Configuration
<a name="EBS-ProvisionedIOPSRule"></a>

**Description**  
Checks for Provisioned IOPS (SSD) volumes that are attached to an Amazon EBS optimizable Amazon Elastic Compute Cloud (Amazon EC2) instance that is not EBS-optimized.   
Provisioned IOPS (SSD) volumes in the Amazon Elastic Block Store (Amazon EBS) are designed to deliver the expected performance only when they are attached to an EBS-optimized instance.

**Check ID**  
`PPkZrjsH2q`

**Alert Criteria**  
Yellow: An Amazon EC2 instance that can be EBS-optimized has an attached Provisioned IOPS (SSD) volume but the instance is not EBS-optimized.

**Recommended Action**  
Create a new instance that is EBS-optimized, detach the volume, and reattach the volume to your new instance. For more information, see [Amazon EBS-Optimized Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html) and [Attaching an Amazon EBS Volume to an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html).

**Additional Resources**  
+ [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
+ [Amazon EBS Volume Performance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSPerformance.html)

**Report columns**  
+ Status
+ Region/AZ
+ Volume ID
+ Volume Name
+ Volume Attachment
+ Instance ID
+ Instance Type
+ EBS Optimized

## Amazon EBS under-provisioned volumes
<a name="amazon-ebs-under-provisioned-volumes"></a>

**Description**  
Checks the Amazon Elastic Block Store (Amazon EBS) volumes that were running at any time during the lookback period. This check alerts you if any EBS volumes were under-provisioned for your workloads. Consistent high utilization can indicate optimized, steady performance, but can also indicate that an application does not have enough resources.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`COr6dfpM04`

**Alert Criteria**  
 Yellow: An EBS Volume that was under-provisioned during the lookback period. To determine if a volume is under-provisioned, we consider all default CloudWatch metrics (including IOPS and throughput). The algorithm used to identify under-provisioned EBS volumes follows AWS best practices. The algorithm is updated when a new pattern has been identified.

**Recommended Action**  
Consider upsizing volumes that have high utilization.  
For more information, see [Opt in AWS Compute Optimizer for Trusted Advisor checks](compute-optimizer-with-trusted-advisor.md).

**Report columns**  
+ Status
+ Region
+ Volume ID
+ Volume Type
+ Volume Size (GB)
+ Volume Baseline IOPS
+ Volume Burst IOPS
+ Volume Burst Throughput
+ Recommended Volume Type
+ Recommended Volume Size (GB)
+ Recommended Volume Baseline IOPS
+ Recommended Volume Burst IOPS
+ Recommended Volume Baseline Throughput
+ Recommended Volume Burst Throughput
+ Lookback Period (days)
+ Performance Risk
+ Last Updated Time

## Amazon EC2 Auto Scaling Group is not Associated with a Launch Template
<a name="ec2-auto-scaling-no-launch-template"></a>

**Description**  
Checks if an Amazon EC2 Auto Scaling group is created from an Amazon EC2 launch template.  
Use a launch template to create your Amazon EC2 Auto Scaling groups to ensure access to the latest Auto Scaling group features and improvements. For example, versioning and multiple instance types.  
For more information, see [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz102`

**Source**  
AWS Config Managed Rule: autoscaling-launch-template

**Alert Criteria**  
Yellow: The Amazon EC2 Auto Scaling group isn’t associated with a valid launch template.

**Recommended Action**  
Use an Amazon EC2 launch template to create your Amazon EC2 Auto Scaling groups.  
For more information, see [Create a launch template for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html).

**Additional Resources**  
+ [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html)
+ [Create a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EC2 to EBS Throughput Optimization
<a name="ebs-throughput-optimization"></a>

**Description**  
Checks for Amazon EBS volumes whose performance might be affected by the maximum throughput capability of the Amazon EC2 instance they are attached to.   
To optimize performance, you should ensure that the maximum throughput of an Amazon EC2 instance is greater than the aggregate maximum throughput of the attached EBS volumes. This check computes the total EBS volume throughput for each five-minute period in the preceding day (based on Coordinated Universal Time (UTC)) for each EBS-optimized instance and alerts you if usage in more than half of those periods was greater than 95% of the maximum throughput of the EC2 instance.

**Check ID**  
`Bh2xRR2FGH`

**Alert Criteria**  
Yellow: In the preceding day (UTC), the aggregate throughput (megabytes/sec) of the EBS volumes attached to the EC2 instance exceeded 95% of the published throughput between the instance and the EBS volumes more than 50% of time.

**Recommended Action**  
Compare the maximum throughput of your Amazon EBS volumes (see [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)) with the maximum throughput of the Amazon EC2 instance they are attached to. See [Instance Types That Support EBS Optimization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html#ebs-optimization-support).   
Consider attaching your volumes to an instance that supports higher throughput to Amazon EBS for optimal performance.

**Additional Resources**  
+ [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
+ [Amazon EBS-Optimized Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html)
+ [Monitoring the Status of Your Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html)
+ [Attaching an Amazon EBS Volume to an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html)
+ [Detaching an Amazon EBS Volume from an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-detaching-volume.html)
+ [Deleting an Amazon EBS Volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-volume.html)

**Report columns**  
+ Status
+ Region
+ Instance ID
+ Instance Type
+ Time Near Maximum

## EC2 Virtualization Type is Paravirtual
<a name="ec2-virtualization-type-is-paravirtual"></a>

**Description**  
Checks if the virtualization type of an Amazon EC2 instance is paravirtual.  
It's a best practice that you use Hardware Virtual Machine (HVM) instances instead of paravirtual instances, when possible. This is because of enhancements in HVM virtualization and the availability of PV drivers for HVM AMIs, which have closed the performance gap that historically existed between PV and HVM guests. It's important to note that current generation instance types do not support PV AMIs. Therefore, choosing an HVM instance type provides the best performance and compatibility with modern hardware.  
For more information, see [Linux AMI virtualization types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz148`

**Source**  
AWS Config Managed Rule: ec2-paravirtual-instance-check

**Alert Criteria**  
Yellow: The virtualization type of Amazon EC2 instances is paravirtual.

**Recommended Action**  
Use HVM virtualization for your Amazon EC2 instances, and use a compatible instance type.  
For information on choosing the appropriate virtualization type, see [Compatibility for changing the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resize-limitations.html).

**Additional Resources**  
[Compatibility for changing the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resize-limitations.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon ECS Memory Hard Limit
<a name="ecs-memory-hard-limit"></a>

**Description**  
Checks if Amazon ECS task definitions have a set memory limit for its container definitions. The total amount of memory reserved for all containers within a task must be lower than the task memory value.  
For more information, see [Container definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definitions).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz176`

**Source**  
AWS Config Managed Rule: ecs-task-definition-memory-hard-limit

**Alert Criteria**  
Yellow: Amazon ECS memory hard limit is not set.

**Recommended Action**  
Allocate memory for your Amazon ECS tasks to avoid running out of memory. If your container attempts to exceed the specified memory, then the container is terminated.   
For more information, see [How can I allocate memory to tasks in Amazon ECS?](https://repost.aws/knowledge-center/allocate-ecs-memory-tasks).

**Additional Resources**  
[Cluster reservation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html#cluster_reservation)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EFS Throughput Mode Optimization
<a name="amazon-efs-throughput-mode-optimization"></a>

**Description**  
Checks if the Amazon EFS file system is currently configured to use Bursting throughput mode. Amazon EFS Bursting throughput uses “credits” for performance above baseline throughput (50 KiB/s per GiB). After credits are depleted, performance throttles to baseline throughput, which potentially causes slowness, application failures, and timeouts for your users. To learn more about bursting mode, see [Throughput mode](https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes) in the *Amazon EFS User Guide*

**Check ID**  
`c1dfprch02`

**Alert Criteria**  
+ Yellow: File system is using Bursting throughput mode.

**Recommended Action**  
If your Bursting throughput credits are low or depleted, consider switching to Provisioned or Elastic throughput mode to provide your users and applications with their desired throughput. With Provisioned throughput, you can set your workload’s required throughput, and you pay for the amount of throughput enabled for the file system. If you're unsure of your throughput requirements, you can use Elastic throughput mode where your throughput scales elastically with your workload and you only pay for what you use, measured by total data transferred. You can update your file system configuration to switch between the throughput modes at any time. To learn more about throughput pricing, see [Amazon EFS Pricing](https://aws.amazon.com/efs/pricing/). You can also estimate your costs using the [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/EFS).

**Additional Resources**  
+ [Bursting throughput](https://docs.aws.amazon.com/efs/latest/ug/performance.html#bursting)
+ [Amazon EFS Pricing](http://aws.amazon.com/efs/pricing/)
+ [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/EFS)

**Report columns**  
+ Status
+ Region
+ EFS File System ID
+ Throughput mode
+ Last Updated Time

## Amazon RDS autovacuum parameter is turned off
<a name="rds-autovacuum-off"></a>

**Description**  
The autovacuum parameter is turned off for your DB instances. Turning autovacuum off increases the table and index bloat and impacts the performance.  
We recommend that you turn on autovacuum in your DB parameter groups.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt025`

**Alert Criteria**  
Yellow: DB parameter groups have autovacuum turned off.

**Recommended Action**  
Turn on the autovacuum parameter in your DB parameter groups.

**Additional Resources**  
PostgreSQL database requires periodic maintenance which is known as vacuuming. Autovacuum in PostgreSQL automates running **VACCUUM** and **ANALYZE** commands. This process gathers the table statistics and deletes the dead rows. When autovacuum is turned off, the increase of the table, index bloat, stale statistics will impact the database performance.  
For more information, see [Understanding autovacuum in Amazon RDS for PostgreSQL environments](https://aws.amazon.com/blogs/database/understanding-autovacuum-in-amazon-rds-for-postgresql-environments/).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS DB clusters support only up to 64 TiB volume
<a name="rds-db-clusters-64-tib-volume"></a>

**Description**  
Your DB clusters support volumes up to 64 TiB. The latest engine versions support volumes up to 128 TiB. We recommend that you upgrade the engine version of your DB cluster to latest versions to support volumes up to 128 TiB.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt017`

**Alert Criteria**  
Yellow: DB clusters have support for volumes only up to 64 TiB.

**Recommended Action**  
Upgrade the engine version of your DB clusters to support volumes up to 128 TiB.

**Additional Resources**  
When you scale up your application on a single Amazon Aurora DB cluster, you may not reach the limit if the storage limit is 128 TiB. The increased storage limit helps to avoid deleting the data or splitting the database across multiple instances.  
For more information, see [Amazon Aurora size limits](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html#RDS_Limits.FileSize.Aurora).

**Report columns**  
+ Status
+ Region
+ Resource
+ Engine Name
+ Engine Version Current
+ Recommended Value
+ Last Updated Time

## Amazon RDS DB instances in the clusters with heterogeneous instance classes
<a name="rds-db-instances-heterogeneous-class"></a>

**Description**  
We recommend that you use the same DB instance class and size for all the DB instances in your DB cluster.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt009`

**Alert Criteria**  
Red: DB clusters have the DB instances with heterogeneous instance classes.

**Recommended Action**  
Use the same instance class and size for all the DB instances in your DB cluster.

**Additional Resources**  
When the DB instances in your DB cluster use different DB instance classes or sizes, there can be an imbalance in the workload for the DB instances. During a failover, one of the reader DB instance changes to a writer DB instance. If the DB instances use the same DB instance class and size, the workload can be balanced for the DB instances in your DB cluster.  
For more information, see [Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html#Aurora.Replication.Replicas).

**Report columns**  
+ Status
+ Region
+ Resource
+ Recommended Value
+ Engine Name
+ Last Updated Time

## Amazon RDS DB instances in the clusters with heterogeneous instance sizes
<a name="rds-db-instances-heterogeneous-size"></a>

**Description**  
We recommend that you use the same DB instance class and size for all the DB instances in your DB cluster.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt008`

**Alert Criteria**  
Red: DB clusters have the DB instances with heterogeneous instance sizes.

**Recommended Action**  
Use the same instance class and size for all the DB instances in your DB cluster.

**Additional Resources**  
When the DB instances in your DB cluster use different DB instance classes or sizes, there can be an imbalance in the workload for the DB instances. During a failover, one of the reader DB instance changes to a writer DB instance. If the DB instances use the same DB instance class and size, the workload can be balanced for the DB instances in your DB cluster.  
For more information, see [Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html#Aurora.Replication.Replicas).

**Report columns**  
+ Status
+ Region
+ Resource
+ Recommended Value
+ Engine Name
+ Last Updated Time

## Amazon RDS DB memory parameters are diverging from default
<a name="rds-db-memory-parameters-diverging"></a>

**Description**  
The memory parameters of the DB instances are significantly different from the default values. These settings can impact performance and cause errors.  
We recommend that you reset the custom memory parameters for the DB instance to their default values in the DB parameter group.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt020`

**Alert Criteria**  
Yellow: DB parameter groups have memory parameters that diverge considerably from the default values.

**Recommended Action**  
Reset the memory parameters to their default values.

**Additional Resources**  
For more information, see [Best practices for configuring parameters for Amazon RDS for MySQL, part 1: Parameters related to performance](https://aws.amazon.com/blogs/database/best-practices-for-configuring-parameters-for-amazon-rds-for-mysql-part-1-parameters-related-to-performance/).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS enable\_indexonlyscan parameter is turned off
<a name="rds-enable-indexonlyscan-parameter-off"></a>

**Description**  
The query planner or optimizer can't use the index-only scan plan type when it is turned off.  
We recommend that you set the **enable\_indexonlyscan** parameter value to 1.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt028`

**Alert Criteria**  
Yellow: DB parameter groups have **enable\_indexonlyscan** parameter turned off.

**Recommended Action**  
Set the parameter **enable\_indexonlyscan** to 1.

**Additional Resources**  
When you turn off **enable\_indexonlyscan** parameter, it prevents the query planner from selecting an optimal execution plan. The query planner uses a different plan type, such as index scan which can increase the query cost and execution time. The index only scan plan type retrieves the data without accessing the table data.  
For more information, see [enable\_indexonlyscan (boolean)](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-ENABLE-INDEXONLYSCAN) on the PostgreSQL documentation website.

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS enable\_indexscan parameter is turned off
<a name="rds-enable-indexscan-parameter-off"></a>

**Description**  
The query planner or optimizer can't use the index scan plan type when it is turned off.  
We recommend that you set the **enable\_indexscan** parameter value to 1.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt029`

**Alert Criteria**  
Yellow: DB parameter groups have **enable\_indexscan** parameter turned off.

**Recommended Action**  
Set the parameter **enable\_indexscan** to 1.

**Additional Resources**  
When you turn off **enable\_indexscan** parameter, it prevents the query planner from selecting an optimal execution plan. The query planner uses a different plan type, such as index scan which can increase the query cost and execution time.  
For more information, see [enable\_indexscan (boolean)](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-ENABLE-INDEXSCAN) on the PostgreSQL documentation website.

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS general\_logging parameter is turned on
<a name="rds-general-logging-on"></a>

**Description**  
The general logging is turned on for your DB instance. This setting is useful while troubleshooting the database issues. However, turning on general logging increases the amount of I/O operations and allocated storage space, which might result in contention and performance degradation.  
Check your requirements for general logging usage. We recommend that you set the **general\_logging** parameter value to **0**.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt037`

**Alert Criteria**  
Yellow: DB parameter groups have **general\_logging** turned on.

**Recommended Action**  
Check your requirements for general logging usage. If it isn't mandatory, we recommend that you to set the **general\_logging** parameter value to **0**.

**Additional Resources**  
The general query log is turned on when the **general\_logging** parameter value is 1. The general query log contains records of the database server operations. The server writes information to this log when clients connect or disconnect and the logs contain each SQL statement received from the clients. The general query log is useful when you suspect an error in a client and you want to find the information the client to sent to the database server.  
For more information, see [Overview of RDS for MySQL database logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.LogFileSize.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS InnoDB\_Change\_Buffering parameter using less than optimum value
<a name="rds-innodb-parameter-less-than-optimal"></a>

**Description**  
Change buffering allows a MySQL DB instance to defer a few writes, which are required to maintain secondary indexes. This feature was useful in environments with slow disks. The change buffering configuration improved the DB performance slightly but caused a delay in crash recovery and long shutdown times during upgrade.  
We recommend that you set the value of **innodb\_change\_buffering** parameter to **NONE**.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt021`

**Alert Criteria**  
Yellow: DB parameter groups have **innodb\_change\_buffering** parameter set to a low optimum value.

**Recommended Action**  
Set **innodb\_change\_buffering** parameter value to **NONE** in your DB parameter groups.

**Additional Resources**  
For more information, see [Best practices for configuring parameters for Amazon RDS for MySQL, part 1: Parameters related to performance](https://aws.amazon.com/blogs/database/best-practices-for-configuring-parameters-for-amazon-rds-for-mysql-part-1-parameters-related-to-performance/).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS innodb\_open\_files parameter is low
<a name="rds-innodb-open-files-parameter-low"></a>

**Description**  
The innodb\_open\_files parameter controls the number of files InnoDB can open at one time. InnoDB opens all of the log and system tablespace files when mysqld is running.  
Your DB instance has a low value for the maximum number of files InnoDB can open at one time. We recommend that you set the innodb\_open\_files parameter to a minimum value of 65.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt033`

**Alert Criteria**  
Yellow: DB parameter groups have the InnoDB open files setting misconfigured.

**Recommended Action**  
Set the innodb\_open\_files parameter to a minimum value of 65.

**Additional Resources**  
The innodb\_open\_files parameter controls the number of files InnoDB can open at one time. InnoDB keeps all the log files and the system tablespace files open when mysqld is running. InnoDB also needs to open a few .ibd files, if file-per-table storage model is used. When the innodb\_open\_files setting is low, it impacts the database performance and the server may fail to start.  
For more information, see [InnoDB Startup Options and System Variables - innodb\_open\_files](https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_open_files) on the MySql documentation website.

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS innodb\_stats\_persistent parameter is turned off
<a name="rds-innodb-stats-persistent-parameter-off"></a>

**Description**  
Your DB instance isn't configured to persist the InnoDB statistics to the disk. When the statistics aren't stored, they are recalculated each time the instance restarts and the table accessed. This leads to variations in the query execution plan. You can modify the value of this global parameter at the table level.  
We recommend that you set the **innodb\_stats\_persistent** parameter value to **ON**.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt032`

**Alert Criteria**  
Yellow: DB parameter groups have optimizer statistics that aren't persisted to the disk.

**Recommended Action**  
Set the **innodb\_stats\_persistent** parameter value to **ON**.

**Additional Resources**  
If the **innodb\_stats\_persistent** parameter is set to **ON**, then the optimizer statistics are persisted when the instance restarts. This improves the execution plan stability and consistent query performance. You can modify global statistics persistence at the table level by using the clause **STATS\_PERSISTENT** when you create or alter a table.  
For more information, see [Best practices for configuring parameters for Amazon RDS for MySQL, part 1: Parameters related to performance](https://aws.amazon.com/blogs/database/best-practices-for-configuring-parameters-for-amazon-rds-for-mysql-part-1-parameters-related-to-performance/).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS instance under-provisioned for system capacity
<a name="amazon-rds-under-provisioned-system-capacity"></a>

**Description**  
Checks whether Amazon RDS instance or Amazon Aurora DB instance has the required system capacity to operate.

**Check ID**  
` c1qf5bt039`

**Alert Criteria**  
Yellow:  
Out-of-memory kills: When a process on the database host is stopped because of memory reduction at the OS level, the Out Of Memory (OOM) kills counter increases.  
Excessive swapping: os.memory.swap.in and os.memory.swap.out metric values were high.

**Recommended Action**  
We recommend that you tune your queries to use less memory or use a DB instance type with higher allocated memory. When the instance is running low on memory, this impacts the database performance.

**Additional Resources**  
Out-of-memory kills were detected: Linux kernel invokes the Out of Memory (OOM) Killer when the processes running on the host require more than the memory physically available from the operating system. In this case, the OOM Killer reviews all the running processes, and stops one or more processes, in order to free up system memory and keep the system running.  
Swapping is detected: When the memory isn't sufficient on the database host, the operating system sends a few minimum used pages to the disk in the swap space. This offloading process impacts the database performance.  
For more information, see [Amazon RDS Instance Types](https://aws.amazon.com/rds/instance-types/) and [Scaling yourAmazon RDS instance](https://aws.amazon.com/blogs/database/scaling-your-amazon-rds-instance-vertically-and-horizontally/).

**Report columns**  
+ Status
+ Region
+ Resource
+ Out-of-memory kills (count)
+ Excessive swapping (count)
+ Last detection period
+ Last Updated Time

## Amazon RDS magnetic volume is in use
<a name="rds-magentic-volume-in-use"></a>

**Description**  
Your DB instances are using magnetic storage. Magnetic storage isn't recommended for most of the DB instances. Choose a different storage type: General Purpose (SSD) or Provisioned IOPS.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt000`

**Alert Criteria**  
Yellow: Amazon RDS resources are using magnetic storage.

**Recommended Action**  
Choose a different storage type: General Purpose (SSD) or Provisioned IOPS.

**Additional Resources**  
Magnetic storage is an earlier generation storage type. The General Purpose (SSD) or Provisioned IOPS is the recommended storage type for new storage requirements. These storage types provide higher and consistent performance, and improved storage size options.  
For more information, see [Previous generation volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#vol-type-prev).

**Report columns**  
+ Status
+ Region
+ Resource
+ Recommended Value
+ Engine Name
+ Last Updated Time

## Amazon RDS parameter groups not using huge pages
<a name="rds--parameter-groups-no-huge-pages"></a>

**Description**  
Large pages can increase database scalability, but your DB instance isn't using large pages. We recommend that you set the **use\_large\_pages** parameter value to **ONLY** in the DB parameter group for your DB instance.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt024`

**Alert Criteria**  
Yellow: DB parameter groups don't use large pages.

**Recommended Action**  
Set the **use\_large\_pages** parameter value to **ONLY** in your DB parameter groups.

**Additional Resources**  
For more information, see [Turning on HugePages for an RDS for Oracle instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.HugePages.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS query cache parameter is turned on
<a name="rds-cache-parameter-on"></a>

**Description**  
When changes require that your query cache is purged, your DB instance will appear to stall. Most workloads don't benefit from a query cache. The query cache was removed from MySQL version 8.0. We recommend that you set the query\_cache\_type parameter to 0.   
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt022`

**Alert Criteria**  
Yellow: DB parameter groups have query cache turned on.

**Recommended Action**  
Set the query\_cache\_type parameter value to 0 in your DB parameter groups.

**Additional Resources**  
For more information, see [Best practices for configuring parameters for Amazon RDS for MySQL, part 1: Parameters related to performance](https://aws.amazon.com/blogs/database/best-practices-for-configuring-parameters-for-amazon-rds-for-mysql-part-1-parameters-related-to-performance/).

**Report columns**  
+ Status
+ Region
+ Resource
+ Parameter Name
+ Recommended Value
+ Last Updated Time

## Amazon RDS resources instance class update is required
<a name="rds-resources-instance-class-update"></a>

**Description**  
Your database is running a previous generation DB instance class. We have replaced DB instance classes from a previous generation with DB instance classes with better cost, performance, or both. We recommend that you run your DB instance with a DB instance class from a newer generation.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt015`

**Alert Criteria**  
Red: DB instances are using end of support DB instance class.

**Recommended Action**  
Upgrade to latest DB instance class.

**Additional Resources**  
For more information, see [Supported DB engines for DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#Concepts.DBInstanceClass.Support).

**Report columns**  
+ Status
+ Region
+ Resource
+ DB Instance Class
+ Recommended Value
+ Engine Name
+ Last Updated Time

## Amazon RDS resources major versions update is required
<a name="rds-resources-major-version-update"></a>

**Description**  
Databases with the current major version for the DB engine won't be supported. We recommend that you upgrade to the latest major version which includes new functionality and enhancements.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt014`

**Alert Criteria**  
Red: RDS resources are using end of support major versions.

**Recommended Action**  
Upgrade to the latest major version for the DB engine.

**Additional Resources**  
Amazon RDS releases new versions for the supported database engines to maintain your databases with the latest version. The new released versions may include bug fixes, security enhancements, and other improvements for the database engine. You can minimize the downtime required for the DB instance upgrade by using a blue/green deployment.  
For more information, see the following resources:  
+  [Upgrading a DB instance engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html)
+  [Amazon Aurora updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Updates.html)
+  [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ Engine Name
+ Engine Current Version
+ Recommended Value
+ Last Updated Time

## Amazon RDS resources using end of support engine edition under license-included
<a name="rds-resources-using-eos-engine"></a>

**Description**  
We recommend that you upgrade the major version to the latest engine version supported by Amazon RDS to continue with the current license support. The engine version of your database won't be supported with the current license.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.
When a DB instance or DB cluster is stopped, you can view the Amazon RDS recommendations in Trusted Advisor for 3 to 5 days. After five days, the recommendations are not available in Trusted Advisor. To view the recommendations, open the Amazon RDS console, and then choose **Recommendations**.  
If you delete a DB instance or DB cluster, then recommendations associated with those instances or clusters are not available in Trusted Advisor or the Amazon RDS management console.

**Check ID**  
`c1qf5bt016`

**Alert Criteria**  
Red: Amazon RDS resources are using end of support engine edition under license-included model.

**Recommended Action**  
We recommend that you upgrade your database to the latest supported version in Amazon RDS to continue using the licensed model.

**Additional Resources**  
For more information, see [Oracle major version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.Major.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ Engine Name
+ Engine Version Current
+ Recommended Value
+ Engine Name
+ Last Updated Time

## Amazon Route 53 Alias Resource Record Sets
<a name="r53-record-sets-alias"></a>

**Description**  
Checks for resource record sets that can be changed to alias resource record sets to improve performance and save money.   
An alias resource record set routes DNS queries to an AWS resource (for example, an Elastic Load Balancing load balancer or an Amazon S3 bucket) or to another Route 53 resource record set. When you use alias resource record sets, Route 53 routes your DNS queries to AWS resources free of charge.  
Hosted zones created by AWS services won’t appear in your check results.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`B913Ef6fb4`

**Alert Criteria**  
+ Yellow: A resource record set is a CNAME to an Amazon S3 website.
+ Yellow: A resource record set is a CNAME to an Amazon CloudFront distribution.
+ Yellow: A resource record set is a CNAME to an Elastic Load Balancing load balancer.

**Recommended Action**  
Replace the listed CNAME resource record sets with alias resource record sets; see [Choosing Between Alias and Non-Alias Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingAliasRRSets.html).   
You also need to change the record type from CNAME to A or AAAA, depending on the AWS resource. See [Values that You Specify When You Create or Edit Amazon Route 53 Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html).

**Additional Resources**  
[Routing Queries to AWS Resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-aws-resources.html)

**Report columns**  
+ Status
+ Hosted Zone Name
+ Hosted Zone ID
+ Resource Record Set Name
+ Resource Record Set Type
+ Resource Record Set Identifier
+ Alias Target

## AWS Lambda under-provisioned functions for memory size
<a name="aws-lambda-under-provisioned-functions-memory-size"></a>

**Description**  
Checks the AWS Lambda functions that were invoked at least once during the lookback period. This check alerts you if any of your Lambda functions were under-provisioned for memory size. When you have Lambda functions that are under-provisioned for memory size, these functions take longer time to complete.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`COr6dfpM06`

**Alert Criteria**  
 Yellow: A Lambda function that was under-provisioned for memory size during the lookback period. To determine if a Lambda function is under-provisioned, we consider all default CloudWatch metrics for that function. The algorithm used to identify under-provisioned Lambda functions for memory size follows AWS best practices. The algorithm is updated when a new pattern has been identified.

**Recommended Action**  
 Consider increasing the memory size of your Lambda functions.  
For more information, see [Opt in AWS Compute Optimizer for Trusted Advisor checks](compute-optimizer-with-trusted-advisor.md).

**Report columns**  
+ Status
+ Region
+ Function Name
+ Function Version
+ Memory Size (MB)
+ Recommended Memory Size (MB)
+ Lookback Period (days)
+ Performance Risk
+ Last Updated Time

## AWS Lambda Functions without Concurrency Limit Configured
<a name="lambda-functions-without-concurrency-limit"></a>

**Description**  
Checks if AWS Lambda functions are configured with function-level concurrent execution limit.  
Concurrency is the number of in-flight requests your AWS Lambda function is handling at the same time. For each concurrent request, Lambda provisions a separate instance of your execution environment.   
You can specify the minimum and maximum reserved concurrency limit using the **concurrencyLimitLow** and **ConcurrencyLimitHigh** parameters in your AWS Config rules.  
For more information, see [Lambda function scaling](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz181`

**Source**  
AWS Config Managed Rule: lambda-concurrency-check

**Alert Criteria**  
Yellow: Lambda function has no concurrency limit configured.

**Recommended Action**  
Make sure that your Lambda functions have concurrency configured. A concurrency limit for your Lambda functions helps make sure that your function processes requests reliably and predictably. A concurrency limit reduces the risk of your function being overwhelmed due to a sudden surge in traffic.  
For more information, see [Configuring reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).

**Additional Resources**  
+ [Lambda function scaling](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html)
+ [Configuring reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## AWS Well-Architected high risk issues for performance
<a name="well-architected-high-risk-issues-performance"></a>

**Description**  
Checks for high risk issues (HRIs) for your workloads in the performance pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Wxdfp4B1L2`

**Alert Criteria**  
+ Red: At least one active high risk issue was identified in the performance pillar for AWS Well-Architected.
+ Green: No active high risk issues were detected in the performance pillar for AWS Well-Architected.

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
+ Number of identified HRIs for Performance
+ Number of HRIs resolved for Performance
+ Number of questions answered for Performance
+ Total number of questions in Performance pillar
+ Last Updated Time

## CloudFront Alternate Domain Names
<a name="cloudfront-domain-name-check"></a>

**Description**  
This check applies to classic Amazon CloudFront distributions.
Checks that DNS is properly configured in classic Amazon CloudFront distributions that use alternate domain names (CNAMEs).   
If a CloudFront distribution includes alternate domain names, the DNS configuration for the domains must route DNS queries to that distribution.  
This check assumes Amazon Route 53 DNS and Amazon CloudFront distribution are configured in the same AWS account. As such the alert list might include resources otherwise working as expected due to DNS setting outsides of this AWS account.

**Check ID**  
`N420c450f2`

**Alert Criteria**  
+ Yellow: A CloudFront distribution includes alternate domain names, but the DNS configuration is not correctly set up with a CNAME record or an Amazon Route 53 alias resource record.
+ Yellow: A CloudFront distribution includes alternate domain names, but Trusted Advisor could not evaluate the DNS configuration because there were too many redirects.
+ Yellow: A CloudFront distribution includes alternate domain names, but Trusted Advisor could not evaluate the DNS configuration for some other reason, most likely because of a timeout. 

**Recommended Action**  
 Update the DNS configuration to route DNS queries to the CloudFront distribution; see [Using Alternate Domain Names (CNAMEs)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html).   
If you're using Amazon Route 53 as your DNS service, see [Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html). If the check timed out, try refreshing the check.

**Additional Resources**  
[Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/)

**Report columns**  
+ Status
+ Distribution ID
+ Distribution Domain Name
+ Alternate Domain Name
+ Reason

## CloudFront Content Delivery Optimization
<a name="cloudfront-content-delivery-optimization"></a>

**Description**  
Checks for cases where data transfer from Amazon Simple Storage Service (Amazon S3) buckets could be accelerated by using Amazon CloudFront, the AWS global content delivery service.   
When you configure CloudFront to deliver your content, requests for your content are automatically routed to the nearest edge location where content is cached. This routing allows content to be delivered to your users with the best possible performance. A high ratio of data transferred out compared to the data stored in the bucket indicates that you could benefit from using Amazon CloudFront to deliver the data.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`796d6f3D83`

**Alert Criteria**  
+ Yellow: The amount of data transferred out of the bucket to your users by GET requests in the 30 days preceding the check is at least 25 times greater than the average amount of data stored in the bucket.
+ Red: The amount of data transferred out of the bucket to your users by GET requests in the 30 days preceding the check is at least 10 TB and at least 25 times greater than the average amount of data stored in the bucket. 

**Recommended Action**  
Consider using CloudFront for better performance. See [Amazon CloudFront Product Details](https://aws.amazon.com/cloudfront/details).  
If the data transferred is 10 TB per month or more, see [Amazon CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing) to explore possible cost savings. 

**Additional Resources**  
+ [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/)
+ [AWS Case Study: PBS](https://aws.amazon.com/solutions/case-studies/pbs/)

**Report columns**  
+ Status
+ Region
+ Bucket Name
+ S3 Storage (GB)
+ Data Transfer Out (GB)
+ Ratio of Transfer to Storage

## CloudFront Header Forwarding and Cache Hit Ratio
<a name="cloudfront-forwarded-headers"></a>

**Description**  
This check applies to classic Amazon CloudFront distributions.
Checks the HTTP request headers that CloudFront currently receives from the client and forwards to your origin server.  
Some headers, such as date, or user-agent, significantly reduce the cache hit ratio (the proportion of requests that are served from a CloudFront edge cache). This increases the load on your origin and reduces performance, because CloudFront must forward more requests to your origin.

**Check ID**  
`N415c450f2`

**Alert Criteria**  
Yellow: One or more request headers that CloudFront forwards to your origin might significantly reduce your cache hit ratio.

**Recommended Action**  
Consider whether the request headers provide enough benefit to justify the negative effect on the cache hit ratio. If your origin returns the same object regardless of the value of a given header, we recommend that you don't configure CloudFront to forward that header to the origin. For more information, see [Configuring CloudFront to Cache Objects Based on Request Headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html).

**Additional Resources**  
+ [Increasing the Proportion of Requests that Are Served from CloudFront Edge Caches](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html#cache-hit-ratio-request-headers)
+ [CloudFront Cache Statistics Reports](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-statistics.html)
+ [HTTP Request Headers and CloudFront Behavior](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-headers-behavior)

**Report columns**  
+ Distribution ID
+ Distribution Domain Name
+ Cache Behavior Path Pattern
+ Headers

## High CPU Utilization Amazon EC2 Instances
<a name="high-utilization-amazon-ec2-instances"></a>

**Description**  
Checks the Amazon Elastic Compute Cloud (Amazon EC2) instances that were running at any time during the last 14 days. An alert is sent if daily CPU utilization was greater than 90% on four or more days.  
Consistent high utilization can indicate optimized, steady performance. However, it can also indicate that an application does not have enough resources. To get daily CPU utilization data, download the report for this check.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`ZRxQlPsb6c`

**Alert Criteria**  
Yellow: An instance had more than 90% daily average CPU utilization on at least 4 of the previous 14 days. 

**Recommended Action**  
Consider adding more instances. For information about scaling the number of instances based on demand, see [What is Auto Scaling?](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/WhatIsAutoScaling.html)

**Additional Resources**  
+ [Monitoring Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-monitoring.html)
+ [Instance Metadata and User Data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html)
+ [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/)
+ [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/latest/userguide/)

**Report columns**  
+ Region/AZ
+ Instance ID
+ Instance Type
+ Instance Name
+ 14-Day Average CPU Utilization
+ Number of Days over 90% CPU Utilization