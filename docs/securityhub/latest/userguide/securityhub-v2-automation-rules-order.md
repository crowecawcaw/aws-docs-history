# Updating the rule order in Security Hub

This topic describes how to update the rule order for automation rules in the console.
If you want to edit the criteria for an automation rule, see [Editing automation rules in Security Hub](securithub-v2-automation-rules-edit.md "securithub-v2-automation-rules-edit.md").

You cannot update the rule order for one automation rule without updating the rule order for every automation rule.
For example, you have four automation rules: Rule A (1), Rule B (2), Rule C (3), and Rule D (4).
You want Rule D to be applied first.
To do this, you change its number from 4 to 1.
As a result, Rule A gets 2, Rule B gets 3, and Rule C gets 4.

###### To update the rule order for your automation rules

1. Sign in to your AWS account.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the navigation pane, under **Management**, choose **Automations**.
3. Select the automation rule you want to edit.
   Under **Order**, choose the pencil icon next to the order number.
   Use the arrows to determine the new order number.
   Choose the **✓** icon to confirm.
   Choose the **X** icon to cancel.
   Alternatively, you can choose **Change order** to move the automation rule down, up, or to the top of the list.
