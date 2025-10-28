# View the details of an opt-out list in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to manage your opt-out lists.

View opt-out list (Console)
To view an opt-out list using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under
   **Configurations**, choose
   **Opt-out lists**.
3. On the **Opt-out lists** page, choose an opt-out list and view the **Opt-out list details**.

Describe opt-out lists (AWS CLI)You can use the [describe-opt-out-lists](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.md") command to view information about the opt-out lists in your
AWS End User Messaging SMS account.

###### To view information about all of your opt-out lists using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-opt-out-lists
```

You can also view information about specific opt-out lists by using the
`OptOutListNames` parameter.

###### To view information about specific opt-out lists using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 describe-opt-out-lists \
`>` --opt-out-list-names `optOutListName`
```

In the preceding command, replace `optOutListName`
with the name or Amazon Resource Name (ARN) of the opt-out list that you want to
find more information about. You can also specify multiple opt-out lists by
separating each list name with a space.

The AWS CLI returns the following information about all of the opt-out lists in
your account.
