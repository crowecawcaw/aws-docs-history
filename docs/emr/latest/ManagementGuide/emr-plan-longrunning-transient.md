# Configuring an Amazon EMR cluster to continue or

terminate after step execution

This topic explains the differences between using a long-running cluster and creating
a transient cluster that shuts down after the last step runs. It also covers how to
configure step execution for a cluster.

## Create a long-running cluster

By default, clusters that you create with the console or the AWS CLI are
long-running. Long-running clusters continue to run, accept work, and accrue charges
until you take action to shut them down.

A long-running cluster is effective in the following situations:

- When you need to interactively or automatically query data.
- When you need to interact with big data applications hosted on the cluster
  on an ongoing basis.
- When you periodically process a data set so large or so frequently that it
  is inefficient to launch new clusters and load data each time.

You can also set termination protection on a long-running cluster to avoid
shutting down EC2 instances by accident or error. For more information, see [Using termination protection to protect your Amazon EMR clusters from
accidental shut down](UsingEMR_TerminationProtection.md "UsingEMR_TerminationProtection.md").

###### Note

Amazon EMR automatically enables termination protection for all clusters with multiple primary
nodes, and overrides any step execution settings that you supply when you
create the cluster. You can disable termination protection after the cluster has been launched. See [Configuring termination
protection for running clusters](UsingEMR_TerminationProtection.md#emr-termination-protection-running-cluster "UsingEMR_TerminationProtection.md#emr-termination-protection-running-cluster").
To shut down a cluster with multiple primary nodes, you must
first modify the cluster attributes to disable termination protection. For
instructions, see [Terminate an Amazon EMR Cluster with
multiple primary nodes](emr-plan-ha-launch.md#emr-plan-ha-launch-terminate "emr-plan-ha-launch.md#emr-plan-ha-launch-terminate").

## Configure a cluster to terminate after step

execution

When you configure termination after step execution, the cluster starts, runs
bootstrap actions, and then runs the steps that you specify. As soon as the last
step completes, Amazon EMR terminates the cluster's Amazon EC2 instances. Clusters that you
launch with the Amazon EMR API have step execution enabled by default.

Termination after step execution is effective for clusters that perform a periodic
processing task, such as a daily data processing run. Step execution also helps you
ensure that you are billed only for the time required to process your data. For more
information about steps, see [Submit work to an Amazon EMR cluster](emr-work-with-steps.md "emr-work-with-steps.md").

Console

###### To turn on termination after step execution with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation
   pane, choose **Clusters**, and then choose
   **Create cluster**.
3. Under **Steps**, choose **Add
   step**. In the **Add step**
   dialog, enter appropriate field values. Options differ depending
   on the step type. To add your step and exit the dialog, choose
   **Add step**.
4. Under **Cluster termination**, select the
   **Terminate cluster after last step
   completes** check box.
5. Choose any other options that apply to your cluster.
6. To launch your cluster, choose **Create
   cluster**.

AWS CLI

###### To turn on termination after step execution with the AWS CLI

- Specify the `--auto-terminate` parameter when you
  use the `create-cluster` command to create a
  transient cluster.

The following example demonstrates how to use the
`--auto-terminate` parameter. You can type the
following command and replace `myKey`
with the name of your EC2 key pair.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name "`Test cluster`" --release-label `emr-7.11.0` \
--applications Name=`Hive` Name=`Pig` --use-default-roles --ec2-attributes KeyName=`myKey` \
--steps Type=PIG,Name="Pig Program",ActionOnFailure=CONTINUE,\
Args=[-f,s3://amzn-s3-demo-bucket/scripts/pigscript.pig,-p,\
INPUT=s3://amzn-s3-demo-bucket/inputdata/,-p,OUTPUT=s3://amzn-s3-demo-bucket/outputdata/,\
$INPUT=s3://amzn-s3-demo-bucket/inputdata/,$OUTPUT=s3://amzn-s3-demo-bucket/outputdata/]
--instance-type `m5.xlarge` --instance-count `3` --auto-terminate
```

API

###### To turn off termination after step execution with the Amazon EMR API in cluster launch

1. When you use the [RunJobFlow](../../../ElasticMapReduce/latest/API/API_RunJobFlow.md "../../../ElasticMapReduce/latest/API/API_RunJobFlow.md") action to create a cluster, set the
   [KeepJobFlowAliveWhenNoSteps](../../../ElasticMapReduce/latest/API/API_JobFlowInstancesConfig.md#EMR-Type-JobFlowInstancesConfig-KeepJobFlowAliveWhenNoSteps "../../../ElasticMapReduce/latest/API/API_JobFlowInstancesConfig.md#EMR-Type-JobFlowInstancesConfig-KeepJobFlowAliveWhenNoSteps") property to
   `false`.
2. To change your configuration of termination after step execution with the Amazon EMR API post cluster launch:

Use SetKeepJobFlowAliveWhenNoSteps action.
