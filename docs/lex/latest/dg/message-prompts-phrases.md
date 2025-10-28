End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Prompts and phrases

Amazon Lex V2 uses a different mechanism for follow up,
clarification, and hang up prompts.

For follow up prompts, use context carryover to switch to a
different intent after fulfillment.

For example, suppose that you have an intent to book a car
rental that is configured to return a output context called
`book_car_fulfilled`. When the intent is
fulfilled, Amazon Lex sets the output context variable to
`book_car_fulfilled`. Since
`book_car_fulfilled` is an active context, an
intent with `book_car_fulfilled` as an input context
is considered for recognition, as long as the user utterance is
recognized as an attempt to elicit that intent. You can use this
for intents that only make sense after booking a car, such as
emailing a receipt or modifying a reservation.

Amazon Lex V2 does not support clarification prompts and hang up
phrases (abort statements). Amazon Lex V2 bots contain a default
fallback intent that is invoked if no intents are matched. To
send a clarification prompt with retries, configure a Lambda
function and enable the dialog code hook in the fallback intent.
The Lambda function can output a clarification prompt as a
response and the retry value in a session attribute. If the
retry value exceeds the maximum number of retries, you can
output a hang up phrase and close the conversation.
