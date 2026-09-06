

# Tutorial: Create and subscribe to an Amazon SNS topic
<a name="batch_sns_create_topic"></a>

 For this tutorial, you configure an Amazon SNS topic to serve as an event target for your new event rule. 

**To create an Amazon SNS topic**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. Choose **Topics**, **Create topic**.

1. For **Type**, choose **Standard**.

1. For **Name**, enter **JobFailedAlert** and choose **Create topic**.

1. On the **JobFailedAlert** screen, choose **Create subscription**. 

1. For **Protocol**, choose **Email**.

1. For **Endpoint**, enter an email address that you currently have access to and choose **Create subscription**.

1. Check your email account, and wait to receive a subscription confirmation email message. When you receive it, choose **Confirm subscription**. 