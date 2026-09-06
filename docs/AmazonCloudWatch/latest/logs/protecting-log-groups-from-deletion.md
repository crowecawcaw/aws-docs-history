

# Protecting log groups from deletion
<a name="protecting-log-groups-from-deletion"></a>

## Enabling deletion protection
<a name="enabling-deletion-protection"></a>

You can enable deletion protection when creating a new log group or on existing log groups. During log group creation, select "Enabled deletion protection" or by passing the parameter `--deletion-protection-enabled`. By default, deletion protection is not enabled.

**To enable or disable deletion protection on an existing log group (console)**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Log Management**.

1. Select the log group you want to protect.

1. Choose **Actions**, **Edit deletion protection**.

1. In the dialog box, review and then submit changes.

If using the AWS CLI, to enable deletion protection on an existing log group:

```
aws logs put-log-group-deletion-protection \
--log-group-identifier "/my-application/logs" \
--deletion-protection-enabled
```

To remove deletion protection on an existing log group:

```
aws logs put-log-group-deletion-protection \
--log-group-identifier "/my-application/logs" \
--no-deletion-protection-enabled
```

### Error handling
<a name="deletion-protection-error-handling"></a>

If you attempt to delete a log group with deletion protection enabled, you receive a `ValidationException` with the message: "Cannot delete log group with deletion protection enabled. Disable deletion protection first."