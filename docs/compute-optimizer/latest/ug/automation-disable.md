

# Disabling Automation

You can disable the Automation feature at any time. However, the management account can't disable Automation for all member accounts in the organization. Each member must disable the feature at the account level, unless an enrollment configuration applies to it.

**Note**  
Disabling Automation stops all of the automation rules in your account. If you opt in again later, all rules will be inactive, and you must enable the rules you want to run. You must wait at least 24 hours after opting out to opt in again.

**Note**  
If an organization enrollment configuration applies to a member account, the member account can't disable Automation. In the member account, **Disable Automation for account** is turned off. To disable Automation for the account, the management account or a delegated administrator must first delete the enrollment configuration that applies to it, or move the account to an OU that no enrollment configuration applies to.

When the management account disables Automation, Compute Optimizer keeps the organization's enrollment configurations. If the management account enables Automation again later, the enrollment configurations become active again and apply to the accounts that they cover.

**To disable the Automation feature**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Account management** under the **Preferences** section.

1. Choose the **Automation** tab.

1. Choose **Disable Automation for account**

1. When prompted for confirmation, choose **Disable Automation**