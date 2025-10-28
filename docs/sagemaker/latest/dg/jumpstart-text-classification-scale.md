# Deploy your model at scale

Set up auto-scaling and CloudWatch monitoring for your SageMaker AI endpoint to make it production-ready.

## Why production monitoring matters for text classification

Text classification workloads require monitoring because they:

- Experience variable traffic patterns with processing bursts.
- Require sub-second response times.
- Need cost optimization through auto-scaling.

## Prerequisites

Before you begin, make sure that you have:

- Your SageMaker AI endpoint deployed from the previous section.
- Your endpoint name (for example, jumpstart-dft-hf-tc).
- Your AWS Region (for example, us-east-2).

For endpoint creation or troubleshooting, see [Real-time inference](realtime-endpoints.md "realtime-endpoints.md").

## Set up production monitoring

Configure CloudWatch monitoring to track your model's performance in production.

1. In your JupyterLab space, open the `sagemaker_production_monitoring.ipynb` notebook from the evaluation package you uploaded earlier.
2. Update your endpoint name and region in the configuration section.
3. Follow the notebook instructions to set up:
   - Auto-scaling (1-10 instances based on traffic).
   - CloudWatch alarms for latency and invocation thresholds.
   - Metrics dashboard for visual monitoring.

## Verify your setup

After you complete the notebook steps, verify that you have:

- **Endpoint Status**: `InService`.
- **Auto-scaling**: 1-10 instances configured.
- **CloudWatch Alarms**: 2 alarms monitoring.
- **Metrics**: 15+ metrics registered.

###### Note

Alarms may show `INSUFFICIENT_DATA` initially - this is normal and will change to `OK` with usage.

## Monitor your endpoint

Access visual monitoring through the AWS Management Console:

- [CloudWatch Metrics](<https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~();query=AWS/SageMaker> "https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~();query=AWS/SageMaker")
- [CloudWatch Alarms](https://console.aws.amazon.com/cloudwatch/home#alarmsV2: "https://console.aws.amazon.com/cloudwatch/home#alarmsV2:")

For more information, see [Monitor SageMaker AI](monitoring-overview.md "monitoring-overview.md").

## Manage cost and clean up resources

Your monitoring setup provides valuable production insights, but it also incurs ongoing AWS charges through CloudWatch metrics, alarms, and auto-scaling policies. Understanding how to manage these costs is essential for cost-effective operations. Clean up resources when they're no longer needed.

###### Warning

Your endpoint continues to incur charges even when not processing requests. To stop all charges, you must delete your endpoint. For instructions, see [Delete Endpoints and Resources](realtime-endpoints-delete-resources.md "realtime-endpoints-delete-resources.md").

For advanced monitoring configurations, see [CloudWatch Metrics for SageMaker AI](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
