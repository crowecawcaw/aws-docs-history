

# Monitoring Amazon EMR metrics with CloudWatch
<a name="UsingEMR_ViewingMetrics"></a>

Metrics are updated every five minutes and automatically collected and pushed to CloudWatch for every Amazon EMR cluster. This interval is not configurable. There is no charge for the Amazon EMR metrics reported in CloudWatch. These five minute datapoint metrics are archived for 63 days, after which the data is discarded. 

## How do I use Amazon EMR metrics?
<a name="UsingEMR_ViewingMetrics_HowDoI"></a>

The following table shows common uses for metrics reported by Amazon EMR. These are suggestions to get you started, not a comprehensive list. For a complete list of metrics reported by Amazon EMR, see [Metrics reported by Amazon EMR in CloudWatch](#UsingEMR_ViewingMetrics_MetricsReported). 



| How do I? | Relevant metrics | 
| --- | --- | 
| Track the progress of my cluster | Look at the RunningMapTasks, RemainingMapTasks, RunningReduceTasks, and RemainingReduceTasks metrics.  | 
| Detect clusters that are idle | The IsIdle metric tracks whether a cluster is live, but not currently running tasks. You can set an alarm to fire when the cluster has been idle for a given period of time, such as thirty minutes.  | 
| Detect when a node runs out of storage | The MRUnhealthyNodes metric tracks when one or more core or task nodes run out of local disk storage and transition to an UNHEALTHY YARN state. For example, core or task nodes are running low on disk space and will not be able to run tasks. | 
| Detect when a cluster runs out of storage | The HDFSUtilization metric monitors the cluster's combined HDFS capacity, and can require resizing the cluster to add more core nodes. For example, the HDFS utilization is high, which may affect jobs and cluster health.  | 
| Detect when a cluster is running at reduced capacity | The MRLostNodes metric tracks when one or more core or task nodes is unable to communicate with the master node. For example, the core or task node is unreachable by the master node. | 

For more information, see [Amazon EMR cluster terminates with NO\_SLAVE\_LEFT and core nodes FAILED\_BY\_MASTER](emr-cluster-NO_SLAVE_LEFT-FAILED_BY_MASTER.md) and [AWSSupport-AnalyzeEMRLogs](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-analyzeemrlogs.html). 

## Access CloudWatch metrics for Amazon EMR
<a name="UsingEMR_ViewingMetrics_Access"></a>

You can view the metrics that Amazon EMR reports to CloudWatch using the Amazon EMR console or the CloudWatch console. You can also retrieve metrics using the CloudWatch CLI command `[mon-get-stats](https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/cli-mon-get-stats.html)` or the CloudWatch `[GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html)` API. For more information about viewing or retrieving metrics for Amazon EMR using CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/).

------
#### [ Console ]

**To view metrics with the console**

1. Sign in to the AWS Management Console, and open the Amazon EMR console at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr).

1. Under **EMR on EC2** in the left navigation pane, choose **Clusters**, and then choose the cluster that you want to view metrics for. This opens the cluster details page.

1. Select the **Monitoring** tab on the cluster details page. Choose any one of the **Cluster status**, **Node status**, or **Inputs and outputs** options to load the reports about the progress and health of the cluster. 

1. After you choose a metric to view, you can enlarge each graph. To filter the time frame of your graph, select a prefilled option or choose **Custom**.

------

## Metrics reported by Amazon EMR in CloudWatch
<a name="UsingEMR_ViewingMetrics_MetricsReported"></a>

The following tables list the metrics that Amazon EMR reports in the console and pushes to CloudWatch.

### Amazon EMR metrics
<a name="emr-metrics-reported"></a>

Amazon EMR sends data for several metrics to CloudWatch. All Amazon EMR clusters automatically send metrics in five-minute intervals. Metrics are archived for two weeks; after that period, the data is discarded. 

The `AWS/ElasticMapReduce` namespace includes the following metrics.

**Note**  
Amazon EMR pulls metrics from a cluster. If a cluster becomes unreachable, no metrics are reported until the cluster becomes available again.

