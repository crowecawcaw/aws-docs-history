

# Editing automation rule order

Rule order sets which rule applies when an action matches more than one rule. Compute Optimizer uses the active rule that has the lowest order value. The lowest value is the top priority. It wins no matter when the rule is set to run. You can change the order at any time. You can change only one rule at a time. For organization rules, you can also set the rule group. The group sets whether a rule applies before or after member account rules.

To learn how to view a rule, see [Viewing automation rules](automation-rules-view.md).

**To reorder automation rules**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, under **Automation**, choose **Automation rules**.

1. Find the rule that you want to move.

1. Choose the **Rule order** cell for that rule. Use the menu to pick the new order. Then choose the check mark.

1. When prompted, choose **Save changes**.

**To edit the rule group (organization rules only)**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, under **Automation**, choose **Automation rules**.

1. Select the rule that you want to edit.

1. In the **Apply rule** section, choose **Before member account rules** or **After member account rules**.

1. Choose **Save changes**.

1. On the **Automation rules** page, check that the order matches the priority you want.