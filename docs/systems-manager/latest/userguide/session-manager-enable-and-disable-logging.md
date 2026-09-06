

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Disabling Session Manager logging in CloudWatch Logs and Amazon S3
<a name="session-manager-enable-and-disable-logging"></a>

You can use the Systems Manager console or AWS CLI to disable session logging in your account.

**To disable session logging (console)**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Session Manager**.

1. Choose the **Preferences** tab, and then choose **Edit**.

1. To disable CloudWatch logging, in the **CloudWatch logging** section, clear the **Enable** checkbox.

1. To disable S3 logging, in the **S3 logging** section, clear the **Enable** checkbox.

1. Choose **Save**.

**To disable session logging (AWS CLI)**  
To disable session logging using the AWS CLI, follow the instructions in [Update Session Manager preferences (command line)](getting-started-configure-preferences-cli.md).

 In your JSON file, make sure that the `s3BucketName` and `cloudWatchLogGroupName` inputs contain no values. For example: 

```
"inputs": {
        "s3BucketName": "",
        ...
        "cloudWatchLogGroupName": "",
        ...
    }
```

Alternatively, to disable logging, you can remove all `S3*` and `cloudWatch*` inputs from your JSON file.

**Note**  
Depending on your configuration, after you disable CloudWatch or S3, a temporary log file might still be generated to disk by SSM Agent. For information about how to disable logging to disk, see [Configuring session logging to disk](session-manager-logging-disk.md).