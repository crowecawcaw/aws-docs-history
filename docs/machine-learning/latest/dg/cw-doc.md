We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Monitoring Amazon ML with Amazon CloudWatch Metrics

Amazon ML automatically sends metrics to Amazon CloudWatch so that you can gather
and analyze usage statistics for your ML models. For example, to keep track of batch
and real-time predictions, you can monitor the PredictCount metric according to the
RequestMode dimension. The metrics are automatically collected and sent to
Amazon CloudWatch every five minutes. You can monitor these metrics by using the
Amazon CloudWatch console, AWS CLI, or AWS SDKs.

There is no charge for the Amazon ML metrics that are reported through CloudWatch.
If you set alarms on the metrics, you will be billed at standard [CloudWatch rates](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

For more information, see the Amazon ML list of metrics in [Amazon
CloudWatch Namespaces, Dimensions, and Metrics Reference](../../../AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.md "../../../AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.md") in the
Amazon CloudWatch Developer Guide.
