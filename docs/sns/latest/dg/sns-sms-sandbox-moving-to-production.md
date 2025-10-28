# Moving out of the Amazon SNS SMS

sandbox

Moving your AWS account out of the [SMS sandbox](sns-sms-sandbox.md "sns-sms-sandbox.md")
requires that you first add, verify, and test destination phone numbers. After doing this,
create a case with AWS Support.

###### To request that your AWS account is moved out of the SMS sandbox

1.  **Verify phone numbers**
    1. While your AWS account is in the SMS sandbox, open the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
    2. In the navigation pane, under Mobile, choose **Text messaging
       (SMS)**.
    3. In the Sandbox destination phone numbers section, [add and verify](sns-sms-sandbox-verifying-phone-numbers.md "sns-sms-sandbox-verifying-phone-numbers.md")
       one or more destination phone numbers. This verification ensures you can
       successfully send and receive messages.

2.  **Test SMS publishing**
    1. Confirm that you are able to send and receive messages to at least one
       verified phone number. For more detailed instructions on how to publish SMS
       messages, see [Publishing SMS messages to a mobile phone using
       Amazon SNS](sms_sending-overview.md#sms_publish-to-phone "sms_sending-overview.md#sms_publish-to-phone").

3.  **Initiate sandbox edit**
    1. On the Amazon SNS console's **Mobile text messaging (SMS)**
       page, under **Account information**, choose **Exit
       SMS sandbox**. This action redirects you to the [Amazon Support Center](https://support.console.aws.amazon.com/support/home?#/case/create?issueType=service-limit-increase "https://support.console.aws.amazon.com/support/home?#/case/create?issueType=service-limit-increase") and automatically creates a support case
       with the **Service quota increase** option selected.

4.  **Fill out the form**
    1. In the support form under **Service quota increase**, do
       the following:
       1. Choose choose **SNS Text Messaging** as the
          service.
       2. Provide the **website URL** or **app
          name** from which you intend to send SMS
          messages.
       3. Specify the type of messages you will send: **One Time
          Password**, **Promotional**, or
          **Transactional**.
       4. Choose the **AWS Region** from which you will
          send SMS messages.
       5. List the **countries** or
          **regions** where you plan to send SMS
          messages.
       6. Describe how your customers **opt-in to receive
          messages**.
       7. Include any **message templates** you intend to
          use.

5.  **Specify quota and Region**
    1. Under **Requests**, do the following:
       1. Choose the **AWS Region** where you want to
          move your AWS account.
       2. Choose **General Limits** for **Resource
          Type**.
       3. Choose **Exit SMS Sandbox** for
          **Quota**.
       4. (Optional) To request additional increases or other adjustments,
          choose **Add another request** and specify the
          necessary details.
       5. For **New quota value**, enter the
          **limit** in USD you are requesting.

6.  **Additional details**
    1. In the **Case description**, provide any additional
       details relevant to your request.
    2. Under **Contact options**, choose your
       **preferred contact language**.

7.  **Submit the request**

        1. Choose **Submit** to send your request to Support.

    The Support team provides an initial response to your request within 24 hours.

To prevent our systems from being used to send unsolicited or malicious content, we
consider each request carefully. If we can, we will grant your request within this 24-hour
period. However, if we need additional information from you, it might take longer to resolve your
request.

If your use case doesn't align with our policies, we might be unable to grant your request.
