# Understanding Amazon EMR node allocation

strategy and scenarios

This section gives an overview of node allocation strategy and common scaling
scenarios that you can use with Amazon EMR managed scaling.

## Node allocation strategy

Amazon EMR managed scaling allocates core and task nodes based on the following
scale-up and scale-down strategies:

**Scale-up strategy**

- For Amazon EMR releases 7.2 and higher, managed scaling first adds nodes based on node labels and the application process restriction YARN property.
- For Amazon EMR releases 7.2 and higher, if you enabled node labels and restricted application processes
  to `CORE` nodes, Amazon EMR managed scaling scales up core nodes and task nodes if application process demand increases
  and executor demand increases. Similarly, if you enabled node labels and restricted application processes
  to `ON_DEMAND` nodes, managed scaling scales up on-demand nodes if application process
  demand increases and scales up spot nodes if executor demand increases.
- If node labels aren't enabled, application process placement aren't restricted to any node or market type.
- By using node labels, managed scaling can scale up and scale down different instance groups and instance fleets
  in the same resize operation. For example, in a scenario in which `instance_group1`
  has `ON_DEMAND` node and `instance_group2` has a `SPOT` node, and node labels
  are enabled and application processes are restricted to nodes with the `ON_DEMAND` label.
  Managed scaling will scale down `instance_group1` and scale up `instance_group2` if application
  process demand decreases and executor demand increases.
- When Amazon EMR experiences a delay in scale-up with the current instance
  group, clusters that use managed scaling automatically switch to a
  different task instance group.
- If the `MaximumCoreCapacityUnits` parameter is set, then
  Amazon EMR scales core nodes until the core units reach the maximum allowed
  limit. All the remaining capacity is added to task nodes.
- If the `MaximumOnDemandCapacityUnits` parameter is set,
  then Amazon EMR scales the cluster by using the On-Demand Instances until the
  On-Demand units reach the maximum allowed limit. All the remaining
  capacity is added using Spot Instances.
- If both the `MaximumCoreCapacityUnits` and
  `MaximumOnDemandCapacityUnits` parameters are set, Amazon EMR
  considers both limits during scaling.

For example, if the `MaximumCoreCapacityUnits` is less than
`MaximumOnDemandCapacityUnits`, Amazon EMR first scales core
nodes until the core capacity limit is reached. For the remaining
capacity, Amazon EMR first uses On-Demand Instances to scale task nodes until
the On-Demand limit is reached, and then uses Spot Instances for task
nodes.

**Scale-down strategy**

- Similar to the scale-up strategy, Amazon EMR removes nodes based on node labels. For more information about
  node labels, see [Understand node types: primary, core, and task nodes](emr-master-core-task-nodes.md "emr-master-core-task-nodes.md").
- If you haven't enabled node labels, managed scaling removes task nodes and then removes
  core nodes until it achieves the desired scale-down target capacity. Managed scaling never scales down the cluster below
  the minimum constraints specified in the managed scaling policy.
- Amazon EMR versions 5.34.0 and higher, and Amazon EMR versions 6.4.0 and higher, support Spark shuffle data
  awareness, which prevents an instance from scaling down while Managed Scaling is aware of existing shuffle data.

For more information on shuffle operations, see the [Spark Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations "https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations"). Managed Scaling makes best effort to prevent scaling-down nodes with shuffle data from the current and previous stage of any active Spark
application, up to a maximum of 30 minutes. This helps minimize unintended shuffle data
loss, avoiding the need for job re-attempts and recomputation of
intermediate data. However, prevention of shuffle data loss is not guaranteed. For guaranteed protection, we recommend shuffle awareness on clusters with release
label 7.4 or higher. See below for how to set up guaranteed shuffle protection.

- Managed scaling first removes task nodes and then
  removes core nodes until it achieves the desired scale-down target capacity.
  The cluster never scales below the minimum constraints specified
  in the managed scaling policy.
- For clusters that are launched with Amazon EMR 5.x releases 5.34.0 and
  higher, and 6.x releases 6.4.0 and higher, Amazon EMR Managed Scaling doesn’t
  scale down nodes that have `ApplicationMaster` for Apache
  Spark, if there are active stages in the applications running on them. This minimizes job failures and retries, which
  helps to improve job performance and reduce costs. To confirm which
  nodes in your cluster are running `ApplicationMaster`, visit
  the Spark History Server and filter for the driver under the
  **Executors** tab of your Spark application
  ID.