The following metrics are available for clusters running Hadoop 2.x versions.


<table>
<thead>
  <tr><th>Metric</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><i>Cluster Status</i></td></tr>
  <tr><td>IsIdle</td><td>Indicates that a cluster is no longer performing work, but is still alive and accruing charges. It is set to 1 if no tasks are running and no jobs are running, and set to 0 otherwise. This value is checked at five-minute intervals and a value of 1 indicates only that the cluster was idle when checked, not that it was idle for the entire five minutes. To avoid false positives, you should raise an alarm when this value has been 1 for more than one consecutive 5-minute check. For example, you might raise an alarm on this value if it has been 1 for thirty minutes or longer.<br />Use case: Monitor cluster performance<br />Units: <i>Boolean</i></td></tr>
  <tr><td>ContainerAllocated</td><td>The number of resource containers allocated by the ResourceManager.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>ContainerReserved</td><td>The number of containers reserved.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>ContainerPending</td><td>The number of containers in the queue that have not yet been allocated.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>ContainerPendingRatio</td><td>The ratio of pending containers to containers allocated (ContainerPendingRatio = ContainerPending / ContainerAllocated). If ContainerAllocated = 0, then ContainerPendingRatio = ContainerPending. The value of ContainerPendingRatio represents a number, not a percentage. This value is useful for scaling cluster resources based on container allocation behavior.<br />Units: <i>Count</i></td></tr>
  <tr><td>AppsCompleted</td><td>The number of applications submitted to YARN that have completed.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>AppsFailed</td><td>The number of applications submitted to YARN that have failed to complete.<br />Use case: Monitor cluster progress, Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>AppsKilled</td><td>The number of applications submitted to YARN that have been killed.<br />Use case: Monitor cluster progress, Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>AppsPending</td><td>The number of applications submitted to YARN that are in a pending state.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>AppsRunning</td><td>The number of applications submitted to YARN that are running.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>AppsSubmitted</td><td>The number of applications submitted to YARN.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td colspan="2"><i>Node Status</i></td></tr>
  <tr><td>CoreNodesRunning</td><td>The number of core nodes working. Data points for this metric are reported only when a corresponding instance group exists.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>CoreNodesPending</td><td>The number of core nodes waiting to be assigned. All of the core nodes requested may not be immediately available; this metric reports the pending requests. Data points for this metric are reported only when a corresponding instance group exists.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>LiveDataNodes</td><td>The percentage of data nodes that are receiving work from Hadoop.<br />Use case: Monitor cluster health<br />Units: <i>Percent</i></td></tr>
  <tr><td>MRTotalNodes</td><td>The number of nodes presently available to MapReduce jobs. Equivalent to YARN metric <code>mapred.resourcemanager.TotalNodes</code>.<br />Use ase: Monitor cluster progress<br />Units: <i>Count</i><br />Note: MRTotalNodes only counts currently active nodes in the system. YARN automatically removes terminated nodes from this count and stops tracking them, so they are not considered in the MRTotalNodes metric.</td></tr>
  <tr><td>MRActiveNodes</td><td>The number of nodes presently running MapReduce tasks or jobs. Equivalent to YARN metric <code>mapred.resourcemanager.NoOfActiveNodes</code>.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MRLostNodes</td><td>The number of nodes allocated to MapReduce that have been marked in a LOST state. Equivalent to YARN metric <code>mapred.resourcemanager.NoOfLostNodes</code>.<br />Use case: Monitor cluster health, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MRUnhealthyNodes</td><td>The number of nodes available to MapReduce jobs marked in an UNHEALTHY state. Equivalent to YARN metric <code>mapred.resourcemanager.NoOfUnhealthyNodes</code>.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MRDecommissionedNodes</td><td>The number of nodes allocated to MapReduce applications that have been marked in a DECOMMISSIONED state. Equivalent to YARN metric <code>mapred.resourcemanager.NoOfDecommissionedNodes</code>.<br />Use ase: Monitor cluster health, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MRRebootedNodes</td><td>The number of nodes available to MapReduce that have been rebooted and marked in a REBOOTED state. Equivalent to YARN metric <code>mapred.resourcemanager.NoOfRebootedNodes</code>.<br />Use case: Monitor cluster health, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MultiMasterInstanceGroupNodesRunning</td><td>The number of running master nodes.<br />Use case: Monitor master node failure and replacement<br />Units: <i>Count</i></td></tr>
  <tr><td>MultiMasterInstanceGroupNodesRunningPercentage</td><td>The percentage of master nodes that are running over the requested master node instance count. <br />Use case: Monitor master node failure and replacement<br />Units: <i>Percent</i></td></tr>
  <tr><td>MultiMasterInstanceGroupNodesRequested</td><td>The number of requested master nodes. <br />Use case: Monitor master node failure and replacement<br />Units: <i>Count</i></td></tr>
  <tr><td colspan="2"><i>IO</i></td></tr>
  <tr><td>S3BytesWritten</td><td>The number of bytes written to Amazon S3. This metric aggregates MapReduce jobs only, and does not apply for other workloads on Amazon EMR. <br />Use case: Analyze cluster performance, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>S3BytesRead</td><td>The number of bytes read from Amazon S3. This metric aggregates MapReduce jobs only, and does not apply for other workloads on Amazon EMR. <br />Use case: Analyze cluster performance, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>HDFSUtilization</td><td>The percentage of HDFS storage currently used.<br />Use case: Analyze cluster performance<br />Units: <i>Percent</i></td></tr>
  <tr><td>HDFSBytesRead</td><td>The number of bytes read from HDFS. This metric aggregates MapReduce jobs only, and does not apply for other workloads on Amazon EMR.<br />Use case: Analyze cluster performance, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>HDFSBytesWritten</td><td>The number of bytes written to HDFS. This metric aggregates MapReduce jobs only, and does not apply for other workloads on Amazon EMR.<br />Use case: Analyze cluster performance, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MissingBlocks</td><td>The number of blocks in which HDFS has no replicas. These might be corrupt blocks.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>CorruptBlocks</td><td>The number of blocks that HDFS reports as corrupted.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>TotalLoad</td><td>The total number of concurrent data transfers.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>MemoryTotalMB</td><td>The total amount of memory in the cluster.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MemoryReservedMB</td><td>The amount of memory reserved.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MemoryAvailableMB</td><td>The amount of memory available to be allocated.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>YARNMemoryAvailablePercentage</td><td>The percentage of remaining memory available to YARN (YARNMemoryAvailablePercentage = MemoryAvailableMB / MemoryTotalMB). This value is useful for scaling cluster resources based on YARN memory usage.<br />Units: <i>Percent</i></td></tr>
  <tr><td>MemoryAllocatedMB</td><td>The amount of memory allocated to the cluster.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>PendingDeletionBlocks</td><td>The number of blocks marked for deletion.<br />Use case: Monitor cluster progress, Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>UnderReplicatedBlocks</td><td>The number of blocks that need to be replicated one or more times.<br />Use case: Monitor cluster progress, Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>DfsPendingReplicationBlocks</td><td>The status of block replication: blocks being replicated, age of replication requests, and unsuccessful replication requests.<br />Use case: Monitor cluster progress, Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>CapacityRemainingGB</td><td>The amount of remaining HDFS disk capacity. <br />Use case: Monitor cluster progress, Monitor cluster health<br />Units: <i>Count</i></td></tr>
