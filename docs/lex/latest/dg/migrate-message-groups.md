End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Message groups

Amazon Lex V2 supports only one message and two alternative messages
per message group. If you have more than three messages per
message group in an Amazon Lex V1 bot, only the first three messages
are migrated. To use more messages in a message group, use a
Lambda function to output various messages.
