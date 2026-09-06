

# Send communication
<a name="journey-flow-block-send-communication"></a>

**Important**  
Before using this block, make sure you completed [channel configuration](how-to-create-campaigns.md) including claimed phone numbers for agent assisted voice or automated voice, claim a phone number or originating identity in AWS End User Messaging SMS and then import the number into Amazon Connect for SMS or WhatsApp, and enabled email at Amazon Connect instance. For instructions, see [Set up SMS messaging](setup-sms-messaging.md), [Enable email campaigns](enable-email.md).

## Description
<a name="journey-flow-block-send-communication-description"></a>

Use this block to send communications through channels such as voice, SMS, WhatsApp, or email. Before using this block, ensure channel setup is complete:
+ Voice: Claim phone numbers for automated or agent-assisted calls.
+ SMS / WhatsApp: Claim numbers or originating identities in AWS End User Messaging, then import them into Connect.
+ Email: Enable email campaigns in your Connect instance.

**Example use cases**
+ Send onboarding, appointment reminder, or promotional messages.
+ Trigger fallback logic to reach a customer on another channel when a prior attempt fails.

## Contact types
<a name="journey-flow-block-send-communication-channels"></a>


| Contact type | Supported? | 
| --- | --- | 
| Voice | Yes | 
| SMS | Yes | 
| WhatsApp | Yes | 
| Email | Yes | 
| Custom channel | Yes, through Custom action | 

## How to configure this block
<a name="journey-flow-block-send-communication-configure"></a>

You configure the **Send communication** block in one of two ways:
+ **Amazon Connect admin website**: Open the block in the journey flow designer and set its properties on the block's properties page. The available properties depend on the channel you send on. For the fields shared across channels, see [Common properties](#journey-flow-block-send-communication-common-properties). For channel-specific fields, see [Send an SMS (text message)](#journey-flow-block-send-communication-sms), [Send an email](#journey-flow-block-send-communication-email), and [Voice call](#journey-flow-block-send-communication-voice).
+ **Flow language**: Define the block programmatically with the `SendCommunication` action in your flow's JSON. The action parameters map to the same properties described in the following sections.

### Common properties
<a name="journey-flow-block-send-communication-common-properties"></a>


| Property | Description | 
| --- | --- | 
| From | Select the originating phone number or email address claimed for your instance. You can set this value manually or dynamically using an attribute. | 
| Message template (non-voice) | Choose a predefined template for SMS, WhatsApp, or email. | 
| Template alias / version | Select a specific version or alias of the message template. | 
| Store outbound communication | Optionally save the outbound message ID in flow attributes for delivery tracking. | 
| Dial criteria (voice) | Specify dialing behavior or targeting logic for voice calls. | 
| Engagement preference (voice) | Define how to prioritize multiple contact numbers per customer. | 

## Send an SMS (text message)
<a name="journey-flow-block-send-communication-sms"></a>

Configure the following properties on the page to send an SMS message:
+ **From**: The phone number that the message is to be sent from. The dropdown menu shows a list of phone numbers that are claimed for your Amazon Connect instance.
  + **Set manually**: Use the dropdown menu to select a phone number claimed for your Amazon Connect instance.
  + **Set dynamically**: Enter an attribute based on a **Namespace** and **Key** that points to the ARN of a phone number claimed for your Amazon Connect instance.
+ **Message template**: Use the dropdown menu to choose from a list of SMS templates. You can choose one template to be sent to the customer.
+ **Template alias or version**: Use the dropdown menu to choose a different SMS template alias or version.
+ **Store outbound communication**: You can choose to store outbound communication in flow attributes. By saving the outbound message ID in a flow attribute, you can track its delivery status.

## Send a WhatsApp message
<a name="journey-flow-block-send-communication-whatsapp"></a>

Configure the following properties on the page to send a WhatsApp message:
+ **From**: The phone number that the message is to be sent from. The dropdown menu shows a list of WhatsApp numbers that are imported into your Amazon Connect instance.
  + **Set manually**: Use the dropdown menu to select a WhatsApp number imported into your Amazon Connect instance.
  + **Set dynamically**: Enter an attribute based on a **Namespace** and **Key** that points to the ARN of a WhatsApp number imported into your Amazon Connect instance.
