

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Creating alarms and notifications for resources protected by Shield Advanced
<a name="add-alarm-ddos"></a>

The following procedure shows how to manage CloudWatch alarms for protected resources. 

**Note**  
CloudWatch incurs additional costs. For CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

**To create alarms and notifications**

1. In the protections page **Create alarms and notifications - *optional***, configure the SNS topics for the alarms and notifications that you want to receive. For resources that you don't want notifications for, choose **No topic**. You can add an Amazon SNS topic or create a new topic. 

1. To create an Amazon SNS topic, follow these steps:

   1. In the dropdown list, choose **Create an SNS topic**.

   1. Enter a topic name. 

   1. Optionally enter an email address that the Amazon SNS messages will be sent to, and then choose **Add email**. You can enter more than one.

   1. Choose **Create**.

1. Choose **Next**.