</tbody>
</table>


The following are Hadoop 1 metrics:


<table>
<thead>
  <tr><th>Metric</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><i>Cluster Status</i></td></tr>
  <tr><td>IsIdle</td><td>Indicates that a cluster is no longer performing work, but is still alive and accruing charges. It is set to 1 if no tasks are running and no jobs are running, and set to 0 otherwise. This value is checked at five-minute intervals and a value of 1 indicates only that the cluster was idle when checked, not that it was idle for the entire five minutes. To avoid false positives, you should raise an alarm when this value has been 1 for more than one consecutive 5-minute check. For example, you might raise an alarm on this value if it has been 1 for thirty minutes or longer.<br />Use case: Monitor cluster performance<br />Units: <i>Boolean</i></td></tr>
  <tr><td>JobsRunning</td><td>The number of jobs in the cluster that are currently running.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>JobsFailed</td><td>The number of jobs in the cluster that have failed.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td colspan="2"><i>Map/Reduce</i></td></tr>
  <tr><td>MapTasksRunning</td><td>The number of running map tasks for each job. If you have a scheduler installed and multiple jobs running, multiple graphs are generated.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MapTasksRemaining</td><td>The number of remaining map tasks for each job. If you have a scheduler installed and multiple jobs running, multiple graphs are generated. A remaining map task is one that is not in any of the following states: Running, Killed, or Completed.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MapSlotsOpen</td><td>The unused map task capacity. This is calculated as the maximum number of map tasks for a given cluster, less the total number of map tasks currently running in that cluster.<br />Use case: Analyze cluster performance<br />Units: <i>Count</i></td></tr>
  <tr><td>RemainingMapTasksPerSlot</td><td>The ratio of the total map tasks remaining to the total map slots available in the cluster.<br />Use case: Analyze cluster performance<br />Units: <i>Ratio</i></td></tr>
  <tr><td>ReduceTasksRunning</td><td>The number of running reduce tasks for each job. If you have a scheduler installed and multiple jobs running, multiple graphs are generated.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>ReduceTasksRemaining</td><td>The number of remaining reduce tasks for each job. If you have a scheduler installed and multiple jobs running, multiple graphs are generated.<br />Use case: Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>ReduceSlotsOpen</td><td>Unused reduce task capacity. This is calculated as the maximum reduce task capacity for a given cluster, less the number of reduce tasks currently running in that cluster.<br />Use case: Analyze cluster performance<br />Units: <i>Count</i></td></tr>
  <tr><td colspan="2"><i>Node Status</i></td></tr>
  <tr><td>CoreNodesRunning</td><td>The number of core nodes working. Data points for this metric are reported only when a corresponding instance group exists.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>CoreNodesPending</td><td>The number of core nodes waiting to be assigned. All of the core nodes requested may not be immediately available; this metric reports the pending requests. Data points for this metric are reported only when a corresponding instance group exists.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>LiveDataNodes</td><td>The percentage of data nodes that are receiving work from Hadoop.<br />Use case: Monitor cluster health<br />Units: <i>Percent</i></td></tr>
  <tr><td>TaskNodesRunning</td><td>The number of task nodes working. Data points for this metric are reported only when a corresponding instance group exists.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>TaskNodesPending</td><td>The number of task nodes waiting to be assigned. All of the task nodes requested may not be immediately available; this metric reports the pending requests. Data points for this metric are reported only when a corresponding instance group exists.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>LiveTaskTrackers</td><td>The percentage of task trackers that are functional.<br />Use case: Monitor cluster health<br />Units: <i>Percent</i></td></tr>
  <tr><td colspan="2"><i>IO</i></td></tr>
  <tr><td>S3BytesWritten</td><td>The number of bytes written to Amazon S3. This metric aggregates MapReduce jobs only, and does not apply for other workloads on Amazon EMR.<br />Use case: Analyze cluster performance, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>S3BytesRead</td><td>The number of bytes read from Amazon S3. This metric aggregates MapReduce jobs only, and does not apply for other workloads on Amazon EMR.<br />Use case: Analyze cluster performance, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>HDFSUtilization</td><td>The percentage of HDFS storage currently used.<br />Use case: Analyze cluster performance<br />Units: <i>Percent</i></td></tr>
  <tr><td>HDFSBytesRead</td><td>The number of bytes read from HDFS.<br />Use case: Analyze cluster performance, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>HDFSBytesWritten</td><td>The number of bytes written to HDFS.<br />Use case: Analyze cluster performance, Monitor cluster progress<br />Units: <i>Count</i></td></tr>
  <tr><td>MissingBlocks</td><td>The number of blocks in which HDFS has no replicas. These might be corrupt blocks.<br />Use case: Monitor cluster health<br />Units: <i>Count</i></td></tr>
  <tr><td>TotalLoad</td><td>The current, total number of readers and writers reported by all DataNodes in a cluster.<br />Use case: Diagnose the degree to which high I/O might be contributing to poor job execution performance. Worker nodes running the DataNode daemon must also perform map and reduce tasks. Persistently high TotalLoad values over time can indicate that high I/O might be a contributing factor to poor performance. Occasional spikes in this value are typical and do not usually indicate a problem.<br />Units: <i>Count</i></td></tr>
