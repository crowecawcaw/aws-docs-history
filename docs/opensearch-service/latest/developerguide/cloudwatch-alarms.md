

# Recommended CloudWatch alarms for Amazon OpenSearch Service
<a name="cloudwatch-alarms"></a>

CloudWatch alarms perform an action when a CloudWatch metric exceeds a specified value for some amount of time. For example, you might want AWS to email you if your cluster health status is `red` for longer than one minute. This section includes some recommended alarms for Amazon OpenSearch Service and how to respond to them.

You can automatically deploy these alarms using CloudFormation. For a sample stack, see the related [GitHub repository](https://github.com/aws-samples/sample-opensearch-on-aws/tree/main/operations/cloudwatch-alarms).

**Note**  
If you deploy the CloudFormation stack, the `KMSKeyError` and `KMSKeyInaccessible` alarms will exists in an `Insufficient Data` state because these metrics only appear if a domain encounters a problem with its encryption key.

For more information about configuring alarms, see [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.


<table>
<thead>
  <tr><th>Alarm</th><th>Issue</th></tr>
</thead>
<tbody>
  <tr><td><code>ClusterStatus.red</code> maximum is &gt;= 1 for 1 minute, 1 consecutive time</td><td>At least one primary shard and its replicas are not allocated to a node. See <a href="handling-errors.md#handling-errors-red-cluster-status">Red cluster status</a>.</td></tr>
  <tr><td><code>ClusterStatus.yellow</code> maximum is &gt;= 1 for 1 minute, 5 consecutive times</td><td>At least one replica shard is not allocated to a node. See <a href="handling-errors.md#handling-errors-yellow-cluster-status">Yellow cluster status</a>.</td></tr>
  <tr><td><code>FreeStorageSpace</code> minimum is &lt;= 20480 for 1 minute, 1 consecutive time</td><td>A node in your cluster is down to 20 GiB of free storage space. See <a href="handling-errors.md#handling-errors-watermark">Lack of available storage space</a>. This value is in MiB, so rather than 20480, we recommend setting it to 25% of the storage space for each node.</td></tr>
  <tr><td><code>ClusterIndexWritesBlocked</code> is &gt;= 1 for 5 minutes, 1 consecutive time</td><td>Your cluster is blocking write requests. See <a href="handling-errors.md#troubleshooting-cluster-block">ClusterBlockException</a>.</td></tr>
  <tr><td><code>Nodes</code> minimum is &lt; <i>x</i> for 1 day, 1 consecutive time</td><td><i>x</i> is the number of nodes in your cluster. This alarm indicates that at least one node in your cluster has been unreachable at some point within one day. See <a href="handling-errors.md#handling-errors-failed-cluster-nodes">Failed cluster nodes</a>.</td></tr>
  <tr><td><code>AutomatedSnapshotFailure</code> maximum is &gt;= 1 for 1 minute, 1 consecutive time</td><td>An automated snapshot failed. This failure is often the result of a red cluster health status. See <a href="handling-errors.md#handling-errors-red-cluster-status">Red cluster status</a>.For a summary of all automated snapshots and some information about failures, try one of the following requests:<pre>GET {{domain_endpoint}}/_snapshot/cs-automated/_all<br />GET {{domain_endpoint}}/_snapshot/cs-automated-enc/_all</pre></td></tr>
  <tr><td><code>CPUUtilization</code> or <code>WarmCPUUtilization</code> maximum is &gt;= 80% for 15 minutes, 3 consecutive times</td><td>100% CPU utilization might occur sometimes, but <i>sustained</i> high usage is problematic. Consider using larger instance types or adding instances.</td></tr>
  <tr><td><code>JVMMemoryPressure</code> maximum is &gt;= 95% for 1 minute, 3 consecutive times</td><td rowspan="2">The cluster could encounter out of memory errors if usage increases. Consider scaling vertically. OpenSearch Service uses half of an instance's RAM for the Java heap, up to a heap size of 32 GiB. You can scale instances vertically up to 64 GiB of RAM, at which point you can scale horizontally by adding instances.</td></tr>
  <tr><td><code>OldGenJVMMemoryPressure</code> maximum is &gt;= 80% for 1 minute, 3 consecutive times</td></tr>
  <tr><td><code>MasterCPUUtilization</code> maximum is &gt;= 50% for 15 minutes, 3 consecutive times</td><td rowspan="3">Consider using larger instance types for your <a href="managedomains-dedicatedmasternodes.md">dedicated master nodes</a>. Because of their role in cluster stability and <a href="managedomains-configuration-changes.md">blue/green deployments</a>, dedicated master nodes should have lower CPU usage than data nodes.</td></tr>
  <tr><td><code>MasterJVMMemoryPressure</code> maximum is &gt;= 95% for 1 minute, 3 consecutive times</td></tr>
  <tr><td><code>MasterOldGenJVMMemoryPressure</code> maximum is &gt;= 80% for 1 minute, 3 consecutive times</td></tr>
  <tr><td><code>KMSKeyError</code> is &gt;= 1 for 1 minute, 1 consecutive time</td><td>The AWS KMS encryption key that is used to encrypt data at rest in your domain is disabled. Re-enable it to restore normal operations. For more information, see <a href="encryption-at-rest.md">Encryption of data at rest for Amazon OpenSearch Service</a>.</td></tr>
  <tr><td><code>KMSKeyInaccessible</code> is &gt;= 1 for 1 minute, 1 consecutive time</td><td>The AWS KMS encryption key that is used to encrypt data at rest in your domain has been deleted or has revoked its grants to OpenSearch Service. You can't recover domains that are in this state. However, if you have a manual snapshot, you can use it to migrate to a new domain. To learn more, see <a href="encryption-at-rest.md">Encryption of data at rest for Amazon OpenSearch Service</a>.</td></tr>
  <tr><td><code>shards.active</code> is &gt;= (25 × JVM heap size in GiB × number of data nodes) for 1 minute, 1 consecutive time</td><td>The total number of active primary and replica shards exceeds the recommended limit of 25 shards per GiB of Java heap memory per node. For example, a 3-node cluster with 32 GiB heap per node should have no more than 2,400 shards (25 × 32 × 3). You might be rotating your indexes too frequently. Consider using ISM to remove indexes once they reach a specific age.</td></tr>
  <tr><td><code>5xx</code> alarms &gt;= 10% of <code>OpenSearchRequests</code></td><td>One or more data nodes might be overloaded, or requests are failing to complete within the idle timeout period. Consider switching to larger instance types or adding more nodes to the cluster. Confirm that you're following <a href="sizing-domains.md">best practices</a> for shard and cluster architecture.</td></tr>
  <tr><td><code>MasterReachableFromNode</code> maximum is &lt; 1 for 5 minutes, 1 consecutive time</td><td>This alarm indicates that the master node stopped or is unreachable. These failures are usually the result of a network connectivity issue or an AWS dependency problem. </td></tr>
  <tr><td><code>ThreadpoolWriteQueue</code> average is &gt;= 100 for 1 minute, 1 consecutive time</td><td>The cluster is experiencing high indexing concurrency. Review and control indexing requests, or increase cluster resources.</td></tr>
  <tr><td><code>ThreadpoolSearchQueue</code> average is &gt;= 500 for 1 minute, 1 consecutive time</td><td rowspan="2">The cluster is experiencing high search concurrency. Consider scaling your cluster. You can also increase the search queue size, but increasing it excessively can cause out of memory errors. </td></tr>
  <tr><td> <code>ThreadpoolSearchQueue</code> maximum is &gt;= 5000 for 1 minute, 1 consecutive time </td></tr>
  <tr><td>Increase in <code>ThreadpoolSearchRejected</code> SUM is &gt;=1{ math expression DIFF ( )} for 1 minute, 1 consecutive time</td><td rowspan="2">These alarms notify you of domain issues that might impact performance and stability.</td></tr>
  <tr><td>Increase in <code>ThreadpoolWriteRejected</code> SUM is &gt;=1{ math expression DIFF ( )} for 1 minute, 1 consecutive time </td></tr>
</tbody>
</table>


**Note**  
If you just want to *view* metrics, see [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](managedomains-cloudwatchmetrics.md).

## Other alarms you might consider
<a name="cw-alarms-additional"></a>

Consider configuring the following alarms depending on which OpenSearch Service features you regularly use. 


<table>
<thead>
  <tr><th>Alarm</th><th>Issue</th></tr>
</thead>
<tbody>
  <tr><td><code>WarmFreeStorageSpace</code> is &gt;= 10%</td><td>You have reached 10% of your total free warm storage. <code>WarmFreeStorageSpace</code> measures the sum of your free warm storage space in MiB. UltraWarm uses Amazon S3 rather than attached disks.</td></tr>
  <tr><td><code>HotToWarmMigrationQueueSize</code> is &gt;= 20 for 1 minute, 3 consecutive times</td><td>A high number of indexes are concurrently moving from hot to UltraWarm storage. Consider scaling your cluster. </td></tr>
  <tr><td><code>HotToWarmMigrationSuccessLatency</code> is &gt;= 1 day, 1 consecutive time</td><td>Configure this alarm so that you're notified if the <code>HotToWarmMigrationSuccessCount</code> x latency is greater than 24 hours if you’re trying to roll daily indexes.</td></tr>
  <tr><td><code>WarmJVMMemoryPressure</code> maximum is &gt;= 95% for 1 minute, 3 consecutive times</td><td rowspan="2">The cluster could encounter out of memory errors if usage increases. Consider scaling vertically. OpenSearch Service uses half of an instance's RAM for the Java heap, up to a heap size of 32 GiB. You can scale instances vertically up to 64 GiB of RAM, at which point you can scale horizontally by adding instances.</td></tr>
  <tr><td><code>WarmOldGenJVMMemoryPressure</code> maximum is &gt;= 80% for 1 minute, 3 consecutive times</td></tr>
  <tr><td><code>WarmToColdMigrationQueueSize</code> is &gt;= 20 for 1 minute, 3 consecutive times</td><td>A high number of indexes are concurrently moving from UltraWarm to cold storage. Consider scaling your cluster. </td></tr>
  <tr><td><code>HotToWarmMigrationFailureCount</code> is &gt;= 1 for 1 minute, 1 consecutive time</td><td>Migrations might fail during snapshots, shard relocations, or force merges. Failures during snapshots or shard relocation are typically due to node failures or S3 connectivity issues. Lack of disk space is usually the underlying cause of force merge failures.</td></tr>
  <tr><td><code>WarmToColdMigrationFailureCount</code> is &gt;= 1 for 1 minute, 1 consecutive time</td><td>Migrations usually fail when attempts to migrate index metadata to cold storage fail. Failures can also happen when the warm index cluster state is being removed.</td></tr>
  <tr><td><code>WarmToColdMigrationLatency</code> is &gt;= 1 day, 1 consecutive time</td><td>Configure this alarm so that you're notified if the <code>WarmToColdMigrationSuccessCount</code> x latency is greater than 24 hours if you’re trying to roll daily indexes.</td></tr>
  <tr><td><code>AlertingDegraded</code> is &gt;= 1 for 1 minute, 1 consecutive time</td><td>Either the alerting index is red, or one or more nodes is not on schedule. </td></tr>
  <tr><td><code>ADPluginUnhealthy</code> is &gt;= 1 for 1 minute, 1 consecutive time</td><td>The anomaly detection plugin isn't functioning properly, either because of high failure rates or because one of the indexes being used is red.</td></tr>
  <tr><td><code>AsynchronousSearchFailureRate</code> is &gt;= 1 for 1 minute, 1 consecutive time</td><td>At least one asynchronous search failed in the last minute, which likely means the coordinator node failed. The lifecycle of an asynchronous search request is managed solely on the coordinator node, so if the coordinator goes down, the request fails.</td></tr>
  <tr><td><code>AsynchronousSearchStoreHealth</code> is &gt;= 1 for 1 minute, 1 consecutive time</td><td>The health of the asynchronous search response store in the persisted index is red. You might be storing large asynchronous responses, which can destabilize a cluster. Try to limit your asynchronous search responses to 10 MB or less.</td></tr>
  <tr><td><code>SQLUnhealthy</code> is &gt;= 1 for 1 minute, 3 consecutive times</td><td>The SQL plugin is returning 5<i>xx</i> response codes or passing invalid query DSL to OpenSearch. Troubleshoot the requests that your clients are making to the plugin. </td></tr>
  <tr><td><code>LTRStatus.red</code> is &gt;= 1 for 1 minute, 1 consecutive time</td><td>At least one of the indexes needed to run the Learning to Rank plugin has missing primary shards and isn't functional.</td></tr>
</tbody>
</table>
