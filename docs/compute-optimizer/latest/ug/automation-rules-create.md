

# Creating automation rules
<a name="automation-rules-create"></a>

You can use an automation rule to manage automated implementation of recommended actions in Compute Optimizer. For background information about how automation rules work, see [Automation rules](automation-rules.md).

Automation rules are global resources that manage automated actions across all AWS Regions where Compute Optimizer Automation is available.

You can only create one automation rule at a time. To create multiple automation rules, follow the console procedures multiple times, or call the API or command multiple times with your desired parameters.

When you create an automation rule in the Compute Optimizer console, you can preview the current recommended actions that match your rule criteria. This can help you validate and iterate on your rule criteria.

**Important**  
When you create an organization rule in the management account and apply it to member accounts, those member accounts will be able to see the details of the rule from their account. AWS recommends that you don't include personally identifying, confidential, or sensitive information in your rule name, description, or other fields.

**To create an automation rule**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Automation rules** under the **Automation** section.

1. Choose **Create Automation rule**.

1. If you are creating a rule in the management account or delegated administrator, you can choose the **rule type**, the **member accounts** you want to apply the rule, and whether to apply the rule **before** or **after member account rules**. You can only select member accounts with Automation enabled and organization rules allowed can be selected for the rule to apply.

1. Choose the **action types** you want this rule to implement.

1. (Optional) You can specify **rule criteria** to refine which recommended actions will be automatically implemented. For each criteria, use the `Attribute`, `Operator`, and `Value` drop down menus and input fields to specify your rule criteria.

   You can also configure the following optional checkboxes for each criteria:
   + **If exists** – Select this to also match recommended actions where the attribute field is absent. For more information, see [Rule criteria](automation-rules.md#automation-rules-criteria).
   + **Ignore case** – Select this for case-insensitive matching. Available only when the operator is `Equals` or `Does not equal` and the attribute uses free-form input (Resource ARN, Resource tags).
**Important**  
If you don't specify rule criteria, Compute Optimizer applies all recommended action types across the accounts in your rule scope, including recommended actions in all AWS Regions where Compute Optimizer Automation is available. 

1. (Optional) Choose **Refresh matching actions** to get a preview of the recommended actions that match your rule criteria.

1. Set a recurring **Schedule** for your rule to automatically implement matching actions. This includes the frequency (daily, weekly, or monthly), start time, end time, and time zone.

1. (Optional) You can add **Tags** as key-value pairs to your rule to help you easily identify the rule.

1. Provide a rule **name** and a **description** (optional) for your rule.

1. For **Rule status**, choose whether you want the rule to be `Active` or `Inactive` after it's created.

1. Choose **Create Automation rule**.

**Note**  
By default, rules are created with the rule order 1 (highest priority) in their rule group. You can update the rule order from the Automation rules page. To learn more more, see [Editing automation rule order](automation-rules-edit.md).