

# Visualize results for real-time endpoints in Amazon SageMaker Studio
<a name="model-monitor-interpreting-visualize-results"></a>

**Note**  
Amazon SageMaker Model Monitor is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Model Monitor, but we do not plan to introduce new features. For more information, see [Amazon SageMaker Model Monitor availability change](model-monitor-availability-change.md). 

If you are monitoring a real-time endpoint, you can also visualize the results in Amazon SageMaker Studio. You can view the details of any monitoring job run, and you can create charts that show the baseline and captured values for any metric that the monitoring job calculates.

**To view the detailed results of a monitoring job**

1. Sign in to Studio. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

1. In the left navigation pane, choose the **Components and registries** icon (![Components and registries icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/Components_registries.png)).

1. Choose **Endpoints** in the drop-down menu.  
![Location of the Endpoints drop-down menu in the console.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mm-studio-endpoints.png)

1. On the endpoint tab, choose the monitoring type for which you want to see job details.  
![The location of the Model Quality tab in the MODEL MONITORING section.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mm-studio-model-quality.png)

1. Choose the name of the monitoring job run for which you want to view details from the list of monitoring jobs.  
![The Model Quality tab of the MOLDEL MONITORING section.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mm-studio-job-history.png)

1. The **MONITORING JOB DETAILS** tab opens with a detailed report of the monitoring job.  
![The MONITORING JOB DETAILS tab.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mm-studio-job-details.png)

You can create a chart that displays the baseline and captured metrics for a time period.

**To create a chart in SageMaker Studio to visualize monitoring results**

1. Sign in to Studio. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

1. In the left navigation pane, choose the **Components and registries** icon (![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/icons/Components_registries.png)).

1. Choose **Endpoints** in the drop-down menu.  
![Location of the Endpoints drop-down menu in the console.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mm-studio-endpoints.png)

1. On the **Endpoint** tab, choose the monitoring type you want to create a chart for. This example shows a chart for the **Model quality** monitoring type.  
![The location of the Model Quality tab in the MODEL MONITORING section.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mm-studio-model-quality.png)

1. Choose **Add chart**.  
![Location of Add chart in the console.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mm-studio-add-chart.png)

1. On the **CHART PROPERTIES** tab, choose the time period, statistic, and metric that you want to chart. This example shows a chart for a **Timeline** of **1 week**, the **Average** **Statistic** of, and the **F1** **Metric**.  
![Location of where to select a metric in the console.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mm-studio-chart-properties.png)

1. The chart that shows the baseline and current metric statistic you chose in the previous step shows up in the **Endpoint** tab.  
![Example chart showing the baseline and current average metric chosen in the previous step.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/model_monitor/mm-studio-f1-chart.png)