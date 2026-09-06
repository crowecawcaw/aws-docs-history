

# What is AWS End User Messaging Notify?
<a name="notify"></a>

AWS End User Messaging Notify is a templated messaging feature that enables you to send SMS and voice messages using AWS-managed identities and pre-approved templates. With Notify, you can start sending code verification messages in minutes without provisioning phone numbers, managing sender IDs, or navigating carrier registration processes.

**Note**  
Notify is a feature of AWS End User Messaging SMS and uses the `pinpoint-sms-voice-v2` API namespace. For general information about AWS End User Messaging SMS, see [What is AWS End User Messaging SMS?](what-is-sms-mms.md).

**Key benefits**  
Notify provides instant messaging access with no phone number provisioning or carrier registration wait times. AWS manages phone number pools, sender IDs, and carrier integrations on your behalf. Pre-approved code verification templates are provided with multi-language support built in. Mandatory SMS Protect integration filters artificially inflated traffic (AIT) and SMS pumping attacks. You can send messages with a single API call using your configuration ID, destination number, and template variables.

**How Notify works**  
Sending a message with Notify involves these steps: (1) Create a Notify configuration with your brand's display name, use case, and channels. AWS automatically validates your account, configures fraud protection, assigns templates, and sets tier-appropriate limits. (2) Browse pre-approved templates using `DescribeNotifyTemplates` to find templates for your tier, channel, and language. (3) Send messages using `SendNotifyTextMessage` or `SendNotifyVoiceMessage` with your configuration ID, destination phone number, and template variables. AWS selects the appropriate identity, resolves the template, and delivers the message. (4) Receive delivery receipts and status updates through your configured event destinations. (5) Optionally call `PutMessageFeedback` to report whether the end user successfully received and used the verification code.

**Note**  
Before sending messages with Notify, ensure you have met the mobile carrier prerequisites for terms, privacy, and opt-in. For more information, see [Notify mobile carrier prerequisites](notify-compliance.md).

**Notify vs. standard SMS sending**  
Use Notify when you need to send OTP or verification codes and want AWS to manage identities, routing, and compliance. Use standard AWS End User Messaging SMS sending (`SendTextMessage`, `SendVoiceMessage`) when you need custom message bodies, marketing or promotional messages, MMS messaging, or full control over which origination identity sends each message.


**Notify vs. standard SMS sending**  

| Feature | Standard SMS | Notify | 
| --- | --- | --- | 
| Phone number provisioning | Required | Not required | 
| Number registration | Customer responsibility | AWS-managed | 
| Time to first message | Days to weeks | Minutes | 
| Message templates | Customer-managed | Pre-approved, AWS-managed | 
| Fraud protection | Optional | Mandatory | 
| Identity management | Customer-managed | AWS-managed | 
| Routing logic | Customer-managed | AWS-managed | 

**Key concepts**  
A *Notify configuration* is the primary resource representing your brand identity and messaging settings, including your display name, use case, enabled channels, enabled countries, and tier. Notify offers two service *tiers*: Basic tier provides immediate access with conservative limits, and Advanced tier unlocks higher limits and premium identities after brand verification. *Templates* are pre-approved message templates for code verification with multi-language support and typed variable substitution. Notify supports SMS and VOICE *channels*. *AWS-managed identities* are shared pools of phone numbers maintained by AWS across regions that Notify automatically selects based on destination country and channel. Each Notify configuration has a service-managed *Protect configuration* that enforces country-level restrictions and artificially inflated traffic filtering, managed by AWS and not modifiable by customers.

**Accessing Notify**  
You can use Notify through the AWS End User Messaging SMS console, the AWS CLI, or the AWS SDKs. For information about accessing the console, see [Accessing AWS End User Messaging SMS](what-is-sms-mms.md#acessing-servicename).

**Pricing**  
Notify pricing includes a per-message Notify service fee and standard SMS or voice transport rates based on destination country. For pricing details, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

**Regional availability**  
Notify is available in the same AWS Regions as AWS End User Messaging SMS. For a list of supported Regions, see [Regional availability](what-is-sms-mms.md#sms-regions).

**Topics**
+ [Getting started with Notify](notify-getting-started.md)
+ [Managing Notify configurations](notify-configurations.md)
+ [Working with Notify templates](notify-templates.md)
+ [Notify tiers](notify-tiers.md)
+ [Sending messages with Notify](notify-send-messages.md)
+ [Using dedicated numbers with Notify](notify-dedicated-numbers.md)
+ [Notify supported countries](notify-countries.md)
+ [Notify spend limits](notify-spend-limits.md)
+ [Notify quotas and limits](notify-quotas.md)
+ [Notify mobile carrier prerequisites](notify-compliance.md)