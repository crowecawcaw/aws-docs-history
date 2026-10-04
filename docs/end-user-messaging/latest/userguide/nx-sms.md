

# Setup SMS
<a name="nx-sms"></a>

SMS (Short Message Service) is a text messaging channel that reaches recipients on virtually any mobile device, with no app or data connection required, in over 200 countries and regions. Common use cases include one-time passcodes and account verification, transactional notifications such as order confirmations and appointment reminders, time-sensitive alerts, and two-way conversations where customers reply to your messages.

You send SMS with the AWS End User Messaging SMS and Voice v2 API (the `sms-voice` namespace, which you call as `aws pinpoint-sms-voice-v2` on the AWS CLI). The main send operation is `SendTextMessage`, which sends a text message to a single destination phone number from one of your origination identities. The same API provisions phone numbers, groups them into pools, and configures the event destinations that track delivery.

**Key concepts**

The following concepts are central to sending SMS with AWS End User Messaging.


| Concept | Description | 
| --- | --- | 
| Origination identity | The phone number (long code, toll-free, short code, or 10DLC) or sender ID that a message is sent from. The types available to you depend on the destination country and its regulations. | 
| Phone pool | A collection of origination identities that share the same settings. When you send through a pool, AWS End User Messaging selects an identity and fails over to another if one is unavailable, which improves the resilience of your messaging. | 
| Configuration set | A set of rules applied to the messages you send, including where to send delivery and engagement events, such as CloudWatch, Amazon SNS, or Amazon Data Firehose. | 
| Sandbox | The restricted environment a new account starts in, where you send only to verified destination numbers while you build and test. You request production access to lift the restrictions. | 
| Opt-out list | A list of destination numbers that have opted out. AWS End User Messaging does not send to a number while it is on an opt-out list, which helps you meet carrier and regulatory requirements. | 
| Registration | The approval process many countries require before you can send, such as 10DLC in the United States or sender ID registration elsewhere. | 

**How this guide is organized**

This chapter walks you through SMS from first setup to scaling in production. Use the following table to find where to start.


| Section | What you'll do | Start here if | 
| --- | --- | --- | 
| [How to get set up](nx-sms-get-set-up.md) | Set up an origination identity, group it into a pool, create a configuration set, and send a test message. | You are new to SMS and want a working test send. | 
| [Send a message](nx-sms-send.md) | Send messages from your application and set up two-way messaging to receive replies. | You have an origination identity and want to send from your own code. | 
| [Scale](nx-sms-scale.md) | Move out of the sandbox, monitor delivery, manage spending and quotas, and apply sending best practices. | You are sending in production and want to keep it healthy and grow. | 
| [Launch in a country](nx-sms-country-support.md) | Review the origination identity types, registration requirements, and features supported in each country. | You need the rules for a specific destination country. | 