- While the intelligent scaling with EMR Managed Scaling minimizes shuffle data loss for Spark, there can be instances when transient shuffle data might
  be not be protected during a scale-down. To provide enhanced resiliency of shuffle data during scale-down, we recommend
  enabling **Graceful Decommissioning for Shuffle Data** in YARN.
  When **Graceful Decommissioning for Shuffle Data** is enabled in YARN, nodes selected for scale-down that have shuffle data will
  enter the **Decommissioning** state and continue to serve shuffle files. The YARN ResourceManager waits until nodes report no shuffle files
  present before removing the nodes from the cluster.
  - Amazon EMR version 6.11.0 and higher support Yarn-based graceful decommissioning for **Hive** shuffle data for both the Tez
    and MapReduce Shuffle Handlers.
    - Enable Graceful Decommissioning for Shuffle Data by setting `yarn.resourcemanager.decommissioning-nodes-watcher.wait-for-shuffle-data`
      to `true`.

  - Amazon EMR version 7.4.0 and higher support Yarn-based graceful decommissioning for Spark shuffle data when the external shuffle service is
    enabled (enabled by default in EMR on EC2).
    - The default behavior of the Spark external shuffle service, when running Spark on Yarn, is for the Yarn NodeManager to remove application
      shuffle files at time of application termination. This may have an impact on the speed of node decommissioning and compute utilization. For long running
      applications, consider setting `spark.shuffle.service.removeShuffle` to `true` to remove shuffle files no longer in use to enable faster
      decommissioning of nodes with no active shuffle data.
    - If either the `yarn.nodemanager.shuffledata-monitor.interval-ms` flag or the `spark.dynamicAllocation.executorIdleTimeout` has been
      changed from the default values, ensure that the condition `spark.dynamicAllocation.executorIdleTimeout > yarn.nodemanager.shuffledata-monitor.interval-ms` remains `true` by
      updating the necessary flag.

If the cluster does not have any load, then Amazon EMR cancels the addition of new
instances from a previous evaluation and performs scale-down operations. If the
cluster has a heavy load, Amazon EMR cancels the removal of instances and performs
scale-up operations.

## Node allocation considerations

We recommend that you use the On-Demand purchasing option for core nodes to
avoid HDFS data loss in case of Spot reclamation. You can use the Spot
purchasing option for task nodes to reduce costs and get faster job execution
when more Spot Instances are added to task nodes.

## Node allocation scenarios

You can create various scaling scenarios based on your needs by setting up the
Maximum, Minimum, On-Demand limit, and Maximum core node parameters in different
combinations.

**Scenario 1: Scale Core Nodes Only**

To scale core nodes only, the managed scaling parameters must meet the
following requirements:

- The On-Demand limit is equal to the maximum boundary.
- The maximum core node is equal to the maximum boundary.

When the On-Demand limit and the maximum core node parameters are not
specified, both parameters default to the maximum boundary.

This scenario isn't applicable if you use managed scaling with node labels
and restrict your application processes to only run on `CORE` nodes,
because managed scaling scales task nodes to accommodate executor demand.

The following examples demonstrate the scenario of scaling cores nodes
only.

| Cluster initial state                                                    | Scaling parameters                                                                                                                                              | Scaling behavior                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance groups**<br>Core: 1 On-Demand<br>Task: 1 On-Demand and 1 Spot | `UnitType`: Instances<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 20<br>`MaximumCoreCapacityUnits`: 20        | Scale between 1 to 20 Instances or instance fleet units on<br>core nodes using On-Demand type. No scaling on task<br>nodes.<br>When you use managed scaling<br>with node labels and restrict your application proccesses to<br>`ON_DEMAND` nodes, the cluster will scale<br>1 to 20 instances or instance fleet units on `CORE` nodes using<br>the `On-Demand` or `Spot` type, depending on the type of demand. |
| **Instance fleets**<br>Core: 1 On-Demand<br>Task: 1 On-Demand and 1 Spot | UnitType: InstanceFleetUnits<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 20<br>`MaximumCoreCapacityUnits`: 20 |

**Scenario 2: Scale task nodes only**

To scale task nodes only, the managed scaling parameters must meet the
following requirement:

- The maximum core node must be equal to the minimum boundary.

The following examples demonstrate the scenario of scaling task nodes
only.

| Cluster initial state                                    | Scaling parameters                                                                                                         | Scaling behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance groups**<br>Core: 2 On-Demand<br>Task: 1 Spot | `UnitType`: Instances<br>`MinimumCapacityUnits`: 2<br>`MaximumCapacityUnits`: 20<br>`MaximumCoreCapacityUnits`: 2          | Keep core nodes steady at 2 and only scale task nodes<br>between 0 to 18 instances or instance fleet units. The<br>capacity between minimum and maximum boundaries is added to<br>the task nodes only.<br>When you use managed scaling with node labels and restrict your<br>application proccesses to ON_DEMAND nodes, the cluster will<br>keep core nodes steady at 2 and only scale task nodes between 0 to 18<br>instances or instance fleet units that use the `On-demand` or `Spot`<br>type, depending on the type of demand. |
| **Instance fleets**<br>Core: 2 On-Demand<br>Task: 1 Spot | `UnitType`: InstanceFleetUnits<br>`MinimumCapacityUnits`: 2<br>`MaximumCapacityUnits`: 20<br>`MaximumCoreCapacityUnits`: 2 |

