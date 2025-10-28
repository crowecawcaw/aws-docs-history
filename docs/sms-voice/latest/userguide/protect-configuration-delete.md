# Delete a protect configuration in AWS End User Messaging SMS

To delete a protect configuration, you can use the AWS End User Messaging SMS console, the
`DeleteProtectConfiguration` action in the AWS End User Messaging SMS and voice v2 API, or the
`aws sms-voice delete-protect-configuration` command in the AWS CLI. This
section shows how to delete a protect configuration using the AWS End User Messaging SMS console and the
AWS CLI.

###### Important

Deletion protection has to be disabled before you can delete a protect
configuration.

The protect configuration has to be disassociated from any configuration sets or the
_account default_ protect configuration before you can delete
it.

Delete a protect configuration (Console)
To delete a protect configuration using the AWS End User Messaging SMS console, follow these
steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Protect**, choose
   **Protect configuration**.
3. Choose the protect configuration to delete and then choose
   **Delete**.
4. On the **Delete protect configurations** enter
   `confirm` and choose
   **Delete**.

###### Note

If your protect configuration is still associated with a
configuration set or as the account default choose **Remove
associations**, then enter
`confirm`, and choose
**Delete**.

The protect configuration has now been removed from your account.

Delete a protect configuration (AWS CLI)
You can use the delete-protect-configuration command to delete a protect
configuration.

###### To delete a protect configuration

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 delete-protect-configuration --protect-configuration-id `ProtectConfigId`
```

In the preceding command, make the following changes:

    + Replace `ProtectConfigId` with the
     unique identifier of the protect configuration.
