

# Endpoints monitoring
<a name="manage-endpoints-console-monitoring"></a>

After creating a SageMaker AI Hosting endpoint, you can monitor your endpoint using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics. Using these metrics, you can access historical information and gain a better perspective on how your endpoint is performing. For more information, see the *[Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/)*.

From the **Monitoring** tab on the endpoint details page, you can view CloudWatch metrics data that has been collected from your endpoint.

The **Monitoring** tab includes the following sections:
+ **Operational metrics**: View metrics that track the utilization of your endpoint’s resources, such as CPU Utilization and Memory Utilization.
+ **Invocation metrics**: View metrics that track the number, health, and status of `InvokeEndpoint` requests coming to your endpoint, such as Invocation Model Errors and Model Latency.
+ **Health metrics**: View metrics that track your endpoint’s overall health, such as Invocation Failures and Notification Failures.

For detailed descriptions of each metric, see [Monitor SageMaker AI with CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html).

The following screenshot shows the **Operational metrics** section for a serverless endpoint.

![Screenshot of metrics graphs in the operational metrics section of the endpoint details page.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/hosting-operational-metrics.png)




You can adjust the **Period** and **Statistic** that you want to track for the metrics in a given section, as well as the length of time for which you want to view metrics data. You can also add and remove metric widgets from the view for each section by choosing **Add widget**. In the **Add widget **dialog box, you can select and deselect the metrics that you want to see.

The metrics that are available may depend on your endpoint type. For example, serverless endpoints have some metrics that aren’t available for real-time endpoints. For more specific metrics information by endpoint type, see the following pages:
+ [Monitor a serverless endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-monitoring.html)
+ [Monitor an asynchronous endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-monitor.html)
+ [CW Metrics for Multi-Model Endpoint Deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoint-cloudwatch-metrics.html)
+ [Inference Pipeline Logs and Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-logs-metrics.html)