**Scenario 3: Only On-Demand Instances in the cluster**

To have On-Demand Instances only, your cluster and the managed scaling
parameters must meet the following requirement:

- The On-Demand limit is equal to the maximum boundary.

When the On-Demand limit is not specified, the parameter value
defaults to the maximum boundary. The default value indicates that Amazon EMR
scales On-Demand Instances only.

If the maximum core node is less than the maximum boundary, the maximum core
node parameter can be used to split capacity allocation between core and task
nodes.

To enable this scenario in a cluster composed of instance groups, all node
groups in the cluster must use the On-Demand market type during initial
configuration.

This scenario is not applicable if you use managed scaling with
node labels and restrict your application processes to only run on `ON_DEMAND` nodes,
because managed scaling scales `Spot` nodes to accommodate executor demand.

The following examples demonstrate the scenario of having On-Demand Instances
in the entire cluster.

| Cluster initial state                                         | Scaling parameters                                                                                                                                                | Scaling behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance groups**<br>Core: 1 On-Demand<br>Task: 1 On-Demand | `UnitType`: Instances<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 20<br>`MaximumCoreCapacityUnits`: 12          | Scale between 1 to 12 instances or instance fleet units on<br>core nodes using On-Demand type. Scale the remaining<br>capacity using On-Demand on task nodes. No scaling using<br>Spot Instances.<br>When you use managed scaling with node labels and restrict your application<br>proccesses to `CORE` nodes, the cluster scales between 1<br>to 20 instances or instance fleet units on `CORE` nodes or<br>`task` nodes using the `ON_DEMAND`type,<br>depending on the type of demand. Scaling on core nodes will not exceed 12 instances or instance fleet units. |
| **Instance fleets**<br>Core: 1 On-Demand<br>Task: 1 On-Demand | `UnitType`: InstanceFleetUnits<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 20<br>`MaximumCoreCapacityUnits`: 12 |

**Scenario 4: Only Spot Instances in the
cluster**

To have Spot Instances only, the managed scaling parameters must meet the
following requirement:

- On-Demand limit is set to 0.

If the maximum core node is less than the maximum boundary, the maximum core
node parameter can be used to split capacity allocation between core and task
nodes.

To enable this scenario in a cluster composed of instance groups, the core
instance group must use the Spot purchasing option during initial configuration.
If there is no Spot Instance in the task instance group, Amazon EMR managed scaling
creates a task group using Spot Instances when needed.

This scenario isn't applicable if you use managed scaling
with node labels and restrict your application processes to
only run on `ON_DEMAND` nodes, because managed scaling scales `ON_DEMAND`
nodes to accommodate application process demand.

The following examples demonstrate the scenario of having Spot Instances in
the entire cluster.

| Cluster initial state                               | Scaling parameters                                                                                                             | Scaling behavior                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Instance groups**<br>Core: 1 Spot<br>Task: 1 Spot | `UnitType`: Instances<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 0          | Scale between 1 to 20 instances or instance<br>fleet units on core nodes using Spot. No scaling using On-Demand<br>type.<br>When you use managed scaling with node labels and restrict<br>your application proccesses to `CORE` nodes, the<br>cluster scales between 1 to 20 instances or instance fleet units on `CORE`<br>or `TASK` nodes using Spot, depending on the type of demand.<br>Amazon EMR doesn't scale using the `ON_DEMAND` type. |
| **Instance fleets**<br>Core: 1 Spot<br>Task: 1 Spot | `UnitType`: InstanceFleetUnits<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 0 |

**Scenario 5: Scale On-Demand Instances on core nodes and
Spot Instances on task nodes**

To scale On-Demand Instances on core nodes and Spot Instances on task nodes,
the managed scaling parameters must meet the following requirements:

- The On-Demand limit must be equal to the maximum core node.
- Both the On-Demand limit and the maximum core node must be less than
  the maximum boundary.

To enable this scenario in a cluster composed of instance groups, the core
node group must use the On-Demand purchasing option.

This scenario isn't applicable if you use managed scaling with node labels and restrict
your application processes to only run on `ON_DEMAND` nodes or `CORE` nodes.

The following examples demonstrate the scenario of scaling On-Demand Instances
on core nodes and Spot Instances on task nodes.

