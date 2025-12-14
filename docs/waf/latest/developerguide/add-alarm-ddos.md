**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Creating alarms and notifications for resources protected by Shield Advanced

The following procedure shows how to manage CloudWatch alarms for protected resources.

###### Note

CloudWatch incurs additional costs. For CloudWatch pricing, see
[Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### To create alarms and notifications

1. In the protections page **Create alarms and notifications - _optional_**, configure the SNS topics
   for the alarms and notifications that you want to receive. For resources that
   you don't want notifications for, choose **No topic**. You can
   add an Amazon SNS topic or create a new topic.
2. To create an Amazon SNS topic, follow these steps:
   1. In the dropdown list, choose **Create an SNS topic**.
   2. Enter a topic name.
   3. Optionally enter an email address that the Amazon SNS messages will be sent to, and then
      choose **Add email**. You can enter more than
      one.
   4. Choose **Create**.

3. Choose **Next**.
