

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Allowing Automation to adapt to your concurrency needs
<a name="adaptive-concurrency"></a>

By default, Automation lets you run up to 100 concurrent automations at a time. Automation also provides an optional setting that you can use to adjust your concurrency automation quota automatically. With this setting, your concurrency automation quota can accommodate up to 500 concurrent automations, depending on available resources. 

**Note**  
If your automation calls API operations, adaptively scaling to your targets can result in throttling exceptions. If recurring throttling exceptions occur when running automations with adaptive concurrency turned on, you might have to request quota increases for the API operation if available.

**To turn on adaptive concurrency using the AWS Management Console**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Automation**.

1. Choose the **Preferences** tab, and then choose **Edit**.

1. Select the check box next to **Enable adaptive concurrency**.

1. Choose **Save**.

**To turn on adaptive concurrency using the command line**
+ Open the AWS CLI or Tools for Windows PowerShell and run the following command to turn on adaptive concurrency for your account in the requesting Region.

------
#### [ Linux & macOS ]

  ```
  aws ssm update-service-setting \
      --setting-id /ssm/automation/enable-adaptive-concurrency \
      --setting-value True
  ```

------
#### [ Windows ]

  ```
  aws ssm update-service-setting ^
      --setting-id /ssm/automation/enable-adaptive-concurrency ^
      --setting-value True
  ```

------
#### [ PowerShell ]

  ```
  Update-SSMServiceSetting `
      -SettingId "/ssm/automation/enable-adaptive-concurrency" `
      -SettingValue "True"
  ```

------