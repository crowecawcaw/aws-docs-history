# Editing automation rule order

An automation rule can be used to automatically update findings in AWS Security Hub CSPM. For background information about how automation rules work, see [Understanding automation rules in Security Hub CSPM](automation-rules.md "automation-rules.md").

After creating an automation rule, the delegated Security Hub CSPM administrator can edit the rule.

If you want to keep the rule criteria and actions the same, but
change the order in which Security Hub CSPM applies an automation rule, you can edit just the rule order. Choose your preferred
method, and follow the steps to edit rule order.

For instructions on editing the criteria or actions of an automation rule, see [Editing automation rules](edit-automation-rules.md "edit-automation-rules.md").

Console

###### To edit automation rule order (console)

1. Using the credentials of the Security Hub CSPM administrator, open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose
   **Automations**.
3. Select the rule whose order you want to change. Choose
   **Edit priority**.
4. Choose **Move up** to increase the rule's
   priority by one unit. Choose **Move down** to
   decrease the rule priority's by one unit. Choose **Move
   to top** to assign the rule an order of
   **1** (this gives the rule precedence over
   other existing rules).

###### Note

When you create a rule in the Security Hub CSPM console, Security Hub CSPM automatically
assigns rule order based on the order of rule creation. The most
recently created rule has the lowest numerical value for rule order
and therefore applies first.

API

###### To edit automation rule order (API)

1. Use the [`BatchUpdateAutomationRules`](../../1.0/APIReference/API_BatchUpdateAutomationRules.md "../../1.0/APIReference/API_BatchUpdateAutomationRules.md") operation from
   the Security Hub CSPM administrator account.
2. For the `RuleArn` parameter, provide the ARN of the
   rule(s) whose order you want to edit.
3. Modify the value of the `RuleOrder` field.

###### Note

If multiple rules have the same `RuleOrder`, Security Hub CSPM
applies a rule with an earlier value for the `UpdatedAt`
field first (that is, the rule which was most recently edited
applies last).
