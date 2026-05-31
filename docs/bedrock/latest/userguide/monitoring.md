# Monitor the `bedrock-runtime` endpoint

The `bedrock-runtime.`region`.amazonaws.com` endpoint
serves the [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"), [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md"), [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md"), and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") API operations.
The topics in this section describe the observability options available for traffic to this
endpoint, including Amazon CloudWatch metrics, AWS CloudTrail logging, and model invocation logging.

For more information about CloudWatch, see [What is
Amazon CloudWatch](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.

If your application calls the `bedrock-mantle.`region`.api.aws`
endpoint, see [Monitor the bedrock-mantle endpoint](monitoring-mantle.md "monitoring-mantle.md") instead.

###### Topics

- [Monitor model invocation using CloudWatch Logs and Amazon S3](model-invocation-logging.md "model-invocation-logging.md")
- [Monitor bedrock-runtime inference using CloudWatch metrics](monitoring-runtime-metrics.md "monitoring-runtime-metrics.md")
- [Monitor Amazon Bedrock API calls using CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
