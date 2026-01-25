# Using the the

Amazon CloudWatch Evidently extension

###### Warning

Amazon CloudWatch Evidently is no longer supported. Please see [this](https://aws.amazon.com/blogs/mt/support-for-amazon-cloudwatch-evidently-ending-soon/ "https://aws.amazon.com/blogs/mt/support-for-amazon-cloudwatch-evidently-ending-soon/") for more details

You can use Amazon CloudWatch Evidently to safely validate new features by serving them to a
specified percentage of your users while you roll out the feature. You can monitor the
performance of the new feature to help you decide when to ramp up traffic to your users.
This helps you reduce risk and identify unintended consequences before you fully launch the
feature. You can also conduct A/B experiments to make feature design decisions based on
evidence and data.

The AWS AppConfig extension for CloudWatch Evidently allows your application to assign variations to
user sessions locally instead of by calling the [EvaluateFeature](../../../cloudwatchevidently/latest/APIReference/API_EvaluateFeature.md "../../../cloudwatchevidently/latest/APIReference/API_EvaluateFeature.md") operation. A local session mitigates the latency and availability
risks that come with an API call. For information about how to configure and use the
extension, see [Perform launches and
A/B experiments with CloudWatch Evidently](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.md") in the
_Amazon CloudWatch User Guide_.
