# Delete an opt-out list in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to delete an opt-out list.

Delete opt-out list (Console)
To delete an opt-out list using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under
   **Configurations**, choose
   **Opt-out lists**.
3. On the **Opt-out lists** page, choose an opt-out list, choose **Delete**.

Delete opt-out list (AWS CLI)
You can use the [delete-opt-out-list](../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-opt-out-list.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-opt-out-list.md") command to delete an opt-out list

At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 delete-opt-out-list \
`>` --opt-out-list-name `optOutListName`
```

In the preceding example, replace `optOutListName`
with a name that makes the opt-out list easy to identify.
