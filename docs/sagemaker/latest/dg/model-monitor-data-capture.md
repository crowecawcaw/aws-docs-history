

# Data capture
<a name="model-monitor-data-capture"></a>

**Note**  
Amazon SageMaker Model Monitor is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Model Monitor, but we do not plan to introduce new features. For more information, see [Amazon SageMaker Model Monitor availability change](model-monitor-availability-change.md). 

To log the inputs to your endpoint and the inference outputs from your deployed model to Amazon S3, you can enable a feature called *Data Capture*. *Data Capture* is commonly used to record information that can be used for training, debugging, and monitoring. Amazon SageMaker Model Monitor automatically parses this captured data and compares metrics from this data with a baseline that you create for the model. For more information about Model Monitor see [Data and model quality monitoring with Amazon SageMaker Model Monitor](model-monitor.md).

You can implement *Data Capture* for both real-time and batch model-monitor modes using the AWS SDK for Python (Boto) or the SageMaker Python SDK. For a real-time endpoint, you will specify your *Data Capture* configuration when you create your endpoint. Due to the persistent nature of your real-time endpoint, you can configure additional options to turn data capturing on or off at certain times, or change the sampling frequency. You can also choose to encrypt your inference data.

For a batch transform job, you can enable *Data Capture* if you want to run on-schedule model monitoring or continuous model-monitoring for regular, periodic batch transform jobs. You will specify your *Data Capture* configuration when you create your batch transform job. Within this configuration, you have the option to turn on encryption or generate the inference ID with your output, which helps you match your captured data to Ground Truth data.