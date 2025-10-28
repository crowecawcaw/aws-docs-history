End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Create an Intent

Now, create the `OrderPizza` intent , an action that the user wants to
perform, with the minimum information needed. You add slot types for the intent and
then configure the intent later.

###### To create an intent

1. In the Amazon Lex console, choose the plus sign (+) next to
   **Intents**, and then choose **Create new
   intent**.
2. In the **Create intent** dialog box, type the name of the
   intent (`OrderPizza`), and then choose
   **Add**.
   The console sends a request to Amazon Lex to create the `OrderPizza` intent.
   In this example you create slots for the intent after you create slot types.

## Next Step

[Create Slot Types](gs2-create-bot-slot-types.md "gs2-create-bot-slot-types.md")
