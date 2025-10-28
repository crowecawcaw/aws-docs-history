# Set values during the

conversation

Amazon Lex V2 provides the ability to set slot values
and session attribute values at every step of the conversation. You
can then use these values during the conversation to evaluate conditions
or use them during intent fulfillment.

You can set slot values for the current intent. If the next
step in the conversation is to invoke another intent, you can set
slot values of the new intent.

If the assigned slot is not filled, or if the JSON path cannot be parsed,
then the attribute will be set to `null`.

Use the following syntax when using slot values and session
attributes:

- **Slot values** –
  surround the slot name with braces ("{ }"). For slot values
  in the current intent, you only need to use the slot name.
  For example, `{slot}`. If you are setting a value
  in the next intent, you must use both the intent name and
  the slot name to identify the slot. For example,
  `{intent.slot}`.

Examples:

    + `{PhoneNumber} = "1234567890"`
    + `{CheckBalance.AccountNumber} = "99999999"`
    + `{BookingID} = "ABC123"`
    + `{FirstName} = "John"`

The value of a slot can be any of the following:

    + a constant string
    + a JSON path that refers to the transcriptions block in the
     Amazon Lex response (for en-US and en-GB)
    + a session attribute

Examples:

    + `{username} = "john.doe"`
    + `{username_confidence} =
     $.transcriptions[0].transcriptionConfidence`
    + `{username_slot_value} = [username]`

###### Note

Slot values can also be set to `null`.
If you need to re-elicit a slot value that has been filled,
you must set the value to `null` before prompting the
customer for the slot value again. If the assigned slot is not
filled, or if the JSON path cannot be parsed, then the attribute
will be set to `null`.

- **Session attributes**
  – surround the attribute name with square brackets ("[
  ]"). For example, `[sessionAttribute]`.

Examples:

    + `[username] = "john.doe"`
    + `[username_confidence] = $.transcriptions[0].transcriptionConfidence`
    + `[username_slot_value] = {username}`

The value of the session attribute can be any of the following:

    + a constant string
    + a JSON path that refers to the transcriptions block in the
     Amazon Lex response (for en-US and en-GB)
    + a slot value reference

###### Note

If the assigned slot is not filled, or if the JSON path
cannot be parsed, then the attribute will be set to
`null`.

###### Note

On August 17, 2022, Amazon Lex V2 released a change to the way conversations
are managed with the user. This change gives you more control over
the path that the user takes through the conversation. For more information,
see [Changes to conversation flows in Amazon Lex V2](understanding-new-flows.md "understanding-new-flows.md").
Bots created before August 17, 2022 do not support dialog code hook messages, setting values,
configuring next steps, and adding conditions.
