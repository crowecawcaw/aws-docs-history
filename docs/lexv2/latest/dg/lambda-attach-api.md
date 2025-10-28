# Attach an AWS Lambda function to a bot using API operations

You must first attach a Lambda function to your bot alias before you can invoke it. You can only associate
one Lambda function with each bot alias. Perform these steps to attach the Lambda function using API operations.

If you are creating a new bot alias, use the [CreateBotAlias](../APIReference/API_CreateBotAlias.md "../APIReference/API_CreateBotAlias.md") operation to attach a Lambda function. To attach
a Lambda function to an existing bot alias, use the [UpdateBotAlias](../APIReference/API_UpdateBotAlias.md "../APIReference/API_UpdateBotAlias.md") operation. Modify the `botAliasLocaleSettings`
field to contain the correct settings:

```
{
    "botAliasLocaleSettings" : {
        `locale`: {
            "codeHookSpecification": {
                "lambdaCodeHook": {
                    "codeHookInterfaceVersion": "1.0",
                    "lambdaARN": "arn:aws:lambda:`region`:`account-id`:function:`function-name`"
                }
            },
            "enabled": true
        },
        ...
    }
}
```

1. The `botAliasLocaleSettings` field maps to an object whose keys are the locales in which you want to attach the Lambda
   function. See [Supported languages and
   locales](how-languages.md#supported-languages "how-languages.md#supported-languages") for a list of supported locales and the
   codes that are valid keys.
2. To find the `lambdaARN` for a Lambda function, open the AWS Lambda console
   at [https://console.aws.amazon.com/lambda/home](https://console.aws.amazon.com/lambda/home "https://console.aws.amazon.com/lambda/home"),
   select **Functions** in the left sidebar, and select the function to associate
   with the bot alias. On the right side of the **Function overview**, find
   the `lambdaARN` under **Function ARN**. It should contain a region, account ID,
   and the name of the function.
3. To allow Amazon Lex V2 to invoke the Lambda function for the alias, set the `enabled` field to `true`.

###### Setting a intent to invoke a Lambda function using API operations

To set up the Lambda function invocation during an intent, use the [CreateIntent](../APIReference/API_CreateIntent.md "../APIReference/API_CreateIntent.md") operation
if you are creating a new intent, or the [UpdateIntent](../APIReference/API_UpdateIntent.md "../APIReference/API_UpdateIntent.md") operation if you are invoking the
function in an existing intent. The fields that control the Lambda function invocation in the
intent operations are `dialogCodeHook`, `initialResponseSetting`, `intentConfirmationSetting`,
and `fulfillmentCodeHook`.

If you invoke the function during the elicitation of a slot, use the [CreateSlot](../APIReference/API_CreateSlot.md "../APIReference/API_CreateSlot.md") operation if
you are creating a new slot, or the [UpdateSlot](../APIReference/API_UpdateSlot.md "../APIReference/API_UpdateSlot.md") operation to invoke the function in an existing slot.
The field that controls the Lambda function invocation in the slot operations is the `slotCaptureSetting`
of the `valueElicitationSetting` object.

1. To set the Lambda dialog code hook to run after every turn of the
   conversation, set the `enabled` field of the following
   [DialogCodeHookSettings](../APIReference/API_DialogCodeHookSettings.md "../APIReference/API_DialogCodeHookSettings.md") object in the `dialogCodeHook` field
   to `true`:

```
"dialogCodeHook": {
    "enabled": `boolean`
}
```

2. Alternatively, you can set the Lambda dialog code hook to run only at specific points in the conversations by modifying the `codeHook` and/or `elicitationCodeHook` field within the structures that correspond to the conversation stages at which you want to invoke the function. To use the Lambda dialog code hook for intent fulfillment, use the `fulfillmentCodeHook` field in the [CreateIntent](../APIReference/API_CreateIntent.md "../APIReference/API_CreateIntent.md") or [UpdateIntent](../APIReference/API_UpdateIntent.md "../APIReference/API_UpdateIntent.md") operation. The structures and uses of these three types of code hooks are as follows:
   The `codeHook` field defines the settings for the code hook to run at a given stage in the conversation. It is a [DialogCodeHookInvocationSetting](../APIReference/API_DialogCodeHookInvocationSetting.md "../APIReference/API_DialogCodeHookInvocationSetting.md") object with the following structure:

```
"codeHook": {
    "active": `boolean`,
    "enableCodeHookInvocation": `boolean`,
    "invocationLabel": `string`,
    "postCodeHookSpecification": PostDialogCodeHookInvocationSpecification object,
}
```

- Change the `active` field to `true` for Amazon Lex V2 to call the code hook at that point in the conversation.
- Change the `enableCodeHookInvocation` field to `true` for Amazon Lex V2 to allow the code hook to run normally. If you mark it `false`, Amazon Lex V2 acts as if the code hook returned successfully.
- The `invocationLabel` indicates the dialog step from which the code hook is invoked.
- Use the `postCodeHookSpecification` field to specify the actions and messages that occur after the code hook succeeds, fails, or times out.
  The `elicitationCodeHook` field defines the settings for the code hook to run in the event that a slot or slots need to be re-elicited. This scenario may occur if slot elicitation fails or intent confirmation is denied. The `elicitationCodeHook` field is an [ElicitationCodeHookInvocationSetting](../APIReference/API_ElicitationCodeHookInvocationSetting.md "../APIReference/API_ElicitationCodeHookInvocationSetting.md") object with the following structure:

```
"elicitationCodeHook": {
    "enableCodeHookInvocation": `boolean`,
    "invocationLabel": `string`
}
```

- Change the `enableCodeHookInvocation` field to `true` for Amazon Lex V2 to allow the code hook to run normally. If you mark it `false`, Amazon Lex V2 acts as if the code hook returned successfully.
- The `invocationLabel` indicates the dialog step from which the code hook is invoked.
  The `fulfillmentCodeHook` field defines the settings for the code hook to run to fulfill the intent. It maps to the following [FulfillmentCodeHookSettings](../APIReference/API_FulfillmentCodeHookSettings.md "../APIReference/API_FulfillmentCodeHookSettings.md") object:

```
"fulfillmentCodeHook": {
    "active": `boolean`,
    "enabled": `boolean`,
    "fulfillmentUpdatesSpecification": FulfillmentUpdatesSpecification object,
    "postFulfillmentStatusSpecification": PostFulfillmentStatusSpecification object
}
```

- Change the `active` field to `true` for Amazon Lex V2 to call the code hook at that point in the conversation.
- Change the `enabled` field to `true` for Amazon Lex V2 to allow the code hook to run normally. If you mark it `false`, Amazon Lex V2 acts as if the code hook returned successfully.
- Use the `fulfillmentUpdatesSpecification` field to specify the messages that appear to update the user during fulfillment of the intent and the timing associated with them.
- Use the `postFulfillmentStatusSpecification`
  field to specify the messages and actions that occur after the code
  hook succeeds, fails, or times out.
  You can invoke the Lambda code hook at the following points in a conversation by setting the `active` and `enableCodeHookInvocation`/`enabled` fields to `true`:

To invoke the Lambda function in the initial response after the intent is recognized, use the `codeHook` structure in the `initialResponse` field of the [CreateIntent](../APIReference/API_CreateIntent.md "../APIReference/API_CreateIntent.md") or [UpdateIntent](../APIReference/API_UpdateIntent.md "../APIReference/API_UpdateIntent.md") operation. The `initialResponse` field maps to the following [InitialResponseSetting](../APIReference/API_InitialResponseSetting.md "../APIReference/API_InitialResponseSetting.md") object:

```
"initialResponse": {
    "codeHook": {
        "active": `boolean`,
        "enableCodeHookInvocation": `boolean`,
        "invocationLabel": `string`,
        "postCodeHookSpecification": PostDialogCodeHookInvocationSpecification object,
    },
    "initialResponse": FulfillmentUpdatesSpecification object,
    "nextStep": PostFulfillmentStatusSpecification object,
    "conditional": ConditionalSpecification object
}
```

To invoke the Lambda function after eliciting a slot value, use the `slotCaptureSetting` field within the `valueElicitation` field of the [CreateSlot](../APIReference/API_CreateSlot.md "../APIReference/API_CreateSlot.md") or [UpdateSlot](../APIReference/API_UpdateSlot.md "../APIReference/API_UpdateSlot.md") operation. The `slotCaptureSetting` field maps to the following [SlotCaptureSetting](../APIReference/API_SlotCaptureSetting.md "../APIReference/API_SlotCaptureSetting.md") object:

```
"slotCaptureSetting": {
    "captureConditional": ConditionalSpecification object,
    "captureNextStep": DialogState object,
    "captureResponse": ResponseSpecification object,
    "codeHook": {
        "active": `true`,
        "enableCodeHookInvocation": `true`,
        "invocationLabel": `string`,
        "postCodeHookSpecification": PostDialogCodeHookInvocationSpecification object,
    },
    "elicitationCodeHook": {
        "enableCodeHookInvocation": `boolean`,
        "invocationLabel": `string`
    },
    "failureConditional": ConditionalSpecification object,
    "failureNextStep": DialogState object,
    "failureResponse": ResponseSpecification object
}
```

- To invoke the Lambda function after slot elicitation is successful, use the `codeHook` field.
- To invoke the Lambda function after slot elicitation fails and Amazon Lex V2 attempts to retry slot elicitation, use the `elicitationCodeHook` field.
  To invoke the Lambda function when confirming an intent, use the `intentConfirmationSetting` field of the [CreateIntent](../APIReference/API_CreateIntent.md "../APIReference/API_CreateIntent.md") or [UpdateIntent](../APIReference/API_UpdateIntent.md "../APIReference/API_UpdateIntent.md") operation. The `intentConfirmation` field maps to the following [IntentConfirmationSetting](../APIReference/API_IntentConfirmationSetting.md "../APIReference/API_IntentConfirmationSetting.md") object:

```
"intentConfirmationSetting": {
    "active": `boolean`,
    "codeHook": {
        "active": `boolean`,
        "enableCodeHookInvocation": `boolean`,
        "invocationLabel": `string`,
        "postCodeHookSpecification": PostDialogCodeHookInvocationSpecification object,
    },
    "confirmationConditional": ConditionalSpecification object,
    "confirmationNextStep": DialogState object,
    "confirmationResponse": ResponseSpecification object,
    "declinationConditional": ConditionalSpecification object,
    "declinationNextStep": FulfillmentUpdatesSpecification object,
    "declinationResponse": PostFulfillmentStatusSpecification object,
    "elicitationCodeHook": {
        "enableCodeHookInvocation": `boolean`,
        "invocationLabel": `string`,
    },
    "failureConditional": ConditionalSpecification object,
    "failureNextStep": DialogState object,
    "failureResponse": ResponseSpecification object,
    "promptSpecification": PromptSpecification object
}
```

- To invoke the Lambda function after the user confirms the intent and its slots, use the `codeHook` field.
- To invoke the Lambda function after the user denies the intent confirmation and Amazon Lex V2 attempts to retry slot elicitation, use the `elicitationCodeHook` field.
  To invoke the Lambda function to fulfill an intent, use the `fulfillmentCodeHook` field in the [CreateIntent](../APIReference/API_CreateIntent.md "../APIReference/API_CreateIntent.md") or [UpdateIntent](../APIReference/API_UpdateIntent.md "../APIReference/API_UpdateIntent.md") operation. The `fulfillmentCodeHook` field maps to the following [FulfillmentCodeHookSettings](../APIReference/API_FulfillmentCodeHookSettings.md "../APIReference/API_FulfillmentCodeHookSettings.md") object:

```
{
    "active": `boolean`,
    "enabled": `boolean`,
    "fulfillmentUpdatesSpecification": FulfillmentUpdatesSpecification object,
    "postFulfillmentStatusSpecification": PostFulfillmentStatusSpecification object
}
```

3. Once you set the conversation stages at which to invoke the Lambda function, use the `BuildBotLocale` operation to
   rebuild the bot in order to test the function.
