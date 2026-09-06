

# Editing automation rule order
<a name="automation-rules-edit"></a>

Rule order determines which rule applies when a recommended action in an account matches multiple rules. Compute Optimizer assigns the action to the active rule with the lowest rule order value (highest priority), regardless of when that rule is scheduled to run. You can edit the rule order at any time. You can only edit one rule at a time. For organization rules, you can also edit the rule group to specify whether the rule applies before or after member account rules.

**To reorder automation rules**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Find the rule that you want to reorder.

1. Choose the **Rule order** cell for the rule you want to reorder, then use the menu to select the new rule order and choose the check mark icon.

1. When prompted choose Save changes. 

**To edit the rule group (organization rules only)**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Select the rule that you want to edit.

1. In the **Apply rule** section, choose **Before member account rules** or **After member account rules**.

1. Choose **Save changes**.

1. Review the rule order on the **Automation rules** page to ensure that it matches your intended priority.