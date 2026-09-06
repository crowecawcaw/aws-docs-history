

# Enable message streaming for AI-powered chat
<a name="message-streaming-ai-chat"></a>

Connect Customer supports message streaming for AI-powered chat interactions. Responses from AI agents appear progressively as they're generated, improving the customer experience during conversations.

The following are integration options, along with features of each option:
+ Connect Customer agents
  + Eliminates Amazon Lex timeout limitations
  + Provides fulfillment messages during processing (such as "One moment while I review your account")
  + Displays partial responses with progressive text (growing text bubble)
+ Third-party bots through Amazon Lex or Lambda
  + Eliminates Amazon Lex timeout limitations
  + Standard bot response behavior

Instances created starting December 2025 are automatically opted into this feature. For existing instances, you must enable message streaming manually using the API or through the console.

## Enable message streaming using the API
<a name="message-streaming-enable-api"></a>

Use the [UpdateInstanceAttribute](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateInstanceAttribute.html) API to enable message streaming. Set the `MESSAGE_STREAMING` attribute to `true`.

```
aws connect update-instance-attribute \
  --instance-id {{your-instance-id}} \
  --attribute-type MESSAGE_STREAMING \
  --value true
```

To opt out, set the attribute to `false`.

## Enable message streaming using the console
<a name="message-streaming-enable-console"></a>

For newly created instances, message streaming is enabled by default.

For existing instances:

1. Open the Connect Customer console and choose your instance.

1. In the navigation pane, choose **Flows** > **Amazon Lex bots**.

1. Under **Lex bots configuration**, select **Enable message streaming in Amazon Connect**.

**Note**  
When you enable message streaming using the console, the required `lex:RecognizeMessageAsync` permission is automatically added to the bot alias resource-based policy. When using the API, you must add this permission manually.

![Enable message streaming option in the Amazon Connect console.](http://docs.aws.amazon.com/connect/latest/adminguide/images/message-streaming-ai-chat-enablement.png)


## Update Lex bot permissions
<a name="message-streaming-lex-permissions"></a>

After message streaming is enabled, Connect Customer needs permission to call the Amazon Lex API:

```
lex:RecognizeMessageAsync
```

You must update the resource-based policy for each Amazon Lex bot alias used by the Connect Customer instance.

### When to update the bot's resource-based policy
<a name="message-streaming-when-to-update"></a>
+ **New instances** – Any newly associated Amazon Lex bot alias will have `lex:RecognizeMessageAsync` in its alias policy by default.
+ **Existing instances with existing bots** – If the instance previously used Amazon Lex and you enable message streaming now, you must update the resource-based policy on all associated Amazon Lex bot aliases to include the new permission.

### Example snippet for Lex bot alias resource-based policy
<a name="message-streaming-rbp-example"></a>

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "connect-us-west-2-MYINSTANCEID",
      "Effect": "Allow",
      "Principal": {
        "Service": "connect.amazonaws.com"
      },
      "Action": [
        "lex:RecognizeMessageAsync",
        "lex:RecognizeText",
        "lex:StartConversation"
      ],
      "Resource": "arn:aws:lex:us-west-2:123456789012:bot-alias/MYBOT/MYBOTALIAS",
      "Condition": {
        "StringEquals": {
          "AWS:SourceAccount": "123456789012"
        },
        "ArnEquals": {
          "AWS:SourceArn": "arn:aws:connect:us-west-2:123456789012:instance/MYINSTANCEID"
        }
      }
    }
  ]
}
```

You can add this permission by calling the Amazon Lex [UpdateResourcePolicy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateResourcePolicy.html) API to update the Amazon Lex bot alias resource-based policy to include the `lex:RecognizeMessageAsync` action for the Connect Customer instance ARN resource.

## Incremental message responses
<a name="message-streaming-incremental"></a>

**Note**  
Incremental message responses (growing message bubble) only work with Connect Customer AI agents of type **Orchestration**.

To enable incremental responses, start a chat with [ParticipantConfiguration](https://docs.aws.amazon.com/connect/latest/APIReference/API_ParticipantConfiguration.html) and set Response Mode to `INCREMENTAL`. The default Response Mode is `COMPLETE`.

## Timeout limits
<a name="message-streaming-timeout-limits"></a>

The following timeout limits apply to chat experiences:
+ **Standard chat experience** – 10-second timeout
+ **Chat streaming** – 60-second timeout