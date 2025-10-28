End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Sharing Information

Between Intents

Amazon Lex supports sharing information between intents. To share
between intents, use session attributes.

For example, a user of the `ShoeOrdering` bot starts by
ordering shoes. The bot engages in a conversation with the user,
gathering slot data, such as shoe size, color, and brand. When the
user places an order, the Lambda function that fulfills the order
sets the `orderNumber` session attribute, which contains
the order number. To get the status of the order, the user uses the
`GetOrderStatus` intent. The bot can ask the user for
slot data, such as order number and order date. When the bot has the
required information, it returns the status of the order.

If you think that your users might switch intents during the same
session, you can design your bot to return the status of the latest
order. Instead of asking the user for order information again, you
use the `orderNumber` session attribute to share
information across intents and fulfill the
`GetOrderStatus` intent. The bot does this by
returning the status of the last order that the user placed.

For an example of cross-intent information sharing, see [Book Trip](ex-book-trip.md "ex-book-trip.md").