</tbody>
</table>


#### Cluster capacity metrics
<a name="emr-metrics-managed-scaling"></a>

The following metrics indicate the current or target capacities of a cluster. These metrics are only available when managed scaling or auto-termination is enabled. 

For clusters composed of instance fleets, the cluster capacity metrics are measured in `Units`. For clusters composed of instance groups, the cluster capacity metrics are measured in `Nodes` or `VCPU` based on the unit type used in the managed scaling policy. For more information, see [Using EMR-managed scaling](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-scaling.html) in the *Amazon EMR Management Guide*.


| Metric | Description | 
| --- | --- | 
| +  `TotalUnitsRequested` <br />+  `TotalNodesRequested` <br />+  `TotalVCPURequested`  | The target total number of units/nodes/vCPUs in a cluster as determined by managed scaling.<br />Units: *Count* | 
| +  `TotalUnitsRunning` <br />+  `TotalNodesRunning` <br />+  `TotalVCPURunning`   | The current total number of units/nodes/vCPUs available in a running cluster. When a cluster resize is requested, this metric will be updated after the new instances are added or removed from the cluster.<br />Units: *Count* | 
| +  `CoreUnitsRequested` <br />+  `CoreNodesRequested` <br />+  `CoreVCPURequested`   | The target number of CORE units/nodes/vCPUs in a cluster as determined by managed scaling.<br />Units: *Count* | 
| +  `CoreUnitsRunning` <br />+  `CoreNodesRunning` <br />+  `CoreVCPURunning`   | The current number of CORE units/nodes/vCPUs running in a cluster.<br />Units: *Count* | 
| +  `TaskUnitsRequested` <br />+  `TaskNodesRequested` <br />+  `TaskVCPURequested`   | The target number of TASK units/nodes/vCPUs in a cluster as determined by managed scaling.<br />Units: *Count* | 
| +  `TaskUnitsRunning` <br />+  `TaskNodesRunning` <br />+  `TaskVCPURunning`   | The current number of TASK units/nodes/vCPUs running in a cluster.<br />Units: *Count* | 

