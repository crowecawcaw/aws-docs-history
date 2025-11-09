AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Disabling Session Manager

logging in CloudWatch Logs and Amazon S3

You can use the Systems Manager console or AWS CLI to disable session logging in your
account.

###### To disable session logging (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Session Manager**.
3. Choose the **Preferences** tab, and then choose
   **Edit**.
4. To disable CloudWatch logging, in the **CloudWatch logging** section,
   clear the **Enable** checkbox.
5. To disable S3 logging, in the **S3 logging** section,
   clear the **Enable** checkbox.
6. Choose **Save**.

###### To disable session logging (AWS CLI)

To disable session logging using the AWS CLI, follow the instructions in [Update Session Manager
preferences (command line)](getting-started-configure-preferences-cli.md "getting-started-configure-preferences-cli.md").

In your JSON file, ensure that the `s3BucketName` and
`cloudWatchLogGroupName` inputs contain no values. For example:

```
"inputs": {
        "s3BucketName": "",
        ...
        "cloudWatchLogGroupName": "",
        ...
    }
```

Alternatively, to disable logging, you can remove all `S3*` and
`cloudWatch*` inputs from your JSON file.

###### Note

Depending on your configuration, after you disable CloudWatch or S3, a temporary log
file might still be generated to disk by SSM Agent. For information about how to
disable logging to disk, see [Configuring session logging to
disk](session-manager-logging-disk.md "session-manager-logging-disk.md").
