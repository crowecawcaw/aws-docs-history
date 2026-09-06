

# Enable in-flight sensitive data redaction and message processing
<a name="redaction-message-processing"></a>

Connect Customer supports message processing that intercepts and modifies chat messages before they reach any participant. This capability enables automatic redaction of sensitive data and custom message processing, helping businesses maintain compliance and security standards.

## Processing options
<a name="redaction-message-processing-options"></a>

The following are processing options, along with features of each option:

**Built-in sensitive data redaction**
+ Automatically detects and removes configurable categories of sensitive information, such as credit card numbers and names
+ Supports multiple languages, including English, French, Portuguese, German, Italian, and Spanish variants. For a list of the languages supported by Conversational Analytics redaction, see [Languages supported by Connect Customer features](supported-languages.md).
+ Choose to redact selected or all sensitive data entities
+ Replace with generic placeholders ([PII]) or entity-specific placeholders ([NAME], [CREDIT\_CARD])

**Custom message processors (through Lambda)**

With a custom processor Lambda, you have the freedom to transform messages in any way you choose. A copy of each message is sent to your Lambda function, and if a valid response is received within the timeout, the content in the response becomes the new canonical form of that message.

This enables use cases such as:
+ Language translation through third-party services
+ Profanity filtering
+ AI/LLM-powered message transformation
+ Business-specific message modifications

For more information about Lambda, see [What is Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) in the *Lambda Developer Guide*.

## How it works
<a name="redaction-message-processing-how-it-works"></a>

When message processing is enabled, every plaintext, markdown, and JSON message passes through the configured processor before being delivered to participants. The processor can modify, approve, or reject the message. If processing fails, you can configure whether the original unprocessed message is delivered or suppressed.

Message processing stays active for the entire duration of the chat, even if an individual contact segment ends (for example, during a transfer). Processing does not retroactively apply to messages sent before it was enabled.

**Note**  
When both built-in redaction and a custom message processor are enabled simultaneously, the output of redaction becomes the input for the custom processor.

## Configure message processing
<a name="redaction-message-processing-configure"></a>

You can enable message processing using either of the following methods:
+ **Flow block** – Use the **Set recording, analytics and processing behavior** flow block. For more information, see [Flow block in Connect Customer: Set recording, analytics and processing behavior](set-recording-analytics-processing-behavior.md).
+ **API** – Call the `StartContactMediaProcessing` API for programmatic activation. For more information, see [StartContactMediaProcessing](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactMediaProcessing.html) in the *Connect Customer API Reference*.

To stop message processing before the chat ends, call the `StopContactMediaProcessing` API. For more information, see [StopContactMediaProcessing](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContactMediaProcessing.html) in the *Connect Customer API Reference*.

**Note**  
The `StartContactMediaProcessing` and `StopContactMediaProcessing` APIs are for custom message processors (BYOP) only. Built-in redaction is configured exclusively through the flow block.

## Enable built-in sensitive data redaction
<a name="redaction-message-processing-builtin"></a>

In-flight sensitive data redaction is powered by Conversational Analytics. To enable it, configure the **Set recording, analytics and processing behavior** flow block with the following settings:

1. **Select Action**: Choose `Set recording and analytics behavior`.

1. **Select Channel**: Choose `Chat`.

1. **Enable Conversational Analytics**: Select **Enable conversational analytics**.

1. Under **Configure Conversational Analytics** > **Redaction** > **In-flight message redaction**: Select **Enable in-flight redaction**.

