

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Disabling the Systems Manager unified console
<a name="systems-manager-disable-integrated-console"></a>

To disable the Systems Manager unified console for an organization, you'll need access to the account you registered as a delegated administrator for Systems Manager. After logging in to the delegated administrator account for your organization, you can disable the setup for your organization in the **Settings** section of the unified console. When you disable the unified console setup for your organization, Systems Manager deletes the resources created, including Resource Explorer managed views, during the setting up process. Disabling the setup for your organization doesn't revoke trusted access or deregister the delegated administrator accounts for dependent services. The following procedure describes how to disable the setup for the unified console.

For related information, see [Setting up Systems Manager console access](systems-manager-setting-up-console-access.md).

**To disable the setup for the Systems Manager unified console**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. Select **Settings** in the navigation pane.

1. Select **Disable**. You must confirm that you want to disable the setup for your organization. This action deletes the resources created for the unified console and can't be undone.

If you can't access the delegated administrator account for Systems Manager, you can disable the unified console setup from the management account. Use the AWS CLI or SDK to call the `DeleteConfigurationManager` API operation. Pass the `ManagerArn` value for the organization setup in your account. The format for the manager ARN is as follows:

`arn:aws:ssm-quicksetup:{{account-id}}:configuration-manager/{{configuration-manager-id}}`.

**Note**  
If you don't know the value for {{configuration-manager-id}}, call the `ListConfigurationManagers` API action and filter the results using the `AWSQuickSetupType-SSM` type.