**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Managing rule group behavior

This section describes your options for modifying how you use a rule group in your protection pack (web ACL).
This information applies to all rule group types. After you add a rule group to a protection pack (web ACL), you can override the actions of the individual rules in the rule group to
Count or to any other valid rule action setting. You can also override the
rule group's resulting action to Count, which has no effect on how the rules
are evaluated inside the rule group.

For information about these options, see [Overriding rule group actions in AWS WAF](web-acl-rule-group-override-options.md "web-acl-rule-group-override-options.md").

## Overriding rule actions in a rule

group

For each rule group in a protection pack (web ACL), you can override the
contained rule's actions for some or all of the rules.

The most common use case for this is overriding the rule actions to Count
to test new or updated rules. If you have metrics enabled, you receive metrics for
each rule that you override. For more information about testing, see [Testing and tuning your AWS WAF protections](web-acl-testing.md "web-acl-testing.md").

You can make these changes when you're adding a managed rule group to the
protection pack (web ACL), and you can make them to any type of rule group when
you edit the protection pack (web ACL). These instructions are for a rule group
that has already been added to the protection pack (web ACL). See additional
information about this option at [Rule group rule action overrides](web-acl-rule-group-override-options.md#web-acl-rule-group-override-options-rules "web-acl-rule-group-override-options.md#web-acl-rule-group-override-options-rules").

Using the new console

###### To override rule actions in a rule group

1. Choose the protection pack (web ACL) that you want to edit. The
   console makes the main protection pack (web ACL) card editable, and also
   opens a side panel with details you can edit.
2. In the protection pack (web ACL) card, choose the
   **Edit** link next to
   **Rules** to open the **Manage
   rules** panel.
3. In the **Manage rules** section for the rule
   group, choose the managed rule to open its action
   settings.
   - **Override rule group**
     – Changes the rule group action to Count mode but
     keeps all individual rule actions unchanged.
   - **Override all rule
     actions** – Applies a rule action to
     all rules, overriding their current state.
   - **Single rule override** –
     Applies a rule action to an individual rule.

4. When you are finished making your changes, choose
   **Save rule**.

Using the standard console

###### To override rule actions in a rule group

1. Edit the web ACL.
2. In the web ACL page **Rules** tab, select the rule
   group, then choose **Edit**.
3. In the **Rules** section for the rule group, manage the action settings
   as needed.
   - **All rules** – To set an override action for all
     rules in the rule group, open the **Override all rule
     actions** dropdown and select the override action.
     To remove the overrides for all rules, select **Remove
     all overrides**.
   - **Single rule** – To set an override action for a
     single rule, open the rule's dropdown and select the override
     action. To remove an override for a rule, open the rule's
     dropdown and select **Remove override**.

4. When you are finished making your changes, choose **Save rule**. The
   rule action and override action settings are listed in the rule group
   page.

The following example JSON listing shows a rule group declaration inside a protection pack (web ACL) that
overrides the rule actions to Count for the rules
`CategoryVerifiedSearchEngine` and
`CategoryVerifiedSocialMedia`. In the JSON, you override all rule
actions by providing a `RuleActionOverrides` entry for each
individual rule.

```
{
    "Name": "AWS-AWSBotControl-Example",
   "Priority": 5,
   "Statement": {
    "ManagedRuleGroupStatement": {
        "VendorName": "AWS",
        "Name": "`AWSManagedRulesBotControlRuleSet`",
        "RuleActionOverrides": [
          {
            "ActionToUse": {
              "Count": {}
            },
            "Name": "CategoryVerifiedSearchEngine"
          },
          {
            "ActionToUse": {
              "Count": {}
            },
            "Name": "CategoryVerifiedSocialMedia"
          }
        ],
        "ExcludedRules": []
    },
   "VisibilityConfig": {
       "SampledRequestsEnabled": true,
       "CloudWatchMetricsEnabled": true,
       "MetricName": "AWS-AWSBotControl-Example"
   }
}
```

## Overriding a rule group's evaluation

result to Count

You can override the action that results from a rule group evaluation, without altering
how the rules in the rule group are configured or evaluated. This option is not
commonly used. If any rule in the rule group results in a match, this override
sets the resulting action from the rule group to Count.

###### Note

This is an uncommon use case. Most action overrides are done at the rule
level, inside the rule group, as described in [Overriding rule actions in a rule
group](#web-acl-rule-group-rule-action-override "#web-acl-rule-group-rule-action-override").

You can override the rule group's resulting action in the protection pack (web ACL) when you add
or edit the rule group. In the console, open the rule group's **Override
rule group action - optional** pane and enable the override. In the
JSON set `OverrideAction` in the rule group statement, as shown in
the following example listing:

```
{
   "Name": "AWS-AWSBotControl-Example",
   "Priority": 5,
   "Statement": {
    "ManagedRuleGroupStatement": {
     "VendorName": "AWS",
     "Name": "`AWSManagedRulesBotControlRuleSet`"
     }
   },
    **"OverrideAction": {
 "Count": {}
 },**   "VisibilityConfig": {
        "SampledRequestsEnabled": true,
        "CloudWatchMetricsEnabled": true,
        "MetricName": "AWS-AWSBotControl-Example"
   }
}
```
