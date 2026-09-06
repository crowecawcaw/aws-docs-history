

# Enabling Runtime Monitoring for multiple-account environments
<a name="enable-runtime-monitoring-multiple-acc-env"></a>

In a multiple-account environments, only the delegated GuardDuty administrator account can enable or disable Runtime Monitoring for the member accounts, and manage automated agent configuration for the resource types belonging to the member accounts in their organization. The GuardDuty member accounts can't modify this configuration from their accounts. The delegated GuardDuty administrator account account manages their member accounts using AWS Organizations. For more information about multi-account environments, see [Managing multiple accounts](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html).

## For delegated GuardDuty administrator account
<a name="runtime-monitoring-config-delegated-admin"></a>

**To enable Runtime Monitoring for delegated GuardDuty administrator account**

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Runtime Monitoring**.

1. Under the **Configuration** tab, choose **Edit** in the **Runtime Monitoring configuration** section.

1. 

**Using Enable for all accounts**

   If you want to enable Runtime Monitoring for all the accounts that belong to the organization, including the delegated GuardDuty administrator account, then choose **Enable for all accounts**.

1. 

**Using Configure accounts manually**

   If you want to enable Runtime Monitoring for each member account individually, then choose **Configure accounts manually**.

   1. Choose **Enable** under the **Delegated Administrator (this account)** section.

1. Manage the security agent for your resource type. For more information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md).

## For all member accounts
<a name="runtime-monitoring-config-all-member-accounts"></a>

**To enable Runtime Monitoring for all member accounts in the organization**

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Sign in using the delegated GuardDuty administrator account.

1. In the navigation pane, choose **Runtime Monitoring**.

1. On the Runtime Monitoring page, under the **Configuration** tab, choose **Edit** in the **Runtime Monitoring configuration** section.

1. Choose **Enable for all accounts**.

1. Manage the security agent for your resource type. For more information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md).

## For all existing active member accounts
<a name="runtime-monitoring-all-existing-active-member-accounts"></a>

**To enable Runtime Monitoring for existing member accounts in the organization**

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Sign in using the delegated GuardDuty administrator account for the organization.

1. In the navigation pane, choose **Runtime Monitoring**.

1. On the **Runtime Monitoring** page, under the **Configuration** tab, you can view the current status of the Runtime Monitoring configuration. 

1. Within the Runtime Monitoring pane, under the **Active member accounts** section, choose **Actions**.

1. From the **Actions** dropdown menu, choose **Enable for all existing active member accounts**.

1. Choose **Confirm**.

1. Manage the security agent for your resource type. For more information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md).

**Note**  
It may take up to 24 hours to update the configuration for the member accounts.

## Auto-enable Runtime Monitoring for new member accounts only
<a name="runtime-monitoring-configure-auto-enable-new-members"></a>

**To enable Runtime Monitoring for new member accounts in your organization**

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Sign in using the designated delegated GuardDuty administrator account of the organization.

1. In the navigation pane, choose **Runtime Monitoring**

1. Under the **Configuration** tab, choose **Edit** in the **Runtime Monitoring configuration** section.

1. Choose **Configure accounts manually**.

1. Select **Automatically enable for new member accounts**.

1. Manage the security agent for your resource type. For more information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md).

## For selective active member accounts only
<a name="runtime-monitoring-enable-selective-member-accounts"></a>

**To enable Runtime Monitoring for individual active member accounts**

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Sign in using the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Accounts**.

1. On the **Accounts** page, review values in the **Runtime Monitoring** and **Manage agent automatically** columns. These values indicate whether Runtime Monitoring and GuardDuty agent management are **Enabled** or **Not enabled** for the corresponding account.

1. From the Accounts table, select the account for which you want to enable Runtime Monitoring. You can choose multiple accounts at a time.

1. Choose **Confirm**.

1. Choose **Edit protection plans**. Choose the appropriate action.

1. Choose **Confirm**.

1. Manage the security agent for your resource type. For more information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md).