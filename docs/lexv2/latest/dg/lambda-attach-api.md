

# Attach an AWS Lambda function to a Amazon Lex V2 bot using API operations
<a name="lambda-attach-api"></a>

You must first attach a Lambda function to your Amazon Lex V2 bot alias before you can invoke it. You can only associate one Lambda function with each bot alias. Perform these steps to attach the Lambda function using API operations. 

If you are creating a new bot alias, use the [CreateBotAlias](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotAlias.html) operation to attach a Lambda function. To attach a Lambda function to an existing bot alias, use the [UpdateBotAlias](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotAlias.html) operation. Modify the `botAliasLocaleSettings` field to contain the correct settings:

```
{
    "botAliasLocaleSettings" : {
        {{locale}}: {
            "codeHookSpecification": {
                "lambdaCodeHook": {
                    "codeHookInterfaceVersion": "1.0",
                    "lambdaARN": "arn:aws:lambda:{{region}}:{{account-id}}:function:{{function-name}}"
                }
            },
            "enabled": true
        },
        ...
    }
}
```

1. The `botAliasLocaleSettings` field maps to an object whose keys are the locales in which you want to attach the Lambda function. See [Supported languages and locales](how-languages.md#supported-languages) for a list of supported locales and the codes that are valid keys.

1. To find the `lambdaARN` for a Lambda function, open the AWS Lambda console at [https://console.aws.amazon.com/lambda/home](https://console.aws.amazon.com/lambda/home), select **Functions** in the left sidebar, and select the function to associate with the bot alias. On the right side of the **Function overview**, find the `lambdaARN` under **Function ARN**. It should contain a region, account ID, and the name of the function.

1. To allow Amazon Lex V2 to invoke the Lambda function for the alias, set the `enabled` field to `true`.

**Setting a Amazon Lex V2 intent to invoke a Lambda function using API operations**

To set up the Lambda function invocation during an intent, use the [CreateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html) operation if you are creating a new intent, or the [UpdateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateIntent.html) operation if you are invoking the function in an existing intent. The fields that control the Lambda function invocation in the intent operations are `dialogCodeHook`, `initialResponseSetting`, `intentConfirmationSetting`, and `fulfillmentCodeHook`.

If you invoke the function during the elicitation of a slot, use the [CreateSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateSlot.html) operation if you are creating a new slot, or the [UpdateSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateSlot.html) operation to invoke the function in an existing slot. The field that controls the Lambda function invocation in the slot operations is the `slotCaptureSetting` of the `valueElicitationSetting` object.

1. To set the Lambda dialog code hook to run after every turn of the conversation, set the `enabled` field of the following [DialogCodeHookSettings](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialogCodeHookSettings.html) object in the `dialogCodeHook` field to `true`:

   ```
   "dialogCodeHook": {
       "enabled": {{boolean}}
   }
   ```

1. Alternatively, you can set the Lambda dialog code hook to run only at specific points in the conversations by modifying the `codeHook` and/or `elicitationCodeHook` field within the structures that correspond to the conversation stages at which you want to invoke the function. To use the Lambda dialog code hook for intent fulfillment, use the `fulfillmentCodeHook` field in the [CreateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html) or [UpdateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateIntent.html) operation. The structures and uses of these three types of code hooks are as follows:

## codeHook
<a name="lambda-code-hook"></a>

The `codeHook` field defines the settings for the code hook to run at a given stage in the conversation. It is a [DialogCodeHookInvocationSetting](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialogCodeHookInvocationSetting.html) object with the following structure:

```
"codeHook": {
    "active": {{boolean}},
    "enableCodeHookInvocation": {{boolean}},
    "invocationLabel": {{string}},
    "postCodeHookSpecification": [PostDialogCodeHookInvocationSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostDialogCodeHookInvocationSpecification.html),
}
```
+ Change the `active` field to `true` for Amazon Lex V2 to call the code hook at that point in the conversation.
+ Change the `enableCodeHookInvocation` field to `true` for Amazon Lex V2 to allow the code hook to run normally. If you mark it `false`, Amazon Lex V2 acts as if the code hook returned successfully.
+ The `invocationLabel` indicates the dialog step from which the code hook is invoked.
+ Use the `postCodeHookSpecification` field to specify the actions and messages that occur after the code hook succeeds, fails, or times out.

## elicitationCodeHook
<a name="lambda-elicitation-code-hook"></a>

The `elicitationCodeHook` field defines the settings for the code hook to run in the event that a slot or slots need to be re-elicited. This scenario may occur if slot elicitation fails or intent confirmation is denied. The `elicitationCodeHook` field is an [ElicitationCodeHookInvocationSetting](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ElicitationCodeHookInvocationSetting.html) object with the following structure:

```
"elicitationCodeHook": {
    "enableCodeHookInvocation": {{boolean}},
    "invocationLabel": {{string}}
}
```
+ Change the `enableCodeHookInvocation` field to `true` for Amazon Lex V2 to allow the code hook to run normally. If you mark it `false`, Amazon Lex V2 acts as if the code hook returned successfully.
+ The `invocationLabel` indicates the dialog step from which the code hook is invoked.

## fulfillmentCodeHook
<a name="lambda-fulfillment-code-hook"></a>

The `fulfillmentCodeHook` field defines the settings for the code hook to run to fulfill the intent. It maps to the following [FulfillmentCodeHookSettings](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentCodeHookSettings.html) object:

```
"fulfillmentCodeHook": {
    "active": {{boolean}},
    "enabled": {{boolean}},
    "fulfillmentUpdatesSpecification": [FulfillmentUpdatesSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentUpdatesSpecification.html),
    "postFulfillmentStatusSpecification": [PostFulfillmentStatusSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostFulfillmentStatusSpecification.html)
}
```
+ Change the `active` field to `true` for Amazon Lex V2 to call the code hook at that point in the conversation.
+ Change the `enabled` field to `true` for Amazon Lex V2 to allow the code hook to run normally. If you mark it `false`, Amazon Lex V2 acts as if the code hook returned successfully.
+ Use the `fulfillmentUpdatesSpecification` field to specify the messages that appear to update the user during fulfillment of the intent and the timing associated with them.
+ Use the `postFulfillmentStatusSpecification` field to specify the messages and actions that occur after the code hook succeeds, fails, or times out.

You can invoke the Lambda code hook at the following points in a conversation by setting the `active` and `enableCodeHookInvocation`/`enabled` fields to `true`:

## During the initial response
<a name="lambda-hook-initial-response"></a>

To invoke the Lambda function in the initial response after the intent is recognized, use the `codeHook` structure in the `initialResponse` field of the [CreateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html) or [UpdateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateIntent.html) operation. The `initialResponse` field maps to the following [InitialResponseSetting](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_InitialResponseSetting.html) object:

```
"initialResponse": {
    "codeHook": {
        "active": {{boolean}},
        "enableCodeHookInvocation": {{boolean}},
        "invocationLabel": {{string}},
        "postCodeHookSpecification": [PostDialogCodeHookInvocationSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostDialogCodeHookInvocationSpecification.html),
    },
    "initialResponse": [FulfillmentUpdatesSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentUpdatesSpecification.html),
    "nextStep": [PostFulfillmentStatusSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostFulfillmentStatusSpecification.html),
    "conditional": [ConditionalSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConditionalSpecification.html)
}
```

## After slot elicitation or during slot re-elicitation
<a name="lambda-hook-elicit-slot"></a>

To invoke the Lambda function after eliciting a slot value, use the `slotCaptureSetting` field within the `valueElicitation` field of the [CreateSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateSlot.html) or [UpdateSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateSlot.html) operation. The `slotCaptureSetting` field maps to the following [SlotCaptureSetting](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotCaptureSetting.html) object:

```
"slotCaptureSetting": {
    "captureConditional": [ConditionalSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConditionalSpecification.html),
    "captureNextStep": [DialogState object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialogState.html),
    "captureResponse": [ResponseSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ResponseSpecification.html),
    "codeHook": {
        "active": {{true}},
        "enableCodeHookInvocation": {{true}},
        "invocationLabel": {{string}},
        "postCodeHookSpecification": [PostDialogCodeHookInvocationSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostDialogCodeHookInvocationSpecification.html),
    },
    "elicitationCodeHook": {
        "enableCodeHookInvocation": {{boolean}},
        "invocationLabel": {{string}}
    },
    "failureConditional": [ConditionalSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConditionalSpecification.html),
    "failureNextStep": [DialogState object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialogState.html),
    "failureResponse": [ResponseSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ResponseSpecification.html)
}
```
+ To invoke the Lambda function after slot elicitation is successful, use the `codeHook` field.
+ To invoke the Lambda function after slot elicitation fails and Amazon Lex V2 attempts to retry slot elicitation, use the `elicitationCodeHook` field.

## After intent confirmation or denial
<a name="lambda-hook-confirm-intent"></a>

To invoke the Lambda function when confirming an intent, use the `intentConfirmationSetting` field of the [CreateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html) or [UpdateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateIntent.html) operation. The `intentConfirmation` field maps to the following [IntentConfirmationSetting](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_IntentConfirmationSetting.html) object:

```
"intentConfirmationSetting": {
    "active": {{boolean}},
    "codeHook": {
        "active": {{boolean}},
        "enableCodeHookInvocation": {{boolean}},
        "invocationLabel": {{string}},
        "postCodeHookSpecification": [PostDialogCodeHookInvocationSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostDialogCodeHookInvocationSpecification.html),
    },
    "confirmationConditional": [ConditionalSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConditionalSpecification.html),
    "confirmationNextStep": [DialogState object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialogState.html),
    "confirmationResponse": [ResponseSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialResponseSpecificationogState.html),
    "declinationConditional": [ConditionalSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConditionalSpecification.html),
    "declinationNextStep": [FulfillmentUpdatesSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentUpdatesSpecification.html),
    "declinationResponse": [PostFulfillmentStatusSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostFulfillmentStatusSpecification.html),
    "elicitationCodeHook": {
        "enableCodeHookInvocation": {{boolean}},
        "invocationLabel": {{string}},
    },
    "failureConditional": [ConditionalSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConditionalSpecification.html),
    "failureNextStep": [DialogState object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DialogState.html),
    "failureResponse": [ResponseSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ResponseSpecification.html),
    "promptSpecification": [PromptSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PromptSpecification.html)
}
```
+ To invoke the Lambda function after the user confirms the intent and its slots, use the `codeHook` field.
+ To invoke the Lambda function after the user denies the intent confirmation and Amazon Lex V2 attempts to retry slot elicitation, use the `elicitationCodeHook` field.

## During intent fulfillment
<a name="lambda-hook-fulfill-intent"></a>

To invoke the Lambda function to fulfill an intent, use the `fulfillmentCodeHook` field in the [CreateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html) or [UpdateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateIntent.html) operation. The `fulfillmentCodeHook` field maps to the following [FulfillmentCodeHookSettings](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentCodeHookSettings.html) object:

```
{
    "active": {{boolean}},
    "enabled": {{boolean}},
    "fulfillmentUpdatesSpecification": [FulfillmentUpdatesSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_FulfillmentUpdatesSpecification.html),
    "postFulfillmentStatusSpecification": [PostFulfillmentStatusSpecification object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_PostFulfillmentStatusSpecification.html)
}
```

3. Once you set the conversation stages at which to invoke the Lambda function, use the `BuildBotLocale` operation to rebuild the bot in order to test the function.