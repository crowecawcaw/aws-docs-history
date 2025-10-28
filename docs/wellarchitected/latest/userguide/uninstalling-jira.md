# Uninstalling the connector

To fully uninstall the AWS Well-Architected Tool Connector for Jira, perform the following tasks:

- Turn off Jira sync in any workloads that override account-level sync settings
- Turn off Jira sync at the account level
- Unlink your AWS account in Jira
- Uninstall the connector from your Jira account

###### To turn off the connector at the account level

###### Note

The following steps are performed in your AWS account.

1. Select **Settings** in the left navigation pane.
2. In the **Jira account syncing** section, choose **Edit**.
3. Clear the **Turn on Jira account syncing** option.
4. Choose **Save settings**.

###### To unlink an AWS account

###### Note

All of the following steps are performed in your Jira account, not in your AWS account.

1. Log in to your Jira account.
2. In the top navigation bar, choose **Apps**, then select **Manage your apps**.
3. Choose the dropdown arrow next to **AWS Well-Architected Tool Connector for Jira**, then choose **Configure**.
4. In the AWS Well-Architected Tool Configuration pane, to unlink an AWS account, choose **X** under **Actions**.

###### To uninstall the connector

###### Note

All of the following steps are performed in your Jira account, not in your AWS account.

We recommend verifying that all connected AWS accounts are unlinked in the configuration of the connector prior to uninstalling the connector.

1. Log in to your Jira account.
2. In the top navigation bar, choose **Apps**, then select **Manage your apps**.
3. Choose the dropdown arrow next to **AWS Well-Architected Tool Connector for Jira**.
4. Choose **Uninstall**, then choose **Uninstall app**.
