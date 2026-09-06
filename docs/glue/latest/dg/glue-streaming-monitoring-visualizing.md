

# Visualizing AWS Glue streaming metrics
<a name="glue-streaming-monitoring-visualizing"></a>

To plot visual metrics:

1. Go to **Metrics** in the Amazon CloudWatch console and then choose the **Browse** tab. Then choose **Glue** under "Custom namespaces".  
![The screenshot shows accessing metrics in the Amazon CloudWatch console when monitoring AWS Glue streaming jobs.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-monitoring-1.png)

1. Choose **Job Metrics** to show you the metrics for all your jobs.

1. Filter the metrics based on your JobName=glue-feb-monitoring and then JobRunId=ALL. You can click on the "\+" sign as shown in the figure below to add it to the search filter. 

1. Select the checkbox for the metrics that you are interested in. In the below figure we have selected `numberAllExecutors` and `numberMaxNeededExecutors`.  
![The screenshot shows applying an average to metrics when monitoring streaming jobs.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-monitoring-2.png)

1. Once you have selected these metrics, you can go to the **Graphed metrics** tab and apply your statistics.

1. Since the metrics are emitted every min, you can apply the "average" over a minute for `batchProcessingTimeInMs` and `maxConsumerLagInMs`. For the `numRecords` you can apply the "sum" over every minute.

1. You can add a horizontal `windowSize` annotation to your graph using the **Options** tab.  
![The screenshot shows adding a windowSize annotation to your graph when monitoring streaming jobs.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-monitoring-3.png)

1. Once you have your metrics selected, create a dashboard and add it. Here is a sample dashboard.  
![The screenshot shows a sample dashboard for monitoring streaming jobs.](http://docs.aws.amazon.com/glue/latest/dg/images/streaming-monitoring-4.png)