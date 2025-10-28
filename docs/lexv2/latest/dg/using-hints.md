# Improving recognition of slot values with runtime hints in the conversation

With _runtime hints_ you can give Amazon Lex V2 a set of
slot values based on context to get better recognition in audio
conversations and improved slot resolutions. You can use runtime hints
to provide a list of phrases at runtime that become candidates for the
resolution of a slot value.

For example, if a user interacting with a flight reservation bot
frequently travels to San Francisco, Jakarta, Seoul, and Moscow you can
configure runtime hints with a list of these four cities when eliciting
for the destination to improve recognition for frequently travelled
cities.

Runtime hints are only available in the English (US) and English (UK)
languages. They can be used with the following slot types:

- Custom slot types
- AMAZON.City
- AMAZON.Country
- AMAZON.FirstName
- AMAZON.LastName
- AMAZON.State
- AMAZON.StreetName
  **Runtime hints basics**

- Runtime hints are used only when eliciting a slot value from a
  user.
- When you use runtime hints, the values of the hints are
  preferred over similar values. For example, for a food ordering
  bot, you can set a list of menu items as runtime hints while
  eliciting for food items in a custom slot to prefer “fillet”
  over similar sounding “fella”.
- If the user input is different from the values provided in
  runtime hints, the original user input will be used for the
  slot.
- For custom slot types, values provided as runtime hints will
  be used for resolution of the slot even if they are not part of
  the custom slot during bot creation.
- Runtime hints are supported only for 8 kHz audio input. They
  are available with [contact center
  integrations](contact-center.md "contact-center.md") supported by Amazon Lex V2. Runtime hints
  aren't provided for audio input from the [test window](test-bot.md "test-bot.md") on the Amazon Lex V2 console because it uses
  16 kHz audio input.

###### Note

Before you can use runtime hints with an existing bot, you
must first rebuild the bot. Existing versions of a bot don't support
runtime hints. You must create a new version of the bot to use
them.

You can send runtime hints to Amazon Lex V2 using the
[PutSession](../APIReference/API_runtime_PutSession.md "../APIReference/API_runtime_PutSession.md"),
[RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md"),
[RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md"), or
[StartConversation](../APIReference/API_runtime_StartConversation.md "../APIReference/API_runtime_StartConversation.md") operation. You can
also add runtime hints using a Lambda function.

You can send runtime hints at the beginning of a conversation to
configure the hints for each slot used in the bot, or you can send hints
as part of the session state during a conversation. The
`runtimeHints` attribute maps a slot to the hints for
that slot.

Once you send a runtime hint to Amazon Lex V2, they persist for every turn of
the conversation until the session ends. If you send a null
`runtimeHints` structure, the existing hints are used.
You can modify the hints by:

- Sending a new `runtimeHints` structure to the bot.
  The contents of the new structure replace the existing
  ones.
- Sending an empty `runtimeHints` structure to the
  bot. This clears the runtime hints for the bot.

## Adding slot values in context

Add context for your bot by providing expected slot values as runtime hints when your application has information about the user's next likely utterance. Add a Lambda dialog code hook to your bot (see [Integrating an AWS Lambda function into your bot](lambda.md "lambda.md") for more information) and use the **proposedNextState** field in the [AWS Lambda input event format for Lex V2](lambda-input-format.md "lambda-input-format.md") to determine the runtime hints that you should include to improve the conversation with the user.

For example, in a banking app you can generate a list of account
nicknames for a specific user, and then use the list when eliciting
the account that the user wants to access.

Send runtime hints at the start of the conversation when you have
context to help your bot interpret user input. For example, if you
have the user's phone number, you can use this information to look
up the user so that you can use the `PutSession` or
`StartConversation` operation to pass first and last
name hints to the bot if you are eliciting for the user's name to
validate their credentials.

During a conversation, you might gather information from one slot
value that can help with another slot value. For example, in a car
care app when you have the user's account number you can do a look
up to find the cars that the customer owns and pass them along as
hints to another slot.

Enter acronyms, or other words whose letters should be pronounced
individually, as single letters separated by a period and a space.
Don't use individual letters unless they are part of a phrase, such
as "J. P. Morgan" or “A.W.S”. You can use upper- or lower-case
letters to define an acronym.

## Adding hints to a slot

To add runtime hints to a slot, you use the
`runtimeHints` structure that is part of the
`sessionState` structure. The following is an example
of the `runtimeHints` structure. It provides hints for
two slots, "FirstName" and "LastName" for the "MakeAppointment"
intent.

```
{
    "sessionState": {
        "intent": {},
        "activeContexts": [],
        "dialogAction": {},
        "originatingRequestId": {},
        "sessionAttributes": {},
        "runtimeHints": {
            "slotHints": {
                "MakeAppointment": {
                    "FirstName": {
                        "runtimeHintValues": [
                            {
                                "phrase": "John"
                            },
                            {
                                "phrase": "Mary"
                            }
                        ]
                    },
                    "LastName": {
                        "runtimeHintValues": [
                            {
                                "phrase": "Stiles"
                            },
                            {
                                "phrase": "Major"
                            }
                        ]
                    }
                }
            }
        }
    }
}
```

You can also use a Lambda function to add runtime hints during a
conversation. To add runtime hints, you add the
`runtimeHints` structure to the session state of the
response that your Lambda function sends to Amazon Lex V2. For more
information, see [AWS Lambda response format for Lex V2](lambda-response-format.md "lambda-response-format.md").

You must specify a valid `intentName` and
`slotName` in the request, otherwise Amazon Lex V2 returns a
runtime error.
