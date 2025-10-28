# Active tracing in Amazon SNS

Use AWS X-Ray to trace and analyze user requests as they pass through your Amazon SNS topics
to [Amazon Data Firehose](sns-firehose-as-subscriber.md "sns-firehose-as-subscriber.md"), [AWS Lambda](../../../xray/latest/devguide/xray-services-lambda.md "../../../xray/latest/devguide/xray-services-lambda.md"), [Amazon SQS](../../../xray/latest/devguide/xray-services-sqs.md "../../../xray/latest/devguide/xray-services-sqs.md"),
and HTTP/S endpoint subscriptions.

With X-Ray, you get an end-to-end view of each request, allowing you to:

- Identify what is calling your Amazon SNS topic and what services are downstream of its
  subscriptions.
- Analyze latencies, such as:
  - Time spent in the Amazon SNS topic before processing.
  - Delivery times for each subscribed endpoint.

###### Important

Amazon SNS topics with numerous subscriptions may reach a size limit and not be fully
traced. For information about trace document size limits, see [X-ray service
quotas](../../../general/latest/gr/xray.md#limits_xray "../../../general/latest/gr/xray.md#limits_xray") in AWS General Reference.

If you call an Amazon SNS API from a service that's already being traced, Amazon SNS passes the
trace through, even if X-Ray tracing isn't enabled on the API.

Amazon SNS supports X-Ray tracing for both standard and FIFO topics. You can enable X-Ray for
an Amazon SNS topic by using the [Amazon SNS
console](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home"), [Amazon SNS `SetTopicAttributes`
API](../api/API_SetTopicAttributes.md "../api/API_SetTopicAttributes.md"), [Amazon Simple Notification Service CLI Reference](../../../cli/latest/reference/sns.md "../../../cli/latest/reference/sns.md"), or [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.md").

To learn more about using Amazon SNS with X-Ray, see [Amazon SNS and AWS X-Ray](../../../xray/latest/devguide/xray-services-sns.md "../../../xray/latest/devguide/xray-services-sns.md") in the
AWS X-Ray Developer Guide.

## Active tracing permissions

When using the Amazon SNS console, Amazon SNS attempts to create the necessary permissions for
the Amazon SNS topic to call X-Ray. The attempt can be rejected if you don't have sufficient
permissions to use the Amazon SNS console. For more information, see [Identity and access management in Amazon SNS](security-iam.md "security-iam.md") and [Example cases for Amazon SNS access control](sns-access-policy-use-cases.md "sns-access-policy-use-cases.md").

When using the CLI, you must manually configure the permissions. Those permissions are
configured using resource policies. For more on using required permissions in X-Ray,
see [Amazon SNS
and AWS X-Ray](../../../xray/latest/devguide/xray-services-sns.md "../../../xray/latest/devguide/xray-services-sns.md").

## Enabling active tracing on an Amazon SNS topic

using the AWS console

When active tracing is enabled on an Amazon SNS topic, it reads the trace ID, sends the
data to the customer based on the trace ID, and propagates the trace ID to downstream
services.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. Choose a topic or create a new one. For more details on creating topics, see
   [Creating an Amazon SNS topic](sns-create-topic.md "sns-create-topic.md").
3. On the **Create topic** page, in the
   **Details** section, choose a topic type:
   **FIFO** or **Standard**.
   1. Enter a **Name** for the topic.
   2. (Optional) Enter a **Display name** for the
      topic.

4. Expand **Active tracing**, and choose **Use active
   tracing**.

Once you've enabled X-Ray for your Amazon SNS topic, you can use the [X-Ray
service map](../../../xray/latest/devguide/xray-services-sns.md "../../../xray/latest/devguide/xray-services-sns.md") to view the end-to-end traces and service maps for the
topic.

## Enabling active tracing on an Amazon SNS

topic using the AWS SDK

The following code example shows how to enable active tracing on an Amazon SNS topic by
using the AWS SDK for Java.

```
public static void enableActiveTracing(SnsClient snsClient, String topicArn) {

        try {

            SetTopicAttributesRequest request = SetTopicAttributesRequest.builder()
                .attributeName("TracingConfig")
                .attributeValue("Active")
                .topicArn(topicArn)
                .build();

            SetTopicAttributesResponse result = snsClient.setTopicAttributes(request);
            System.out.println("\n\nStatus was " + result.sdkHttpResponse().statusCode() + "\n\nTopic " + request.topicArn()
                + " updated " + request.attributeName() + " to " + request.attributeValue());

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
        }
    }
```

## Enabling active tracing on an Amazon SNS

topic using the AWS CLI

The following code example shows how to enable active tracing on an Amazon SNS topic by
using the AWS CLI.

```
aws sns set-topic-attributes \
    --topic-arn arn:aws:sns:us-west-2:123456789012:MyTopic \
    --attribute-name TracingConfig \
    --attribute-value Active
```

## Enabling active tracing on an Amazon SNS topic

using AWS CloudFormation

The following AWS CloudFormation stack shows how to enable active tracing on an Amazon SNS topic.

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyTopicResource:
    Type: 'AWS::SNS::Topic'
    Properties:
      TopicName: 'MyTopic'
      TracingConfig: 'Active'

```

## Verifying active tracing is enabled for your

topic

You can use the Amazon SNS console to verify if active tracing is enabled for your topic,
or when the resource policy has failed to be added.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the left navigation pane, choose **Topics**.
3. On the **Topics** page, select a topic.
4. Choose the **Integrations** tab.

When active tracing is enabled, a green **Active** icon is
displayed. 5. If you have enabled active tracing and you don't see that the resource policy
has been added, choose **Create policy** to add the additional
required permissions.

![Screen shot displaying the details of an Amazon SNS topic named "SampleTopic" in the AWS Management Console. It indicates that AWS X-Ray active tracing is enabled for this topic, but a resource policy allowing Amazon SNS to send trace data is missing. A "Create policy" button is provided to resolve this issue.](images/xray.png)

## Testing active tracing

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. Create an Amazon SNS topic. For details on how to do this, see [To create a topic using the AWS Management Console](sns-create-topic.md#create-topic-aws-console "sns-create-topic.md#create-topic-aws-console").
3. Expand **Active tracing**, and choose **Use active
   tracing**.
4. Publish a message to the Amazon SNS topic. For details on how to do this, see [To publish messages to Amazon SNS topics using the
   AWS Management Console](sns-publishing.md#sns-publishing-messages "sns-publishing.md#sns-publishing-messages").
5. Use the [X-Ray service map](../../../xray/latest/devguide/xray-services-sns.md "../../../xray/latest/devguide/xray-services-sns.md")
   to view the end-to-end traces and service maps for the topic.

![Displays an AWS X-Ray service map that shows the tracing of a request flowing from a client to an Amazon SNS topic named "xray-topic." From there, the message is distributed to various downstream services, including an Amazon SQS queue, a Lambda function, a Kinesis firehose, and a remote service. Each connection displays metrics such as latency in milliseconds (ms) and the rate of transactions per minute (t/min), helping to analyze the performance and identify any latency issues in the message delivery process.](images/xray-troubleshooting.png)