| Cluster initial state                                                    | Scaling parameters                                                                                                                                              | Scaling behavior                                                                                                                                                                                         |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance groups**<br>Core: 1 On-Demand<br>Task: 1 On-Demand and 1 Spot | `UnitType`: Instances<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 7<br>`MaximumCoreCapacityUnits`: 7          | Scale up to 6 On-Demand units on the core node since there<br>is already 1 On-Demand unit on the task node and the maximum<br>limit for On-Demand is 7. Then scale up to 13 Spot units on<br>task nodes. |
| **Instance fleets**<br>Core: 1 On-Demand<br>Task: 1 On-Demand and 1 Spot | `UnitType`: InstanceFleetUnits<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 7<br>`MaximumCoreCapacityUnits`: 7 |

**Scenario 6: Scale `CORE` instances for application process demand and `TASK` instances for executor demand.**

This scenario is only applicable if you use managed scaling with node labels and restrict application processes to only run on
`CORE` nodes.

To scale `CORE` nodes based on application process demand and `TASK` nodes based on executor demand, you must set the following configurations at
cluster launch:

- `yarn.node-labels.enabled:true`
- `yarn.node-labels.am.default-node-label-expression: 'CORE'`

If you don't specify the `ON_DEMAND` limit and the maximum `CORE` node parameters, both parameters default to the maximum boundary.

If the maximum `ON_DEMAND` node is less than the maximum boundary, managed scaling uses the maximum `ON_DEMAND` node parameter
to split capacity allocation between `ON_DEMAND` and `SPOT` nodes. If you set the the maximum `CORE` node parameter
to less than or equal to the minimum capacity parameter, `CORE` nodes remain static at the maximum core capacity.

The following examples demonstrate the scenario of scaling CORE instances
based on application process demand and TASK instances based on executor demand.

| Cluster initial state                                         | Scaling parameters                                                                                                                                                | Scaling behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance groups**<br>Core: 1 On-Demand<br>Task: 1 On-Demand | `UnitType`: Instances<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 10<br>`MaximumCoreCapacityUnits`: 20          | Scales `CORE` nodes between 1 and 20 nodes based on the cluster's<br>application process demand using the On-Demand or Spot market type. Scales `TASK` nodes based on executor demand<br>and remaining available capacity after Amazon EMR allocates `CORE` nodes.<br>The sum of requested `CORE` and `TASK` nodes won't exceed the `maximumCapacity` of 20. The sum of requested<br>on-demand core nodes and on-demand task nodes won't exceed the `maximumOnDemandCapacity` of 10. Additional core or task nodes<br>use the Spot market type. |
| **Instance fleets**<br>Core: 1 On-Demand<br>Task: 1 On-Demand | `UnitType`: InstanceFleetUnits<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 10<br>`MaximumCoreCapacityUnits`: 20 |

**Scenario 7: Scale `ON_DEMAND` instances for application
process demand and `SPOT` instances for executor demand.**

This scenario is only applicable if you use managed scaling with node labels and restrict application processes to only run on
`ON_DEMAND` nodes.

To scale `ON_DEMAND` nodes based on application process demand and `SPOT` nodes based on executor demand, you must set the following configurations at
cluster launch:

- `yarn.node-labels.enabled:true`
- `yarn.node-labels.am.default-node-label-expression: 'ON_DEMAND'`

If you don't specify the `ON_DEMAND` limit and the maximum `CORE` node parameters, both parameters default to the maximum boundary.

If the maximum `CORE` node is less than the maximum boundary, managed scaling uses the maximum `CORE` node parameter
to split capacity allocation between `CORE` and `TASK` nodes. If you set the the maximum `CORE` node parameter
to less than or equal to the minimum capacity parameter, `CORE` nodes remain static at the maximum core capacity.

The following examples demonstrate the scenario of scaling On-Demand Instances
based on application process demand and Spot instances based on executor demand.

| Cluster initial state                                         | Scaling parameters                                                                                                                                                | Scaling behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Instance groups**<br>Core: 1 On-Demand<br>Task: 1 On-Demand | `UnitType`: Instances<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 20<br>`MaximumCoreCapacityUnits`: 10          | Scales `ON_DEMAND` nodes between 1 and 20 nodes based on the cluster's<br>application process demand using the `CORE` or `TASK` node type. Scales `SPOT` nodes based on executor demand<br>and remaining available capacity after Amazon EMR allocates `ON_DEMAND` nodes.<br>The sum of requested `ON_DEMAND` and `SPOT` nodes won't exceed the `maximumCapacity` of 20. The sum of requested<br>on-demand core nodes and spot core nodes won't exceed the `maximumCoreCapacity` of 10. Additional on-demand or spot nodes<br>use the `TASK` node type. |
| **Instance fleets**<br>Core: 1 On-Demand<br>Task: 1 On-Demand | `UnitType`: InstanceFleetUnits<br>`MinimumCapacityUnits`: 1<br>`MaximumCapacityUnits`: 20<br>`MaximumOnDemandCapacityUnits`: 20<br>`MaximumCoreCapacityUnits`: 10 |
