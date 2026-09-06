

# Viewing Amazon CloudWatch metrics
<a name="view-optimization-metrics"></a>

 After running the table optimizers successfully, the service creates Amazon CloudWatch metrics on the optimization job performance. You can go to the **CloudWatch Metrics** and choose **Metrics**, **All metrics**. You can to filter metrics by the specific namespace (for example AWS Glue), table name, or database name.

 For more information, see [View available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html) in the *Amazon CloudWatch User Guide*. 

****Compaction****
+ Number of bytes compacted 
+ Number of files compacted
+ Number of DPU allocated to job 
+ Duration of job (Hours) 

****Snapshot retention****
+ Number of data files deleted 
+ Number of manifest files deleted
+ Number of Manifest lists deleted 
+ Duration of job (Hours)

****Orphan file deletion****
+ Number of orphan files deleted 
+ Duration of job (Hours) 