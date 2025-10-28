# Using intent confidence

scores to improve intent selection with Lex V2

When a user makes an utterance, Amazon Lex V2 uses natural language
understanding (NLU) to understand the user's request and return the
proper intent. By default Amazon Lex V2 returns the most likely intent defined
by your bot.

In some cases it may be difficult for Amazon Lex V2 to determine the most
likely intent. For example, the user might make an ambiguous utterance,
or there might be two intents that are similar. To help determine the
proper intent, you can combine your domain knowledge with the
_NLU confidence scores_ in a list of
interpretations. A confidence score is a rating that Amazon Lex V2 provides
that shows how confident it is that an intent is the correct
intent.

To determine the difference between two intents within an
interpretation, you can compare their confidence scores. For example, if
one intent has a confidence score of 0.95 and another has a score of
0.65, the first intent is probably correct. However, if one intent has a
score of 0.75 and another has a score of 0.72, there is ambiguity
between the two intents that you may be able to discriminate using
domain knowledge in your application.

You can also use confidence scores to create test applications that
determine if changes to an intent's utterances make a difference in the
behavior of the bot. For example, you can get the confidence scores for
a bot's intents using a set of utterances, then update the intents with
new utterances. You can then check the confidence scores to see if there
was an improvement.

The confidence scores that Amazon Lex V2 returns are comparative values. You
should not rely on them as an absolute score. The values may change
based on improvements to Amazon Lex V2.

Amazon Lex V2 returns the most likely intent and up to 4 alternative intents
with their associated scores in the `interpretations`
structure in each response. The following JSON code shows the
`interpretations` structure in the response from the
[RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md") operation:

```
   "interpretations": [
      {
         "intent": {
            "confirmationState": "string",
            "name": "string",
            "slots": {
               "string" : {
                  "value": {
                     "interpretedValue": "string",
                     "originalValue": "string",
                     "resolvedValues": [ "string" ]
                  }
               }
            },
            "state": "string"
         },
         "nluConfidence": number
      }
   ]

```

## AMAZON.FallbackIntent

Amazon Lex V2 returns `AMAZON.FallbackIntent` as the top intent in
two situations:

1. If the confidence scores of all possible intents are less than
   the confidence threshold. You can use the default threshold or
   you can set your own threshold. If you have the
   `AMAZON.KendraSearchIntent` configured, Amazon Lex V2 returns it
   as well in this situation.
2. If the interpretation confidence for `AMAZON.FallbackIntent`
   is higher than the interpretation confidence of all other intents.

Note that Amazon Lex V2 does not display a confidence score for
`AMAZON.FallbackIntent`.

## Setting and changing

the confidence threshold

The confidence threshold must be a number between 0.00 and 1.00. You
can set the threshold for each language in your bot in the following ways:

**Using the Amazon Lex V2 console**

- To set the threshold when you add a language to your bot with
  **Add language**, you can insert your desired value
  in the **Confidence score threshold** panel.
- To update the threshold, you can select **Edit**
  in the **Language details** panel in a language
  for your bot. Then insert your desired value
  in the **Confidence score threshold** panel.

**Using API operations**

- To set the threshold, set the `nluIntentConfidenceThreshold`
  parameter of the [CreateBotLocale](../APIReference/API_CreateBotLocale.md "../APIReference/API_CreateBotLocale.md") operation.
- To update the confidence threshold, set the
  `nluIntentConfidenceThreshold`
  parameter of the [UpdateBotLocale](../APIReference/API_UpdateBotLocale.md "../APIReference/API_UpdateBotLocale.md") operation.

## Session

Management

To change the intent that Amazon Lex V2 uses in a conversation with the
user, you can use the response from your dialog code hook Lambda
function, or you can use the session management APIs in your custom
application.

### Using a Lambda

function with your Lex V2 bot

When you use a Lambda function, Amazon Lex V2 calls it with a JSON
structure that contains the input to the function. The JSON
structure contains a field called `currentIntent`
that contains the intent that Amazon Lex V2 has identified as the most
likely intent for the user's utterance. The JSON structure also
includes an `alternativeIntents` field that contains
up to four additional intents that may satisfy the user's
intent. Each intent includes a field called
`nluIntentConfidenceScore` that contains the
confidence score that Amazon Lex V2 assigned to the intent.

To use an alternative intent, you specify it in the
`ConfirmIntent` or the `ElicitSlot`
dialog action in your Lambda function.

For more information, see [Integrating an AWS Lambda function into your bot](lambda.md "lambda.md").

### Using the Session

Management API with your Lex V2 bot

To use a different intent from the current intent, use the
[PutSession](../APIReference/API_runtime_PutSession.md "../APIReference/API_runtime_PutSession.md") operation. For
example, if you decide that the first alternative is preferable
to the intent that Amazon Lex V2 chose, you can use the
`PutSession` operation to change intents so that
the next intent that the user interacts with is the one that you
selected.

For more information, see [Understanding Amazon Lex V2 bot sessions](managing-sessions.md "managing-sessions.md").
