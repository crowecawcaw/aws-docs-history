# Disabling Automation

You can disable the Automation feature at any time. However, the management account can't disable Automation for all member accounts in the organization. Each member must disable the feature at the account level.

###### Note

Disabling Automation stops all of the automation rules in your account. If you opt in again later, all rules will be inactive, and you must enable the rules you want to run. You must wait at least 24 hours after opting out to opt in again.

When the management account disables the Automation feature, Compute Optimizer retains the associations between the management account and its member accounts. If the management account opts back in later, Compute Optimizer automatically restores these associations. However, if a member account opted out independently during the period when the management account had the feature disabled, that member account will not be re-associated when the management account opts back in.

###### To disable the Automation feature

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. In the navigation pane, choose **Automation rules** under the
   **Automation** section.
3. Choose the **Automation** tab.
4. Choose **Disable Automation for account**
5. When prompted for confirmation, choose **Disable Automation**
