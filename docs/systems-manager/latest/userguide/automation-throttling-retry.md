

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Configuring automatic retry for throttled operations
<a name="automation-throttling-retry"></a>

There is a limit on the number of concurrent automation executions that can run in each account. Attempting to run several automations concurrently in an account can lead to throttling issues. You can use the automatic throttling retry capability to configure retry behavior for throttled automation steps.

Automatic throttling retry for automation actions provides a more resilient execution environment for high-scale operations. The throttling retry capability supports all [automation actions](automation-actions.md) except for `aws:executeScript`.

The throttling retry setting works alongside the existing `maxAttempts` step property. When both are configured, the system first attempts throttling retries within the specified time limit, then applies the `maxAttempts` setting if the step continues to fail.

**To configure throttling retry using the AWS Management Console**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Automation**.

1. Choose the **Preferences** tab, and then choose **Edit**.

1. In the **Throttled retry time limit** field, enter a value between 0 and 3600 seconds. This specifies the maximum time that the system retries a step that is throttled.

1. Choose **Save**.

**To configure throttling retry using the command line**
+ Open the AWS CLI or Tools for Windows PowerShell and run the following command to configure throttling retry for your account in the requesting Region.

------
#### [ Linux & macOS ]

  ```
  aws ssm update-service-setting \
      --setting-id /ssm/automation/throttled-retry-time-limit \
      --setting-value {{3600}}
  ```

------
#### [ Windows ]

  ```
  aws ssm update-service-setting ^
      --setting-id /ssm/automation/throttled-retry-time-limit ^
      --setting-value {{3600}}
  ```

------
#### [ PowerShell ]

  ```
  Update-SSMServiceSetting `
      -SettingId "/ssm/automation/throttled-retry-time-limit" `
      -SettingValue "{{3600}}"
  ```

------