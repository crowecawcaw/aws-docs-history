End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# AMAZON.StopIntent

Responds to words and phrases that indicate that the user
wants to stop processing the current intent and end the
interaction with a bot. Your Lambda function or application
should clear any existing attributes and slot type values and
then end the interaction.

Common utterances:

- stop
- off
- shut up
