

# Managing Custom Detection Rules in multiple-account environments

In an organization, the delegated GuardDuty administrator account manages Custom Detection Rules for member accounts centrally using *organization configurations*. The administrator declares intent for each rule, and GuardDuty applies it to member accounts automatically, including accounts that join later.

**Note**  
Multi-account management of Custom Detection Rules is supported only for accounts managed through AWS Organizations. Invitation-based member accounts are not supported for centralized rule management.

## Organization configurations
<a name="custom-detection-rules-multi-account-org-configs"></a>

A member account cannot enable, disable, or change a Custom Detection Rule for itself. If you attempt to call the single-account association operations from a member account, GuardDuty returns an `AccessDeniedException` error. The administrator manages the rule on the member's behalf. For more information about the delegated administrator and member accounts, see [Managing multiple accounts in GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html).

An organization configuration links a single rule to a set of member accounts. It records the mode, live or dry run, in which the rule operates for those accounts. GuardDuty then creates an individual association for the rule in each targeted member account. You can configure rules for all members or for specific accounts by using include and exclude lists.

------
#### [ Console ]

**To configure a Custom Detection Rule for the organization**

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Custom Detection Rules**.

1. Choose a rule name to open the rule details, and then choose the **Accounts** tab.

1. Choose **Configure** next to **Organization Configuration**.

1. Select the mode (**Live** or **Dry run**) and choose which accounts to include or exclude.

------
#### [ API/CLI ]

Create an organization configuration  
Run [CreateCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateCustomDetectionRuleOrgConfiguration.html) to create a rule configuration for member accounts.

Update an organization configuration  
Run [UpdateCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateCustomDetectionRuleOrgConfiguration.html) to replace the account scope of an existing configuration. Because a rule can hold one configuration per mode, `mode` selects which configuration to update. An update doesn't change the mode of the configuration. When you update a dry run configuration, its 14-day expiry restarts.

Change the mode of an organization configuration  
To change the mode of an organization configuration, complete the following steps:  

1. Delete the existing configuration with [DeleteCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteCustomDetectionRuleOrgConfiguration.html).

1. Create a configuration in the new mode with [CreateCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateCustomDetectionRuleOrgConfiguration.html).
The new configuration has the status `PROCESSING` until GuardDuty applies it to the targeted member accounts, and then the status changes to `ACTIVE`.  
Delete the existing configuration first. Otherwise, creating a configuration in the other mode returns `ConflictException` if either configuration targets the whole organization, or if both name the same account.  
You don't need to delete the member account associations. After you create the new configuration, GuardDuty switches the existing associations in the targeted member accounts to the new mode.  
If the existing configuration has the status `PROCESSING`, the delete request can return `ConflictException`. Retry when the status is no longer `PROCESSING`.

Delete an organization configuration  
Run [DeleteCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteCustomDetectionRuleOrgConfiguration.html) to remove the organization configuration. Because a rule can hold one configuration per mode, `mode` selects which one to remove; the other is left in place.

**Note**  
Deleting an organization configuration does not cascade-delete the existing member account associations. The rule stays enabled in the member accounts where GuardDuty already applied it.

------

**Note**  
A dry run organization configuration expires 14 days after you create it or last update it. The member account associations that GuardDuty created from that configuration expire with it, rather than 14 days after each association was created.

## Running both modes for the same rule
<a name="custom-detection-rules-multi-account-both-modes"></a>

A rule holds at most one organization configuration per mode, so a rule can run in live mode and dry run mode at the same time only under the following condition: both configurations must name their target accounts with an explicit include list.

A configuration that claims the whole organization is one-shot for its rule. A configuration claims the whole organization when it names no accounts at all, or when it names accounts to exclude. No configuration for the other mode can coexist with it, and attempting to create one returns `ConflictException`. To move a whole-organization configuration to a different mode, delete it, and then create a configuration in the new mode. For more information, see [Organization configurations](#custom-detection-rules-multi-account-org-configs).

## Example: Apply a rule in dry run mode to all member accounts
<a name="custom-detection-rules-multi-account-example"></a>

The following AWS CLI command creates an organization configuration that targets every member account, including accounts that join later. Omitting both `--include-account-ids` and `--exclude-account-ids` targets the entire organization.

```
aws guardduty create-custom-detection-rule-org-configuration \
    --rule-id {{rule-id}} \
    --mode DRY_RUN
```

The following AWS CLI commands move the rule to live detection by deleting the dry run configuration and then creating a live configuration.

```
aws guardduty delete-custom-detection-rule-org-configuration \
    --rule-id {{rule-id}} \
    --mode DRY_RUN

aws guardduty create-custom-detection-rule-org-configuration \
    --rule-id {{rule-id}} \
    --mode LIVE
```

After you create the live configuration, GuardDuty switches the existing dry run associations in the member accounts to live.

## Applying every rule across an organization
<a name="custom-detection-rules-org-all-rules"></a>

The console configures one rule at a time. To apply the same mode to every available rule across the organization, loop over the rule catalog with the AWS CLI. Omitting both `--include-account-ids` and `--exclude-account-ids` targets every member account, including accounts that join later.

```
for RULE in $(aws guardduty list-custom-detection-rules \
    --query 'Rules[].RuleId' --output text); do
    aws guardduty create-custom-detection-rule-org-configuration \
        --rule-id "$RULE" \
        --mode DRY_RUN
done
```

This loop uses `--mode DRY_RUN` so you can measure signal volume before any rule generates findings. Because the loop names no accounts, each configuration claims the whole organization and is one-shot for its rule. Running the loop again with `--mode LIVE` returns `ConflictException`, because the whole-organization dry run configuration already exists.

When you are ready, the following AWS CLI loop moves each rule to live detection by deleting its dry run configuration and then creating a live configuration.

```
for RULE in $(aws guardduty list-custom-detection-rules \
    --query 'Rules[].RuleId' --output text); do
    aws guardduty delete-custom-detection-rule-org-configuration \
        --rule-id "$RULE" \
        --mode DRY_RUN
    aws guardduty create-custom-detection-rule-org-configuration \
        --rule-id "$RULE" \
        --mode LIVE
done
```