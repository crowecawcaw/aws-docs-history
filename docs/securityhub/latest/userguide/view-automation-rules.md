# Viewing automation rules

An automation rule can be used to automatically update findings in AWS Security Hub CSPM. For background information about how automation rules work, see [Understanding automation rules in Security Hub CSPM](automation-rules.md "automation-rules.md").

Choose your preferred method, and follow the steps to view your existing automation rules and
the details of each rule.

To view a history of how automation rules have changed your findings, see [Reviewing finding details and history in
Security Hub CSPM](securityhub-findings-viewing.md "securityhub-findings-viewing.md").

Console

###### To view automation rules (console)

1. Using the credentials of the Security Hub CSPM administrator, open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose
   **Automations**.
3. Choose a rule name. Alternatively, select a rule.
4. Choose **Actions** and
   **View**.

API

###### To view automation rules (API)

1. To view the automation rules for your account, run [`ListAutomationRules`](../../1.0/APIReference/API_ListAutomationRules.md "../../1.0/APIReference/API_ListAutomationRules.md") from the Security Hub CSPM
   administrator account. This API returns the rule ARNs and other
   metadata for your rules. No input parameters are required for this
   API, but you can optionally provide `MaxResults` to limit
   the number of results and `NextToken` as a pagination
   parameter. The initial value of `NextToken` should be
   `NULL`.
2. For additional rule details, including the criteria and actions
   for a rule, run [`BatchGetAutomationRules`](../../1.0/APIReference/API_BatchGetAutomationRules.md "../../1.0/APIReference/API_BatchGetAutomationRules.md") from the Security Hub CSPM
   administrator account. Provide the ARNs of the automation rules that you want details for.

The following example retrieves details for the specified automation rules. This example is formatted for Linux, macOS, or Unix,
and it uses the backslash (\) line-continuation character to improve
readability.

```
`$` `aws securityhub batch-get-automation-rules \
--automation-rules-arns '["arn:aws:securityhub:`us-east-1:123456789012`:automation-rule/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`", "arn:aws:securityhub:`us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`"]' \
--region `us-east-1``
```
