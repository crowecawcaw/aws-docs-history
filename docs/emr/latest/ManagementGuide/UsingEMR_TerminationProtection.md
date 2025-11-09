# Using termination protection to protect your Amazon EMR clusters from

accidental shut down

Termination protection protects your clusters from accidental termination, which can be especially useful
for long running clusters processing critical workloads.
When termination protection is enabled on a long-running cluster, you can still
terminate the cluster, but you must explicitly remove termination protection from the
cluster first. This helps ensure that EC2 instances are not shut down by an accident or
error. You can enable termination protection when you create a cluster, and you can change the
setting on a running cluster.

With termination protection enabled, the `TerminateJobFlows` action in the
Amazon EMR API does not work. Users cannot terminate the cluster using this API or the
`terminate-clusters` command from the AWS CLI. The API returns an error,
and the CLI exits with a non-zero return code. When you use the Amazon EMR console to
terminate a cluster, you are prompted with an extra step to turn termination protection
off.

###### Warning

Termination protection does not guarantee that data is retained in the event of a human error or a workaround—for example, if
a reboot command is issued from the command line while connected to the instance using SSH, if an application or script running on the instance issues a reboot command,
or if the Amazon EC2 or Amazon EMR API is used to disable termination protection. This is true as well if you're running Amazon EMR releases 7.1 and higher
and an instance becomes unhealthy and unrecoverable. Even with termination protection enabled, data saved to instance storage,
including HDFS data, can be lost. Write data output to Amazon S3 locations and create backup strategies as appropriate for your business continuity requirements.

Termination protection does not affect your ability to scale cluster resources using
any of the following actions:

- Resizing a cluster manually with the AWS Management Console or AWS CLI. For more information,
  see [Manually resize a running Amazon EMR cluster](emr-manage-resize.md "emr-manage-resize.md").
- Removing instances from a core or task instance group using a scale-in policy
  with automatic scaling. For more information, see [Using automatic scaling with a custom policy for
  instance groups in Amazon EMR](emr-automatic-scaling.md "emr-automatic-scaling.md").
