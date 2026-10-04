

# Send a message
<a name="nx-notify-send"></a>

Notify sends templated one-time passcode (OTP) and verification messages over SMS and voice. You send a message by supplying your Notify configuration, a destination phone number in E.164 format, a pre-approved template, and the template variable values to substitute. How you send depends on whether you generate the passcode yourself or let AWS End User Messaging generate and validate it.

## API operations
<a name="nx-notify-send-operations"></a>

Use the following API operations to send Notify messages.


**API operations**  

| Operation | Description | Use for | 
| --- | --- | --- | 
| `SendNotifyTextMessage` | Sends an SMS message from a pre-approved template; you supply the code. | You generate the code (SMS). | 
| `SendNotifyVoiceMessage` | Places a voice call that reads a template with text-to-speech; you supply the code. | You generate the code (voice). | 
| `SendNotifyCodeVerification` | AWS End User Messaging generates and sends the passcode from a code configuration. | AWS End User Messaging generates the code. | 
| `ValidateNotifyCodeVerification` | Validates the passcode the recipient entered. | AWS End User Messaging validates the code. | 

## Types of send
<a name="nx-notify-send-types"></a>

Notify provides two ways to send a verification message, which differ in who generates the one-time passcode.


**Types of send**  

| Type | How it works | 
| --- | --- | 
| You generate the code | Use the SMS and Voice v2 API (the `sms-voice` namespace) operations `SendNotifyTextMessage` and `SendNotifyVoiceMessage`. You create the passcode in your own application and pass it in the template variables, and Notify delivers it over AWS-managed origination identities using a pre-approved template. | 
| AWS End User Messaging generates and validates the code | Use the `endusermessaging` namespace operations `SendNotifyCodeVerification` and `ValidateNotifyCodeVerification`, backed by a Notify code configuration that defines the code-generation and validation policy such as code length and validity period. AWS End User Messaging generates the passcode, sends it, and validates the code the recipient enters. | 

For full send detail and code examples, see [Send OTP code](nx-notify-send-outbound.md).

## In this section
<a name="nx-notify-send-in-section"></a>



|  |  | 
| --- |--- |
| [Send OTP code](nx-notify-send-outbound.md) | Choose a template and send a one-time passcode over SMS or voice, whether you generate the code or AWS End User Messaging generates it. | 
| [Validate OTP code](nx-notify-send-validate.md) | Validate the passcode the recipient entered, when AWS End User Messaging generated the code. | 