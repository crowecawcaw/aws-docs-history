# Monitoring CloudWatch metrics

MemoryDB and CloudWatch are integrated so you can gather a variety of
metrics. You can monitor these metrics using CloudWatch.

###### Note

The following examples require the CloudWatch command line tools. For more
information about CloudWatch and to download the developer tools, see the
[CloudWatch product
page](https://aws.amazon.com/cloudwatch "https://aws.amazon.com/cloudwatch").

The following procedures show you how to use CloudWatch to gather storage space
statistics for an cluster for the past hour.

###### Note

The `StartTime` and `EndTime` values supplied in the examples following
are for illustrative purposes. Make sure to substitute appropriate start and end time values
for your nodes.

For information on MemoryDB limits, see [AWS service limits](../../../general/latest/gr/aws_service_limits.md#limits_memorydb "../../../general/latest/gr/aws_service_limits.md#limits_memorydb") for MemoryDB.

## Monitoring CloudWatch metrics (Console)

**To gather CPU utilization statistics for a cluster**

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. Select the nodes you want to view metrics for.

###### Note

Selecting more than 20 nodes disables viewing metrics on the console.

    1. On the  **Clusters** page of the AWS Management Console,
     click the name of one or more clusters.


    The detail page for the cluster appears.
    2. Click the **Nodes** tab at the top of the
     window.
    3. On the **Nodes** tab of the detail window, select the nodes
     that you want to view metrics for.


    A list of available CloudWatch Metrics appears at the bottom of the
     console window.
    4. Click on the **CPU Utilization** metric.


    The CloudWatch console will open, displaying your selected
     metrics. You can use the **Statistic** and
     **Period** drop-down list boxes and **Time
     Range** tab to change the metrics being displayed.

## Monitoring CloudWatch metrics using the CloudWatch CLI

**To gather CPU utilization statistics for a cluster**

- Use the CloudWatch command **aws cloudwatch get-metric-statistics** with the
  following parameters (note that the start and end times are shown as examples only; you will
  need to substitute your own appropriate start and end times):

For Linux, macOS, or Unix:

```
aws cloudwatch get-metric-statistics CPUUtilization \
    --dimensions=`ClusterName=mycluster,NodeId=0002`" \
    --statistics=`Average` \
    --namespace="`AWS/MemoryDB`" \
    --start-time `2013-07-05T00:00:00` \
    --end-time `2013-07-06T00:00:00` \
    --period=`60`
```

For Windows:

```
mon-get-stats CPUUtilization ^
    --dimensions=`ClusterName=mycluster,NodeId=0002`" ^
    --statistics=`Average` ^
    --namespace="`AWS/MemoryDB`" ^
    --start-time `2013-07-05T00:00:00` ^
    --end-time `2013-07-06T00:00:00` ^
    --period=`60`
```

## Monitoring CloudWatch metrics using the CloudWatch API

**To gather CPU utilization statistics for a cluster**

- Call the CloudWatch API `GetMetricStatistics`
  with the following parameters (note that the start and end times are shown as examples only; you will
  need to substitute your own appropriate start and end times):
  - `Statistics.member.1``=Average`
  - `Namespace``=AWS/MemoryDB`
  - `StartTime``=2013-07-05T00:00:00`
  - `EndTime``=2013-07-06T00:00:00`
  - `Period``=60`
  - `MeasureName``=CPUUtilization`
  - `Dimensions``=ClusterName=mycluster,NodeId=0002`

###### Example

```

http://monitoring.amazonaws.com/
    ?SignatureVersion=4
    &Action=GetMetricStatistics
    &Version=2014-12-01
    &StartTime=2013-07-16T00:00:00
    &EndTime=2013-07-16T00:02:00
    &Period=60
    &Statistics.member.1=Average
    &Dimensions.member.1="ClusterName=mycluster"
    &Dimensions.member.2="NodeId=0002"
    &Namespace=Amazon/memorydb
    &MeasureName=CPUUtilization
    &Timestamp=2013-07-07T17%3A48%3A21.746Z
    &AWS;AccessKeyId=<&AWS; Access Key ID>
    &Signature=<Signature>

```
