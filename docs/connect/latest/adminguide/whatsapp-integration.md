

# Set up WhatsApp Business messaging
<a name="whatsapp-integration"></a>

The topics in this section explain how to set up and test WhatsApp Business messaging for Connect Customer. You use [AWS End User Messaging Social](https://docs.aws.amazon.com/social-messaging/latest/userguide/what-is-service.html) to link a WhatsApp Business Account and phone number to a Connect Customer instance, then import the linked phone number into Connect Customer. Customers can then use WhatsApp to send messages to your call center. 

You can also use Amazon Lex to automate responses to customer questions, which saves agents time and effort. For more information, see [Getting started with Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/getting-started.html) in the *Amazon Lex Developer Guide*.

**Topics**
+ [Prerequisites](#whatsapp-prerequisites)
+ [Step 1: Enable Connect Customer as the event destination](#enable-connect-destination)
+ [Step 2: Configure an inbound contact flow on your phone number](#inbound-contact-flow)
+ [Step 3: Send and receive test messages](#send-receive-test-messages)
+ [Next steps: Prepare to go live](#whatsapp-next-steps)
+ [Troubleshoot common problems](#whatsapp-troubleshooting)
+ [WhatsApp Business messaging capabilities and limitations with Connect Customer](whatsapp-messaging-capabilities.md)

## Prerequisites
<a name="whatsapp-prerequisites"></a>

Before you can integrate WhatsApp with Connect Customer, you must have the following items:
+ A WhatsApp Business Account.
+ A WhatsApp phone number. The number must be able to receive a voice call or an SMS text message to complete Meta's phone number verification process for WhatsApp Business messaging. You can use a Connect Customer voice number or an AWS End User Messaging SMS number for the WhatsApp phone number. You can also use a phone number that you own outside of AWS.

  When using a Connect Customer voice number or AWS End User Messaging SMS number, we recommend claiming a new number that isn’t used with live voice or SMS traffic to avoid potential disruption of service.

  You can use the AWS End User Messaging Social console at [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/) to create the WhatsApp Business Account and phone number. For more information, see [Signing up for WhatsApp](https://docs.aws.amazon.com/social-messaging/latest/userguide/getting-started.html#getting-started-embedded) in the *AWS End User Messaging Social User Guide*. 

**Important**  
WhatsApp has an automated business verification process that can take up to 2 weeks to complete. We recommend you begin this process early. WhatsApp can disable WhatsApp Business Accounts if the WhatsApp Business policy is violated or the business identity can't be verified.   
Also, we strongly recommend reviewing [Best practices for AWS End User Messaging Social](https://docs.aws.amazon.com/social-messaging/latest/userguide/best-practices.html) and [WhatsApp Best Practices](https://business.whatsapp.com/policy#best_practices) before creating and linking WhatsApp resources. 

After you create the account and phone number, complete the steps in the following sections in the order listed. 

## Step 1: Enable Connect Customer as the event destination
<a name="enable-connect-destination"></a>

The following steps explain how to use AWS End User Messaging Social to enable Connect Customer as the event destination for your linked WhatsApp Business Account. This enables the system to import your WhatsApp phone number.

 You can use the [AWS End User Messaging Social console](https://console.aws.amazon.com/social-messaging/) or the AWS CLI to complete this task. To use the AWS CLI, see [ImportPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ImportPhoneNumber.html) in the *Connect Customer API Reference*, and [PutWhatsAppBusinessAccountEventDestinations](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PutWhatsAppBusinessAccountEventDestinations.html) in the *AWS End User Messaging Social API Reference*.

The following steps explain how to use the console.

**To use the console**

1. Sign in to the AWS End User Messaging Social console at [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/).

1. In the navigation pane, choose **WhatsApp Business accounts**, then choose the desired account.

1. On the **Event destination** tab, choose **Edit destination**. 

1.  For **Destination type**, choose **Connect Customer**. 

1.  For **Connect instance**, choose your Connect Customer instance from the dropdown list. 

1.  For **Role ARN**, choose an IAM role that grants permission to deliver messages and events, and to import phone numbers. For example IAM policies, see [Add a message and event destination to AWS End User Messaging Social](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-event-destinations-add.html#managing-event-destinations-amazon-connect-policies) in the *AWS End User Messaging Social User Guide*.  

1. Choose **Save changes**.

   This starts the process of importing your phone number to Connect Customer. 

   After the operation finishes, the number appears in the Connect Customer admin website.

**To view the number**
   + In the navigation pane, choose **Channels**, then **Phone numbers**. 

     The **Active Channels** column displays **WhatsApp** for all WhatsApp numbers.   
![The Phone numbers page showing a WhatsApp number.](http://docs.aws.amazon.com/connect/latest/adminguide/images/whats-app-imported-number.png)

## Step 2: Configure an inbound contact flow on your phone number
<a name="inbound-contact-flow"></a>

You can create an inbound contact flow for use with your WhatsApp phone number, or you can reuse an existing flow. If you reuse a flow, you can add a `CheckContactAttribute` block and enable branching for the flow. With the block, you can send WhatsApp contacts to a specific queue, or take another action.

For more information about building your contact flow, including interactive messages and rich link previews, see [WhatsApp Business messaging capabilities and limitations with Connect Customer](whatsapp-messaging-capabilities.md) later in this section.

The following sets of steps explain how to configure an inbound contact flow and add a `CheckContactAttribute` block to the flow.

**To configure a flow**

1. Start the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/)

1. In the navigation pane, choose **Channels**, then **Phone numbers**. 

1. Choose the WhatsApp number, then choose **Edit**.

1. Under **Flow/IVR**, choose the flow you updated.  
![The Contact flow or IVR section of the Edit page showing a WhatsApp flow.](http://docs.aws.amazon.com/connect/latest/adminguide/images/whatsapp-flow-ivr.png)

1. Choose **Save**.

**To add the CheckContactAttribute block**

1. Follow steps 1–4 [in the previous section](#enable-connect-destination).

1. Open the **Properties** page for the flow.

1. In the **Attribute to check** section, set **Namespace** to **Segment attributes**, and **key** to **Subtype**. For more information about segment attributes, see [SegmentAttributes](ctr-data-model.md#segmentattributes), later in this guide.

1. In the **Conditions to check** section, set **condition** to **Equals** and **value** to **connect:WhatsApp**. 

1. Choose **Save**.

## Step 3: Send and receive test messages
<a name="send-receive-test-messages"></a>

In this step, you use the Contact Control Panel (CCP) and a mobile phone to send and receive WhatsApp test messages. 

**To test the integration**

1. In your CCP, set your status to **Available**. 

1. Using WhatsApp on your mobile phone, start a conversation by entering the phone number you added previously. 

   The following image shows a message with **Options**, and the resulting list of options.  
![Mobile phone screen showing an example message.](http://docs.aws.amazon.com/connect/latest/adminguide/images/whatsapp-options-results.png)

## Next steps: Prepare to go live
<a name="whatsapp-next-steps"></a>

After you test your integration, we recommend adding the following features and capabilities to your WhatsApp messaging channel. 

### Add Connect Customer features
<a name="add-features"></a>

The links in the following list take you to information about Connect Customer features that you can add to your customer and agent experiences.
+  Learn more about the [WhatsApp Business messaging capabilities and limitations with Connect Customer](whatsapp-messaging-capabilities.md). 
+  [Enable customers to resume chat conversations in Connect Customer](chat-persistence.md) – Customers can resume previous conversations with the context, metadata, and transcripts carried forward. They don't need to repeat themselves when they return to a chat, and agents have access to the entire conversation history. 
+  [Create quick responses for use with chat and email contacts in Connect Customer](create-quick-responses.md) – Provide agents with pre-written responses to common customer inquiries that they can use while they chat with customers. Quick responses make it faster for agents to respond to customers. 

### Add entry points
<a name="add-entry-points"></a>

The links in the following list take you to information about adding different types of customer entry points.
+ Entry points: [5 ways to direct leads and customers to business messaging conversations](https://business.whatsapp.com/blog/messaging-app-entry-points) (WhatsApp blog post) 
+  QR codes: [Manage your WhatsApp Business Platform QR code](https://business.facebook.com/business/help/890732351439459) (Meta help article) 
+  Choose-to-WhatsApp ads: [Create Ads that Choose to WhatsApp in Ads Manager](https://business.facebook.com/business/help/447934475640650?id=371525583593535) (Meta help article) 

### Add a display name to your phone number
<a name="add-display-name"></a>

To add a verified display name that customers see, [About WhatsApp Business display name](https://business.facebook.com/business/help/338047025165344) in the Meta help.

### Scale traffic
<a name="scale-traffic"></a>

After you onboard live traffic to your WhatsApp integration, we recommend monitoring the following quotas.

**Connect Customer quotas**  
For more information about default quotas, and about raising them, see [Connect Customer service quotas](amazon-connect-service-limits.md).
+ [Concurrent active chats per instance](amazon-connect-service-limits.md#concurrent-active-chats) quota. For information about monitoring this quota, see [Monitoring your Connect Customer instance using CloudWatch](monitoring-cloudwatch.md),
+ [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) throttling quota.
+ [SendChatIntegrationEvent](https://docs.aws.amazon.com/connect/latest/APIReference/API_SendChatIntegrationEvent.html) throttling quota.
+ `SendIntegrationEvent` throttling quota. A permission only API used by AWS End User Messaging Social to publish inbound WhatsApp events.

**End User Messaging Social quotas**  
AWS End User Messaging Social enforces rate limits on a number of messaging APIs. Monitor the following APIs to see if you need to change one or more quotas. The links take you to the *AWS End User Messaging Social API Reference*.
+  [SendWhatsAppMessage](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html)
+  [PostWhatsAppMessageMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html)
+  [GetWhatsAppMessageMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppMessageMedia.html)

For more information about increasing AWS End User Messaging Social quotas, see the following topics in the *AWS End User Messaging Social User Guide*:
+ [Quotas for AWS End User Messaging Social](https://docs.aws.amazon.com/social-messaging/latest/userguide/quotas.html)
+ [Increase messaging conversation limits in WhatsApp](https://docs.aws.amazon.com/social-messaging/latest/userguide/increase-message-limit.html)
+ [Increase message throughput in WhatsApp](https://docs.aws.amazon.com/social-messaging/latest/userguide/increase-message-throughput.html)

## Troubleshoot common problems
<a name="whatsapp-troubleshooting"></a>

Use the following information to troubleshoot common problems with a WhatsApp integration.

**Topics**
+ [Unable to see imported phone numbers in your Connect Customer instance](#no-imported-number)
+ [Inbound messages from customers are not delivered](#whatsapp-messages-not-delivered)

### Unable to see imported phone numbers in your Connect Customer instance
<a name="no-imported-number"></a>

If your imported number fails to appear in the Connect Customer admin website, follow these steps:
+ Make sure that the event destination IAM role has the necessary permissions. For more information, see [Step 1: Enable Connect Customer as the event destination](#enable-connect-destination).
+ See if your *Phone numbers per instance* quota needs to be raised. For more information, see [Connect Customer service quotas](amazon-connect-service-limits.md).
+ To reassign a linked WhatsApp Business Account to a different Connect Customer instance, you must first release the imported phone numbers from the original Connect Customer instance. After the phone numbers are released, you can update the event destination on your linked WhatsApp Business Account to another Connect Customer instance.
**Important**  
Do not release numbers that handle live customer traffic. Instead, [claim new phone numbers](https://docs.aws.amazon.com/connect/latest/adminguide/claim-and-manage-phonenumbers.html).
+ To help determine the cause of the import issue, search your CloudTrail logs for `ImportPhoneNumber` events and check for error details. If the `ImportPhoneNumber` call succeeds, you can call `DescribePhoneNumber` for other error details.

If you made a fix, you must import the phone numbers again. To do this, repeat [Step 1: Enable Connect Customer as the event destination](#enable-connect-destination).

### Inbound messages from customers are not delivered
<a name="whatsapp-messages-not-delivered"></a>

If WhatsApp inbound message delivery stops, search your AWS CloudTrail logs for `SendIntegrationEvent` and `SendChatIntegrationEvent` for error details.

You can also check these common scenarios:
+ Make sure that your linked WhatsApp Business Account in AWS End User Messaging Social has a Connect Customer event destination enabled.
+ Ensure your event destination IAM role has the necessary permissions. For more information, see [Step 1: Enable Connect Customer as the event destination](#enable-connect-destination) earlier in this section. You have a misconfigured role if CloudTrail throws `AccessDeniedException` errors from the `SendIntegrationEvent` API. 
+ Make sure that your WhatsApp phone number imported successfully to your Connect Customer instance, and that the number has an associated inbound contact flow. For more information, see [Step 2: Configure an inbound contact flow on your phone number](#inbound-contact-flow).
+ Inbound messages were dropped because they are not yet supported. For more information, see [WhatsApp Business messaging capabilities and limitations with Connect Customer](whatsapp-messaging-capabilities.md). 