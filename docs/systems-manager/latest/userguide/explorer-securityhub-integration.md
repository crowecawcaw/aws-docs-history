

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Receiving findings from AWS Security Hub CSPM in Explorer
<a name="explorer-securityhub-integration"></a>

[AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS. The service collects security data, called *findings*, from across AWS accounts, services, and supported third-party products. Security Hub CSPM findings can help you check your environment against security industry standards and best practices, analyze your security trends, and identify the highest priority security issues.

Security Hub CSPM sends findings to Amazon EventBridge, which uses an event rule to send the findings to Explorer. After you enable integration, as described here, you can view Security Hub CSPM findings in an Explorer widget and view finding details in OpsCenter OpsItems. The widget provides a summary of all Security Hub CSPM findings based on severity. New findings in Security Hub CSPM are usually visible in Explorer within seconds of being created.

**Warning**  
Note the following important information:  
Explorer is integrated with OpsCenter. After you enable Explorer integration with Security Hub CSPM, OpsCenter automatically creates OpsItems for Security Hub CSPM findings. Depending on your AWS environment, enabling integration can result in large numbers of OpsItems, at a cost.   
Before you continue, read about OpsCenter integration with Security Hub CSPM. The topic includes specific details about how changes and updates to findings and OpsItems are charged to your account. For more information, see [Understanding OpsCenter integration with AWS Security Hub CSPM](OpsCenter-applications-that-integrate.md#OpsCenter-integrate-with-security-hub). For OpsCenter pricing information, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/).
If you create a resource data sync in Explorer while logged into the administrator account, Security Hub CSPM integration is automatically enabled for the administrator and all member accounts in the sync. Once enabled, OpsCenter automatically creates OpsItems for Security Hub CSPM findings, at a cost. For more information about creating a resource data sync, see [Setting up Systems Manager Explorer to display data from multiple accounts and Regions](Explorer-resource-data-sync.md).

## Types of findings that Explorer receives
<a name="explorer-securityhub-integration-finding-types-received"></a>

Explorer receives [all findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cwe-integration-types.html#securityhub-cwe-integration-types-all-findings) from Security Hub CSPM. You can see all findings based on severity in the Explorer widget when you turn on the Security Hub CSPM default settings. By default, Explorer creates OpsItems for Critical severity findings. You can manually configure Explorer to create OpsItems for other severity levels (High, Medium, and Low).

Though Explorer doesn't create OpsItems for informational findings, you can view informational operations data (OpsData) in the Security Hub CSPM findings summary widget. Explorer creates OpsData for all findings regardless of severity. For more information about Security Hub CSPM severity levels, see [Severity](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Severity.html) in the *AWS Security Hub API Reference*.

## Enabling integration
<a name="explorer-securityhub-integration-receive-enable"></a>

This section describes how to enable and configure Explorer to start receiving Security Hub CSPM findings.

**Before you begin**  
Complete the following tasks before you configure Explorer to start receiving Security Hub CSPM findings.
+ Enable and configure Security Hub CSPM. For more information, see [Setting up Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) in the *AWS Security Hub User Guide*.
+ Log in to the AWS Organizations management account. Systems Manager requires access to AWS Organizations to create OpsItems from Security Hub CSPM findings. After you log in to the management account, you can enable this access from the Explorer **Configure dashboard** tab, as described in the following procedure. If the **Enable access** button is not shown, trusted access is already enabled. If you don't log in to the AWS Organizations management account, you can't allow access and Explorer can't create OpsItems from Security Hub CSPM findings.

**Note**  
If your account isn't part of an organization in AWS Organizations, you don't need to enable OpsData Sync trusted access. The management account requirement described in this section doesn't apply. Enable AWS Security Hub CSPM in each AWS Region where you want to receive findings, and then, on the Explorer **Configure dashboard** tab, turn on the **OpsItems created by Security Hub CSPM findings** toggle.

**To start receiving Security Hub CSPM findings**

1. (management account) Enable AWS Security Hub CSPM in each AWS Region where you want to receive findings. For more information, see [Setting up Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) in the *AWS Security Hub User Guide*.

1. (management account) Enable OpsData Sync trusted access for AWS Organizations. You must enable trusted access before you can turn on the management account's own OpsData source in step 3. Steps 4 and 5, for member and delegated administrator accounts, don't depend on trusted access. Choose one of the following options:
   + In Explorer, on the **Configure dashboard** tab, under the **OpsItems created by Security Hub CSPM findings** section, choose the **Enable access** button.
   + Run the following command by using the AWS CLI.

     ```
     aws organizations enable-aws-service-access --service-principal opsdatasync.ssm.amazonaws.com
     ```
**Note**  
If you are signed in to the management account and the **Enable access** button is not shown, trusted access is already enabled. To confirm, run the following command.  

   ```
   aws organizations list-aws-service-access-for-organization
   ```
**Note**  
The **Enable access** alert also appears in the **Create resource data sync** wizard, a common entry point from the management account.

1. (management account, optional) Complete this step only if you also want findings from the management account itself. Turn on the **OpsItems created by Security Hub CSPM findings** toggle. By default, Explorer creates OpsItems for Critical severity findings, and you can configure it to create OpsItems for additional severity levels.

1. (Each member or delegated administrator account) Enable AWS Security Hub CSPM in the relevant AWS Region.

1. (Each member or delegated administrator account) Turn on the **OpsItems created by Security Hub CSPM findings** toggle. These accounts can complete this step at any time, with no dependency on step 2. If you create an organization-scoped resource data sync in Explorer from the management account (that is, a sync whose source is the entire organization or specific organizational units), this OpsData source is enabled automatically for all member accounts in the sync.

## How to view findings from Security Hub CSPM
<a name="explorer-securityhub-integration-view-received-findings"></a>

The following procedure describes how to view Security Hub CSPM findings.

**To view Security Hub CSPM findings**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Explorer**.

1. Find the **AWS Security Hub CSPM findings summary** widget. This displays your Security Hub CSPM findings. You can select a severity level to view a detailed description of the corresponding OpsItem.

## How to stop receiving findings
<a name="explorer-securityhub-integration-disable-receive"></a>

The following procedure describes how to stop receiving Security Hub CSPM findings.

**To stop receiving Security Hub CSPM findings**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Explorer**.

1. Select **Settings**.

1. Select the **Configure dashboard** tab.

1. Select the **Enabled** slider to turn off **AWS Security Hub CSPM**.

**Important**  
If the option to disable Security Hub CSPM findings is grayed out in the console, you can disable this setting by running the following command in the AWS CLI. You must run the command while logged into either the AWS Organizations management account or the Systems Manager delegated administrator account. For the `region` parameter, specify the AWS Region where you want to stop receiving Security Hub CSPM findings in Explorer.   

```
aws ssm update-service-setting --setting-id /ssm/opsdata/SecurityHub --setting-value Disabled --region {{AWS Region}}
```
Here's an example.  

```
aws ssm update-service-setting --setting-id /ssm/opsdata/SecurityHub --setting-value Disabled --region us-east-1
```