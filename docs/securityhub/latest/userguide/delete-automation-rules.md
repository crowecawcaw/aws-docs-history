

# Deleting or disabling automation rules
<a name="delete-automation-rules"></a>

An automation rule can be used to automatically update findings in AWS Security Hub CSPM. For background information about how automation rules work, see [Understanding automation rules in Security Hub CSPM](automation-rules.md).

When you delete an automation rule, Security Hub CSPM removes it from your account and no longer applies the rule to findings. As an alternative to deletion, you can *disable* a rule. This retains the rule for future use, but Security Hub CSPM won't apply the rule to any matching findings until you enable it.

Choose your preferred method, and follow the steps to delete an automation rule. You can delete one or more rules in a single request.

------
#### [ Console ]

**To delete or disable automation rules (console)**

1. Using the credentials of the Security Hub CSPM administrator, open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. In the navigation pane, choose **Automations**.

1. Select the rule(s) that you want to delete. Choose **Action** and **Delete** (to retain a rule, but disable it temporarily, choose **Disable**).

1. Confirm your choice, and choose **Delete**.

------
#### [ API ]

**To delete or disable automation rules (API)**

1. Use the [`BatchDeleteAutomationRules`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchDeleteAutomationRules.html) operation from the Security Hub CSPM administrator account.

1. For the `AutomationRulesArns` parameter, provide the ARN of the rule(s) that you want to delete (to retain a rule, but disable it temporarily, provide `DISABLED` for the `RuleStatus` parameter).

The following example deletes the specified automation rule. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securityhub batch-delete-automation-rules \
--automation-rules-arns '["arn:aws:securityhub:{{us-east-1:123456789012}}:automation-rule/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}"]' \
--region {{us-east-1}}
```

------