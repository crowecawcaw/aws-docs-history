End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 4 (Optional): Clean up

Delete the resources that you created and clean up your account to avoid incurring
more charges for the resources you created.

You can delete only resources that are not in use. For example, you cannot delete a
slot type that is referenced by an intent. You cannot delete an intent that is
referenced by a bot.

Delete resources in the following order:

- Delete bots to free up intent resources.
- Delete intents to free up slot type resources.
- Delete slot types last.

###### To clean up your account

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the list of bots, choose **PizzaOrderingBot**.
3. To delete the bot, choose **Delete**, and then choose
   **Continue**.
4. In the left pane, choose **Intents**.
5. In the list of intents, choose **OrderPizza**.
6. To delete the intent, choose **Delete**, and then choose
   **Continue**.
7. In the left menu, choose **Slot types**.
8. In the list of slot types, choose **Crusts**.
9. To delete the slot type, choose **Delete**, and then choose
   **Continue**.
10. Repeat [Step 8](#chooseSlots "#chooseSlots") and [Step 9](#deleteSlots "#deleteSlots") for the
    `Sizes` and `PizzaKind` slot types.
    You have removed all of the resources that you created and cleaned up your
    account.

## Next Steps

- [Publish
  a Version and Create an Alias](gettingstarted-ex3.md "gettingstarted-ex3.md")
- [Create an Amazon Lex bot
  with the AWS Command Line Interface](gs-cli.md "gs-cli.md")
