

# Viewing idle resource recommendations

Compute Optimizer helps you find idle resources. You can delete or stop these resources to reduce your AWS cloud costs. You can access idle recommendations through the Compute Optimizer console and our [ set of APIs](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetIdleRecommendations.html). Idle recommendations are available for the following supported AWS resources:
+ Amazon EC2 instances
+ Amazon EC2 Auto Scaling groups
+ Amazon EBS volumes
+ Amazon ECS services on Fargate
+ Amazon Aurora and RDS databases
+ Amazon NAT Gateway
+ Amazon DynamoDB
+ Amazon ElastiCache
+ Amazon MemoryDB
+ Amazon DocumentDB
+ Amazon WorkSpaces
+ Amazon SageMaker endpoints

Compute Optimizer refreshes the recommendations daily. To make them, Compute Optimizer looks at the specifications and use of your AWS resources over the lookback period. The lookback period depends on the resource and your recommendation preferences. If you don't set any recommendation preferences, we use the default lookback period of 14 days. For more information, see [Idle criteria for each resource](#idle-criteria).

**Lookback period exceptions**  
For EBS volumes and NAT Gateway we analyze the attachment status over a 32-day lookback period. For WorkSpaces, we analyze user connection activity over a 63-day lookback period.
Changing the lookback period for EBS volume recommendations to 14 days does not affect the 32-day lookback period used to determine whether an EBS volume is unattached.
For ElastiCache, recommendations might take up to 48 hours to appear after you opt in to Compute Optimizer.

