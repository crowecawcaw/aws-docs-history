# What tools are available for

troubleshooting an Amazon EMR cluster?

To identify and fix cluster errors, you can use the tools described on this page. You
might need to initialize some of the tools when you launch the cluster. Other tools are
available for every cluster by default.

###### Topics

- [View EMR cluster details](#emr-troubleshoot-tools-details "#emr-troubleshoot-tools-details")
- [View EMR cluster error details](#emr-troubleshoot-errordetail "#emr-troubleshoot-errordetail")
- [Run scripts and configure Amazon EMR
  processes](#emr-troubleshoot-tools-commands "#emr-troubleshoot-tools-commands")
- [View log files](#emr-troubleshoot-tools-logs "#emr-troubleshoot-tools-logs")
- [Monitor EMR cluster
  performance](#emr-troubleshoot-tools-performance "#emr-troubleshoot-tools-performance")

## View EMR cluster details

You can use the AWS Management Console, AWS CLI, or EMR API to retrieve detailed information about an
EMR cluster and job execution. For more information about using the AWS Management Console and AWS CLI,
see [View Amazon EMR cluster status and details](emr-manage-view-clusters.md "emr-manage-view-clusters.md").

### Amazon EMR console details pane

In the **Clusters** list on the Amazon EMR console, you can see
high-level information about the status of each cluster in your account and
AWS Region. The list displays all active and terminated clusters that you launched
in the past two months. From the **Clusters** list, you can select
a cluster **Name** to view cluster details. This information is
organized in different categories to make it easy to navigate.

The **Application user interfaces** available in the cluster
details page can be useful to troubleshoot clusters. It provides status of YARN
applications, and for some, such as Spark applications you can drill into different
metrics and facets such as jobs, stages, and executors. For more information, see
[View Amazon EMR application history](emr-cluster-application-history.md "emr-cluster-application-history.md"). This feature is available
only for Amazon EMR releases 5.8.0 and higher.

### Amazon EMR command line interface

You can locate details about a cluster from the AWS CLI with the
`--describe` argument.

### Amazon EMR API

You can locate details about a cluster from the API using the
`DescribeJobFlows` action.

## View EMR cluster error details

When an EMR cluster terminates with an error, the `DescribeCluster` and
`ListClusters` APIs return an error code and an error message. For select
cluster errors, the `ErrorDetail` data array can help you troubleshoot the
failure.

For a list of error codes that include `ErrorDetail` data, see [Error codes with ErrorDetail
information in Amazon EMR](emr-troubleshoot-error-errordetail.md "emr-troubleshoot-error-errordetail.md").

###### Note

We continuously refine our error messages so that you receive the most recent and
pertinent information. We don't recommend that you parse the text from
`ErrorMessage` because this text is subject to change.

## Run scripts and configure Amazon EMR

processes

As part of your troubleshooting process, you might find it helpful to run custom
scripts on your cluster or view and configure cluster processes.

### View and restart

application processes

It can be helpful to view running processes on your cluster in order to diagnose
potential issues. You can stop and restart cluster processes by connecting to the
master node of your cluster. For more information, see [View and restart Amazon EMR and application
processes (daemons)](emr-process-restart-stop-view.md "emr-process-restart-stop-view.md").

### Run commands and scripts

without an SSH connection

To run a command or a script on your cluster as a step, you can use the
`command-runner.jar` or `script-runner.jar` tools without
establishing an SSH connection to the master node. For more information, see [Run
commands and scripts on an Amazon EMR cluster](../ReleaseGuide/emr-commandrunner.md "../ReleaseGuide/emr-commandrunner.md").

## View log files

Amazon EMR and Hadoop both generate log files as the cluster runs. You can access these log
files from several different tools, depending on the configuration that you specified
when you launched the cluster. For more information, see [Configure Amazon EMR cluster logging and debugging](emr-plan-debugging.md "emr-plan-debugging.md").

### Log files on the master

node

Every cluster publishes logs files to the /mnt/var/log/ directory on the master
node. These log files are only available while the cluster is running.

### Log files archived to Amazon S3

If you launch the cluster and specify an Amazon S3 log path, the cluster copies the log
files stored in /mnt/var/log/ on the master node to Amazon S3 in 5-minute intervals. This
ensures that you have access to the log files even after the cluster is terminated.
Because the files are archived in 5-minute intervals, the last few minutes of an
suddenly terminated cluster may not be available.

## Monitor EMR cluster

performance

Amazon EMR provides several tools to monitor the performance of your cluster.

### Hadoop web interfaces

Every cluster publishes a set of web interfaces on the master node that contain
information about the cluster. You can access these web pages by using an SSH tunnel
to connect them on the master node. For more information, see [View web interfaces hosted on Amazon EMR
clusters](emr-web-interfaces.md "emr-web-interfaces.md").

### CloudWatch metrics

Every cluster reports metrics to CloudWatch. CloudWatch is a web service that tracks metrics,
and which you can use to set alarms on those metrics. For more information, see
[Monitoring Amazon EMR metrics with CloudWatch](UsingEMR_ViewingMetrics.md "UsingEMR_ViewingMetrics.md").
