# Enabling Runtime Monitoring for multiple-account environments

In a multiple-account environments, only the delegated GuardDuty administrator account can enable or disable Runtime Monitoring
for the member accounts, and manage automated agent configuration for the resource types
belonging to the member accounts in their organization. The GuardDuty member accounts can't
modify this configuration from their accounts. The delegated GuardDuty administrator account account manages their member
accounts using AWS Organizations. For more information about multi-account environments, see
[Managing multiple accounts](guardduty_accounts.md "guardduty_accounts.md").

###### To enable Runtime Monitoring for delegated GuardDuty administrator account

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Runtime Monitoring**.
3. Under the **Configuration** tab, choose
   **Edit** in the **Runtime Monitoring
   configuration** section.
4. ###### Using Enable for all accounts

If you want to enable Runtime Monitoring for all the accounts that belong to the
organization, including the delegated GuardDuty administrator account, then choose **Enable for
all accounts**. 5. ###### Using Configure accounts manually

If you want to enable Runtime Monitoring for each member account individually,
then choose **Configure accounts manually**.

    1. Choose **Enable** under the
     **Delegated Administrator (this account)**
     section.

6. Manage the security agent for your resource type. For more
information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md "runtime-monitoring-managing-agents.md").

###### To enable Runtime Monitoring for all member accounts in the organization

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Sign in using the delegated GuardDuty administrator account. 2. In the navigation pane, choose **Runtime Monitoring**. 3. On the Runtime Monitoring page, under the **Configuration**
tab, choose **Edit** in the **Runtime Monitoring
configuration** section. 4. Choose **Enable for all accounts**. 5. Manage the security agent for your resource type. For more
information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md "runtime-monitoring-managing-agents.md").

###### To enable Runtime Monitoring for existing member accounts in the organization

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Sign in using the delegated GuardDuty administrator account for the organization. 2. In the navigation pane, choose **Runtime Monitoring**. 3. On the **Runtime Monitoring** page, under the
**Configuration** tab, you can view the current
status of the Runtime Monitoring configuration. 4. Within the Runtime Monitoring pane, under the **Active member
accounts** section, choose
**Actions**. 5. From the **Actions** dropdown menu, choose
**Enable for all existing active member
accounts**. 6. Choose **Confirm**. 7. Manage the security agent for your resource type. For more
information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md "runtime-monitoring-managing-agents.md").

###### Note

It may take up to 24 hours to update the configuration for the member accounts.

###### To enable Runtime Monitoring for new member accounts in your organization

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Sign in using the designated delegated GuardDuty administrator account of the organization. 2. In the navigation pane, choose **Runtime Monitoring** 3. Under the **Configuration** tab, choose
**Edit** in the **Runtime Monitoring
configuration** section. 4. Choose **Configure accounts manually**. 5. Select **Automatically enable for new member
accounts**. 6. Manage the security agent for your resource type. For more
information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md "runtime-monitoring-managing-agents.md").

###### To enable Runtime Monitoring for individual active member accounts

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").

Sign in using the delegated GuardDuty administrator account credentials. 2. In the navigation pane, choose **Accounts**. 3. On the **Accounts** page, review values in the
**Runtime Monitoring** and **Manage agent
automatically** columns. These values indicate whether
Runtime Monitoring and GuardDuty agent management are **Enabled** or
**Not enabled** for the corresponding
account. 4. From the Accounts table, select the account for which you want to
enable Runtime Monitoring. You can choose multiple accounts at a time. 5. Choose **Confirm**. 6. Choose **Edit protection plans**. Choose the
appropriate action. 7. Choose **Confirm**. 8. Manage the security agent for your resource type. For more
information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md "runtime-monitoring-managing-agents.md").
