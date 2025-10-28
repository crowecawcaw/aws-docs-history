# Guidelines and best practices

Refer to the following guidelines and best practices to optimize your bot's behavior and interactions with customers.

**Signing requests**

All Amazon Lex V2 model-building and runtime requests in the [API Reference](../APIReference/welcome.md "../APIReference/welcome.md")
use signature V4 for authenticating requests. For more
information about authenticating requests, see [Signature Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the
AWS General Reference.

**Protecting confidential information**

The runtime API operations [RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md") and
[RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md") take a session ID as a required parameter. Developers
can set this to any value that meets the constraints described in the API. We recommend
that you not use this parameter to send any confidential
information, such as user logins, emails, or social security numbers. This ID is primarily used to
uniquely identify a conversation with a bot.

**Capturing slot values from user utterances**

Amazon Lex V2 uses the enumeration values that you provide in a slot type definition to train
its machine learning models. Suppose that you define an intent called
`GetPredictionIntent` with the following sample utterance:

```
"Tell me the prediction for {sign}"
```

where {sign} is a slot with the custom type `ZodiacSign` that has 12
enumeration values: `Aries` through `Pisces`. Now suppose the user
says "Tell me the prediction for earth":

- Amazon Lex V2 infers that "earth" is a ZodiacSign value if you do one of the
  following actions:
  - Set the `valueSelectionStrategy` field to
    `ORIGINAL_VALUE` using the [CreateSlotType](../APIReference/API_CreateSlotType.md "../APIReference/API_CreateSlotType.md")
    operation
  - Select **Expand values** in the console

- Amazon Lex V2 does not recognize the value "earth" if you limit recognition to the
  values that you defined for the slot type by doing one of the following
  actions:

      + Set the `valueSelectionStrategy` field to
       `TOP_RESOLUTION` using the `CreateSlotType`
       operation
      + Select **Restrict to slot values and synonyms** in
       the console

  When you define synonyms for slot values, they are recognized to be the same as a slot
  value. However, the slot value is returned instead of the synonym.

Because Amazon Lex V2 passes this value to your client application or to the
Lambda function, you should check that the slot values are valid values before
using them in your fulfillment activity.

When Amazon Lex V2 calls a Lambda function or returns the result of a speech interaction with
your client, the case of the slot values is not guaranteed. In text interactions, the
case of the slot values matches the text entered or the slot value, depending on the
value of the `valueResolutionStrategy` field.

**Acronyms in slot values**

When defining slot values that contain acronyms, use the following patterns:

- Capital letters separated by periods (D.V.D.)
- Capital letters separated by spaces (D V D)
  **Built-in slots for date and time**

The [AMAZON.Date](built-in-slot-date.md "built-in-slot-date.md")
and [AMAZON.Time](built-in-slot-time.md "built-in-slot-time.md") built-in
slot types capture dates and times (both absolute and relative). Relative dates
and times are resolved at the time and date that Amazon Lex V2 receives the request
and in the region where it processes the request.

For the `AMAZON.Time` built-in slot type, if the user doesn't
specify that a time is before or after noon, the time is ambiguous. In that case, Amazon Lex V2
will prompt the user again. We recommend prompts that elicit an absolute time. For
example, use a prompt such as "When do you want your pizza delivered? You can say 6 PM
or 6 in the evening."

**Avoiding ambiguity in training data for your bot**

Providing confusable training data in your bot reduces the ability of Amazon Lex V2
to understand user input. Suppose you have two intents (`OrderPizza` and
`OrderDrink`) in your
bot, and you include "I want to order" as a sample utterance. When you build your bot, Amazon Lex V2
is unable to map this utterance to a specific intent. As a
result, when a user inputs this utterance at runtime, Amazon Lex V2 can't pick an intent with a
high degree of confidence.

If you have two intents with the same sample utterance, use input contexts to help
Amazon Lex V2 distinguish between the two intents at runtime. For more information, see [Setting
intent context](context-mgmt-active-context.md "context-mgmt-active-context.md").

**Using the TSTALIASID alias**

- The TSTALIASID alias of your bot points to the
  Draft version and should only be used for manual
  testing. Amazon Lex limits the number of runtime requests
  that you can make to the TSTALIASID alias of the
  bot.
- When you update the Draft version of the bot, Amazon Lex shuts down any
  in-progress conversations for any client application using the TSTALIASID alias
  of the bot. Generally, you should not use the TSTALIASID alias of a bot in
  production because the Draft version can be updated. You should publish a
  version and an alias and use them instead.
- When you update an alias, Amazon Lex takes a few
  minutes to pick up the changes. When you modify the
  Draft version of the bot, the change is picked up by
  the TSTALIASID alias immediately.
