# Configuring delivery status logging using the

AWS Management Console

This topic explains how to enable message delivery status logging for Amazon SNS topics,
including configuring logging settings, assigning IAM roles, and verifying that CloudWatch Logs
capture delivery logs for monitoring and troubleshooting.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Topics**.
3. Select the desired **topic** and then choose
   **Edit**.
4. Expand the **Delivery status logging** section.
5. Choose the **protocol** for which you want to
   enable logging (for example, HTTP, Lambda, Amazon SQS).
6. Enter the **Success sample rate**, which is the percentage of
   successful messages for which you want to receive CloudWatch Logs.
7. In the **IAM roles** section, you must configure roles for
   both **success** and **failure** logging:
   - **Use an existing service role** –
     Select an existing IAM role that has the required permissions for
     Amazon SNS to write logs to CloudWatch.

   - **Create a new service role** –
     Choose **Create new roles** to define the IAM roles
     for successful and failed deliveries in the IAM console. For
     permission details, see [Prerequisites for delivery status logging](topics-attrib-prereq.md "topics-attrib-prereq.md").

8. Choose **Save changes**.

After enabling logging, you can view and parse the CloudWatch Logs containing the
message delivery status. For more information about using CloudWatch, see the [CloudWatch
documentation](https://aws.amazon.com/documentation/cloudwatch "https://aws.amazon.com/documentation/cloudwatch").
**Verifying log setup**

1. Sign into the CloudWatch Logs console.
2. Locate the log group named
   `sns/<region>/<account-id>/<topic-name>`.
3. Ensure log streams exist for the configured endpoint protocol.
4. Send a test message to your topic and confirm that log entries appear,
   indicating successful or failed deliveries.
