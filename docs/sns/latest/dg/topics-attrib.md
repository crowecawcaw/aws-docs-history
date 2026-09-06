

# Configuring delivery status logging using the AWS Management Console
<a name="topics-attrib"></a>

This topic explains how to enable message delivery status logging for Amazon SNS topics, including configuring logging settings, assigning IAM roles, and verifying that CloudWatch Logs capture delivery logs for monitoring and troubleshooting.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home).

1. On the navigation panel, choose **Topics**.

1. Select the desired **topic** and then choose **Edit**.

1. Expand the **Delivery status logging** section.

1. Choose the **protocol** for which you want to enable logging (for example, HTTP, Lambda, Amazon SQS).

1. Enter the **Success sample rate**, which is the percentage of successful messages for which you want to receive CloudWatch Logs.

1. In the **IAM roles** section, you must configure roles for both **success** and **failure** logging:
   + **Use an existing service role** – Select an existing IAM role that has the required permissions for Amazon SNS to write logs to CloudWatch.
   + **Create a new service role** – Choose **Create new roles** to define the IAM roles for successful and failed deliveries in the IAM console. For permission details, see [Prerequisites for delivery status logging](topics-attrib-prereq.md).

1. Choose **Save changes**.

   After enabling logging, you can view and parse the CloudWatch Logs containing the message delivery status. For more information about using CloudWatch, see the [CloudWatch documentation](https://aws.amazon.com/documentation/cloudwatch).

**Verifying log setup**

1. Sign into the CloudWatch Logs console.

1. Locate the log group named `sns/<region>/<account-id>/<topic-name>`.

1. Ensure log streams exist for the configured endpoint protocol.

1. Send a test message to your topic and confirm that log entries appear, indicating successful or failed deliveries.