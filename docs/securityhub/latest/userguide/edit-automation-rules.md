# Editing automation rules

An automation rule can be used to automatically update findings in AWS Security Hub CSPM. For background information about how automation rules work, see [Understanding automation rules in Security Hub CSPM](automation-rules.md "automation-rules.md").

After creating an automation rule, the delegated Security Hub CSPM administrator can edit the rule. When you edit an automation rule, the changes apply to new and updated findings that
Security Hub CSPM generates or ingests after the rule edit.

Choose your preferred method, and follow the steps to edit the contents of an
automation rule. You can edit one or more rules with a single request. For instructions
on editing rule order, see [Editing automation rule order](edit-rule-order.md "edit-rule-order.md").

Console

###### To edit automation rules (console)

1. Using the credentials of the Security Hub CSPM administrator, open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose
   **Automations**.
3. Select the rule that you want to edit. Choose
   **Action** and
   **Edit**.
4. Change the rule as desired, and choose **Save
   changes**.

API

###### To edit automation rules (API)

1. Run [`BatchUpdateAutomationRules`](../../1.0/APIReference/API_BatchUpdateAutomationRules.md "../../1.0/APIReference/API_BatchUpdateAutomationRules.md") from the
   Security Hub CSPM administrator account.
2. For the `RuleArn` parameter, provide the ARN of the
   rule(s) that you want to edit.
3. Provide the new values for the parameters that you want to edit.
   You can edit any parameter except `RuleArn`.

The following example updates the specified automation rule. This example is formatted for Linux, macOS, or Unix,
and it uses the backslash (\) line-continuation character to improve
readability.

```
`$` `aws securityhub batch-update-automation-rules \
--update-automation-rules-request-items '[
 {
 "Actions": [{
 "Type": "FINDING_FIELDS_UPDATE",
 "FindingFieldsUpdate": {
 "Note": {
 "Text": "`Known issue that is a risk`",
 "UpdatedBy": "`sechub-automation`"
 },
 "Workflow": {
 "Status": "`NEW`"
 }
 }
 }],
 "Criteria": {
 "SeverityLabel": [{
 "Value": "`LOW`",
 "Comparison": "`EQUALS`"
 }]
 },
 "RuleArn": "arn:aws:securityhub:`us-east-1:123456789012`:automation-rule/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
 "RuleOrder": `14`,
 "RuleStatus": "`DISABLED`",
 }
 ]' \
--region `us-east-1``
```
