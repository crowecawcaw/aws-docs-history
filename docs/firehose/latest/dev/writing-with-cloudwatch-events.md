

# Send CloudWatch Events to Firehose
<a name="writing-with-cloudwatch-events"></a>

You can configure Amazon CloudWatch to send events to a Firehose stream by adding a target to a CloudWatch Events rule.

**To create a target for a CloudWatch Events rule that sends events to an existing Firehose stream**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Create rule**.

1. On the **Step 1: Create rule** page, for **Targets**, choose **Add target**, and then choose **Firehose stream**.

1. Choose an existing **Firehose stream**.

For more information about creating CloudWatch Events rules, see [Getting Started with Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CWE_GettingStarted.html).