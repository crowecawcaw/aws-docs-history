# Terminate an Amazon EMR cluster in the starting, running, or waiting states

###### Warning

A terminated EMR Cluster is irrecoverable. Ensure that the resource and any data on HDFS or jupyter notebooks is no longer required prior to removal. HDFS data is lost when
the cluster is terminated.

This section describes the methods of terminating a cluster. For information about
enabling termination protection and auto-terminating clusters, see [Control Amazon EMR cluster termination](emr-plan-termination.md "emr-plan-termination.md"). You can terminate
clusters in the `STARTING`, `RUNNING`, or `WAITING` states.
A cluster in the `WAITING` state must be terminated or it runs indefinitely,
generating charges to your account. You can terminate a cluster that fails to leave the
`STARTING` state or is unable to complete a step.

If you want to terminate a cluster that has termination protection set on it, you must
disable termination protection before you can terminate the cluster. Clusters can be
terminated using the console, the AWS CLI, or programmatically using the
`TerminateJobFlows` API.

Depending on the configuration of the cluster, it could take from 5 to 20 minutes for the
cluster to completely terminate and release allocated resources, such as EC2
instances.

###### Note

You can't restart a terminated cluster, but you can clone a terminated cluster to
reuse its configuration for a new cluster. For more information, see [Clone an Amazon EMR cluster using the console](clone-console.md "clone-console.md").

###### Important

Amazon EMR uses the [Amazon EMR service role](emr-iam-role.md "emr-iam-role.md") and the
`AWSServiceRoleForEMRCleanup` role to clean up cluster resources
in your account that you no longer use, such as Amazon EC2 instances. You must include
actions for the role policies to delete or terminate the resources. Otherwise, Amazon EMR
can’t perform these cleanup actions, and you might incur costs for unused resources that
remain on the cluster.

## Terminate a cluster with the

console

You can terminate one or more clusters using the Amazon EMR console. The steps to terminate
a cluster in the console vary depending on whether termination protection is on or off.
To terminate a protected cluster, you must first disable termination protection.

Console

###### To terminate a cluster with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Choose **Clusters**, and then choose the cluster
   you want to terminate.
3. Under the **Actions** dropdown menu, choose
   **Terminate cluster** to open the
   **Terminate cluster** prompt.
4. At the prompt, choose **Terminate**. Depending on
   the cluster configuration, termination may take 5 to 10 minutes. For
   more information on how to Amazon EMR clusters, see [Terminate an Amazon EMR cluster in the starting, running, or waiting states](UsingEMR_TerminateJobFlow.md "UsingEMR_TerminateJobFlow.md").

## Terminate a cluster with the

AWS CLI

###### To terminate an unprotected cluster using the AWS CLI

To terminate an unprotected cluster using the AWS CLI, use the
`terminate-clusters` subcommand with the --cluster-ids parameter.

- Type the following command to terminate a single cluster and replace
  `j-3KVXXXXXXX7UG` with your cluster ID.

```
aws emr terminate-clusters --cluster-ids `j-3KVXXXXXXX7UG`
```

To terminate multiple clusters, type the following command and replace
`j-3KVXXXXXXX7UG` and
`j-WJ2XXXXXX8EU` with your cluster IDs.

```
aws emr terminate-clusters --cluster-ids `j-3KVXXXXXXX7UG` `j-WJ2XXXXXX8EU`
```

For more information on using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

###### To terminate a protected cluster using the AWS CLI

To terminate a protected cluster using the AWS CLI, first disable termination
protection using the `modify-cluster-attributes` subcommand with the
`--no-termination-protected` parameter. Then use the
`terminate-clusters` subcommand with the `--cluster-ids`
parameter to terminate it.

1. Type the following command to disable termination protection and replace
   `j-3KVTXXXXXX7UG` with your cluster ID.

```
aws emr modify-cluster-attributes --cluster-id `j-3KVTXXXXXX7UG` --no-termination-protected
```

2. To terminate the cluster, type the following command and replace
   `j-3KVXXXXXXX7UG` with your cluster ID.

```
aws emr terminate-clusters --cluster-ids `j-3KVXXXXXXX7UG`
```

To terminate multiple clusters, type the following command and replace
`j-3KVXXXXXXX7UG` and
`j-WJ2XXXXXX8EU` with your cluster IDs.

```
aws emr terminate-clusters --cluster-ids `j-3KVXXXXXXX7UG` `j-WJ2XXXXXX8EU`
```

For more information on using Amazon EMR commands in the AWS CLI, see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

## Terminate a cluster with the

API

The `TerminateJobFlows` operation ends step processing, uploads any log
data from Amazon EC2 to Amazon S3 (if configured), and terminates the Hadoop cluster. A cluster
also terminates automatically if you set `KeepJobAliveWhenNoSteps` to
`False` in a `RunJobFlows` request.

You can use this action to terminate either a single cluster or a list of clusters by
their cluster IDs.

For more information about the input parameters unique to
`TerminateJobFlows`, see [TerminateJobFlows](../../../ElasticMapReduce/latest/API/API_TerminateJobFlows.md "../../../ElasticMapReduce/latest/API/API_TerminateJobFlows.md"). For more
information about the generic parameters in the request, see [Common request parameters](../../../ElasticMapReduce/latest/API/CommonParameters.md "../../../ElasticMapReduce/latest/API/CommonParameters.md").
