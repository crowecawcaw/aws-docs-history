End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Migrating a Lambda function from

Amazon Lex V1 to Amazon Lex V2

Amazon Lex V2 allows only one Lambda function for each language in a bot.
The Lambda function and its settings are configured for the bot alias
that you use at runtime.

The Lambda function is invoked for all intents in that language if
dialog and fulfillment code hooks are enabled for the intent.

Amazon Lex V2 Lambda functions have a different input and output message
format from Amazon Lex V1. These are the differences in the Lambda function
input format.

- Amazon Lex V2 replaces the `currentIntent` and
  `alternativeIntents` structures with the
  `interpretations` structure. Each
  interpretation contains an intent, the NLU confidence score
  for the intent, and an optional sentiment analysis.
- Amazon Lex V2 moves the `activeContexts`,
  `sessionAttributes` in Amazon Lex V1 to the unified
  `sessionState` structure. This structure
  provides information about the current state of the
  conversation, including the originating request ID.
- Amazon Lex V2 doesn't return the
  `recentIntentSummaryView`. Use the
  information in the `sessionState` structure
  instead.
- The Amazon Lex V2 input provides the `botId` and
  `localeId` in the `bot`
  attribute.
- The input structure contains an `inputMode`
  attribute that provides information on the type of input:
  text, speech, or DTMF.
  These are the differences in the Lambda function output
  format:

- The `activeContexts` and
  `sessionAttributes` structures in Amazon Lex V1 are
  replaced by the `sessionState` structure in
  Amazon Lex V2.
- The `recentIntentSummaryView` isn't included in
  the output.
- The Amazon Lex V1 `dialogAction` structure is split
  into two structures, `dialogAction` that is part
  of the `sessionState` structure, and
  `messages` that is required when the
  `dialogAction.type` is
  `ElicitIntent`. Amazon Lex chooses messages from
  this structure to show to the user.
  When you build a bot with the Amazon Lex V2 APIs, there is only one
  Lambda function per bot alias per language instead of a Lambda
  function for each intent. If you want to continue to use separate
  functions, you can create a router function that activates a
  separate function for each intent. The following is a router
  function that you can use or modify for your application.

```
import os
import json
import boto3

# reuse client connection as global
client = boto3.client('lambda')

def router(event):
    intent_name = event['sessionState']['intent']['name']
    fn_name = os.environ.get(intent_name)
    print(f"Intent: {intent_name} -> Lambda: {fn_name}")
    if (fn_name):
        # invoke lambda and return result
        invoke_response = client.invoke(FunctionName=fn_name, Payload = json.dumps(event))
        print(invoke_response)
        payload = json.load(invoke_response['Payload'])
        return payload
    raise Exception('No environment variable for intent: ' + intent_name)

def lambda_handler(event, context):
    print(event)
    response = router(event)
    return response
```

## List of updated

fields

The following tables provide detailed information about the
updated fields in the Amazon Lex V2 Lambda request and response. You can
use these tables to map fields between the versions.

### Request

The following fields have been updated in the Lambda
function request format.

#### Active

contexts

The `activeContexts` structure is now part
of the `sessionState` structure.

