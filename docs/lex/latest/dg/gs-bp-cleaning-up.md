End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 7 (Optional): Clean Up

(Console)

Now, delete the resources that you created and clean up your
account.

You can delete only resources that are not in use. In general, you
should delete resources in the following order:

- Delete bots to free up intent resources.
- Delete intents to free up slot type resources.
- Delete slot types last.

###### To clean up your account (console)

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the list of bots, choose the check box next to
   **OrderFlowers**.
3. To delete the bot, choose **Delete**, and
   then choose **Continue** in the
   confirmation dialog box.
4. In the left pane, choose
   **Intents**.
5. In the list of intents, choose
   **OrderFlowersIntent**.
6. To delete the intent, choose **Delete**,
   and then choose **Continue** in the
   confirmation dialog box.
7. In the left pane, choose **Slot
   types**.
8. In the list of slot types, choose
   **Flowers**.
9. To delete the slot type, choose
   **Delete**, and then choose
   **Continue** in the confirmation dialog
   box.
   You have removed all of the Amazon Lex resources that you created and
   cleaned up your account. If desired, you can use the [Lambda
   console](https://console.aws.amazon.com/lambda "https://console.aws.amazon.com/lambda") to delete the Lambda function used in this
   exercise.
