

# Setup Notify
<a name="nx-notify"></a>

Notify is a managed feature of AWS End User Messaging for sending one-time passcode (OTP) and verification messages over SMS and voice. AWS manages the origination identities, carrier integrations, and pre-approved templates, so you can start sending verification messages in minutes without provisioning phone numbers or navigating carrier registration. Every Notify configuration includes mandatory fraud protection that filters artificially inflated traffic (AIT). Common use cases include sign-up and login verification, transaction authentication, and account recovery.

Notify provides two ways to send a verification message, which differ in who generates the one-time passcode:
+ **You generate the code.** Use the SMS and Voice v2 API (the `sms-voice` namespace) operations `SendNotifyTextMessage` and `SendNotifyVoiceMessage`. You create the passcode in your own application and pass it to Notify, which delivers it over AWS-managed origination identities using a pre-approved template.
+ **AWS End User Messaging generates and validates the code.** Use the `endusermessaging` API operations `SendNotifyCodeVerification` and `ValidateNotifyCodeVerification`, backed by a Notify code configuration that defines the code-generation and validation policy, such as code length and validity period. AWS End User Messaging generates the passcode, sends it, and validates the code the recipient enters.

**Key concepts**


| Concept | Description | 
| --- | --- | 
| Notify configuration | The central Notify resource that holds your brand identity and messaging settings, including the display name, use case, and enabled channels and countries. | 
| Notify code configuration | A reusable policy for AWS-generated passcodes, defining code length and validity period, used by `SendNotifyCodeVerification` and `ValidateNotifyCodeVerification`. | 
| Template | An AWS-managed, pre-approved message template for OTP and verification messages, pre-validated across supported countries with multi-language support. You select a template but do not create or modify one. | 
| Service tier | Notify offers a Basic tier with immediate access and conservative limits, and an Advanced tier with higher limits and more countries after you complete tier upgrade verification. | 
| AIT protection | Mandatory fraud protection included with every Notify configuration that filters artificially inflated traffic. | 

**How this guide is organized**

Use the following table to find where to start.


| Section | What you'll do | Start here if | 
| --- | --- | --- | 
| [How to get set up](nx-notify-get-set-up.md) | Create a Notify configuration, choose your sending mode, and send a test verification message. | You are new to Notify and want a working test send. | 
| [Send a message](nx-notify-send.md) | Send OTP and verification messages from your application over SMS and voice. | You have a Notify configuration and want to send from your own code. | 
| [Scale](nx-notify-scale.md) | Upgrade to the Advanced tier, monitor delivery, and manage spending and the carrier compliance prerequisites. | You are sending in production and want higher limits and more countries. | 

**Note**  
Before you send messages with Notify, complete the mobile carrier prerequisites for terms, privacy, and opt-in described in the Compliance section of [Scale](nx-notify-scale.md).