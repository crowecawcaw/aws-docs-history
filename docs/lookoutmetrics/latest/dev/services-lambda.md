Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Using AWS Lambda with Lookout for Metrics

You can use AWS Lambda as a channel for anomaly alerts from an Amazon Lookout for Metrics detector. With a Lambda function, you can
process anomaly alerts in your preferred programming language, and use the AWS SDK to interact with other AWS
services.

Lambda is a serverless way for you to run code in AWS. Your code only runs and only incurs charges when it is
invoked. If you don't already have a Lambda function, see [Create a Lambda function with the console](../../../lambda/latest/dg/getting-started-create-function.md "../../../lambda/latest/dg/getting-started-create-function.md") in the
Lambda Developer Guide to get started.

###### To create a Lambda alert

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Add alert**.
4. Choose **AWS Lambda**.
5. Choose a function.

###### Note

When you add a Lambda alert to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md "permissions-service.md") with permission to invoke the function.

When your detector finds an anomaly with a severity score that meets or exceeds the alert's threshold, it
invokes your Lambda function with an event that contains details about the anomaly. The Lambda runtime converts this
document into an object and passes it to your function's _handler method_. You can use this
object to perform additional processing, to record details about the anomaly in a database or storage, or to call
another service.

For sample code in all programming languages supported by Lambda, see [Lambda sample applications](../../../lambda/latest/dg/lambda-samples.md "../../../lambda/latest/dg/lambda-samples.md") in the AWS Lambda Developer Guide.
