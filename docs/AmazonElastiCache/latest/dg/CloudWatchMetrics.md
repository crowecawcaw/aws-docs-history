# Monitoring CloudWatch Cluster and Node Metrics

ElastiCache and CloudWatch are integrated so you can gather a variety of
metrics. You can monitor these metrics using CloudWatch.

###### Note

The following examples require the CloudWatch command line tools. For more
information about CloudWatch and to download the developer tools, see the
[CloudWatch product page](https://aws.amazon.com/cloudwatch "https://aws.amazon.com/cloudwatch").

The following procedures show you how to use CloudWatch to gather storage space
statistics for an cluster for the past hour.

###### Note

The `StartTime` and `EndTime` values supplied in the examples below
are for illustrative purposes. You must substitute appropriate start and end time values
for your cache nodes.

For information on ElastiCache limits, see [AWS Service Limits](../../../general/latest/gr/aws_service_limits.md#limits_elasticache "../../../general/latest/gr/aws_service_limits.md#limits_elasticache") for ElastiCache.

## Monitoring CloudWatch Cluster and Node Metrics (Console)

**To gather CPU utilization statistics for a cache
cluster**

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. Select the cache nodes you want to view metrics for.

###### Note

Selecting more than 20 nodes disables viewing metrics on the console.

    1. On the **Cache Clusters** page of the AWS Management Console,
     click the name of one or more clusters.


    The detail page for the cluster appears.
    2. Click the **Nodes** tab at the top of the
     window.
    3. On the **Nodes** tab of the detail window, select the cache nodes
     that you want to view metrics for.


    A list of available CloudWatch Metrics appears at the bottom of the
     console window.
    4. Click on the **CPU Utilization** metric.


    The CloudWatch console will open, displaying your selected
     metrics. You can use the **Statistic** and
     **Period** drop-down list boxes and **Time
     Range** tab to change the metrics being displayed.

## Monitoring CloudWatch Cluster and Node Metrics using the CloudWatch CLI

**To gather CPU utilization statistics for a cache
cluster**

- For Linux, macOS, or Unix:

```
aws cloudwatch get-metric-statistics \
    --namespace AWS/ElastiCache \
    --metric-name CPUUtilization \
    --dimensions=`'[{"Name":"CacheClusterId","Value":"test"},{"Name":"CacheNodeId","Value":"0001"}]'` \
    --statistics=`Average` \
    --start-time `2018-07-05T00:00:00` \
    --end-time `2018-07-06T00:00:00` \
    --period=`3600`
```

For Windows:

```
aws cloudwatch get-metric-statistics ^
    --namespace AWS/ElastiCache ^
    --metric-name CPUUtilization ^
    --dimensions=`'[{"Name":"CacheClusterId","Value":"test"},{"Name":"CacheNodeId","Value":"0001"}]'` ^
    --statistics=`Average` ^
    --start-time `2018-07-05T00:00:00` ^
    --end-time `2018-07-06T00:00:00` ^
    --period=`3600`
```

## Monitoring CloudWatch Cluster and Node Metrics using the CloudWatch API

**To gather CPU utilization statistics for a cache
cluster**

- Call the CloudWatch API `GetMetricStatistics`
  with the following parameters (note that the start and end times are shown as examples only; you will
  need to substitute your own appropriate start and end times):
  - `Statistics.member.1``=Average`
  - `Namespace``=AWS/ElastiCache`
  - `StartTime``=2013-07-05T00:00:00`
  - `EndTime``=2013-07-06T00:00:00`
  - `Period``=60`
  - `MeasureName``=CPUUtilization`
  - `Dimensions``=CacheClusterId=mycachecluster,CacheNodeId=0002`

###### Example

```

http://monitoring.amazonaws.com/
    ?Action=GetMetricStatistics
    &SignatureVersion=4
    &Version=2014-12-01
    &StartTime=2018-07-05T00:00:00
    &EndTime=2018-07-06T23:59:00
    &Period=3600
    &Statistics.member.1=Average
    &Dimensions.member.1="CacheClusterId=mycachecluster"
    &Dimensions.member.2="CacheNodeId=0002"
    &Namespace=&AWS;/ElastiCache
    &MeasureName=CPUUtilization
    &Timestamp=2018-07-07T17%3A48%3A21.746Z
    &AWS;AccessKeyId=<&AWS; Access Key ID>
    &Signature=<Signature>
```
