# Configuring AWS AppConfig deletion protection

AWS AppConfig provides an account setting to help prevent users from unintentionally deleting
actively-used environments and configuration profiles. AWS AppConfig monitors calls to [GetLatestConfiguration](../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md "../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md") and [GetConfiguration](../../2019-10-09/APIReference/API_GetConfiguration.md "../../2019-10-09/APIReference/API_GetConfiguration.md") and
tracks which configuration profiles and environments have been included in these calls within a
60-minute interval (the default setting). Any configuration profile or environment that was
accessed within that interval will be considered active. If you attempt to delete an active
configuration profile or environment, AWS AppConfig returns an error. If needed, you can bypass this
error by using the `DeletionProtectionCheck` parameter. For more information, see
[Bypassing or forcing a deletion protection
check](deletion-protection-check.md "deletion-protection-check.md").

###### Configure deletion protection using the console

Use the following procedure to configure deletion protection by using the AWS Systems Manager
console.

###### To configure deletion protection (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/ "https://console.aws.amazon.com/systems-manager/appconfig/").
2. In the navigation pane, choose **Settings**.
3. Use the toggle to enable or disable deletion protection.
4. For **Protection period**, set the definition of an active resource to
   be between 15 and 1440 minutes.
5. Click **Apply**.

###### Configure deletion protection using the AWS CLI

Use the following procedure to configure deletion protection by using the AWS CLI. Replace
`value` in the following commands with the value you want to use in
your environment.

###### Note

Before you begin, we recommend you update to the latest version of the AWS CLI. For more
information, see [Install or update to the latest
version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

###### To configure deletion protection (CLI)

1. Run the following command to view the current deletion protection settings.

```
aws appconfig get-account-settings
```

2. Run the following command to enable or disable deletion protection. Specify
   `false` to disable deletion protection or `true` to enable
   it.

```
aws appconfig update-account-settings --deletion-protection Enabled=`value`
```

3. You can increase the default interval to a maximum of 24 hours. Run the following
   command to specify a new interval.

```
aws appconfig update-account-settings --deletion-protection Enabled=true,ProtectionPeriodInMinutes=`a number between 15 and 1440`
```