- Removing instances from an instance fleet by reducing target capacity. For
  more information, see [Instance fleet options](emr-instance-fleet.md#emr-instance-fleet-options "emr-instance-fleet.md#emr-instance-fleet-options").

## Termination protection and Amazon EC2

The termination protection setting in an Amazon EMR cluster corresponds with the `DisableApiTermination`
attribute for all Amazon EC2 instances in the cluster. For example, if you enable termination protection
in an EMR cluster, Amazon EMR automatically sets `DisableApiTermination` to true for all EC2
instances within the EMR cluster. The same applies if you disable termination protection.
Amazon EMR automatically sets `DisableApiTermination` to false
for all EC2 instances within the EMR cluster. If you terminate or
scale down a cluster from Amazon EMR and the Amazon EC2 settings conflict for an EC2 instance,
Amazon EMR prioritizes the Amazon EMR setting over the `DisableApiStop` and `DisableApiTermination`
settings in Amazon EC2 and continues to terminate the EC2 instance.

For example, you can use the Amazon EC2 console to enable termination protection on an
Amazon EC2 instance in an EMR cluster with termination protection disabled.
If you terminate or scale down the cluster with the Amazon EMR console, the AWS CLI, or the Amazon EMR API,
Amazon EMR overrides the `DisableApiTermination` setting, sets it to false, and
terminates the instance along with other instances.

You can also use the Amazon EC2 console to enable stop protection on an Amazon EC2 instance
in an EMR cluster with termination protection disabled. If you terminate or scale down the cluster,
Amazon EMR sets `DisableApiStop` to false in Amazon EC2 and terminates the instance along with other
instances.

Amazon EMR overrides the `DisableApiStop` setting only when you terminate or scale
down a cluster. When you enable or disable termination protection in an EMR cluster,
Amazon EMR doesn’t change the `disableApiStop` setting for any of the EC2 instances in the
respective EMR cluster.

###### Important

If you create an instance as part of an Amazon EMR cluster with termination
protection, and you use the Amazon EC2 API or AWS CLI commands to modify the instance
so that `DisableApiTermination` is `false`, and then the
Amazon EC2 API or AWS CLI commands run the `TerminateInstances` operation,
the Amazon EC2 instance terminates.

## Termination protection and

unhealthy YARN nodes

Amazon EMR periodically checks the Apache Hadoop YARN status of nodes running on core
and task Amazon EC2 instances in a cluster. The health status is reported by the [NodeManager health checker service](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/NodeManager.html#Health_checker_service "https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/NodeManager.html#Health_checker_service"). If a node reports
`UNHEALTHY`, the Amazon EMR instance controller adds the node to a denylist and
does not allocate YARN containers to it until it becomes healthy again. Depending on the statuses of termination protection,
unhealthy node replacement, and Amazon EMR release version, Amazon EMR will either [replace the unhealthy instance or stop allocating controllers to the instance](emr-plan-node-replacement.md "emr-plan-node-replacement.md").

## Termination protection and termination after step

execution

When you enable termination after step execution and _also_ enable
termination protection, Amazon EMR ignores the termination protection.

When you submit steps to a cluster, you can set the `ActionOnFailure`
property to determine what happens if the step can't complete execution because of
an error. The possible values for this setting are `TERMINATE_CLUSTER`
(`TERMINATE_JOB_FLOW` with earlier versions),
`CANCEL_AND_WAIT`, and `CONTINUE`. For more information,
see [Submit work to an Amazon EMR cluster](emr-work-with-steps.md "emr-work-with-steps.md").

If a step fails that is configured with `ActionOnFailure` set to
`CANCEL_AND_WAIT`, if termination after step execution is enabled, the cluster
terminates without executing subsequent steps.

If a step fails that is configured with `ActionOnFailure` set to
`TERMINATE_CLUSTER`, use the table of settings below to determine the
outcome.

| ActionOnFailure     | Termination after step execution | Termination protection | Result             |
| ------------------- | -------------------------------- | ---------------------- | ------------------ |
| `TERMINATE_CLUSTER` | Enabled                          | Disabled               | Cluster terminates |
| Enabled             | Enabled                          | Cluster terminates     |
| Disabled            | Enabled                          | Cluster continues      |
| Disabled            | Disabled                         | Cluster terminates     |

## Termination protection and Spot

Instances

Amazon EMR termination protection does not prevent an Amazon EC2 Spot Instance from
terminating when the Spot price rises above the maximum Spot price.

## Configuring termination

protection when you launch a cluster

You can enable or disable termination protection when you launch a cluster using
the console, the AWS CLI, or the API.

For single-node clusters, default termination protection settings are as follows:

- Launching a cluster by Amazon EMR Console —Termination Protection is **disabled** by default.
- Launching a cluster by AWS CLI `aws emr create-cluster`—Termination Protection is
  **disabled** unless
  `--termination-protected` is specified.
- Launching a cluster by Amazon EMR API [RunJobFlow](../../../ElasticMapReduce/latest/API/API_RunJobFlow.md "../../../ElasticMapReduce/latest/API/API_RunJobFlow.md")
  command—Termination Protection is **disabled** unless the `TerminationProtected`
  boolean value is set to `true`.

For high-availability clusters, default termination protection settings are as follows:

- Launching a cluster by Amazon EMR Console — Termination Protection is **enabled** by default.
- Launching a cluster by AWS CLI `aws emr create-cluster`—Termination Protection is
  **disabled** unless
  `--termination-protected` is specified.
- Launching a cluster by Amazon EMR API [RunJobFlow](../../../ElasticMapReduce/latest/API/API_RunJobFlow.md "../../../ElasticMapReduce/latest/API/API_RunJobFlow.md")
  command—Termination Protection is **disabled** unless the `TerminationProtected`
  boolean value is set to `true`.

Console

###### To turn termination protection on or off when you create a

cluster with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. For **EMR release version**, choose
   **emr-6.6.0** or later.
4. Under **Cluster termination and node replacement**, make sure that
   **Use termination protection** is
   pre-selected, or clear the selection to turn it off.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

AWS CLI

###### To turn termination protection on or off when you create a

cluster using the AWS CLI

- With the AWS CLI, you can launch a cluster with termination
  protection enabled with the `create-cluster` command
  with the `--termination-protected` parameter.
  Termination protection is disabled by default.

The following example creates cluster with termination
protection enabled:

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name "`TerminationProtectedCluster`" --release-label `emr-7.10.0` \
--applications Name=`Hadoop` Name=`Hive` Name=`Pig` \
--use-default-roles --ec2-attributes KeyName=`myKey` --instance-type `m5.xlarge` \
--instance-count `3` --termination-protected
```

For more information about using Amazon EMR commands in the AWS CLI,
see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

## Configuring termination

protection for running clusters

You can configure termination protection for a running cluster with the console or
the AWS CLI.

Console

###### To turn termination protection on or off for a running cluster

with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and select the
   cluster that you want to update.
3. On the **Properties** tab on the cluster
   details page, find **Cluster termination** and
   select **Edit**.
4. Select or clear the **Use termination
   protection** check box to turn the feature on or
   off. Then select **Save changes** to
   confirm.

AWS CLI

###### To turn termination protection on or off for a running cluster

using the AWS CLI

- To enable termination protection on a running cluster with the
  AWS CLI, use the `modify-cluster-attributes` command
  with the `--termination-protected` parameter. To
  disable it, use the `--no-termination-protected`
  parameter.

The following example enables termination protection on the
cluster with ID
`j-3KVTXXXXXX7UG`:

```
aws emr modify-cluster-attributes --cluster-id `j-3KVTXXXXXX7UG` --termination-protected
```

The following example disables termination protection on the
same cluster:

```
aws emr modify-cluster-attributes --cluster-id `j-3KVTXXXXXX7UG` --no-termination-protected
```