+ **Message template**: Use the dropdown menu to choose from a list of WhatsApp templates. You can choose one template to be sent to the customer.
+ **Template alias or version**: Use the dropdown menu to choose a different WhatsApp template alias or version.
+ **Store outbound communication**: You can choose to store outbound communication in flow attributes. By saving the outbound message ID in a flow attribute, you can track its delivery status.

## Send an email
<a name="journey-flow-block-send-communication-email"></a>

Configure the following properties on the page to send an email message:
+ **From**: The email address that the message is to be sent from. The dropdown menu shows a list of email addresses that are configured for your Amazon Connect instance.
  + **Set manually**: Use the dropdown menu to select an email address configured for your Amazon Connect instance.
  + **Set dynamically**: Enter an attribute based on a **Namespace** and **Key** that points to an email address configured for your Amazon Connect instance.
+ **Display name**: Personalize how your email address appears to your customers in their inbox.
  + **Set manually**: Enter the display name directly.
  + **Set dynamically**: Enter an attribute based on a **Namespace** and **Key**.
+ **Message template**: Use the dropdown menu to choose from a list of email templates. You can choose one template to be sent to the customer.
+ **Template alias or version**: Use the dropdown menu to choose different email template alias or version.
+ **Store outbound communication**: You can choose to store outbound communication in flow attributes. By saving the outbound message ID in a flow attribute, you can track its delivery status.

## Voice call
<a name="journey-flow-block-send-communication-voice"></a>

Configure the following properties on the page to use outbound voice channel:
+ **From**: The phone number that the voice call is to be made from. The dropdown menu shows a list of phone numbers that are claimed for your Amazon Connect instance.
  + **Set manually**: Use the dropdown menu to select a phone number claimed for your Amazon Connect instance.
  + **Set dynamically**: Enter an attribute based on a **Namespace** and **Key** that points to the phone number address (in E.164 format — for example, `+12025551234`) of a phone number claimed for your Amazon Connect instance. For voice, use the address, not the phone number ARN or ID.
+ **Dial criteria**: Configure how the voice call should be handled based on detection criteria. Use the dropdown to choose a segment that the voice call will target for.
+ **Engagement preference**: If your contact list includes single account with more than 1 profile, such as joint account holders, and 1 profile could have more than 1 phone number, you can use engagement preference to set contact strategy based on preference.
+ **Store outbound communication**: You can choose to store outbound communication in flow attributes. By saving the outbound message ID in a flow attribute, you can track its delivery status.

## How to set From dynamically with Lambda
<a name="journey-flow-block-send-communication-dynamic-from-lambda"></a>

**Pricing**  
Custom action channel and Lambda pricing will apply.

You can use an **Invoke Lambda** block earlier in the journey flow to determine the source phone number or email address at runtime. The **Send communication** block then references the returned value dynamically.

### How it works
<a name="journey-flow-block-send-communication-dynamic-from-lambda-how"></a>

1. Add a [**Custom action (Invoke Lambda)**](journey-flow-block-custom-action.md) block before the **Send communication** block in your journey flow.

1. The Lambda function runs and returns a JSON response that includes the source value in a key of your choice. The expected format depends on the channel: for a voice call, return the phone number address in E.164 format; for SMS or WhatsApp, return the phone number ARN; for email, return the email address. For example, for a voice call:

   ```
   {
     "sourcePhoneNumber": "+12025551234"
   }
   ```

1. The returned value becomes available in the flow at `$.LambdaInvocation.ResultData.{{key}}`. In this example, the value is at `$.LambdaInvocation.ResultData.sourcePhoneNumber`.

1. In the **Send communication** block, set the **From** field to **Set dynamically** and reference the Lambda output. Set the **Namespace** to `Lambda invocation` and the **Key** to the field name your Lambda returns.  
![The From field set dynamically with Namespace set to Lambda invocation, Key set to Result data, and Attribute set to sourcePhoneNumber.](http://docs.aws.amazon.com/connect/latest/adminguide/images/send-communication-dynamic-from-lambda.png)

Your Lambda function can use any logic to determine the source address. Use any field name in the Lambda response, as long as it matches what you specify in the **From** field's dynamic reference.