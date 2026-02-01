• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Configuring automatic retry for

throttled operations

There is a limit on the number of concurrent automation executions that can run in
each account. Attempting to run several automations concurrently in an account can
lead to throttling issues. You can use the automatic throttling retry capability to
configure retry behavior for throttled automation steps.

Automatic throttling retry for automation actions provides a more resilient
execution environment for high-scale operations. The throttling retry capability
supports all [automation actions](automation-actions.md "automation-actions.md") except for
`aws:executeScript`.

The throttling retry setting works in addition to the existing
`maxAttempts` step property. When both are configured, the system
first attempts throttling retries within the specified time limit, then applies the
`maxAttempts` setting if the step continues to fail.

###### To configure throttling retry using the AWS Management Console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Automation**.
3. Choose the **Preferences** tab, and then choose
   **Edit**.
4. In the **Throttling retry time limit** field, enter a
   value between 0 and 3600 seconds. This specifies the maximum time that the
   system retries a step that is throttled.
5. Choose **Save**.

###### To configure throttling retry using the command line

- Open the AWS CLI or Tools for Windows PowerShell and run the following command to configure
  throttling retry for your account in the requesting Region.

Linux & macOS

```
aws ssm update-service-setting \
    --setting-id /ssm/automation/throttling-retry-time-limit \
    --setting-value `3600`
```

Windows

```
aws ssm update-service-setting ^
    --setting-id /ssm/automation/throttling-retry-time-limit ^
    --setting-value `3600`
```

PowerShell

```
Update-SSMServiceSetting `
    -SettingId "/ssm/automation/throttling-retry-time-limit" `
    -SettingValue "`3600`"
```