![The Set recording, analytics and processing behavior flow block configured with conversational analytics enabled for chat.](http://docs.aws.amazon.com/connect/latest/adminguide/images/message-processing-enable-analytics.png)


![The in-flight message redaction configuration with redaction enabled.](http://docs.aws.amazon.com/connect/latest/adminguide/images/message-processing-redaction-config.png)


For more information about how Conversational Analytics redacts sensitive data, see [Enable redaction of sensitive data](enable-analytics.md#enable-redaction).

## Create a custom message processor
<a name="redaction-message-processing-custom"></a>

You can create a custom Lambda function that transforms messages in-flight. Custom processors can perform any transformation, such as language translation, profanity filtering, or AI-powered message enhancement.

**Add the Lambda function to your instance first**  
Before using a custom processor Lambda, you must add it to your Connect Customer instance. In the Connect Customer console, choose **Flows**, choose **Lambda functions**, and select the use case **Custom processor lambda**.

### Step 1: Create your Lambda function
<a name="redaction-message-processing-custom-step1"></a>

**Note**  
Connect Customer honors your Lambda function's configured timeout, which must be between 3 seconds and 3 minutes.

Your custom processor Lambda receives an input event in the following format:

```
{
  "version": "1.0",
  "instanceId": "string",
  "associatedResourceArn": "string",
  "chatContent": {
    "absoluteTime": "string",
    "content": "string",
    "contentType": "string",
    "id": "string",
    "participantId": "string",
    "displayName": "string",
    "participantRole": "string",
    "initialContactId": "string",
    "contactId": "string"
  }
}
```

Your Lambda function must return a response in the following format:

```
{
  "status": "PROCESSED | APPROVED | REJECTED",
  "result": {
    "processedChatContent": {
      "content": "string",
      "contentType": "text/plain | text/markdown | application/json"
    }
  }
}
```

The processed content replaces the original message when published to chat participants.

### Step 2: Grant Connect Customer permission to invoke your Lambda function
<a name="redaction-message-processing-custom-step2"></a>

You must grant Connect Customer permission to invoke your Lambda function:

1. In the Connect Customer console, choose your instance.

1. In the navigation pane, choose **Flows**.

1. In the **Lambda** section, select your Lambda function.

1. Under **Lambda Usecase**, select `Custom Processor Lambda`.

Alternatively, you can use the `CreateIntegrationAssociation` API with `IntegrationType` set to `MESSAGE_PROCESSOR`. For more information, see [CreateIntegrationAssociation](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html) in the *Connect Customer API Reference*.

![The Lambda section in the Amazon Connect console showing the Custom Processor Lambda usecase selection.](http://docs.aws.amazon.com/connect/latest/adminguide/images/message-processing-lambda-integration.png)


### Step 3: Activate your Lambda function
<a name="redaction-message-processing-custom-step3"></a>

Choose one of the following methods to activate your custom processor:

**Option 1: Use the flow block**

Configure the **Set recording, analytics and processing behavior** flow block with the following settings:

1. **Select Action**: Choose `Set message processor`.

1. **Select Channel**: Choose `Chat`.

1. **Enable Processing**: Select the checkbox.

1. **Function ARN**: Select your Lambda function.

1. **Processing failure handling**: Choose whether to deliver the original unprocessed message or suppress it if processing fails.

**Option 2: Use the StartContactMediaProcessing API**

![The Set recording, analytics and processing behavior flow block configured with Set message processor action for chat.](http://docs.aws.amazon.com/connect/latest/adminguide/images/message-processing-activate-flow-block.png)


Alternatively, you can activate message processing by calling the `StartContactMediaProcessing` API. This requires your instance ID, the chat's contact ID, the Lambda processor ARN, and a failure mode. For more information, see [StartContactMediaProcessing](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactMediaProcessing.html) in the *Connect Customer API Reference*.

## Additional information
<a name="redaction-message-processing-additional"></a>

### Transcript storage
<a name="redaction-message-processing-transcripts"></a>
+ Processed chat messages replace the original messages in the S3 Chat Transcripts folder: `<bucket-name>/connect/<instance-name>/<path-prefix>/`
+ The unprocessed (original) chat transcript is stored in a separate S3 folder: `<bucket-name>/connect/<instance-name>/Unprocessed<path-prefix>/`

### Important considerations
<a name="redaction-message-processing-considerations"></a>
+ Message processing stays active for the entire duration of the chat, even if an individual contact segment ends (for example, during a transfer).
+ `StartContactMediaProcessing` and the **Set recording, analytics and processing behavior** flow block do not retroactively process prior messages.
+ To stop message processing before the chat ends, call the [StopContactMediaProcessing](https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContactMediaProcessing.html) API.
+ Message processing is not available in the AWS GovCloud (US-West) Region.