Amazon EMR emits the following metrics at a one-minute granularity when you enable auto-termination using an auto-termination policy. Some metrics are only available for Amazon EMR versions 6.4.0 and later. To learn more about auto-termination, see [Using an auto-termination policy for Amazon EMR cluster cleanup](emr-auto-termination-policy.md).



| Metric | Description | 
| --- | --- | 
| TotalNotebookKernels | The total number of running and idle notebook kernels on the cluster. This metric is only available for Amazon EMR versions 6.4.0 and later. | 
| AutoTerminationIsClusterIdle | Indicates whether the cluster is in use.A value of **0** indicates that the cluster is in active use by one of the following components:+  A YARN application <br />+  HDFS <br />+  A notebook <br />+  An on-cluster UI, such as the Spark History Server <br />A value of **1** indicates that the cluster is idle. Amazon EMR checks for continuous cluster idleness (`AutoTerminationIsClusterIdle` = 1). When a cluster's idle time equals the `IdleTimeout` value in your auto-termination policy, Amazon EMR terminates the cluster. | 

### Dimensions for Amazon EMR metrics
<a name="emr-metrics-dimensions"></a>

Amazon EMR data can be filtered using any of the dimensions in the following table. 


| Dimension  | Description  | 
| --- | --- | 
| JobFlowId | The same as cluster ID, which is the unique identifier of a cluster in the form j-XXXXXXXXXXXXX. Find this value by clicking on the cluster in the Amazon EMR console.  | 