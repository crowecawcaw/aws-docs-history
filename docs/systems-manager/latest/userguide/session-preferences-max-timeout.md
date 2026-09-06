

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Specify maximum session duration
<a name="session-preferences-max-timeout"></a>

With Session Manager, you can specify the maximum duration of a session before it ends. By default, sessions do not have a maximum duration. The value you specify for maximum session duration must be between 1 and 1,440 minutes.

**To specify maximum session duration (console)**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Session Manager**.

1. Choose the **Preferences** tab, and then choose **Edit**.

1. Select the check box next to **Enable maximum session duration**.

1. Specify the maximum duration of session before it ends in the **minutes** field under **Maximum session duration**.

1. Choose **Save**.