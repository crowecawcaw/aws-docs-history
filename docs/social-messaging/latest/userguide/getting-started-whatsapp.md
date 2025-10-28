# Getting started with AWS End User Messaging Social

These topics guide you through the steps to link or migrate your WhatsApp Business Account (WABA) to
AWS End User Messaging Social.

###### Topics

- [Signing up for WhatsApp](#getting-started-embedded "#getting-started-embedded")

## Signing up for WhatsApp

A WhatsApp Business Account (WABA) allows your business to use the WhatsApp Business Platform to send messages
directly to your customers. All of your WABAs are part of your Meta business portfolio. A WABA
contains your customer facing assets, like phone number, templates, and WhatsApp Business
Profile. A WhatsApp Business Profile contains your business's contact information that users see.
For more information on WABAs, see [WhatsApp Business Account (WABA) in AWS End User Messaging Social](managing-whatsapp-waba.md "managing-whatsapp-waba.md").

Follow the steps in this section to get started with AWS End User Messaging Social. Use the embedded sign-up
process to either create a new WhatsApp Business Account (WABA) or migrate an existing WABA to AWS End User Messaging Social.

### Prerequisites

###### Important

###### Working with Meta/WhatsApp

- Your use of the WhatsApp Business Solution is subject to the terms and conditions of the
  [WhatsApp Business Terms of
  Service](https://www.whatsapp.com/legal/business-terms "https://www.whatsapp.com/legal/business-terms"), the [WhatsApp Business Solution Terms](https://www.whatsapp.com/legal/business-solution-terms "https://www.whatsapp.com/legal/business-solution-terms"), the [WhatsApp Business Messaging Policy](https://business.whatsapp.com/policy "https://business.whatsapp.com/policy"), the
  [WhatsApp Messaging
  Guidelines](https://www.whatsapp.com/legal/messaging-guidelines "https://www.whatsapp.com/legal/messaging-guidelines"), and all other terms, policies, or guidelines incorporated therein by
  reference (as each may be updated from time to time).
- Meta or WhatsApp may at any time prohibit your use of the WhatsApp Business
  Solution.
- You must create a WhatsApp Business Account ("WABA") with Meta and WhatsApp.
- You must create a Business Manager account with Meta and link it to your WABA.
- You must provide control of your WABA to us. At your request, we will transfer control
  of your WABA back to you in a reasonable and timely manner using the methods Meta makes
  available to us.
- In connection with your use of the WhatsApp Business Solution, you will not submit any
  content, information, or data that is subject to safeguarding and/or limitations on
  distribution pursuant to applicable laws and/or regulation.
- WhatsApp’s pricing for use of the WhatsApp Business Solution can be found at
  [Conversation-Based Pricing](https://developers.facebook.com/docs/whatsapp/pricing "https://developers.facebook.com/docs/whatsapp/pricing").

- To create a WhatsApp Business Account (WABA), your business needs a [Meta Business Account](https://business.facebook.com/ "https://business.facebook.com/"). Check if your company already has a Meta Business Account. If
  you don't have a Meta Business Account, you can create one during the sign-up process.
- To use a phone number that's already in use with the WhatsApp Messenger application or
  WhatsApp Business application, you must delete it first.
- A phone number that can receive either an SMS or a voice One-Time Passcode (OTP). The
  phone number used for sign-up becomes associated with your WhatsApp account and the phone
  number is used when you send messages. The phone number can still be used for SMS, MMS, and
  voice messaging.
- If you are importing an existing WABA, you need the PINs for all the phone numbers
  associated with the imported WABA. To reset a lost or forgotten PIN, follow the directions in
  [Updating PIN](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification/#updating-pin "https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification/#updating-pin") in the _WhatsApp Business Platform Cloud API
  Reference_.

The following prerequisites must be met to use either an Amazon SNS topic or Amazon Connect instance as
a message and event destination.

###### Amazon SNS topic

- An Amazon SNS topic has been [created](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") and [permissions](managing-event-destinations-add.md#managing-event-destinations-sns-policies "managing-event-destinations-add.md#managing-event-destinations-sns-policies") have been
  added.

###### Note

Amazon SNS FIFO topics are not supported.

- **(Optional)** To use an Amazon SNS topic that is encrypted
  using AWS KMS keys you have to grant AWS End User Messaging Social permissions to the [existing key policy](managing-event-destinations-add.md#managing-event-destinations-topic-policies "managing-event-destinations-add.md#managing-event-destinations-topic-policies").

###### Amazon Connect instance

- An Amazon Connect instances has been [created](../../../connect/latest/adminguide/tutorial1-set-up-your-instance.md "../../../connect/latest/adminguide/tutorial1-set-up-your-instance.md") and [permissions](managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies "managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies") have been added.

### Sign up through the console

Follow these directions to create a new WhatsApp account, migrate your existing account, or
add a phone number to an existing WABA. As part of the sign-up process, you give AWS End User Messaging Social
access to your WABA. You also allow AWS End User Messaging Social to bill you for messages. For more information
on WABAs, see [Understanding WhatsApp business account types](whatsapp-business-account.md "whatsapp-business-account.md").

1. Open the AWS End User Messaging Social console at
   [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/ "https://console.aws.amazon.com/social-messaging/").
2. Choose **Business accounts**.
3. On the **Link business account** page, choose **Launch Facebook
   portal**. A new login window from Meta will appear.
4. In the Meta login window, enter your Facebook account credentials.

On the **WhatsApp business account** page, choose **Add WhatsApp
phone number**. On the **Add WhatsApp phone number** page, choose
**Launch Facebook portal**. A new login window from Meta will appear. 5. In the Meta login window, enter your Facebook account credentials. 6. As part of the sign-up process, you give AWS End User Messaging Social access to your WhatsApp Business Account (WABA). You also
allow AWS End User Messaging Social to bill you for messages. Choose **Continue**. 7. For **Meta Business account**, choose an existing Meta business account
or **Create a Meta Business account**.

    1. (Optional) If you need to create a Meta Business account, follow these steps:
    2. For **Business name**, enter the name of your business.
    3. For **Business website or profile page**, enter either the URL for
     your company's website, or if your company doesn't have a website, enter the URL to your
     social media page.
    4. For **Country**, choose the country your business is located
     in.
    5. (Optional) Choose **Add address** and enter your business's address.

8. Choose **Next**.
9. For **Choose a WhatsApp Business Account**, choose an existing
   WhatsApp Business Account (WABA), or if you need to create an account, choose **Create a WhatsApp Business
   Account**.

For **Create or Select a WhatsApp Business Profile**, choose an existing
WhatsApp business profile, or **Create a new WhatsApp Business Profile**. 10. Choose **Next**. 11. For **Create a Business Profile**, enter the following information:

    * For **WhatsApp Business Account Name**, enter a name for your
     account. This field is not customer facing.
    * For **WhatsApp Business Profile display name**, enter the name to
     display to your customers when they receive a message from you. We recommend that you use
     your company name as the display name. The name is reviewed by Meta and must comply with
     [WhatsApp
     display name rules](https://developers.facebook.com/docs/whatsapp/guides/display-name/ "https://developers.facebook.com/docs/whatsapp/guides/display-name/"). To use a brand name that is different from your company name,
     there must be an externally published association between your company and the brand. This
     association must be displayed on your website and on the brand represented by the display
     name's website.


    Once you complete registration, Meta performs a review of your display name. Meta
     sends you an email telling you whether the display name has been approved or rejected. If
     your display name is rejected, your per day messaging limit is lowered and you could be
     disconnected from WhatsApp.


    ###### Important

    To change your display name, you have to create a ticket with Meta support.
    * For **Timezone**, choose the time zone the business is located in.
    * For **Category**, choose a category that best aligns with your
     business. Customers can view the category you as part of your contact information.
    * For **Business Description**, enter a description of your company.
     Customers can view your business description as part of your contact information.
    * For **Website**, enter your company's website. Customers can view
     your website as part of your contact information.
    * Choose **Next**.

12. For **Add a phone number for WhatsApp**, enter a phone number to
    register. This phone number is displayed to your customers when you send them a message.
13. For **Choose how you would like to verify your number**, choose either
    **Text message** or **Phone call**.
    - Once you are ready to receive the verification code, choose
      **Next**.
    - Enter the verification code, and then choose **Next**.

14. Once your number has been verified, you can choose **Next** to close the
    window from Meta.
15. For **WhatsApp business account** expand **Tags - optional** to add tags to your WhatsApp business account.

Tags are pairs of keys and values that you can optionally apply to your AWS resources to
control access or usage. Choose **Add new tag** and enter a key-value pair to
attach. 16. A WABA can have one message and event destination to log events for the WABA and all
resources associated to the WABA. To enable event logging in Amazon SNS, including logging of
receiving a customer message, you must turn on **Message and event
publishing**. For more information, see [Message and event destinations in AWS End User Messaging Social](managing-event-destinations.md "managing-event-destinations.md").

###### Important

To be able to respond to customer messages, you must enable **Message and event
publishing**.

In the **Message and event destination details** section, turn on
**Event publishing**. For Amazon SNS, choose either **New Amazon SNS standard
topic** and enter a name in **Topic name**, or choose
**Existing Amazon SNS standard topic** and choose a topic from the
**Topic arn** dropdown list. 17. Under **Phone numbers**:

For each phone number under **WhatsApp Phone numbers**:

    1. For **Phone number verification**, enter the existing PIN or enter a
     new PIN code. To reset a lost or forgotten PIN, follow the directions in [Updating PIN](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification/#updating-pin "https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification/#updating-pin") in the *WhatsApp Business Platform Cloud API
     Reference*.
    2. For **Additional setting**:


    	1. For **Data localization region - optional** choose one of Meta's
    	 regions in which to store your data at rest. For more information on Meta's data privacy policies,
    	 see [Data Privacy & Security](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/data-privacy-and-security "https://developers.facebook.com/docs/whatsapp/cloud-api/overview/data-privacy-and-security") and [Cloud
    	 API Local Storage](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage/ "https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage/") in the *WhatsApp Business Platform Cloud API
    	 Reference*.
    	2. Tags are pairs of keys and values that you can optionally apply to your AWS resources
    	 to control access or usage. Choose **Add new tag** and enter a key-value
    	 pair to attach.

18. A WABA can have one message and event destination to log events for the WABA and all
    resources associated to the WABA. To enable event logging , including logging of
    receiving a customer message, you need to turn on **Message and event
    publishing**. For more information, see [Message and event destinations in AWS End User Messaging Social](managing-event-destinations.md "managing-event-destinations.md").

###### Important

You must enable **Message and event publishing** to be able to respond to customer messages.

In the **Message and event destination details** section, turn on
**Event publishing**. 19. For **Destination type** choose either Amazon SNS or Amazon Connect

    1. To send your events to an Amazon SNS destination, enter an existing topic ARN in
     **Topic ARN**. For example IAM policies, see [IAM policies for Amazon SNS topics](managing-event-destinations-add.md#managing-event-destinations-sns-policies "managing-event-destinations-add.md#managing-event-destinations-sns-policies").
    2. For Amazon Connect


    	1. For **Connect instance** choose an instance from the drop down.
    	2. For Role ARN, choose either:


    		1. **Choose existing IAM role** – Choose an existing IAM policy from the **Existing IAM roles** drop down. For example IAM policies, see [IAM policies for Amazon Connect](managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies "managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies").
    		2. **Enter IAM role ARN** – Enter the ARN of the IAM policy into **Use existing IAM role Arn**. For example IAM policies, see [IAM policies for Amazon Connect](managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies "managing-event-destinations-add.md#managing-event-destinations-amazon-connect-policies").

20. To complete setup, choose **Add phone number**.

### Next steps

Once you've completed sign-up, you can start sending messages. When you're ready to start
sending messages at scale, complete [Business Verification](https://www.facebook.com/business/help/1095661473946872 "https://www.facebook.com/business/help/1095661473946872").
Now that your WABA and AWS End User Messaging Social accounts are linked, see the following topics:

- Learn about [event destination](managing-event-destinations.md "managing-event-destinations.md") to log events and receive incoming messages.
- Learn how to create [message templates](managing-templates.md "managing-templates.md").
- Learn how to [send a text or media message](whatsapp-send-message.md "whatsapp-send-message.md").
- Learn how to [receive a message](whatsapp-receive-message.md "whatsapp-receive-message.md").
- Learn about [Official Business Accounts](whatsapp-business-account.md "whatsapp-business-account.md") to have a green check mark beside your display name and
  increase your message throughput.
