# Managing Custom Detection Rules in multiple-account environments

In an organization, the delegated GuardDuty administrator account manages Custom Detection Rules for member accounts
centrally using _organization configurations_. The administrator
declares intent for each rule, and GuardDuty applies it to member accounts
automatically, including accounts that join later.

###### Note

Multi-account management of Custom Detection Rules is supported only for accounts managed
through AWS Organizations. Invitation-based member accounts are not supported for
centralized rule management.

## Organization configurations

A member account cannot enable, disable, or change a Custom Detection Rule for itself.
If you attempt to call the single-account association operations from a member
account, GuardDuty returns an `AccessDeniedException` error. The administrator
manages the rule on the
member's behalf. For more information about the delegated administrator and member
accounts, see [Managing multiple accounts in GuardDuty](guardduty_accounts.md "guardduty_accounts.md").

An organization configuration links a single rule to a set of member accounts. It
records the mode, live or dry run, in which the rule operates for those accounts.
GuardDuty then creates an individual association for the rule in each targeted member
account. You can configure rules for all members or for specific accounts by using
include and exclude lists.

Console

###### To configure a Custom Detection Rule for the organization

1. Open the GuardDuty console at
   [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose
   **Custom Detection Rules**.
3. Choose a rule name to open the rule details, and then choose
   the **Accounts** tab.
4. Choose **Configure** next to
   **Organization Configuration**.
5. Select the mode (**Live** or
   **Dry run**) and choose which accounts to
   include or exclude.

API/CLI

Create an organization configuration

Run [CreateCustomDetectionRuleOrgConfiguration](../APIReference/API_CreateCustomDetectionRuleOrgConfiguration.md "../APIReference/API_CreateCustomDetectionRuleOrgConfiguration.md")
to create a rule configuration for member accounts.

Update an organization configuration

Run [UpdateCustomDetectionRuleOrgConfiguration](../APIReference/API_UpdateCustomDetectionRuleOrgConfiguration.md "../APIReference/API_UpdateCustomDetectionRuleOrgConfiguration.md")
to modify the mode or account scope.

Delete an organization configuration

Run [DeleteCustomDetectionRuleOrgConfiguration](../APIReference/API_DeleteCustomDetectionRuleOrgConfiguration.md "../APIReference/API_DeleteCustomDetectionRuleOrgConfiguration.md")
to remove the organization configuration. Because a rule can
hold one configuration per mode, `mode` selects
which one to remove; the other is left in place.

###### Note

Deleting an organization configuration does not cascade-delete the
existing member account associations. The rule stays enabled in the
member accounts where GuardDuty already applied it.

###### Note

A dry run organization configuration expires 14 days after you create it. The
member account associations that GuardDuty created from that configuration expire with
it, rather than 14 days after each association was created.

## Running both modes for the same rule

A rule holds at most one organization configuration per mode, so a rule can run in
live mode and dry run mode at the same time only under the following condition: both
configurations must name their target accounts with an explicit include list.

A configuration that claims the whole organization is one-shot for its rule. A
configuration claims the whole organization when it names no accounts at all, or when
it names accounts to exclude. No configuration for the other mode can coexist with it,
and attempting to create one returns `ConflictException`. To move a
whole-organization configuration to a different mode, update the existing
configuration instead of creating a second one.

## Example: Apply a rule in dry run mode to all member accounts

The following AWS CLI command creates an organization configuration that
targets every member account, including accounts that join later. Omitting both
`--include-account-ids` and `--exclude-account-ids` targets
the entire organization.

```
aws guardduty create-custom-detection-rule-org-configuration \
    --rule-id "EXAMPLE_RULE_ID" \
    --mode DRY_RUN
```

To move the rule to live detection, update the existing configuration with
[UpdateCustomDetectionRuleOrgConfiguration](../APIReference/API_UpdateCustomDetectionRuleOrgConfiguration.md "../APIReference/API_UpdateCustomDetectionRuleOrgConfiguration.md").

## Applying every rule across an organization

The console configures one rule at a time. To apply the same mode to every
available rule across the organization, loop over the rule catalog with the AWS
CLI. Omitting both `--include-account-ids` and
`--exclude-account-ids` targets every member account, including
accounts that join later.

```
for RULE in $(aws guardduty list-custom-detection-rules \
    --query 'Rules[].RuleId' --output text); do
    aws guardduty create-custom-detection-rule-org-configuration \
        --rule-id "$RULE" \
        --mode DRY_RUN
done
```

This loop uses `--mode DRY_RUN` so you can measure signal volume
before any rule generates findings. Because the loop names no accounts, each
configuration claims the whole organization and is one-shot for its rule. When you
are ready, move each rule to live detection by updating the existing configuration
with [UpdateCustomDetectionRuleOrgConfiguration](../APIReference/API_UpdateCustomDetectionRuleOrgConfiguration.md "../APIReference/API_UpdateCustomDetectionRuleOrgConfiguration.md"). Running the
loop again with `--mode LIVE` returns
`ConflictException`, because the whole-organization dry run
configuration already exists.
