

# Configuring AWS AppConfig deletion protection
<a name="deletion-protection"></a>

AWS AppConfig provides an account setting to help prevent users from unintentionally deleting actively-used environments and configuration profiles. AWS AppConfig monitors calls to [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) and [GetConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfiguration.html) and tracks which configuration profiles and environments have been included in these calls within a 60-minute interval (the default setting). Any configuration profile or environment that was accessed within that interval will be considered active. If you attempt to delete an active configuration profile or environment, AWS AppConfig returns an error. If needed, you can bypass this error by using the `DeletionProtectionCheck` parameter. For more information, see [Bypassing or forcing a deletion protection check](deletion-protection-check.md).

**Configure deletion protection using the console**  
Use the following procedure to configure deletion protection by using the AWS Systems Manager console.

**To configure deletion protection (console)**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Settings**.

1. Use the toggle to enable or disable deletion protection.

1. For **Protection period**, set the definition of an active resource to be between 15 and 1440 minutes.

1. Click **Apply**.

**Configure deletion protection using the AWS CLI**  
Use the following procedure to configure deletion protection by using the AWS CLI. Replace {{value}} in the following commands with the value you want to use in your environment.

**Note**  
Before you begin, we recommend you update to the latest version of the AWS CLI. For more information, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

**To configure deletion protection (CLI)**

1. Run the following command to view the current deletion protection settings. 

   ```
   aws appconfig get-account-settings
   ```

1. Run the following command to enable or disable deletion protection. Specify `false` to disable deletion protection or `true` to enable it.

   ```
   aws appconfig update-account-settings --deletion-protection Enabled={{value}}
   ```

1. You can increase the default interval to a maximum of 24 hours. Run the following command to specify a new interval.

   ```
   aws appconfig update-account-settings --deletion-protection Enabled=true,ProtectionPeriodInMinutes={{a number between 15 and 1440}}
   ```