**Topics**
+ [Idle criteria for each resource](#idle-criteria)
+ [Estimated monthly savings](#idle-savings-calculation)

## Idle criteria for each resource
<a name="idle-criteria"></a>

Each supported resource has its own idle criteria. The following table lists the idle criteria for each resource. It also lists the action that Compute Optimizer recommends for the idle resource.


| Resource | Metric analyzed | Idle criteria | Recommended action | 
| --- | --- | --- | --- | 
| Amazon EC2 instances | CPU utilization, network IO, GPU utilization, GPU encoder usage (the percentage of time the GPU's video encoder is active), and GPU memory usage | The peak CPU utilization is below 5% and your network I/O is less than 5 MB/day over the 14-day lookback period.<br />G or P instance types are considered idle if they meet the following criteria over the 14-day lookback period:+  GPU isn’t actively working for more than 99% of the lookback period <br />+  GPU encoder isn't used for 99% or more of the instance's runtime <br />+  GPU memory usage at instance level is less than 5%  <br />+  CPU maximum utilization is less than 5% <br />+  Network utilization is less than 5 MB/day  | Verify whether you need this instance. If you don't need it, consider deleting this instance. | 
| EC2 Auto Scaling groups | CPU utilization, network IO, GPU utilization, GPU encoder usage, and GPU memory usage | The EC2 Auto Scaling group has no instances with more than 5% peak CPU utilization or 5 MB/day network utilization over the 14-day lookback period.<br />EC2 Auto Scaling groups that use G or P instance types are considered idle if the instances meet the following criteria over the 14-day lookback period:+  GPU isn’t actively working for more than 99% of the lookback period <br />+  GPU encoder isn't used for 99% or more of the instance's runtime <br />+  GPU memory usage at instance level is less than 5%  <br />+  CPU maximum utilization is less than 5% <br />+  Network utilization is less than 5 MB/day  | Verify whether you need this group. Consider scaling down this group to one instance or consider deleting it. | 
| Amazon EBS volumes | Read/Write operations and attachment status | Compute Optimizer can find an EBS volume to be idle or unattached.+  **Idle** — If the sum of read/write operations is less than 1 per day over the look-back period, and the volume is not a root volume. The default look-back period is 14 days, which you can extend up to 32 days. <br />+  **Unattached** — If the volume isn’t attached to any EC2 instance over the 32-day lookback period.    Changing the lookback period for EBS volume recommendations to 14 days does not affect the 32-day lookback period used to determine whether an EBS volume is unattached.    | Verify whether you need this volume. If you don't need it, we recommend that you create a snapshot of the volume and consider deleting it. | 
| Amazon ECS services on Fargate | CPU utilization and memory utilization | The peak CPU and memory utilization is below 1% over the lookback period. The default lookback period is 14 days, which you can extend up to 32 days. | Verify whether your containerized application is running as expected. If the application is not running, consider deleting this service. | 
| Amazon Aurora and RDS databases | Database connections, read/write IOPS, and CPU utilization | **RDS for MySQL and RDS for PostgreSQL**<br />The DB instance is not a read replica, and had no database connections, low CPU usage, and low read/write activity over the lookback period.<br />**Aurora MySQL and Aurora PostgreSQL**<br />The DB instance is not part of a secondary cluster in an Aurora Global Database, and had no database connections, low CPU usage, and low read/write activity over the lookback period. | Verify whether you need this DB instance. If you don’t need this instance temporarily, you can stop RDS MySQL and RDS PostgreSQL DB instances for up to 7 days. If you no longer need this instance, you can create a DB snapshot and delete the instance. For idle Aurora MySQL and Aurora PostgreSQL instances, you can also change the DB instance class to db.serverless. | 
| Amazon NAT Gateway | Active connection count, Packets in from source, Packets in from destination | The NAT Gateway is in available state, is not associated with any AWS Route Tables, and has no active connection, no Packets in from both source and destination over the lookback period. | Verify whether you need this NAT Gateway. Check if it's part of a disaster recovery setup or serves as a backup in your network architecture. | 
| Amazon DynamoDB | Consumed read capacity units and consumed write capacity units | Applies to provisioned tables only. A table is considered idle when there are no consumed read or write capacity units at both the table level and all Global Secondary Index (GSI) levels over the 14-day lookback period. | Verify whether this table is unused. Consider switching to on-demand mode or minimize provisioned capacity. If no longer needed, consider exporting data to S3 and deleting the resource. | 
| Amazon ElastiCache | New connections, engine CPU utilization, cache hits, cache misses, get commands, and set commands | Applies to Redis and Valkey engines only.<br />**Node-based (provisioned)**<br />The cluster has no new connections, engine CPU utilization is below 1%, and no cache hits, misses, get commands, or set commands over the 14-day lookback period. Metrics are evaluated at the node level; a cluster is idle only if all nodes are idle.<br />**Serverless**<br />The cluster has no processing units consumed, no current or new connections, and no cache hits, misses, get commands, or set commands over the 14-day lookback period. | Verify whether your application still requires this caching layer. For provisioned clusters, consider switching to ElastiCache Serverless for variable workloads. If not required, consider deleting the resource. | 
| Amazon MemoryDB | New connections, engine CPU utilization, keyspace hits, and keyspace misses | The cluster has no new connections, engine CPU utilization is below 1%, and no keyspace hits or misses over the 14-day lookback period. The cluster must be in available status. | Verify whether your application still requires this caching layer. If not required, consider deleting the resource. | 
| Amazon DocumentDB | Database connections | Applies to both provisioned and serverless clusters. Elastic clusters are excluded.<br />The cluster has no database connections over the 14-day lookback period. The cluster must be in available status. | **Provisioned**<br />Verify whether you need this cluster. If not needed temporarily, you can stop the resource for up to 7 days or consider switching to DocumentDB Serverless. If no longer needed, create a DB snapshot and delete the resource.<br />**Serverless**<br />Verify whether you need this cluster. If not needed temporarily, you can stop the resource for up to 7 days. If no longer needed, create a DB snapshot and delete the resource. | 
| Amazon WorkSpaces | User connection activity | Applies to Always On WorkSpaces only. Auto Stop and Standby WorkSpaces are excluded.<br />No one has connected to the WorkSpace over the 63-day lookback period. | Verify whether this WorkSpace is still needed by the assigned user. If temporarily not needed, consider switching to Auto Stop mode. If the user no longer requires access, consider deleting the resource. | 
| Amazon SageMaker endpoints | Invocations | The endpoint had zero invocations over the 14-day lookback period. | Verify whether this endpoint is still in use. If infrequently used, consider enabling scale-to-zero functionality for inference components if supported. If no longer required, consider deleting the resource. | 

## Estimated monthly savings
<a name="idle-savings-calculation"></a>

**Estimated monthly savings (after discounts)**

This column lists the approximate monthly cost savings that you experience by taking Compute Optimizer’s recommended action per idle resource under the supported pricing models. The supported pricing models depends on the specific AWS resource. For example, EC2 instances supports Savings Plans and Reserved Instances discounts but ECS services only supports the Savings Plans pricing model. To receive recommendations with supported pricing models, the savings estimation mode preference needs to be activated. For more information, see [ Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Note**  
If you don't activate the savings estimation mode preference, this column on both the Instance and Storage tabs display the default On-Demand pricing discount information.

**Estimated monthly savings (On-Demand)**

This column lists the approximate monthly cost savings that you experience by taking Compute Optimizer’s recommended action per idle resource under the On-Demand pricing model.

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts, to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.