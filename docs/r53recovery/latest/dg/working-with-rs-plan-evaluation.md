

# Plan evaluation for Region switch plans
<a name="working-with-rs-plan-evaluation"></a>

When you create a multi-Region recovery plan, you need confidence that the plan will execute successfully, without errors, when you need it most. With Region switch plan evaluation, you can continuously validate your plan's configuration and permissions, and identify issues before they block a recovery.

## How can you use plan evaluation
<a name="working-with-rs-plan-evaluation-how"></a>

Plan evaluation runs check the resource configurations and IAM permissions in your plan, and surface execution-blocking warnings that you can proactively resolve. You don't need to configure or opt in to plan evaluation. With every Region switch plan, you get plan evaluation automatically. Region switch automatically evaluates your plan multiple times per hour. If any checks fail, Region switch returns warning messages that you can view in the AWS Management Console. You can also receive validation warnings through Amazon EventBridge or by using the [GetPlanEvaluationStatus](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html) API.

## What is evaluated by execution block
<a name="working-with-rs-plan-evaluation-checks"></a>

Region switch performs specific checks for each execution block type in your plan. The following table lists the checks performed for each execution block.


**Plan evaluation checks by execution block**  


- **[Amazon EC2 Auto Scaling group execution block](ec2-auto-scaling-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that Auto Scaling groups exist and are accessible to Region switch via the plan's configured execution role or cross-account role.
  - **Check category:** Capacity / **Description:** Checks that the maximum capacity of the target Region's Auto Scaling group is sufficient to scale up to the source Region's capacity.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Auto Scaling operations.

- **[Amazon EKS resource scaling execution block](eks-resource-scaling-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the Amazon EKS cluster exists and the Kubernetes resource is present in the cluster.
  - **Check category:** Kubernetes permissions / **Description:** Checks that the IAM role is mapped to the AmazonARCRegionSwitchScalingPolicy EKS Access Entry so Region switch can act on the Kubernetes resources. The EKS Access Entry policy is not mandatory as long as the required EKS permissions are supplied through k8 User Groups.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon EKS operations.

- **[Amazon ECS service scaling execution block](ecs-service-scaling-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the Amazon ECS cluster and service exist and are correctly associated.
  - **Check category:** Capacity / **Description:** Checks that the maximum autoscaling capacity of the target Amazon ECS service is sufficient to handle the required traffic load during failover.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon ECS operations.

- **[ARC routing control execution block](arc-routing-controls-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the routing control exists and the role is authorized to access the control panel.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for routing control operations.

- **[Amazon Aurora Global Database execution block](aurora-global-database-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the global cluster exists, DB clusters are members of the global cluster, DB clusters are in an available state, and DB instances exist in both clusters.
  - **Check category:** Engine compatibility / **Description:** Checks that the engine version supports switchover and that clusters have compatible versions across Regions.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Aurora failover and switchover.

- **[Aurora Provisioned Scaling execution block](aurora-provisioned-scaling-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that instance and cluster ARNs are well-formed, instances exist, instances belong to the expected cluster, and clusters are members of the specified global cluster.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Aurora provisioned scaling.

- **[Aurora Serverless Scaling execution block](aurora-serverless-scaling-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that Aurora Serverless clusters are present in the expected Regions and contain Serverless v2 instances.
  - **Check category:** Capacity / **Description:** Checks that the scaling target for the target Region's cluster is within the 256 ACU limit.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Aurora Serverless scaling.

- **[Amazon DocumentDB Global Cluster execution block](documentdb-global-cluster-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the global cluster exists, clusters are members of the global cluster, clusters are in an available state, and instances exist in both clusters.
  - **Check category:** Engine compatibility / **Description:** Checks that cluster engine versions are compatible and the global cluster has the expected engine type.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon DocumentDB failover and switchover.

- **[Amazon Neptune Global Cluster execution block](neptune-global-database-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the global cluster exists, DB clusters are members of the global cluster, DB clusters exist in both Regions, and DB clusters are in an available state.
  - **Check category:** Engine compatibility / **Description:** Checks that engine versions are consistent across regional clusters and meet the minimum required version for failover/switchover.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon Neptune failover and switchover.

- **[Amazon RDS Promote Read Replica execution block](rds-promote-read-replica-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that DB instances exist, instances in non-primary Regions are read replicas, and the source instance is correctly configured for replication.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Amazon RDS read replica promotion.

- **[Amazon RDS Create Cross-Region Replica execution block](rds-create-cross-region-replica-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that DB instances exist and backup is enabled on the source instance.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for creating Amazon RDS read replicas.

- **[Amazon RDS Switchover Read Replica execution block](rds-switchover-read-replica-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the standby instance is in mounted or open read-only state, is actively replicating, and has automatic backups enabled.
  - **Check category:** Engine compatibility / **Description:** Checks that the engine version supports switchover (Oracle 19c or higher) and that both instances have the same engine version.
  - **Check category:** Configuration / **Description:** Checks that no pending maintenance actions block switchover and that the option group is exclusive to the replication configuration.

- **[Manual approval execution block](manual-approval-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the manual approval IAM role ARN is well-formed and the role exists.
  - **Check category:** Configuration / **Description:** Checks that the manual approval role is in the same account that owns the plan.
  - **Check category:** IAM permissions / **Description:** Checks that the approver role has the arc-region-switch:ApprovePlanExecutionStep permission.

- **[Custom action Lambda execution block](custom-action-lambda-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the Lambda function exists and is in an Active state.
  - **Check category:** Configuration / **Description:** Checks that the Lambda function concurrency is greater than 0, that a dry-run invocation succeeds, and that durable Lambda functions have an execution timeout of 15 minutes or less.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for Lambda execution.

- **[Lambda event source mapping execution block](lambda-event-source-mapping-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the Lambda event source mapping exists and the associated Lambda function exists and is in an Active state.
  - **Check category:** Configuration / **Description:** Checks that the Lambda function for the Lambda event source mapping has reserved concurrency greater than 0.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role has the required policies for managing event source mappings.

- **[Amazon Route 53 health check execution block](route53-health-check-block.md)**
  - **Check category:** Resource accessibility / **Description:** Checks that the hosted zone exists and record sets can be mapped to the configured Regions.
  - **Check category:** Configuration / **Description:** Checks that the Region switch-allocated health check is associated with the correct record set.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's IAM role is authorized to access the hosted zone.



## Plan-level evaluation checks
<a name="working-with-rs-plan-evaluation-plan-level"></a>

In addition to execution block checks, Region switch evaluates plan-level configurations including triggers, report generation, and application health alarms.


**Plan-level evaluation checks**  


- **Triggers**
  - **Check category:** Resource accessibility / **Description:** Checks that the CloudWatch alarm configured for the trigger exists and is accessible with the configured role.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's execution role has the arc-region-switch:StartPlanExecution permission required for automated trigger-based execution.

- **Report generation**
  - **Check category:** IAM permissions / **Description:** Checks that the plan's execution role has the s3:PutObject permission required to write reports to the configured Amazon S3 bucket.
  - **Check category:** Role assumption / **Description:** Checks that the plan's execution role can be assumed for report generation validation.

- **Application health alarms**
  - **Check category:** Resource accessibility / **Description:** Checks that the CloudWatch alarm exists and is accessible with the configured role.
  - **Check category:** IAM permissions / **Description:** Checks that the plan's role has cloudwatch:DescribeAlarms and cloudwatch:DescribeAlarmHistory permissions required to validate alarm state.
  - **Check category:** Cross-account configuration / **Description:** Checks that the external ID is provided and valid when a cross-account role is specified for the alarm.

