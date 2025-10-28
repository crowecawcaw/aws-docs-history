End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Encryption at Rest

Amazon Lex encrypts the user utterances that it stores.

###### Topics

- [Sample Utterances](#at-rest-sample "#at-rest-sample")
- [Customer Utterances](#at-rest-utterances "#at-rest-utterances")
- [Session Attributes](#at-rest-session "#at-rest-session")
- [Request Attributes](#at-rest-request "#at-rest-request")

## Sample Utterances

When you develop a bot, you can provide sample utterances for each
intent and slot. You can also provide custom values and synonyms for
slots. This information is encrypted at rest, and it is used to build
the bot and to create the user experience.

## Customer Utterances

Amazon Lex encrypts utterances that users send to your bot unless the
`childDirected` field is set to `true`.

When the `childDirected` field is set to
`true`, no user utterances are stored.

When the `childDirected` field is set to
`false` (the default), user utterances are encrypted and
stored for 15 days for use with the [GetUtterancesView](API_GetUtterancesView.md "API_GetUtterancesView.md") operation. To delete stored
utterances for a specific user, use the [DeleteUtterances](API_DeleteUtterances.md "API_DeleteUtterances.md") operation .

When your bot accepts voice input, the input is stored
indefinitely. Amazon Lex uses it to improve your bot's ability to respond
to user input.

Use the [DeleteUtterances](API_DeleteUtterances.md "API_DeleteUtterances.md") operation to delete stored
utterances for a specific user.

## Session Attributes

Session attributes contain application-specific information that
is passed between Amazon Lex and client applications. Amazon Lex passes session
attributes to all AWS Lambda functions configured for a bot. If a Lambda
function adds or updates session attributes, Amazon Lex passes the new
information back to the client application.

Session attributes persist in an encrypted store for the duration
of the session. You can configure the session to remain active for a
minimum of 1 minute and up to 24 hours after the last user utterance.
The default session duration is 5 minutes.

## Request Attributes

Request attributes contain request-specific information and apply
only to the current request. A client application uses request
attributes to send information to Amazon Lex at runtime.

You use request attributes to pass information that doesn't need
to persist for the entire session. Because request attributes don't
persist across requests, they aren't stored.
