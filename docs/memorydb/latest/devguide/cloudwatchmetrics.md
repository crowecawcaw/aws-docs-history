

# Monitoring CloudWatch metrics
<a name="cloudwatchmetrics"></a>

MemoryDB and CloudWatch are integrated so you can gather a variety of metrics. You can monitor these metrics using CloudWatch. 

**Note**  
The following examples require the CloudWatch command line tools. For more information about CloudWatch and to download the developer tools, see the [ CloudWatch product page](https://aws.amazon.com/cloudwatch). 

The following procedures show you how to use CloudWatch to gather storage space statistics for an cluster for the past hour. 

**Note**  
The `StartTime` and `EndTime` values supplied in the examples following are for illustrative purposes. Make sure to substitute appropriate start and end time values for your nodes.

For information on MemoryDB limits, see [AWS service limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_memorydb) for MemoryDB.

## Monitoring CloudWatch metrics (Console)
<a name="cloudwatchmetricsclusters.viewdetails"></a>

 **To gather CPU utilization statistics for a cluster** 

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. Select the nodes you want to view metrics for. 
**Note**  
Selecting more than 20 nodes disables viewing metrics on the console.

   1. On the ** Clusters** page of the AWS Management Console, click the name of one or more clusters.

      The detail page for the cluster appears. 

   1. Click the **Nodes** tab at the top of the window.

   1. On the **Nodes** tab of the detail window, select the nodes that you want to view metrics for.

      A list of available CloudWatch Metrics appears at the bottom of the console window. 

   1. Click on the **CPU Utilization** metric. 

      The CloudWatch console will open, displaying your selected metrics. You can use the **Statistic** and **Period** drop-down list boxes and **Time Range** tab to change the metrics being displayed. 

## Monitoring CloudWatch metrics using the CloudWatch CLI
<a name="cloudwatchmetrics.cli"></a>

 **To gather CPU utilization statistics for a cluster** 
+ Use the CloudWatch command **aws cloudwatch get-metric-statistics** with the following parameters (note that the start and end times are shown as examples only; you will need to substitute your own appropriate start and end times):

  For Linux, macOS, or Unix:

  ```
  1. aws cloudwatch get-metric-statistics CPUUtilization \
  2.     --dimensions={{ClusterName=mycluster,NodeId=0002}}" \
  3.     --statistics={{Average}} \
  4.     --namespace="{{AWS/MemoryDB}}" \
  5.     --start-time {{2013-07-05T00:00:00}} \
  6.     --end-time {{2013-07-06T00:00:00}} \
  7.     --period={{60}}
  ```

  For Windows:

  ```
  1. mon-get-stats CPUUtilization ^
  2.     --dimensions={{ClusterName=mycluster,NodeId=0002}}" ^
  3.     --statistics={{Average}} ^
  4.     --namespace="{{AWS/MemoryDB}}" ^
  5.     --start-time {{2013-07-05T00:00:00}} ^
  6.     --end-time {{2013-07-06T00:00:00}} ^
  7.     --period={{60}}
  ```

## Monitoring CloudWatch metrics using the CloudWatch API
<a name="cloudwatchmetrics.api"></a>

 **To gather CPU utilization statistics for a cluster** 
+ Call the CloudWatch API `GetMetricStatistics` with the following parameters (note that the start and end times are shown as examples only; you will need to substitute your own appropriate start and end times):
  + `Statistics.member.1``=Average`
  + `Namespace``=AWS/MemoryDB`
  + `StartTime``=2013-07-05T00:00:00`
  + `EndTime``=2013-07-06T00:00:00`
  + `Period``=60`
  + `MeasureName``=CPUUtilization`
  + `Dimensions``=ClusterName=mycluster,NodeId=0002`  
**Example**  

  ```
   1. http://monitoring.amazonaws.com/
   2.     ?SignatureVersion=4
   3.     &Action=GetMetricStatistics
   4.     &Version=2014-12-01
   5.     &StartTime=2013-07-16T00:00:00
   6.     &EndTime=2013-07-16T00:02:00
   7.     &Period=60
   8.     &Statistics.member.1=Average
   9.     &Dimensions.member.1="ClusterName=mycluster"
  10.     &Dimensions.member.2="NodeId=0002"
  11.     &Namespace=Amazon/memorydb
  12.     &MeasureName=CPUUtilization						
  13.     &Timestamp=2013-07-07T17%3A48%3A21.746Z
  14.     &AWS;AccessKeyId=<&AWS; Access Key ID>
  15.     &Signature=<Signature>
  ```