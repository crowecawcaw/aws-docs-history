# Using managed scaling in Amazon EMR

###### Important

We strongly recommend that you use the latest Amazon EMR release (Amazon EMR
7.10.0) for managed scaling. In some early releases, you might
experience intermittent application failures or delays in scaling. Amazon EMR resolved
this issue with 5.x releases 5.30.2, 5.31.1, 5.32.1, 5.33.1 and higher, and with 6.x
releases 6.1.1, 6.2.1, 6.3.1 and higher. For more information Region and
release availability, see [Managed scaling
availability](#emr-managed-scaling-availability "#emr-managed-scaling-availability").

## Overview

With Amazon EMR versions 5.30.0 and higher (except for Amazon EMR 6.0.0), you can enable
Amazon EMR managed scaling. Managed scaling lets you automatically increase or decrease
the number of instances or units in your cluster based on workload. Amazon EMR
continuously evaluates cluster metrics to make scaling decisions that optimize your
clusters for cost and speed. Managed scaling is available for clusters composed of
either instance groups or instance fleets.

## Managed scaling

availability

- In the following AWS Regions, Amazon EMR managed scaling is available with Amazon EMR 6.14.0 and higher:
  - Europe (Spain) (eu-south-2)

- In the following AWS Regions, Amazon EMR managed scaling is available with
  Amazon EMR 5.30.0 and 6.1.0 and higher:
  - US East (N. Virginia) (us-east-1)
  - US East (Ohio) (us-east-2)
  - US West (Oregon) (us-west-2)
  - US West (N. California) (us-west-1)
  - Africa (Cape Town) (af-south-1)
  - Asia Pacific (Hong Kong) (ap-east-1)
  - Asia Pacific (Mumbai) (ap-south-1)
  - Asia Pacific (Hyderabad) (ap-south-2)
  - Asia Pacific (Seoul) (ap-northeast-2)
  - Asia Pacific (Singapore) (ap-southeast-1)
  - Asia Pacific (Sydney) (ap-southeast-2)
  - Asia Pacific (Jakarta) (ap-southeast-3)
  - Asia Pacific (Tokyo) (ap-northeast-1)
  - Asia Pacific (Osaka) (ap-northeast-3)
  - Canada (Central) (ca-central-1)
  - South America (São Paulo) (sa-east-1)
  - Europe (Frankfurt) (eu-central-1)
  - Europe (Zurich) (eu-central-2)
  - Europe (Ireland) (eu-west-1)
  - Europe (London) (eu-west-2)
  - Europe (Milan) (eu-south-1)
  - Europe (Paris) (eu-west-3)
  - Europe (Stockholm) (eu-north-1)
  - Israel (Tel Aviv) (il-central-1)
  - Middle East (UAE) (me-central-1)
  - China (Beijing) (cn-north-1)
  - China (Ningxia) (cn-northwest-1)
  - AWS GovCloud (US-East) (us-gov-east-1)
  - AWS GovCloud (US-West) (us-gov-west-1)

- Amazon EMR managed scaling only works with YARN applications, such as Spark,
  Hadoop, Hive, and Flink. It doesn't support applications that are not based
  on YARN, such as Presto and HBase.

## Managed scaling parameters

You must configure the following parameters for managed scaling. The limit only
applies to the core and task nodes. You cannot scale the primary node after
initial configuration.

- **Minimum** (`MinimumCapacityUnits`) –
  The lower boundary of allowed EC2 capacity in a cluster. It is measured
  through virtual central processing unit (vCPU) cores or instances for
  instance groups. It is measured through units for instance fleets.
- **Maximum** (`MaximumCapacityUnits`) –
  The upper boundary of allowed EC2 capacity in a cluster. It is measured
  through virtual central processing unit (vCPU) cores or instances for
  instance groups. It is measured through units for instance fleets.
- **On-Demand limit**
  (`MaximumOnDemandCapacityUnits`) (Optional) – The
  upper boundary of allowed EC2 capacity for On-Demand market type in a
  cluster. If this parameter is not specified, it defaults to the value of
  `MaximumCapacityUnits`.
  - This parameter is used to split capacity allocation between
    On-Demand and Spot Instances. For example, if you set the minimum
    parameter as 2 instances, the maximum parameter as 100 instances,
    the On-Demand limit as 10 instances, then Amazon EMR managed scaling
    scales up to 10 On-Demand Instances and allocates the remaining
    capacity to Spot Instances. For more information, see [Node allocation scenarios](managed-scaling-allocation-strategy.md#node-allocation-scenarios "managed-scaling-allocation-strategy.md#node-allocation-scenarios").

- **Maximum core nodes** (`MaximumCoreCapacityUnits`) (Optional) –
  The upper boundary of allowed EC2 capacity for core node type in a cluster.
  If this parameter is not specified, it defaults to the value of
  `MaximumCapacityUnits`.
  - This parameter is used to split capacity allocation between core
    and task nodes. For example, if you set the minimum parameter as 2
    instances, the maximum as 100 instances, the maximum core node as 17
    instances, then Amazon EMR managed scaling scales up to 17 core nodes and
    allocates the remaining 83 instances to task nodes. For more
    information, see [Node allocation scenarios](managed-scaling-allocation-strategy.md#node-allocation-scenarios "managed-scaling-allocation-strategy.md#node-allocation-scenarios").

For more information about managed scaling parameters, see [`ComputeLimits`](../APIReference/API_ComputeLimits.md "../APIReference/API_ComputeLimits.md").

## Considerations for Amazon EMR managed scaling

- Managed scaling is supported in limited AWS Regions and Amazon EMR releases.
  For more information, see [Managed scaling
  availability](#emr-managed-scaling-availability "#emr-managed-scaling-availability").
- You must configure the required parameters for Amazon EMR managed scaling. For
  more information, see [Managed scaling parameters](#emr-managed-scaling-parameters "#emr-managed-scaling-parameters").
- To use managed scaling, the metrics-collector process must be able to
  connect to the public API endpoint for managed scaling in API Gateway. If you use
  a private DNS name with Amazon Virtual Private Cloud, managed scaling won't function
  properly. To ensure that managed scaling works, we recommend that you take
  one of the following actions:
  - Remove the API Gateway interface VPC endpoint from your Amazon VPC.
  - Follow the instructions in [Why do I get an HTTP 403 Forbidden error when connecting to my
    API Gateway APIs from a VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-vpc-connections/ "https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-vpc-connections/") to disable the private DNS name
    setting.
  - Launch your cluster in a private subnet instead. For more
    information, see the topic on [Private subnets](emr-clusters-in-a-vpc.md#emr-vpc-private-subnet "emr-clusters-in-a-vpc.md#emr-vpc-private-subnet").

- If your YARN jobs are intermittently slow during scale down, and YARN
  Resource Manager logs show that most of your nodes were deny-listed during
  that time, you can adjust the decommissioning timeout threshold.

Reduce the `spark.blacklist.decommissioning.timeout` from one
hour to one minute to make the node available for other pending containers
to continue task processing.

You should also set
`YARN.resourcemanager.nodemanager-graceful-decommission-timeout-secs`
to a larger value to ensure Amazon EMR doesn’t force terminate the node while the
longest “Spark Task” is still running on the node. The current default is 60
minutes, which means YARN force-terminates the container after 60 minutes
once the node enters the decomissioning state.

The following example YARN Resource Manager Log line shows nodes added to
the decomissioning state:

```
2021-10-20 15:55:26,994 INFO org.apache.hadoop.YARN.server.resourcemanager.DefaultAMSProcessor (IPC Server handler 37 on default port 8030): blacklist are updated in Scheduler.blacklistAdditions: [ip-10-10-27-207.us-west-2.compute.internal, ip-10-10-29-216.us-west-2.compute.internal, ip-10-10-31-13.us-west-2.compute.internal, ... , ip-10-10-30-77.us-west-2.compute.internal], blacklistRemovals: []
```

See more [details on how Amazon EMR integrates with YARN deny listing during
decommissioning of nodes](https://aws.amazon.com/blogs/big-data/spark-enhancements-for-elasticity-and-resiliency-on-amazon-emr/ "https://aws.amazon.com/blogs/big-data/spark-enhancements-for-elasticity-and-resiliency-on-amazon-emr/"), [cases when nodes in Amazon EMR can be deny listed](emr-troubleshoot-error-resource-3.md "emr-troubleshoot-error-resource-3.md"), and [configuring Spark node-decommissioning behavior](../ReleaseGuide/emr-spark-configure.md#spark-decommissioning "../ReleaseGuide/emr-spark-configure.md#spark-decommissioning").

- For Spark workloads, disabling Spark Dynamic Resource Allocator (DRA) by changing the Spark property **spark.dynamicAllocation.enabled** to
  `FALSE` can cause Managed Scaling issues, where clusters can be scaled up more than required for your workloads (up to the maximum compute). When using Managed Scaling for these
  workloads, we recommend that you keep Spark DRA enabled, which is the default state of this property.
- Over-utilization of EBS volumes can cause Managed Scaling issues. We
  recommend that you maintain EBS volume below 90% utilization. For more
  information, see [Instance storage options and behavior in Amazon EMR](emr-plan-storage.md "emr-plan-storage.md").
- Amazon CloudWatch metrics are critical for Amazon EMR managed scaling to operate. We
  recommend that you closely monitor Amazon CloudWatch metrics to make sure data is not
  missing. For more information about how you can configure CloudWatch alarms to
  detect missing metrics, see [Using
  Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").
- Managed scaling operations on 5.30.0 and 5.30.1 clusters without Presto installed may cause application failures or cause a uniform instance group or instance fleet to stay in the `ARRESTED` state, particularly when a scale down operation is followed quickly by a scale up operation.

As a workaround, choose Presto as an application to install when you create a cluster with Amazon EMR releases 5.30.0 and 5.30.1, even if your job does not require Presto.

- When you set the maximum core node and the On-Demand limit for Amazon EMR
  managed scaling, consider the differences between instance groups and
  instance fleets. Each instance group consists of the same instance type and
  the same purchasing option for instances: On-Demand or Spot. For each
  instance fleet, you can specify up to five instance types, which can be
  provisioned as On-Demand and Spot Instances. For more information, see
  [Create
  a cluster with instance fleets or uniform instance groups](emr-instance-group-configuration.md "emr-instance-group-configuration.md"),
  [Instance fleet options](emr-instance-fleet.md#emr-instance-fleet-options "emr-instance-fleet.md#emr-instance-fleet-options"), and [Node allocation scenarios](managed-scaling-allocation-strategy.md#node-allocation-scenarios "managed-scaling-allocation-strategy.md#node-allocation-scenarios").
- With Amazon EMR 5.30.0 and higher, if you remove the default **Allow
  All** outbound rule to 0.0.0.0/ for the master security group,
  you must add a rule that allows outbound TCP connectivity to your security
  group for service access on port 9443. Your security group for service
  access must also allow inbound TCP traffic on port 9443 from the master
  security group. For more information about configuring security groups, see
  [Amazon EMR-managed security group for the primary instance (private
  subnets)](emr-man-sec-groups.md#emr-sg-elasticmapreduce-master-private "emr-man-sec-groups.md#emr-sg-elasticmapreduce-master-private").
- You can use AWS CloudFormation to configure Amazon EMR managed scaling. For more
  information, see [AWS::EMR::Cluster](../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.md") in the
  _AWS CloudFormation User Guide_.
- If you're using Spot nodes, consider using node labels to prevent Amazon EMR from removing application processes when Amazon EMR removes Spot nodes. For more information
  about node labels, see [Task nodes](emr-master-core-task-nodes.md#emr-plan-task "emr-master-core-task-nodes.md#emr-plan-task").
- Node labeling is not supported by default in Amazon EMR releases 6.15 or lower. For more information, see
  [Understand node types: primary, core, and task nodes.](emr-master-core-task-nodes.md "emr-master-core-task-nodes.md")
- If you're using Amazon EMR releases 6.15 or lower, you can only assign node labels by node type, such as core and task nodes. However, if you're using Amazon EMR release 7.0 or higher,
  you can configure node labels by node type and market type, such as On-Demand and Spot.
- If application process demand increases and executor demand decreases when you restricted the application process to core nodes, you can add
  back core nodes and remove task nodes in the same resize operation. For more information, see [Understanding node allocation strategy and scenarios](managed-scaling-allocation-strategy.md "managed-scaling-allocation-strategy.md").
- Amazon EMR doesn't label task nodes, so you can't set the YARN properties to restrict application processes only for task nodes. However, if you want to use
  market types as node labels, you can use the `ON_DEMAND` or `SPOT` labels for
  application process placement. We don't recommend using Spot nodes for application primary processes.
- When using node labels, the total running units in the cluster can temporarily exceed the max compute set in your managed scaling policy while Amazon EMR decommissions
  some of your instances. Total requested units will always stay at or below your policy’s max compute.
- Managed scaling only supports the node labels `ON_DEMAND` and `SPOT` or `CORE` and
  `TASK`. Custom node labels aren't supported.
- Amazon EMR creates node labels when creating the cluster and provisioning resources. Amazon EMR doesn't
  support adding node labels when you reconfigure the cluster. You also can't modify the node labels
  when configuring managed scaling after launching the cluster.
- Managed scaling scales core and task nodes independently based on application process and executor demand.
  To prevent HDFS data loss issues during core scale down, follow standard practice for core nodes. To
  learn more about best practices about core nodes and HDFS replication, see [Considerations and best practices](emr-plan-ha-considerations.md "emr-plan-ha-considerations.md").
- You can't place both the application process and executors
  on only the `core` or the `ON_DEMAND` node. If you want to add both the application
  process and executors on one of the nodes, don't use the `yarn.node-labels.am.default-node-label-expression`
  configuration.

For example, to place both the application process and executors in `ON_DEMAND` nodes,
set max compute to the same as the maximum in the `ON_DEMAND` node. Also remove the `yarn.node-labels.am.default-node-label-expression`
configuration.

To add both the application process and executors on `core` nodes, remove the `yarn.node-labels.am.default-node-label-expression`
configuration.

- When you use managed scaling with node labels, set the property `yarn.scheduler.capacity.maximum-am-resource-percent: 1`
  if you plan to run multiple applications in parallel. Doing so ensures that your application
  processes fully utilize the available `CORE` or `ON_DEMAND` nodes.
- If you use managed scaling with node labels, set the property `yarn.resourcemanager.decommissioning.timeout`
  to a value that's longer than the longest running application on your cluster. Doing so
  reduces the chance that Amazon EMR managed scalling needs to reschedule your applications
  to recommission `CORE` or `ON_DEMAND` nodes.
- To reduce the risk of application failures due to shuffle data loss, Amazon EMR collects metrics from the cluster to determine nodes that
  have existing transient shuffle data from the current and previous stage. In rare cases, metrics can continue to report stale data for
  applications that are already completed or terminated. This can impact timely scale down of instances in your cluster. For clusters that have large
  amount of shuffle data, consider using EMR versions 6.13 and later.

## Feature history

This table lists updates to the Amazon EMR managed scaling capability.

| Release date          | Capability                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Amazon EMR versions                 |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **November 20, 2024** | Managed scaling is available in the `il-central-1` Israel (Tel Aviv), `me-central-1` Middle East (UAE), and `ap-northeast-3` Asia Pacific (Osaka) regions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 5.30.0 and 6.1.0 and higher         |
| **November 15, 2024** | Managed scaling is available in the `eu-central-2` Europe (Zurich) Region.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 5.30.0 and 6.1.0 and higher         |
| **August 20, 2024**   | Node labels are now available in managed scaling, so you can label your instances based on market type or node type to improve automatic scaling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 7.2.0 and higher                    |
| **March 31, 2024**    | Managed scaling is available in the `ap-south-2` Asia Pacific (Hyderabad) Region.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 6.14.0 and higher                   |
| **February 13, 2024** | Managed scaling is available in the `eu-south-2` Europe (Spain) Region.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 6.14.0 and higher                   |
| **October 10, 2023**  | Managed scaling is available in the `ap-southeast-3` Asia Pacific (Jakarta) Region.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 6.14.0 and higher                   |
| **July 28, 2023**     | Enhanced managed scaling to switch to different task instance group on scale-up when Amazon EMR experiences a delay in scale-up with the current instance group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 5.34.0 and higher, 6.4.0 and higher |
| **June 16, 2023**     | Enhanced managed scaling to be aware of the nodes running application master so that those nodes are not scaled down. For more information, see [Understanding Amazon EMR node allocation strategy and scenarios](managed-scaling-allocation-strategy.md "managed-scaling-allocation-strategy.md").                                                                                                                                                                                                                                                                                                                                                                                                                  | 5.34.0 and higher, 6.4.0 and higher |
| **March 21, 2022**    | Added Spark shuffle data awareness used when scaling-down clusters. For Amazon EMR clusters with Apache Spark and the managed scaling feature enabled, Amazon EMR continuously monitors Spark executors and intermediate shuffle data locations. Using this information, Amazon EMR scales-down only under-utilized instances which don't contain actively used shuffle data. This prevents recomputation of lost shuffle data, helping to lower cost and improve job performance. For more information, see the [Spark Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations "https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations"). | 5.34.0 and higher, 6.4.0 and higher |
