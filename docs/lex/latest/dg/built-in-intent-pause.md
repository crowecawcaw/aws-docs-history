End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# AMAZON.PauseIntent

Responds to words and phrases that enable the user to pause an
interaction with a bot so that they can return to it later. Your
Lambda function or application needs to save intent data in
session variables, or you need to use the [GetSession](API_runtime_GetSession.md "API_runtime_GetSession.md") operation to
retrieve intent data when you resume the current intent.

Common utterances:

- pause
- pause that
