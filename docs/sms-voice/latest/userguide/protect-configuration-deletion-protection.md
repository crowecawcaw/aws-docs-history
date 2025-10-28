# Set up deletion protection in AWS End User Messaging SMS

When you turn on deletion protection for a protect configuration you will not be able to
delete the protect configuration until deletion protection is disabled and the protect
configuration is no longer associated with a configuration set or the _account
default_ protect configuration. By default, deletion protection is
disabled.

To enable deletion protection for a protect configuration, you can use the AWS End User Messaging SMS console, the
`DeleteProtectConfiguration` action in the AWS End User Messaging SMS and voice v2 API, or the `aws
 sms-voice delete-protect-configuration` command in the AWS CLI. This section shows how to
delete a protect configuration using the AWS End User Messaging SMS console and the AWS CLI.

Enable deletion protection (Console)###### Enable deletion protection

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Protect**, choose
   **Protect configuration**.
3. On the **Protect configurations** page, choose the protect configuration that will have deletion protection enabled.
4. On the **Deletion protection** tab, choose **Edit settings**.
5. Check **Enable deletion protection** and then **Save changes**.

Enable or disable deletion protection (AWS CLI)
You can use the update-protect-configuration command to enable deletion protection.

###### Enable deletion protection

- At the command line, enter the following command:

```
`$` update-protect-configuration --protect-configuration-id `ProtectConfigurationId` --deletion-protection-enabled `Status`
```

In the preceding command, make the following changes:

    + Replace `ProtectConfigId` with the
     unique identifier of the protect configuration.
    + Replace `Status` with *true* to enable or *false* to disable deletion protection.

Disable deletion protection (Console)

###### Disable deletion protection

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Protect**, choose
   **Protect configuration**.
3. On the **Protect configurations** page, choose the protect configuration that will have deletion protection disabled.
4. On the **Deletion protection** tab, choose **Edit settings**.
5. Uncheck **Enable deletion protection** and then **Save changes**.
