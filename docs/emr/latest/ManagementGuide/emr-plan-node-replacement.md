# Replacing unhealthy nodes with Amazon EMR

Amazon EMR periodically uses the [NodeManager health checker service](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/NodeManager.html#Health_checker_service "https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/NodeManager.html#Health_checker_service") in Apache Hadoop to monitor the statuses of core nodes in your
Amazon EMR on Amazon EC2 clusters. If a node is not functioning optimally, the node is marked as unhealthy and the health checker reports that node
to the Amazon EMR controller. The Amazon EMR controller adds the node to a deny list,
preventing the node from receiving new YARN applications until the status of the node improves.

###### Note

A common reason for a node to be unhealthy is that it is out of disk space. For more information about
when a core node is almost out of disk space, the following **re:Post Knowledge Center** article is helpful:
[Why is the core node in my Amazon EMR cluster running out of disk space?](https://repost.aws/knowledge-center/core-node-emr-cluster-disk-space "https://repost.aws/knowledge-center/core-node-emr-cluster-disk-space")

###### Note

Hadoop does provide the ability to run customized node-health checks. This is explained in further detail in the Apache Hadoop documentation
at [NodeManager](https://hadoop.apache.org/docs/r3.3.2/hadoop-yarn/hadoop-yarn-site/NodeManager.html "https://hadoop.apache.org/docs/r3.3.2/hadoop-yarn/hadoop-yarn-site/NodeManager.html").

You can choose whether Amazon EMR should terminate unhealthy nodes or keep them in the cluster.
If you turn off unhealthy-node replacement, they stay in the
deny list and continue to count toward cluster capacity. You can still connect to your Amazon EC2 core instance
for configuration and recovery, so you can resize your cluster if you want to add capacity. For more information about how node replacement and termination work, see [Using termination protection](UsingEMR_TerminationProtection.md "UsingEMR_TerminationProtection.md").

If unhealthy node replacement is turned on, Amazon EMR terminates an unhealthy core node and provisions a new instance,
based on the number of instances in the instance group, or based on the target capacity for instance fleets. If any nodes are unhealthy for
more than 45 minutes, Amazon EMR will [gracefully replace the nodes](emr-scaledown-behavior.md#emr-scaledown-terminate-task "emr-scaledown-behavior.md#emr-scaledown-terminate-task"). If graceful decommissioning for a node doesn't complete within one hour, the
node is forcefully terminated, unless terminating it brings the cluster below replication factor or HDFS capacity constraints.

###### Important

Note that the time it takes before a node is gracefully decommissioned or terminated can be subject to change.

While unhealthy node replacement significantly mitigates the possibility for data loss, it doesn't eliminate the risk entirely. HDFS data can be permanently lost during the graceful replacement of an unhealthy core instance. We recommend that you
always back up your data.

For more information about identifying unhealthy nodes and recovery, see
[Resource errors](emr-troubleshoot-error-resource.md "emr-troubleshoot-error-resource.md"). Additionally, for more best practices you can follow in order to maintain the health of a cluster, see
the following documentation for the resource error [Amazon EMR cluster terminates with NO_SLAVE_LEFT and
core nodes FAILED_BY_MASTER](emr-cluster-NO_SLAVE_LEFT-FAILED_BY_MASTER.md "emr-cluster-NO_SLAVE_LEFT-FAILED_BY_MASTER.md").

Amazon EMR publishes Amazon CloudWatch Events for unhealthy node replacement, so you can keep track of what's happening
with your unhealthy core instances. For more information, see
[unhealthy node replacement events](emr-manage-cloudwatch-events.md#emr-cloudwatch-unhealthy-node-replacement-events "emr-manage-cloudwatch-events.md#emr-cloudwatch-unhealthy-node-replacement-events").

## Default node replacement and termination protection settings

Unhealthy node replacement is available for all Amazon EMR releases, but the default settings depend on the
release label you choose. You can change any of these settings by configuring unhealthy node replacement
when creating a new cluster or by going to cluster configuration at any time.

If you're creating a single-node cluster or high-availability cluster that is running Amazon EMR release 7.0 or lower, the default
setting of unhealthy node replacement is dependent on termination protection:

- Enabling termination protection **disables** unhealthy node replacement.
- Disabling termination protection **enables** unhealthy node replacement.

## Configuring unhealthy node replacement when you launch a cluster

You can enable or disable unhealthy node replacement when you launch a cluster using the console, the AWS CLI, or the API.

The default unhealthy node replacement setting depends on how you launch the cluster:

- Amazon EMR console — unhealthy node replacement is **enabled** by default.
- AWS CLI `aws emr create-cluster` — unhealthy node replacement is **enabled** by default unless you specify
  `--no-unhealthy-node-replacement`.
- Amazon EMR [RunJobFlow API command](../APIReference/API_RunJobFlow.md "../APIReference/API_RunJobFlow.md") — unhealthy node replacement is **enabled** by default unless you set the `UnhealthyNodeReplacement` Boolean value
  to `True` or `False`.

Console

###### To turn unhealthy node replacement on or off when you create a

cluster with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. For **EMR release version**, choose
   the Amazon EMR release label you want.
4. Under **Cluster termination and node replacement**, make sure that
   **Unhealthy node replacement (recommended)** is
   pre-selected, or clear the selection to turn it off.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

AWS CLI

###### To turn unhealthy node replacement on or off when you create a

cluster using the AWS CLI

- With the AWS CLI, you can launch a cluster with unhealthy node replacement
  enabled with the `create-cluster` command
  with the `--unhealthy-node-replacement` parameter.
  Unhealthy node replacement is on by default.

The following example creates a cluster with unhealthy node replacement enabled:

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name "`SampleCluster`" --release-label `emr-7.10.0` \
--applications Name=`Hadoop` Name=`Hive` Name=`Pig` \
--use-default-roles --ec2-attributes KeyName=`myKey` --instance-type `m5.xlarge` \
--instance-count `3` --unhealthy-node-replacement
```

For more information about using Amazon EMR commands in the AWS CLI,
see [Amazon EMR AWS CLI commands](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

## Configuring unhealthy node replacement in a running cluster

You can turn unhealthy node replacement on or off for a running cluster using the console, the AWS CLI, or the API.

Console

###### To turn unhealthy node replacement on or off for a running cluster

with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and select the
   cluster that you want to update.
3. On the **Properties** tab on the cluster
   details page, find **Cluster termination and node replacement** and
   select **Edit**.
4. Select or clear the **unhealthy node replacement** check box to turn the feature on or
   off. Then select **Save changes** to
   confirm.

AWS CLI

###### To turn unhealthy node replacement on or off for a running cluster

using the AWS CLI

- To turn on unhealthy node replacement on a running cluster with the
  AWS CLI, use the `modify-cluster-attributes` command
  with the `--unhealthy-node-replacement` parameter. To
  disable it, use the `--no-unhealthy-node-replacement`
  parameter.

The following example turns on unhealthy node replacement on the
cluster with ID
`j-3KVTXXXXXX7UG`:

```
aws emr modify-cluster-attributes --cluster-id `j-3KVTXXXXXX7UG` --unhealthy-node-replacement
```

The following example turns off unhealthy node replacement on the
same cluster:

```
aws emr modify-cluster-attributes --cluster-id `j-3KVTXXXXXX7UG` --no-unhealthy-node-replacement
```
