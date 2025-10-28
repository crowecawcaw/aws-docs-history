# Viewing text logs in Amazon CloudWatch Logs from Lex V2

Amazon Lex V2 stores text logs for your conversations in Amazon CloudWatch Logs. To view
the logs, use the CloudWatch Logs console or API. For more information, see [Search Log Data Using Filter Patterns](../../../AmazonCloudWatch/latest/logs/SearchDataFilterPattern.md "../../../AmazonCloudWatch/latest/logs/SearchDataFilterPattern.md") and [CloudWatch Logs Insights Query Syntax](../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md "../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md") in the _Amazon CloudWatch Logs User
Guide_.

###### To view logs using the Amazon Lex V2 console

1. Open the Amazon Lex V2 console [https://console.aws.amazon.com/lexv2](https://console.aws.amazon.com/lexv2 "https://console.aws.amazon.com/lexv2").
2. From the list, choose a bot.
3. From the left menu, choose **Analytics** and then
   choose **CloudWatch metrics**.
4. View metrics for your bot on the **CloudWatch metrics**
   page.
   You can also use the CloudWatch console or API to view your log entries. To
   find the log entries, navigate to the log group that you configured for
   the alias. You can find the log stream prefix for your logs in the Amazon Lex V2
   console or by using the [DescribeBotAlias](../APIReference/API_DescribeBotAlias.md "../APIReference/API_DescribeBotAlias.md") operation.

Log entries for a user utterance are found in multiple log streams. An
utterance in the conversation has an entry in one of the log streams with
the specified prefix. An entry in the log stream contains the following
information:

message-version

The message schema version.

bot

Details about the bot that the customer is interacting
with.

messages

The response that the bot sent back to the user.

utteranceContext

Information about processing this utterance.

- `runtimeHints`—runtime context used to
  transcribe and interpret the user's input. For more information,
  see [Improving recognition of slot values with runtime hints in the conversation](using-hints.md "using-hints.md").
- `slotElicitationStyle`—Slot elicitation
  style used to interpret user input. For more information, see
  [Capturing slot values with spelling styles during the conversation](spelling-styles.md "spelling-styles.md").

sessionState

The current state of the conversation between the user and the
bot. For more information, see [Understanding bot conversations](managing-conversations.md "managing-conversations.md").

interpretations

A list of intents that Amazon Lex V2 determined could satisfy the
user's utterance. [Using confidence
scores to improve conversation accuracy](confidence-scores.md "confidence-scores.md").

interpretationSource

Indicates whether a slot is resolved by or Amazon Bedrock. Values: Lex | Bedrock

sessionId

The identifier of the user session that is having the
conversation.

inputTranscript

A transcription of the input from the user.

- For text input, this is the text that the user typed. For DTMF input, this is the key that the user input.
- For speech input, this is the text to which Amazon Lex V2 converts the user utterance in order to invoke an intent or fill a slot.

rawInputTranscript

The raw transcript of the user input before any text processing is applied.
Note: Text processing is only for en-US and en-GB locales.

transcriptions

A list of potential transcriptions of the user's input. For more
information, see [Using voice transcription confidence scores to improve conversations with your Lex V2 bot](using-transcript-confidence-scores.md "using-transcript-confidence-scores.md").

rawTranscription

Using voice transcription confidence scores. For more
information, see [Using voice transcription confidence scores to improve conversations with your Lex V2 bot](using-transcript-confidence-scores.md "using-transcript-confidence-scores.md").

missedUtterance

Indicates whether Amazon Lex V2 was able to recognize the user's
utterance.

requestId

Amazon Lex V2 generated request ID for the user input.

timestamp

The timestamp of the user's input.

developerOverride

Indicates whether the conversation flow was updated using a
dialog code hook. For more information on using a dialog code hook,
see [Integrating an AWS Lambda function into your bot](lambda.md "lambda.md").

inputMode

