End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# AMAZON.RepeatIntent

Responds to words and phrases that enable the user to repeat
the previous message. Your application needs to use a Lambda
function to save the previous intent information in session
variables, or you need to use the [GetSession](API_runtime_GetSession.md "API_runtime_GetSession.md") operation to get
the previous intent information.

Common utterances:

- repeat
- say that again
- repeat that
