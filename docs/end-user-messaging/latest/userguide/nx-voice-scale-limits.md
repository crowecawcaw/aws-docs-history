

# Limits and quotas
<a name="nx-voice-scale-limits"></a>

AWS End User Messaging applies limits and quotas to voice messaging. Some limits are fixed and some are account quotas that you can request to increase through Service Quotas. This topic describes the limits that apply to voice messages and how to request increases.

## Voice message length
<a name="nx-voice-scale-limits-message-length"></a>

When you send a voice message with the `SendVoiceMessage` API, the `MessageBody` that AWS End User Messaging converts to speech is limited by the body type. For a plain text message body, the maximum length is 3,000 characters. For a message body that uses Speech Synthesis Markup Language (SSML), the maximum length is 6,000 characters, which includes the SSML tags.

## Calls per second and concurrent calls
<a name="nx-voice-scale-limits-throughput"></a>

AWS End User Messaging limits how fast you can originate voice calls and how many calls your account can have in progress at the same time. These are account quotas that are visible and, where supported, adjustable in the Service Quotas console.
+ **Calls per second** — the maximum number of voice messages that your account can originate each second. The default value is [needs SME confirmation].
+ **Concurrent calls** — the maximum number of voice calls that your account can have in progress at the same time. The default value is [needs SME confirmation].

**Note**  
While your account is in the voice sandbox, additional restrictions apply. For more information, see [Move out of the sandbox](nx-voice-scale-sandbox.md).

## Request a quota increase
<a name="nx-voice-scale-limits-request-increase"></a>

For account quotas that support adjustment, you can request an increase in the Service Quotas console.

**To request a voice quota increase**

1. Sign in to the AWS Management Console and open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **AWS Services**.

1. Choose AWS End User Messaging from the list, or search for it in the search box.

1. Choose the voice quota that you want to change, and then choose **Request increase at account level**.

1. For the increased quota value, enter the new value. The new value must be greater than the current value, and then choose **Request**.