Indicates the type of input. Can be audio, DTMF, or text.

requestAttributes

The request attributes used when processing the user's
input.

audioProperties

If audio conversation logs are enabled and the user input was in
audio format, includes the total duration of the audio input, the
duration of voice and the duration of silence in the audio. It also
includes a link to the audio file.

bargeIn

Indicates whether the user input interrupted the previous bot
response.

responseReason

The reason a response was generated. Can be one of:

- `UtteranceResponse` – response to user
  input
- `StartTimeout` – server generated response
  when the user didn't provide input
- `StillWaitingResponse` – server generated
  response when the user requests the bot wait
- `FulfillmentInitiated` – server generated
  response that fulfillment is about to be initiated
- `FulfillmentStartedResponse` – server
  generated response that fulfillment has begun
- `FulfillmentUpdateResponse` – periodic
  server generated response while fulfillment is in
  progress
- `FulfillmentCompletedResponse` – server
  generated response when fulfillment is complete.

operationName

The API used to interact with the bot. Can be one of
`PutSession`, `RecognizeText`,
`RecognizeUtterance`, or
`StartConversation`.

```

{
    "message-version": "2.0",
    "bot": {
        "id": "string",
        "name": "string",
        "aliasId": "string",
        "aliasName": "string",
        "localeId": "string",
        "version": "string"
    },
    "messages": [
        {
            "contentType": "PlainText | SSML | CustomPayload | ImageResponseCard",
            "content": "string",
            "imageResponseCard": {
                "title": "string",
                "subtitle": "string",
                "imageUrl": "string",
                "buttonsList": [
                    {
                        "text": "string",
                        "value": "string"
                    }
                ]
            }
        }
    ],
    "utteranceContext": {
        "activeRuntimeHints": {
            "slotHints": {
                "string": {
                    "string": {
                        "runtimeHintValues": [
                            {
                                "phrase": "string"
                            },
                            {
                                "phrase": "string"
                            }
                        ]
                    }
                }
            }
        },
        "slotElicitationStyle": "string"
    },
    "sessionState": {
        "dialogAction": {
            "type": "Close | ConfirmIntent | Delegate | ElicitIntent | ElicitSlot",
            "slotToElicit": "string"
        },
        "intent": {
            "name": "string",
            "slots": {
                "string": {
                    "value": {
                       "interpretedValue": "string",
                       "originalValue": "string",
                       "resolvedValues": [ "string" ]
                    }
                 },
                "string": {
                    "shape": "List",
                    "value": {
                        "originalValue": "string",
                        "interpretedValue": "string",
                        "resolvedValues": [ "string" ]
                    },
                    "values": [
                        {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "string",
                                "interpretedValue": "string",
                                "resolvedValues": [ "string" ]
                            }
                        },
                        {
                            "shape": "Scalar",
                            "value": {
                                "originalValue": "string",
                                "interpretedValue": "string",
                                "resolvedValues": [ "string" ]
                            }
                        }
                    ]
                }
            },
            "kendraResponse": {
                // Only present when intent is KendraSearchIntent. For details, see
                // https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html#API_Query_ResponseSyntax
                },
            "state": "InProgress | ReadyForFulfillment | Fulfilled | Failed",
            "confirmationState": "Confirmed | Denied | None"
        },
        "originatingRequestId": "string",
        "sessionAttributes": {
            "string": "string"
        },
        "runtimeHints": {
            "slotHints": {
                "string": {
                    "string": {
                        "runtimeHintValues": [
                            {
                                "phrase": "string"
                            },
                            {
                                "phrase": "string"
                            }
                        ]
                    }
                }
            }
        }
    },
   "dialogEventLogs": [
        {
	  // only for conditional
     "conditionalEvaluationResult":[
      // all the branches until true

     {
     "conditionalBranchName": "string",
     "expressionString": "string",
     "evaluatedExpression": "string",
     "evaluationResult": "true | false"
     }
    ],
  "dialogCodeHookInvocationLabel": "string",
  "response": "string",
  "nextStep": {
        "dialogAction": {
            "type": "Close | ConfirmIntent | Delegate | ElicitIntent | ElicitSlot",
            "slotToElicit": "string"
        },
	      "intent": {
                          "name": "string",
           "slots": {
               }
        }
       }
    ]
    "interpretations": [
        {
            "interpretationSource": "Bedrock | Lex",
            "nluConfidence": "string",
            "intent": {
                "name": "string",
                "slots": {
                    "string": {
                        "value": {
                            "originalValue": "string",
                            "interpretedValue": "string",
                            "resolvedValues": [ "string" ]
                        }
                    },
                    "string": {
                        "shape": "List",
                        "value": {
                            "interpretedValue": "string",
                            "originalValue": "string",
                            "resolvedValues": [ "string" ]
                        },
                        "values": [
                            {
                                "shape": "Scalar",
                                "value": {
                                    "interpretedValue": "string",
                                    "originalValue": "string",
                                    "resolvedValues": [ "string" ]
                                }
                            },
                            {
                                "shape": "Scalar",
                                "value": {
                                    "interpretedValue": "string",
                                    "originalValue": "string",
                                    "resolvedValues": [ "string" ]
                                }

                            }
                        ]
                    }
                },
                "kendraResponse": {
                    // Only present when intent is KendraSearchIntent. For details, see
                    // https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html#API_Query_ResponseSyntax
                    },
                "state": "InProgress | ReadyForFulfillment | Fulfilled | Failed",
                "confirmationState": "Confirmed | Denied | None"
                },
            "sentimentResponse": {
                "sentiment": "string",
                "sentimentScore": {
                    "positive": "string",
                    "negative": "string",
                    "neutral": "string",
                    "mixed": "string"
                }
            }
        }
    ],
    "sessionId": "string",
    "inputTranscript": "string",
    "rawInputTranscript": "string",
    "transcriptions": [
        {
            "transcription": "string",
            "rawTranscription": "string",
            "transcriptionConfidence": "number",
            },
            "resolvedContext": {
                "intent": "string"
            },
            "resolvedSlots": {
                "string": {
                    "name": "slotName",
                    "shape": "List",
                    "value": {
                        "originalValue": "string",
                        "resolvedValues": [
                            "string"
                        ]
                    }
                }
            }
        }
    ],
    "missedUtterance": "bool",
    "requestId": "string",
    "timestamp": "string",
    "developerOverride": "bool",
    "inputMode": "DTMF | Speech | Text",
    "requestAttributes": {
        "string": "string"
    },
    "audioProperties": {
        "contentType": "string",
        "s3Path": "string",
        "duration": {
            "total": "integer",
            "voice": "integer",
            "silence": "integer"
        }
    },
    "bargeIn": "string",
    "responseReason": "string",
    "operationName": "string"
}

```

The contents of the log entry depend on the result of a transaction
and the configuration of the bot and request.

- The `intent`, `slots`, and
  `slotToElicit` fields don't appear in an entry if the
  `missedUtterance` field is `true`.
- The `s3PathForAudio` field doesn't appear if audio logs
  are disabled or if the `inputDialogMode`field is
  `Text`.
- The `responseCard` field only appears when you have
  defined a response card for the bot.
- The `requestAttributes` map only appears if you have
  specified request attributes in the request.
- The `kendraResponse` field is only present when the
  `AMAZON.KendraSearchIntent` makes a request to search an
  Amazon Kendra index.
- The `developerOverride` field is true when an
  alternative intent was specified in the bot's Lambda function.
- The `sessionAttributes` map only appears if you have
  specified session attributes in the request.
- The `sentimentResponse` map only appears if you
  configure the bot to return sentiment values.

###### Note

The input format may change without a corresponding change in the
`messageVersion`. Your code should not throw an error if
new fields are present.
