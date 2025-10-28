# Create an opt-out list in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to create an opt-out list.

Create opt-out list (Console)
To create an opt-out list using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under
   **Configurations**, choose
   **Opt-out lists**.
3. On the **Opt-out lists** page, choose an opt-out list and then choose **Edit**.
4. On the **List details** page enter a **List name**.
5. Choose **Create list**.

Create opt-out list (AWS CLI)
At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 create-opt-out-list \
`>` --opt-out-list-name `optOutListName`
```

In the preceding example, replace `optOutListName`
with a name that makes the opt-out list easy to identify.
