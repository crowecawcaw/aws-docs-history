# Delete a configuration set in AWS End User Messaging SMS

Use the AWS End User Messaging SMS console or AWS CLI to delete a configuration set.

Deleting a configuration set (Console)
To delete a configuration set using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Configuration sets**.
3. Select the **Configuration set** you want to delete and then choose
   **Delete**.

Deleting a configuration set (AWS CLI)
You can use the [delete-configuration-set](../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-configuration-set.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/delete-configuration-set.md") command to delete a configuration set.

```
`$` aws pinpoint-sms-voice-v2 delete-configuration-set \
`>` --configuration-set-name `configurationSet`
```

In the preceding command, replace `configurationSet`
with the name of the configuration set that you want to delete.
