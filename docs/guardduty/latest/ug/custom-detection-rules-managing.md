# Managing Custom Detection Rules

GuardDuty applies a rule to an account through an
_association_. An association links a rule to your account and
records the mode, live or dry run, in which the rule operates.

In an organization, the delegated GuardDuty administrator account uses organization configurations to manage rules
for member accounts centrally. An organization configuration supports include and
exclude lists to control which accounts a rule applies to. For more information, see
[Managing Custom Detection Rules in multiple-account environments](custom-detection-rules-multi-account.md "custom-detection-rules-multi-account.md").

## Listing available rules

The rule catalog lists every available rule, with filters for name, severity,
data source, MITRE ATT&CK® tactic, technique, and AWS service.

Console

###### To list available rules

1. Open the GuardDuty console at
   [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose
   **Custom Detection Rules**.
3. Use the filter controls to narrow the list by property
   (for example, severity or tactic).

API/CLI
Run the [ListCustomDetectionRules](../APIReference/API_ListCustomDetectionRules.md "../APIReference/API_ListCustomDetectionRules.md") operation. You can
pass filters to narrow results by name, severity, data source,
tactic, technique, or service.

```
aws guardduty list-custom-detection-rules \
    --filters Name=severity,Values=HIGH
```

## Viewing rule status

Each rule in your account has one of three statuses:

- **Live** – The rule is associated
  in live mode and generates findings.
- **Dry run** – The rule is
  associated in dry run mode and emits Amazon CloudWatch metrics only.
- **Disabled** – The rule has no
  association and is not evaluated.

Console
The **Status** column on the
**Custom Detection Rules** page shows the current status for
each rule. You can filter by status using the dropdown.

API/CLI
Run the [ListCustomDetectionRuleAssociations](../APIReference/API_ListCustomDetectionRuleAssociations.md "../APIReference/API_ListCustomDetectionRuleAssociations.md") operation
to see which rules are associated with your account and their current
mode.

```
aws guardduty list-custom-detection-rule-associations
```

## Bulk operations

Bulk operations apply the same mode change to more than one rule, or to one
rule across more than one account.

Console
On the **Custom Detection Rules** page, select multiple rules
using the checkboxes, then choose **Actions** to
enable or disable all selected rules in a single action.

API/CLI
To apply the same change to more than one rule, call [CreateCustomDetectionRuleAssociation](../APIReference/API_CreateCustomDetectionRuleAssociation.md "../APIReference/API_CreateCustomDetectionRuleAssociation.md") once
per rule.

```
for RULE in `rule-id-1` `rule-id-2`; do
    aws guardduty create-custom-detection-rule-association \
        --rule-id "$RULE" \
        --mode LIVE
done
```

To cover every rule in the catalog rather than a named list,
replace the rule IDs with the output of [ListCustomDetectionRules](../APIReference/API_ListCustomDetectionRules.md "../APIReference/API_ListCustomDetectionRules.md"):
`$(aws guardduty list-custom-detection-rules --query
 'Rules[].RuleId' --output text)`.

To apply a single rule to many accounts, use an organization
configuration instead of per-account calls. An organization
configuration targets member accounts with include and exclude lists,
and GuardDuty creates the individual associations. For more information,
see [Managing Custom Detection Rules in multiple-account environments](custom-detection-rules-multi-account.md "custom-detection-rules-multi-account.md").

## Dry run

In dry run mode, GuardDuty evaluates events against the rule but does not generate
findings. Instead, GuardDuty emits Amazon CloudWatch metrics that you can use to evaluate
signal volume and rule behavior before enabling live detection. GuardDuty publishes
these metrics only when the rule matches an event; if a rule never matches, it
produces no dry run metrics.

Use dry run mode to understand how a rule behaves in your environment without
triggering automated responses or generating findings in the console.

###### Note

A dry run association expires 14 days after it is created. When it expires,
GuardDuty stops evaluating the rule for that account and the rule returns to
disabled. To evaluate the rule again, create a new dry run association. Live
associations do not expire.

Console

###### To enable a rule in dry run mode

1. Open the GuardDuty console at
   [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Custom Detection Rules**.
3. Select one or more rules.
4. Choose **Actions**, and then choose
   **Enable (Dry Run)**.

API/CLI
Run the [CreateCustomDetectionRuleAssociation](../APIReference/API_CreateCustomDetectionRuleAssociation.md "../APIReference/API_CreateCustomDetectionRuleAssociation.md")
operation with `mode` set to
`DRY_RUN`.

```
aws guardduty create-custom-detection-rule-association \
    --rule-id `rule-id` \
    --mode DRY_RUN
```

## Live

In live mode, GuardDuty generates findings that appear in the GuardDuty console.
Findings are exported to Amazon EventBridge and, if you configure one, to an Amazon S3 bucket
that you own. Findings are also sent to integrated AWS services such as AWS
Security Hub. Use live mode for active threat detection in your
environment.

Console

###### To enable a rule in live mode

1. Open the GuardDuty console at
   [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Custom Detection Rules**.
3. Select one or more rules.
4. Choose **Actions**, and then choose
   **Enable (Live)**.

To switch an existing rule from dry run to live, select the rule,
choose **Actions**, and then choose
**Enable (Live)**.

API/CLI
To enable a new rule in live mode, run the [CreateCustomDetectionRuleAssociation](../APIReference/API_CreateCustomDetectionRuleAssociation.md "../APIReference/API_CreateCustomDetectionRuleAssociation.md")
operation with `mode` set to
`LIVE`.

```
aws guardduty create-custom-detection-rule-association \
    --rule-id `rule-id` \
    --mode LIVE
```

To switch an existing rule from dry run to live, run the
[UpdateCustomDetectionRuleAssociation](../APIReference/API_UpdateCustomDetectionRuleAssociation.md "../APIReference/API_UpdateCustomDetectionRuleAssociation.md")
operation.

## Disabling rules

Disabling a rule removes the association and stops GuardDuty from evaluating events
against that rule for your account.

Console

###### To disable Custom Detection Rules

1. Open the GuardDuty console at
   [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Custom Detection Rules**.
3. Select one or more rules that you want to disable.
4. Choose **Actions**, and then choose
   **Disable**.
5. Confirm the action when prompted.

API/CLI
Run the [DeleteCustomDetectionRuleAssociation](../APIReference/API_DeleteCustomDetectionRuleAssociation.md "../APIReference/API_DeleteCustomDetectionRuleAssociation.md")
operation.

```
aws guardduty delete-custom-detection-rule-association \
    --rule-id `rule-id`
```
