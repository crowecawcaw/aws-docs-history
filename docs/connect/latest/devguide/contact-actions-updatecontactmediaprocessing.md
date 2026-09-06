

# UpdateContactMediaProcessing
<a name="contact-actions-updatecontactmediaprocessing"></a>

Allows customers to configure their own Lambda processor, which will be applied to in-flight messages.

## Parameter object
<a name="updatecontactmediaprocessing-parameter"></a>

```
{
    "ChatProcessor": { // Configuration for bring-your-own-processor for chat channel.
        "ProcessingEnabled": either "True" or "False". Must be set statically. Determines whether to enable custom Lambda processing for chat messages.
        "LambdaProcessorARN": The ARN of the Lambda function to process chat messages. Must be set statically. Format: arn:aws:lambda:region:account-id:function:function-name
        "ChatProcessorSettings": { // An object that holds chat processor behavior settings
            "DeliverUnprocessedMessages": either "True" or "False". Must be set statically. Determines whether to deliver messages that fail Lambda processing.
        }
    }
}
```

## Results and conditions
<a name="updatecontactmediaprocessing-results"></a>

None.

## Errors
<a name="updatecontactmediaprocessing-errors"></a>
+ **NoMatchingError** - if no other Error matches. Must always be defined.
+ **ChannelMismatch** - if the media channel that initiated the contact is not the same as the one defined in the action. As of now, only chat is supported in this action.

## Corresponding block in the UI
<a name="updatecontactmediaprocessing-ui"></a>

[Set recording, analytics and processing behavior](https://docs.aws.amazon.com/connect/latest/adminguide/set-recording-analytics-processing-behavior.html)