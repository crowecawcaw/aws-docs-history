

# Manage monitoring accounts and source accounts
<a name="Unified-Cross-Account-Manage"></a>

After you set up your monitoring accounts and source accounts, you can use the steps in these sections to manage them.

**Contents**
+ [Link more source accounts to an existing monitoring account](#Unified-Cross-Account-Setup-AddSourceAccounts)
+ [Remove the link between a monitoring account and source account](#Unified-Cross-Account-Setup-UnlinkAccount)
+ [View information about a monitoring account](#Unified-Cross-Account-Setup-ManageMonitoringAccount)

## Link more source accounts to an existing monitoring account
<a name="Unified-Cross-Account-Setup-AddSourceAccounts"></a>

Follow the steps in this section to add links from additional source accounts to an existing monitoring account. 

Each source account can be linked to as many as five monitoring accounts. Each monitoring account can be linked to as many as 100,000 source accounts.

To manage a source account, you must have certain permissions. For more information, see [Necessary permissions](CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-permissions).

**To add more source accounts to a monitoring account**

1. Sign in to the monitoring account.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation pane, choose **Settings**.

1. By **Monitoring account configuration**, choose **Manage source accounts**.

1. Choose the **Configuration policy** tab.

1. In the **Configuration policy** box, add the new source account ID in the **Principal** line.

   For example, suppose the **Principal** line is currently the following:

   ```
   "Principal": {"AWS": ["111111111111", "222222222222"]}
   ```

   To add `999999999999` as a third source account, edit the line to the following:

   ```
   "Principal": {"AWS": ["111111111111", "222222222222", "999999999999"]}
   ```

1. Choose **Update**.

1. Choose the **Configuration details** tab.

1. Choose the copy icon that is next to the monitoring account's sink ARN.

1. Sign in to the account that you want to use as a new source account.

1. Paste the monitoring account's sink ARN that you copied in Step 9.

   You see the CloudWatch settings page, with some information filled in.

1. For **Select data**, choose whether this source account will send **Logs**, **Metrics**, **Traces**, and **Application Insights - Applications**, **Internet Monitor - Monitors**, and **Application Signals -Services, Service Level Objectives (SLOs)** data to the monitoring accounts it is linked to.

1. Do not change the ARN in **Enter monitoring account configuration ARN**.

1. The **Define a label to identify your source account** section is pre-filled with the label choice from the monitoring account, if there is one. Optionally, choose **Edit** to change it.
**Note**  
In the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, the only supported option is to use custom labels, and the `$AccountName`, `$AcccountEmail`, and `$AcccountEmailNoDomain` variables all resolve as {{account-id}} instead of the specified variable.

1. Choose **Link**.

1. Enter **Confirm** in the box and choose **Confirm**.

## Remove the link between a monitoring account and source account
<a name="Unified-Cross-Account-Setup-UnlinkAccount"></a>

Follow the steps in this section to stop sending data from one source account to a monitoring account. 

**Note**  
After the source account stops sharing the metrics with the *Monitoring* account, the *Source* account metrics data is not accessible to the monitoring account. Source metric names can be visible to the monitoring account for upto 14 days.

You must have the permissions required to manage a source account to complete this task. For more information, see [Necessary permissions](CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-permissions).

**To remove the link between a source account and a monitoring account**

1. Sign in to the source account.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation pane, choose **Settings**.

1. By **Source account configuration**, choose **View linked monitoring accounts**.

1. Select the check box next to the monitoring account that you want to stop sharing data with.

1. Choose **Remove monitoring account**, **Confirm**.

1. Sign in to the monitoring account.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Settings**.

1. By **Monitoring account configuration**, choose **Manage monitoring account**.

1. In the **Configuration policy** box, delete the source account ID from the **Principal** line and choose **Update**.

## View information about a monitoring account
<a name="Unified-Cross-Account-Setup-ManageMonitoringAccount"></a>

Follow the steps in this section to view the cross-account settings for a monitoring account. 

To manage a monitoring account, you must have certain permissions. For more information, see [Necessary permissions](CloudWatch-Unified-Cross-Account-Setup.md#CloudWatch-Unified-Cross-Account-Setup-permissions).

**To manage a monitoring account**

1. Sign in to the monitoring account.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation pane, choose **Settings**.

1. By **Monitoring account configuration**, choose **Manage monitoring accounts**.

1. To view the Observability Access Manager policy that enables this account to be a monitoring account, choose the **Configuration policy** tab.

1. To view the source accounts that are linked to this monitoring account, choose the **Linked source accounts** tab.

1. To view the monitoring account sink ARN, and the types of data that this monitoring account can view in linked source accounts, choose the **Linked source accounts** tab.