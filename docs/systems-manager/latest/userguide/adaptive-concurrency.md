AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Allowing Automation to adapt to your

concurrency needs

By default, Automation allows you to run up to 100 concurrent automations at a
time. Automation also provides an optional setting that you can use to adjust your
concurrency automation quota automatically. With this setting, your concurrency
automation quota can accommodate up to 500 concurrent automations, depending on
available resources.

###### Note

If your automation calls API operations, adaptively scaling to your targets
can result in throttling exceptions. If recurring throttling exceptions occur
when running automations with adaptive concurrency turned on, you might have to
request quota increases for the API operation if available.

###### To turn on adaptive concurrency using the AWS Management Console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Automation**.
3. Choose the **Preferences** tab, and then choose
   **Edit**.
4. Select the check box next to **Enable adaptive
   concurrency**.
5. Choose **Save**.

###### To turn on adaptive concurrency using the command line

- Open the AWS CLI or Tools for Windows PowerShell and run the following command to turn on adaptive
  concurrency for your account in the requesting Region.

Linux & macOS

```
aws ssm update-service-setting \
    --setting-id /ssm/automation/enable-adaptive-concurrency \
    --setting-value True
```

Windows

```
aws ssm update-service-setting ^
    --setting-id /ssm/automation/enable-adaptive-concurrency ^
    --setting-value True
```

PowerShell

```
Update-SSMServiceSetting `
    -SettingId "/ssm/automation/enable-adaptive-concurrency" `
    -SettingValue "True"
```
