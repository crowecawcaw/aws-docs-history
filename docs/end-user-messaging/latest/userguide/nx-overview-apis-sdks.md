

# APIs and SDKs
<a name="nx-overview-apis-sdks"></a>

AWS End User Messaging is a family of APIs rather than a single API. Each channel group has its own API, and you choose the one that matches the service and features you want to use. The channel-level APIs give you direct control over sending and managing resources for a specific channel, and a top-level AWS End User Messaging API lets you orchestrate across channels, so you can manage shared resources such as brand profiles and coordinate how your brand sends across SMS, RCS, and the other channels from one place. You can call every AWS End User Messaging API through the AWS Management Console, the AWS AWS CLI, the AWS SDKs for your programming language, and the AWS Tools for PowerShell.

## The AWS End User Messaging APIs
<a name="nx-overview-apis-sdks-apis"></a>

The following table lists the AWS End User Messaging APIs and what each one manages.


| API | AWS CLI command | What it manages | API reference | 
| --- | --- | --- | --- | 
| AWS End User Messaging SMS and Voice, version 2 | `aws pinpoint-sms-voice-v2` | Phone numbers, sender IDs, phone pools, opt-out lists, and configuration sets, and sending SMS, MMS, voice, and RCS messages. Also manages Notify configurations. | [SMS and Voice v2 API Reference](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/Welcome.html) | 
| AWS End User Messaging Social | `aws socialmessaging` | WhatsApp, including linking a WhatsApp Business Account, managing message templates, and sending WhatsApp messages. | [Social Messaging API Reference](https://docs.aws.amazon.com/social-messaging/latest/APIReference/Welcome.html) | 
| AWS End User Messaging Push | `aws pinpoint` | Push notifications through Apple Push Notification service (APNs), Firebase Cloud Messaging (FCM), Amazon Device Messaging (ADM), and Baidu Cloud Push, including applications, channels, and endpoints. | [Amazon Pinpoint API Reference](https://docs.aws.amazon.com/pinpoint/latest/apireference/Welcome.html) | 
| AWS End User Messaging | `aws endusermessaging` | Brand profiles and Notify code configurations, and syncing brand profile data with SMS and RCS registrations. | [AWS End User Messaging API Reference](https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/Welcome.html) | 

## Using each service programmatically
<a name="nx-overview-apis-sdks-by-service"></a>

Use the following API for each service and its features.

### SMS, MMS, voice, and RCS
<a name="nx-overview-apis-sdks-sms-voice"></a>

Use the `pinpoint-sms-voice-v2` APIs to provision and manage the identities you send from and to send messages. This API covers phone numbers, sender IDs, phone pools, opt-out lists, and configuration sets, and the operations that send SMS, MMS, voice, and RCS messages. For example, you send a text message with `send-text-message` and send an RCS message with `send-text-message` using an RCS-capable phone pool.

### Notify
<a name="nx-overview-apis-sdks-notify"></a>

Notify spans two APIs that play different roles. The Notify configuration is the shared resource that holds the origination identities and settings Notify sends from, and you manage it with the `pinpoint-sms-voice-v2` API using `create-notify-configuration`. The Notify code configuration is where you set the policy for how passcodes are generated and validated, such as code length and validity period. You manage it, and send and validate passcodes, with the `endusermessaging` API using operations such as `create-notify-code-configuration`, `send-notify-code-verification`, and `validate-notify-code-verification`.

### Brand profiles
<a name="nx-overview-apis-sdks-brand-profiles"></a>

Use the `endusermessaging` APIs to create and manage brand profiles and their attributes, and to sync brand profile data with registrations. For example, you create a brand profile with `create-brand-profile` and create registrations from a profile with `create-registrations-from-brand-profile`.

### WhatsApp
<a name="nx-overview-apis-sdks-whatsapp"></a>

Use the `socialmessaging` APIs to link a WhatsApp Business Account, manage message templates, and send WhatsApp messages. For example, you send a message with `send-whatsapp-message`.

### Push notifications
<a name="nx-overview-apis-sdks-push"></a>

Use the `pinpoint` API to send push notifications through APNs, FCM, ADM, and Baidu Cloud Push. You create an application, configure the push channels you use, register device endpoints, and send messages to those endpoints.

## Accessing the APIs with SDKs, the AWS CLI, and PowerShell
<a name="nx-overview-apis-sdks-access"></a>

You can call any of the AWS End User Messaging APIs in the following ways:
+ **AWS SDKs** – Use an AWS SDK to call the APIs from your application in a supported programming language, such as Java, Python, JavaScript, .NET, Go, and others. The SDK handles request signing, retries, and error handling for you. For the list of available SDKs, see [Tools to Build on AWS](https://aws.amazon.com/developer/tools/).
+ **AWS AWS CLI** – Use the AWS CLI to call the APIs from the command line or from scripts. For more information, see the [AWSAWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/).
+ **AWS Tools for PowerShell** – Use the Tools for PowerShell to call the APIs from PowerShell scripts. For more information, see the [AWS Tools for PowerShell Cmdlet Reference](https://docs.aws.amazon.com/powershell/latest/reference/).