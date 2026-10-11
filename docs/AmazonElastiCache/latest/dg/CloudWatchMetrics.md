

# Monitoring CloudWatch Cluster and Node Metrics
<a name="CloudWatchMetrics"></a>

ElastiCache and CloudWatch are integrated so you can gather a variety of metrics. You can monitor these metrics using CloudWatch. 

**Note**  
The following command line examples use the AWS Command Line Interface (AWS CLI). For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

The following procedures show you how to use CloudWatch to gather CPU utilization statistics for a cluster. 

**Note**  
The `StartTime` and `EndTime` values supplied in the examples below are for illustrative purposes. You must substitute appropriate start and end time values for your cache nodes.

For information on ElastiCache limits, see [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_elasticache) for ElastiCache.

## Monitoring CloudWatch Cluster and Node Metrics (Console)
<a name="CloudWatchMetrics.CON"></a>

 **To view metrics for the nodes in a cluster** 

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. From the navigation pane, choose **Valkey caches**, **Redis OSS caches**, or **Memcached caches**, depending on the engine of your cluster.

1. Choose your cluster.

1. Choose the **Metrics** tab.

   The charts show the metrics for the nodes in the cluster. For a Valkey cluster with more than 16 nodes, the charts show the first 16 nodes by default.
**Note**  
The **Metrics** tab charts up to 16 nodes at a time.

1. (Valkey only, optional) To choose which nodes to chart, use the **Node ID** or **Shard ID** filter.

   If the filter matches more than 16 nodes, the console shows **Cannot select more than 16 nodes**. To see other nodes, change the filter, for example, to `Shard ID = 0003`.

1. (Redis OSS and Memcached only) To choose which nodes to chart, choose **Compare nodes**, and then select the nodes.

   For a cluster with more than 16 nodes, the charts show no metrics until you choose the nodes to chart.

(Valkey only) The **Metrics** tab has two views. The **Classic** view, which is the default, shows CloudWatch metrics. The **Detailed** view shows OpenTelemetry metrics, and appears only in Regions where detailed monitoring is available. For more information about the **Detailed** view, see [Monitoring ElastiCache with OpenTelemetry metrics](otel-metrics.md).

## Monitoring CloudWatch Cluster and Node Metrics using the AWS CLI
<a name="CloudWatchMetrics.CLI"></a>

 **To gather CPU utilization statistics for a cache cluster** 
+ For Linux, macOS, or Unix:

  ```
  aws cloudwatch get-metric-statistics \
      --namespace AWS/ElastiCache \
      --metric-name CPUUtilization \
      --dimensions={{'[{"Name":"CacheClusterId","Value":"test"},{"Name":"CacheNodeId","Value":"0001"}]'}} \
      --statistics={{Average}} \
      --start-time {{2018-07-05T00:00:00}} \
      --end-time {{2018-07-06T00:00:00}} \
      --period={{3600}}
  ```

  For Windows:

  ```
  aws cloudwatch get-metric-statistics ^
      --namespace AWS/ElastiCache ^
      --metric-name CPUUtilization ^
      --dimensions {{Name=CacheClusterId,Value=test Name=CacheNodeId,Value=0001}} ^
      --statistics={{Average}} ^
      --start-time {{2018-07-05T00:00:00}} ^
      --end-time {{2018-07-06T00:00:00}} ^
      --period={{3600}}
  ```

## Monitoring CloudWatch Cluster and Node Metrics using the CloudWatch API
<a name="CloudWatchMetrics.API"></a>

 **To gather CPU utilization statistics for a cache cluster** 
+ Call the CloudWatch API `GetMetricStatistics` with the following parameters (note that the start and end times are shown as examples only; you will need to substitute your own appropriate start and end times):
  + `Statistics.member.1``=Average`
  + `Namespace``=AWS/ElastiCache`
  + `StartTime``=2018-07-05T00:00:00`
  + `EndTime``=2018-07-06T23:59:00`
  + `Period``=3600`
  + `MetricName``=CPUUtilization`
  + `Dimensions.member.1.Name``=CacheClusterId`
  + `Dimensions.member.1.Value``=mycachecluster`
  + `Dimensions.member.2.Name``=CacheNodeId`
  + `Dimensions.member.2.Value``=0002`  
**Example**  

  ```
   1. https://monitoring.amazonaws.com/
   2.     ?Action=GetMetricStatistics
   3.     &SignatureVersion=4
   4.     &Version=2010-08-01
   5.     &StartTime=2018-07-05T00:00:00
   6.     &EndTime=2018-07-06T23:59:00
   7.     &Period=3600
   8.     &Statistics.member.1=Average
   9.     &Dimensions.member.1.Name=CacheClusterId
  10.     &Dimensions.member.1.Value=mycachecluster
  11.     &Dimensions.member.2.Name=CacheNodeId
  12.     &Dimensions.member.2.Value=0002
  13.     &Namespace=AWS/ElastiCache
  14.     &MetricName=CPUUtilization
  15.     &Timestamp=2018-07-07T17%3A48%3A21.746Z
  16.     &SignatureMethod=HmacSHA256
  17.     &X-Amz-Credential=<credential>
  ```