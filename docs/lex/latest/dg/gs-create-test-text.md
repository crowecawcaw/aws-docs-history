End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Test the Bot Using Text Input

(AWS CLI)

To verify that the bot works correctly with text input, use the [PostText](API_runtime_PostText.md "API_runtime_PostText.md")
operation. To run the commands in this exercise, you need to know the region
where the commands will be run. For a list of regions, see [Runtime Service
Quotas](gl-limits.md#gl-limits-runtime "gl-limits.md#gl-limits-runtime").

###### Note

The following AWS CLI example is formatted for Unix, Linux, and macOS. For
Windows, change `"\$LATEST"` to `$LATEST` and replace
the backslash (\) continuation character at the end of each line with a
caret (^).

###### To use text to test the bot (AWS CLI)

1. In the AWS CLI, start a conversation with the
   `OrderFlowersBot` bot. The example is formatted for Unix,
   Linux, and macOS. For Windows, replace the backslash (\) Unix
   continuation character at the end of each line with a caret (^).

```
aws lex-runtime post-text \
    --region `region` \
    --bot-name OrderFlowersBot \
    --bot-alias "\$LATEST" \
    --user-id UserOne \
    --input-text "i would like to order flowers"
```

Amazon Lex recognizes the user's intent and starts a conversation by
returning the following response:

```
{
    "slotToElicit": "FlowerType",
    "slots": {
        "PickupDate": null,
        "PickupTime": null,
        "FlowerType": null
    },
    "dialogState": "ElicitSlot",
    "message": "What type of flowers would you like to order?",
    "intentName": "OrderFlowers"
}
```

2. Run the following commands to finish the conversation with the
   bot.

```
aws lex-runtime post-text \
    --region `region` \
    --bot-name OrderFlowersBot \
    --bot-alias "\$LATEST" \
    --user-id UserOne \
    --input-text "roses"
```

```
aws lex-runtime post-text  \
    --region `region` \
    --bot-name OrderFlowersBot \
    --bot-alias "\$LATEST" \
    --user-id UserOne \
    --input-text "tuesday"
```

```
aws lex-runtime post-text  \
    --region `region` \
    --bot-name OrderFlowersBot --bot-alias "\$LATEST" \
    --user-id UserOne \
    --input-text "10:00 a.m."
```

```
aws lex-runtime post-text  \
    --region `region` \
    --bot-name OrderFlowersBot \
    --bot-alias "\$LATEST" \
    --user-id UserOne \
    --input-text "yes"
```

After you confirm the order, Amazon Lex sends a fulfillment response to
complete the conversation:

```
{
    "slots": {
        "PickupDate": "2017-05-16",
        "PickupTime": "10:00",
        "FlowerType": "roses"
    },
    "dialogState": "ReadyForFulfillment",
    "intentName": "OrderFlowers"
}
```

## Next Step

[Test the Bot Using Speech Input
(AWS CLI)](gs-create-test-speech.md "gs-create-test-speech.md")
