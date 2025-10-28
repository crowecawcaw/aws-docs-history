# Add a phone number to a WhatsApp Business Account (WABA)

You can add phone numbers to an existing WhatsApp Business Account (WABA) or create a new WABA for the phone
number.

## Prerequisites

Before you begin, the following prerequisites must be met:

- The phone number must be able to receive either an SMS or a voice One-Time
  Passcode (OTP). This is the phone number that is added to your WABA.
- The phone number must not be associated with any other WABA.

The following prerequisites must be met to use either an Amazon SNS topic
or Amazon Connect instance as a message and event destination.

###### Amazon SNS topic

- An Amazon SNS topic has been [created](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") and [permissions](managing-event-destinations-add.md#managing-event-destinations-sns-policies "managing-event-destinations-add.md#managing-event-destinations-sns-policies") have
  been added.

###### Note

Amazon SNS FIFO topics are not supported.

- **(Optional)** To use an Amazon SNS topic that is
  encrypted using AWS KMS keys you have to grant AWS End User Messaging Social permissions to the [existing key
  policy](managing-event-destinations-add.md#managing-event-destinations-topic-policies "managing-event-destinations-add.md#managing-event-destinations-topic-policies").

###### Amazon Connect instance

- An Amazon Connect instances has been [created](../../../connect/latest/adminguide/tutorial1-set-up-your-instance.md "../../../connect/latest/adminguide/tutorial1-set-up-your-instance.md") and [permissions](managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies "managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies") have been added.

## Add a phone number to a WABA

To add a new phone number to your existing WABA

1. Open the AWS End User Messaging Social console at
   [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/ "https://console.aws.amazon.com/social-messaging/").
2. Choose **Business Accounts**, and then **Add WhatsApp
   phone number**.
3. On the **Add WhatsApp phone number** page, choose
   **Launch Facebook portal**. A new login window from Meta
   will appear.
4. In the Meta login window, enter your Meta developer account credentials and
   choose your business portfolio.
5. Choose the WABA and WhatsApp Business Profile that you want to add the phone
   number to.
6. Choose **Next**.
7. For **Add a phone number for WhatsApp**, enter a phone number to register.
   This phone number is displayed to your customers when you send them a message.
8. For **Choose how you would like to verify your number**, choose either
   **Text message** or **Phone call**.
9. Once you are ready to receive the verification code, choose **Next**
10. Enter the verification code, and then choose **Next**. Once your number has
    been verified, you can choose **Next** to close the window from
    Meta.
11. Under **WhatsApp Phone numbers**:
    1. For **Phone number verification**, enter the existing
       PIN or enter a new PIN code. To reset a lost or forgotten PIN, follow
       the directions in [Updating PIN](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification/#updating-pin "https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification/#updating-pin") in the _WhatsApp Business Platform
       Cloud API Reference_.
    2. For **Additional setting**:
       1. For **Data localization region - optional**, choose one of Meta's regions in
          which to store your data at rest. For more information on Meta's
          data privacy policies, see [Data Privacy & Security](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/data-privacy-and-security "https://developers.facebook.com/docs/whatsapp/cloud-api/overview/data-privacy-and-security") and [Cloud API Local Storage](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage/ "https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage/") in the _WhatsApp
          Business Platform Cloud API Reference_.
       2. Tags are pairs of keys and values that you can
          optionally apply to your AWS resources to control access or
          usage. Choose **Add new tag** and enter a
          key-value pair to attach.

12. A WABA can have one message and event destination to log events for the
    WABA and all resources associated to the WABA. To enable event logging,
    including logging of receiving a customer message, turn on **Message and
    event publishing**. For more information, see [Message and event destinations in AWS End User Messaging Social](managing-event-destinations.md "managing-event-destinations.md").

###### Important

You must enable **Message and event publishing** to be able to respond to customer messages.

In the **Message and event destination details** section,
turn on **Event publishing**. 13. For **Destination type** choose either Amazon SNS or Amazon Connect

    1. To send your events to an Amazon SNS destination, enter an existing topic
     ARN in **Topic ARN**. For example IAM policies, see
     [IAM policies for Amazon SNS topics](managing-event-destinations-add.md#managing-event-destinations-sns-policies "managing-event-destinations-add.md#managing-event-destinations-sns-policies").
    2. For Amazon Connect


    	1. For **Connect instance** choose an instance from the drop down.
    	2. For **Two-way channel role**, choose either:


    		1. **Choose existing IAM role** – Choose an existing IAM policy from the **Existing IAM roles** drop down. For example IAM policies, see [IAM policies for Amazon Connect](managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies "managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies").
    		2. **Enter IAM role ARN** – Enter the ARN of the IAM policy into **Use existing IAM role Arn**. For example IAM policies, see [IAM policies for Amazon Connect](managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies "managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies").

14. To complete setup, choose **Add phone number**.
