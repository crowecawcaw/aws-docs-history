# Creating automation rules

An automation rule can be used to automatically update findings in AWS Security Hub CSPM. You can create a custom automation rule from scratch or, on the Security Hub CSPM console, use a pre-populated rule
template. For background information about how automation rules work, see [Understanding automation rules in Security Hub CSPM](automation-rules.md "automation-rules.md").

You can only create one automation rule at a time. To create multiple automation
rules, follow the console procedures multiple times, or call the API or command multiple
times with your desired parameters.

You must create an automation rule in each Region and account in which you want the
rule to apply to findings.

When you create an automation rule in the Security Hub CSPM console, Security Hub CSPM shows you a beta of
the findings to which your rule applies. The beta is currently not supported if your
rule criteria include a CONTAINS or NOT_CONTAINS filter. You can choose these filters
for map and string field types.

###### Important

AWS recommends that you don't include personally identifying, confidential, or
sensitive information in your rule name, description, or other fields.

## Creating a custom automation rule

Choose your preferred method, and complete the following steps to create a custom
automation rule.

Console

###### To create a custom automation rule (console)

1. Using the credentials of the Security Hub CSPM administrator, open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose
   **Automations**.
3. Choose **Create rule**. For **Rule
   Type**, choose **Create custom
   rule**.
4. In the **Rule** section, provide a unique
   rule name and a description for your rule.
5. For **Criteria**, use the
   **Key**, **Operator**, and
   **Value** drop down menus to specify your
   rule criteria. You must specify at least one rule
   criterion.

If supported for your selected criteria, the console shows you
a beta of findings that match your criteria. 6. For **Automated action**, use the drop down
menus to specify which finding fields to update when findings
match your rule criteria. You must specify at least one rule
action. 7. For **Rule status**, choose whether you want
the rule to be **Enabled** or
**Disabled** after it's created. 8. (Optional) Expand the **Additional settings**
section. Select **Ignore subsequent rules for findings
that match these criteria** if you want this rule
to be the last rule applied to findings that match the rule
criteria. 9. (Optional) For **Tags**, add tags as
key-value pairs to help you easily identify the rule. 10. Choose **Create rule**.

API

###### To create a custom automation rule (API)

1. Run [`CreateAutomationRule`](../../1.0/APIReference/API_CreateAutomationRule.md "../../1.0/APIReference/API_CreateAutomationRule.md") from the
   Security Hub CSPM administrator account. This API creates a rule with a
   specific Amazon Resource Name (ARN).
2. Provide a name and description for the rule.
3. Set the `IsTerminal` parameter to `true`
   if you want this rule to be the last rule applied to findings
   that match the rule criteria.
4. For the `RuleOrder` parameter, provide the order of
   the rule. Security Hub CSPM applies rules with a lower numerical value for
   this parameter first.
5. For the `RuleStatus` parameter, specify if you want
   Security Hub CSPM to enable and start applying the rule to findings after
   creation. If no value is specified, the default value is
   `ENABLED`. A value of `DISABLED` means
   that the rule is paused after creation.
6. For the `Criteria` parameter, provide the criteria
   that you want Security Hub CSPM to use to filter your findings. The rule
   action will apply to findings that match the criteria. For a
   list of supported criteria, see [Available rule criteria and rule
   actions](automation-rules.md#automation-rules-criteria-actions "automation-rules.md#automation-rules-criteria-actions").
7. For the `Actions` parameter, provide the actions
   that you want Security Hub CSPM to take when there's a match between a
   finding and your defined criteria. For a list of supported
   actions, see [Available rule criteria and rule
   actions](automation-rules.md#automation-rules-criteria-actions "automation-rules.md#automation-rules-criteria-actions").

The following example AWS CLI command creates an automation rule the updates the workflow status and note of matching
findings. This example
is formatted for Linux, macOS, or Unix, and it uses the backslash (\)
line-continuation character to improve readability.

```
`$` `aws securityhub create-automation-rule \
--actions '[{
 "Type": "FINDING_FIELDS_UPDATE",
 "FindingFieldsUpdate": {
 "Severity": {
 "Label": "`HIGH`"
 },
 "Note": {
 "Text": "`Known issue that is a risk. Updated by automation rules`",
 "UpdatedBy": "`sechub-automation`"
 }
 }
 }]' \
--criteria '{
 "SeverityLabel": [{
 "Value": "`INFORMATIONAL`",
 "Comparison": "`EQUALS`"
 }]
 }' \
--description "`A sample rule`" \
--no-is-terminal \
--rule-name "`sample rule`" \
--rule-order `1` \
--rule-status "`ENABLED`" \
--region `us-east-1``
```

## Creating an automation rule from a template (console only)

Rule templates reflect
common use cases for automation rules. Currently, only the Security Hub CSPM console supports rule templates.
Complete the following steps to create an automation rule from a template in the
console.

###### To create an automation rule from a template (console)

1. Using the credentials of the Security Hub CSPM administrator, open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose
   **Automations**.
3. Choose **Create rule**. For **Rule
   Type**, choose **Create a rule from
   template**.
4. Select a rule template from the drop down menu.
5. (Optional) If necessary for your use case, modify the
   **Rule**, **Criteria**,
   and **Automated action** sections. You must
   specify at least one rule criterion and one rule action.

If supported for your selected criteria, the console shows you
a beta of findings that match your criteria. 6. For **Rule status**, choose whether you want
the rule to be **Enabled** or
**Disabled** after it's created. 7. (Optional) Expand the **Additional settings**
section. Select **Ignore subsequent rules for findings
that match these criteria** if you want this rule
to be the last rule applied to findings that match the rule
criteria. 8. (Optional) For **Tags**, add tags as
key-value pairs to help you easily identify the rule. 9. Choose **Create rule**.
