

# Deploy your model at scale
<a name="jumpstart-text-classification-scale"></a>

Set up auto-scaling and CloudWatch monitoring for your SageMaker AI endpoint to make it production-ready.

## Why production monitoring matters for text classification
<a name="w2aac37c15c27b5"></a>

Text classification workloads require monitoring because they:
+ Experience variable traffic patterns with processing bursts.
+ Require sub-second response times.
+ Need cost optimization through auto-scaling.

## Prerequisites
<a name="w2aac37c15c27b7"></a>

Before you begin, make sure that you have:
+ Your SageMaker AI endpoint deployed from the previous section.
+ Your endpoint name (for example, jumpstart-dft-hf-tc).
+ Your AWS Region (for example, us-east-2).

For endpoint creation or troubleshooting, see [Real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html).

## Set up production monitoring
<a name="w2aac37c15c27b9"></a>

Configure CloudWatch monitoring to track your model's performance in production.

1. In your JupyterLab space, open the `sagemaker_production_monitoring.ipynb` notebook from the evaluation package you uploaded earlier.

1. Update your endpoint name and region in the configuration section.

1. Follow the notebook instructions to set up:
   + Auto-scaling (1-10 instances based on traffic).
   + CloudWatch alarms for latency and invocation thresholds.
   + Metrics dashboard for visual monitoring.

## Verify your setup
<a name="w2aac37c15c27c11"></a>

After you complete the notebook steps, verify that you have:
+ **Endpoint Status**: `InService`.
+ **Auto-scaling**: 1-10 instances configured.
+ **CloudWatch Alarms**: 2 alarms monitoring.
+ **Metrics**: 15\+ metrics registered.

**Note**  
Alarms may show `INSUFFICIENT_DATA` initially - this is normal and will change to `OK` with usage.

## Monitor your endpoint
<a name="w2aac37c15c27c13"></a>

Access visual monitoring through the AWS Management Console:
+ [CloudWatch Metrics](https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~();query=AWS/SageMaker)
+ [CloudWatch Alarms](https://console.aws.amazon.com/cloudwatch/home#alarmsV2:)

For more information, see [Monitor SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-overview.html).

## Manage cost and clean up resources
<a name="w2aac37c15c27c15"></a>

Your monitoring setup provides valuable production insights, but it also incurs ongoing AWS charges through CloudWatch metrics, alarms, and auto-scaling policies. Understanding how to manage these costs is essential for cost-effective operations. Clean up resources when they're no longer needed.

**Warning**  
Your endpoint continues to incur charges even when not processing requests. To stop all charges, you must delete your endpoint. For instructions, see [Delete Endpoints and Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-delete-resources.html).

For advanced monitoring configurations, see [CloudWatch Metrics for SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html).