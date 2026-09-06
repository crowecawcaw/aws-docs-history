

# Sending messages with Notify
<a name="notify-send-messages"></a>

Notify provides two APIs for sending messages:
+ `SendNotifyTextMessage` – Sends an SMS message using a pre-approved template.
+ `SendNotifyVoiceMessage` – Sends a voice call that reads the template content using text-to-speech.

## Sending an SMS message
<a name="notify-send-text"></a>

------
#### [ Console ]

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to a Notify configuration and choose the **Test** tab.

1. For channel, select **Text**.

1. Select a template from the templates table.

1. Enter the destination phone number in E.164 format.

1. Fill in the template variables.

1. Choose **Send**.

------
#### [ AWS CLI ]

```
aws pinpoint-sms-voice-v2 send-notify-text-message \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --destination-phone-number {{+12065550100}} \
  --template-id {{notify-code-verification-english-001}} \
  --template-variables '{"code":"123456"}'
```

------
#### [ Python (boto3) ]

```
import boto3

client = boto3.client('pinpoint-sms-voice-v2')

response = client.send_notify_text_message(
    NotifyConfigurationId='nc-1234567890abcdef0',
    DestinationPhoneNumber='+12065550100',
    TemplateId='notify-code-verification-english-001',
    TemplateVariables={
        'code': '123456'
    }
)

print(f"Message sent. MessageId: {response['MessageId']}")
print(f"Resolved body: {response.get('ResolvedMessageBody')}")
```

------

## Sending a voice message
<a name="notify-send-voice"></a>

Voice messages require the `VOICE` channel to be enabled on your Notify configuration.

**Tip**  
For voice messages, separate digits with periods or spaces (for example, `"1. 2. 3. 4. 5. 6."`) so that the text-to-speech engine reads each digit individually instead of as a single number.

------
#### [ Console ]

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to a Notify configuration and choose the **Test** tab.

1. For channel, select **Voice**.

1. Select a voice template from the templates table.

1. Enter the destination phone number and fill in template variables.

1. Choose **Send**.

------
#### [ AWS CLI ]

```
aws pinpoint-sms-voice-v2 send-notify-voice-message \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --destination-phone-number {{+12065550100}} \
  --template-id {{notify-code-verification-english-001}} \
  --template-variables '{"code":"123456"}' \
  --voice-id JOANNA
```

------

## Using DryRun mode
<a name="notify-send-dryrun"></a>

Set `DryRun` to `true` to validate a send request without actually delivering the message. DryRun mode checks template variable validation, country restrictions, and spend limits, but does not send the message or deduct from your spend limit.

```
aws pinpoint-sms-voice-v2 send-notify-text-message \
  --notify-configuration-id {{nc-1234567890abcdef0}} \
  --destination-phone-number {{+12065550100}} \
  --template-id {{notify-code-verification-english-001}} \
  --template-variables '{"code":"123456"}' \
  --dry-run
```

## Send request parameters
<a name="notify-send-parameters"></a>

Both `SendNotifyTextMessage` and `SendNotifyVoiceMessage` accept the following parameters:

NotifyConfigurationId (required)  
The ID or ARN of the Notify configuration.

DestinationPhoneNumber (required)  
The recipient's phone number in E.164 format.

TemplateVariables (required)  
A map of variable names to values. All values are strings, even for integer or boolean variables.

TemplateId  
The template to use. If omitted, the configuration's default template is used.

ConfigurationSetName  
A configuration set for event routing.

Context  
Key-value pairs included in event records.

DryRun  
Validates the request without sending.

TimeToLive  
How long the message is valid, in seconds. Default is 72 hours.

MessageFeedbackEnabled  
Enables message feedback tracking via the `PutMessageFeedback` API.

VoiceId (voice only)  
The Amazon Polly voice to use (for example, `JOANNA`, `MATTHEW`).

## How message routing works
<a name="notify-send-routing"></a>

AWS automatically selects the best origination identity for each message based on the destination country. If you have associated a phone pool with your Notify configuration, customer-owned identities in the pool are tried first. If no suitable customer-owned identity is available, AWS-managed identities are used as a fallback.

## Message feedback
<a name="notify-send-feedback"></a>

If you enable `MessageFeedbackEnabled` when sending a message, you can report whether the end user successfully received and used the code:

```
client.put_message_feedback(
    MessageId='{{msg-1234567890abcdef}}',
    MessageFeedbackStatus='RECEIVED'  # or 'FAILED'
)
```

## Delivery events
<a name="notify-send-delivery-events"></a>

Notify emits delivery events to your configured event destinations (CloudWatch, Amazon Data Firehose, or Amazon SNS). For information about setting up event destinations, see [Configuration sets in AWS End User Messaging SMS](configuration-sets.md).


**Delivery event types**  

| Event | Description | 
| --- | --- | 
| PENDING | Message is queued for delivery. | 
| DELIVERED | Message was delivered to the recipient's device. | 
| FAILED | Message delivery failed. Check the failure reason for details. | 
| BLOCKED | Message was blocked by Protect configuration rules. | 

## Error handling
<a name="notify-send-errors"></a>

ValidationException  
Missing or invalid template variables, invalid phone number format, or destination country not enabled on the configuration.

ResourceNotFoundException  
The Notify configuration or template was not found.

ServiceQuotaExceededException  
Daily message limit (Basic tier) or monthly spend limit reached.

ConflictException  
The Notify configuration is not in `ACTIVE` status.

## Important notes
<a name="notify-send-important-notes"></a>
+ **Two-way messaging** – Two-way messaging is not supported when using AWS-managed origination identities. If you need two-way messaging, associate your own phone pool. See [Using dedicated numbers with Notify](notify-dedicated-numbers.md).
+ **Opt-out behavior** – For OTP use cases with AWS-managed identities, STOP keyword responses are informational only. No persistent opt-out list is maintained because each OTP request is an implicit opt-in. If you associate your own phone pool, the pool's opt-out list is respected.

## Troubleshooting
<a name="notify-send-troubleshooting"></a>

**Messages not delivering**  
If your messages are not being delivered, verify the following:

1. Verify the destination phone number is in E.164 format (starts with `+` and country code).

1. Check that the destination country is in your `EnabledCountries` list.

1. Verify your configuration status is `ACTIVE`.

1. Check your spend limit hasn't been exceeded.

**BLOCKED status**  
The message was blocked by a Protect configuration. Common reasons include the destination country not being in your enabled countries list, or the message being flagged as potential AIT (artificially inflated traffic).

**Validation errors**  
Ensure all required `TemplateVariables` are provided. Check that variable values match their declared types (for example, integers are valid numbers). Verify the template ID exists and is active.