| V1 structure                                                       | V2 structure                                                                                                       |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| activeContexts                                                     | sessionState.activeContexts                                                                                        |
| activeContexts[\*].timeToLive                                      | sessionState.activeContexts[\*].timeToLive                                                                         |
| activeContexts[\*].timeToLive.timeToLiveInSeconds                  | sessionState.activeContexts[\*].timeToLive.timeToLiveInSeconds                                                     |
| activeContexts[\*].timeToLive.turnsToLive                          | sessionState.activeContexts[\*].timeToLive.turnsToLive                                                             |
| activeContexts[\*].name                                            | sessionState.activeContexts[\*].name                                                                               |
| activeContexts[\*].parameters                                      | sessionState.activeContexts[\*].contextAttributes                                                                  | #### Alternative intents The interpretations list from index 1 to N contains the list of alternative intents predicted by Amazon Lex V2, along with their confidence scores. The `recentIntentSummaryView` is removed from the request structure in Amazon Lex V2. To see the details from the `recentIntentSummaryView`, use the [GetSession](API_runtime_GetSession.md "API_runtime_GetSession.md") operation.          |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| alternativeIntents                                                 | interpretations[1:\*]                                                                                              |
| recentIntentSummaryView                                            | N/A                                                                                                                | #### Bot In Amazon Lex V2, bots and aliases have identifiers. The bot ID is part of the codehook input. The alias ID is included, but not the alias name. Amazon Lex V2 supports multiple locales for the same bot so the locale ID is included.                                                                                                                                                                          |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| bot                                                                | bot                                                                                                                |
| bot.name                                                           | bot.name                                                                                                           |
| N/A                                                                | bot.id                                                                                                             |
| bot.alias                                                          | N/A                                                                                                                |
| N/A                                                                | bot.aliasId                                                                                                        |
| bot.version                                                        | bot.version                                                                                                        |
| N/A                                                                | bot.localeId                                                                                                       | #### Current intent The `sessionState.intent` structure contains the details of the active intent. Amazon Lex V2 also returns a list of all of the intents, including alternative intents, in the `interpretations` structure. The first element in the interpretations list is always the same as `sessionState.intent`.                                                                                                 |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| currentIntent                                                      | sessionState.intent OR interpretations[0].intent                                                                   |
| currentIntent.name                                                 | sessionState.intent.name OR interpretations[0].intent.name                                                         |
| currentIntent.nluConfidenceScore                                   | interpretations[0].nluConfidence.score                                                                             | #### Dialog action The `confirmationStatus` field is now part of the `sessionState` structure.                                                                                                                                                                                                                                                                                                                            |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| currentIntent.confirmationStatus                                   | sessionState.intent.confirmationState OR interpretations[0].intent.confirmationState                               |
| N/A                                                                | sessionState.intent.state OR interpretations[\*].intent.state                                                      | #### Amazon Kendra The `kendraResponse` field is now part of the `sessionState` and `interpretations` structures.                                                                                                                                                                                                                                                                                                         |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| kendraResponse                                                     | sessionState.intent.kendraResponse OR interpretations[0].intent.kendraResponse                                     | #### Sentiment The `sentimentResponse` structure is moved to the new `interpretations` structure.                                                                                                                                                                                                                                                                                                                         |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| sentimentResponse                                                  | interpretations[0].sentimentResponse                                                                               |
| sentimentResponse.sentimentLabel                                   | interpretations[0].sentimentResponse.sentiment                                                                     |
| sentimentResponse.sentimentScore                                   | interpretations[0].sentimentResponse.sentimentScore                                                                | #### Slots Amazon Lex V2 provides a single `slots` object inside the `sessionState.intent` structure that contains the resolved values, interpreted value, and the original value of what the user said. Amazon Lex V2 also supports multi-valued slots by setting the `slotShape` as `List` and setting the `values` list. Single-value slots are supported by the `value` field, their shape is assumed to be `Scalar`. |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| currentIntent.slots                                                | sessionState.intent.slots OR interpretations[0].intent.slots                                                       |
| currentIntent.slots[\*].value                                      | sessionState.intent.slots[\*].value.interpretedValue OR interpretations[0].intent.slots[\*].value.interpretedValue |
| N/A                                                                | sessionState.intent.slots[\*].value.shape OR interpretations[0].intent.slots[\*].shape                             |
| N/A                                                                | sessionState.intent.slots[\*].values OR interpretations[0].intent.slots[\*].values                                 |
| currentIntent.slotDetails                                          | sessionState.intent.slots OR interpretations[0].intent.slots                                                       |
| currentIntent.slotDetails[\*].resolutions                          | sessionState.intent.slots[\*].resolvedValues OR interpretations[0].intent.slots[\*].resolvedValues                 |
| currentIntent.slotDetails[\*].originalValue                        | sessionState.intent.slots[\*].originalValue OR interpretations[0].intent.slots[\*].originalValue                   | #### Others The Amazon Lex V2 `sessionId` field is the same as the `userId` field in Amazon Lex V1. Amazon Lex V2 also sends the `inputMode` of the caller: text, DTMF, or speech.                                                                                                                                                                                                                                        |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| userId                                                             | sessionId                                                                                                          |
| inputTranscript                                                    | inputTranscript                                                                                                    |
| invocationSource                                                   | invocationSource                                                                                                   |
| outputDialogMode                                                   | responseContentType                                                                                                |
| messageVersion                                                     | messageVersion                                                                                                     |
| sessionAttributes                                                  | sessionState.sessionAttributes                                                                                     |
| requestAttributes                                                  | requestAttributes                                                                                                  |
| N/A                                                                | inputMode                                                                                                          |
| N/A                                                                | originatingRequestId                                                                                               | ### Response The following fields have been changed in the Lambda function response message format. #### Active contexts The `activeContexts` structure moved to the `sessionState` structure.                                                                                                                                                                                                                            |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| activeContexts                                                     | sessionState.activeContexts                                                                                        |
| activeContexts[\*].timeToLive                                      | sessionState.activeContexts[\*].timeToLive                                                                         |
| activeContexts[\*].timeToLive.timeToLiveInSeconds                  | sessionState.activeContexts[\*].timeToLive.timeToLiveInSeconds                                                     |
| activeContexts[\*].timeToLive.turnsToLive                          | sessionState.activeContexts[\*].timeToLive.turnsToLive                                                             |
| activeContexts[\*].name                                            | sessionState.activeContexts[\*].name                                                                               |
| activeContexts[\*].parameters                                      | sessionState.activeContexts[\*].contextAttributes                                                                  | #### Dialog action The `dialogAction` structure moved to the `sessionState` structure. You can now specify multiple messages in a dialog action, and the `genericAttachments` structure is now the `imageResponseCard` structure.                                                                                                                                                                                         |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| dialogAction                                                       | sessionState.dialogAction                                                                                          |
| dialogAction.type                                                  | sessionState.dialogAction.type                                                                                     |
| dialogAction.slotToElicit                                          | sessionState.intent.dialogAction.slotToElicit                                                                      |
| dialogAction.type.fulfillmentState                                 | sessionState.intent.state                                                                                          |
| dialogAction.message                                               | messages                                                                                                           |
| dialogAction.message.contentType                                   | messages[\*].contentType                                                                                           |
| dialogAction.message.content                                       | messages[\*].content                                                                                               |
| dialogAction.responseCard                                          | messages[\*].imageResponseCard                                                                                     |
| dialogAction.responseCard.version                                  | N/A                                                                                                                |
| dialogAction.responseCard.contentType                              | messages[\*].contentType                                                                                           |
| dialogAction.responseCard.genericAttachments                       | N/A                                                                                                                |
| dialogAction.responseCard.genericAttachments[\*].title             | messages[\*].imageResponseCard.title                                                                               |
| dialogAction.responseCard.genericAttachments[\*].subTitle          | messages[\*].imageResponseCard.subtitle                                                                            |
| dialogAction.responseCard.genericAttachments[\*].imageUrl          | messages[\*].imageResponseCard.imageUrl                                                                            |
| dialogAction.responseCard.genericAttachments[\*].buttons           | messages[\*].imageResponseCard.buttons                                                                             |
| dialogAction.responseCard.genericAttachments[\*].buttons[\*].value | messages[\*].imageResponseCard.buttons[\*].value                                                                   |
| dialogAction.responseCard.genericAttachments[\*].buttons[\*].text  | messages[\*].imageResponseCard.buttons[\*].text                                                                    |
| dialogAction.kendraQueryRequestPayload                             | dialogAction.kendraQueryRequestPayload                                                                             |
| dialogAction.kendraQueryFilterString                               | dialogAction.kendraQueryFilterString                                                                               | #### Intents and slots Intent and slot fields that were part of the `dialogAction` structure are now part of the `sessionState` structure.                                                                                                                                                                                                                                                                                |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| dialogAction.intentName                                            | sessionState.intent.name                                                                                           |
| dialogAction.slots                                                 | sessionState.intent.slots                                                                                          |
| dialogAction.slots[\*].key                                         | sessionState.intent.slots[\*].key                                                                                  |
| dialogAction.slots[\*].value                                       | sessionState.intent.slots[\*].value.interpretedValue                                                               |
| N/A                                                                | sessionState.intent.slots[\*].value.shape                                                                          |
| N/A                                                                | sessionState.intent.slots[\*].values                                                                               | #### Others The `sessionAttributes` structure is now part of the `sessionState` structure. The `recentIntentSummaryReview` structure has been removed.                                                                                                                                                                                                                                                                    |
| V1 structure                                                       | V2 structure                                                                                                       |
| ---                                                                | ---                                                                                                                |
| sessionAttributes                                                  | sessionState.sessionAttributes                                                                                     |
| recentIntentSummaryView                                            | N/A                                                                                                                |
