End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Setting the Session

Timeout

Amazon Lex retains context information—slot data and session
attributes—until a conversation session ends. To control how
long a session lasts for a bot, set the session timeout. By default,
session duration is 5 minutes, but you can specify any duration
between 0 and 1,440 minutes (24 hours).

For example, suppose that you create a `ShoeOrdering`
bot that supports intents such as `OrderShoes` and
`GetOrderStatus`. When Amazon Lex detects that the
user's intent is to order shoes, it asks for slot data. For example,
it asks for shoe size, color, brand, etc. If the user provides some
of the slot data but doesn't complete the shoe purchase, Amazon Lex
remembers all of the slot data and session attributes for the entire
session. If the user returns to the session before it expires, he or
she can provide the remaining slot data, and complete the
purchase.

In the Amazon Lex console, you set the session timeout when you create
a bot. With the AWS command line interface (AWS CLI) or API, you set
the timeout when you create or update a bot with the [PutBot](API_PutBot.md "API_PutBot.md") operation by
setting the [idleSessionTTLInSeconds](API_PutBot.md#lex-PutBot-request-idleSessionTTLInSeconds "API_PutBot.md#lex-PutBot-request-idleSessionTTLInSeconds") field.
