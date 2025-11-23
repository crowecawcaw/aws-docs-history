# Automation rules

Automation rules automatically implement recommended actions based on your defined criteria and schedule. Automation rules are global resources that manage automated actions across all AWS Regions where Compute Optimizer Automation is available. You can create, update, and delete automation rules from any AWS Region where Compute Optimizer Automation is available.

## Rule type

There are two types of rules:

- Account rules: Rules that apply recommended actions only to your account.
- Organization rules: Rules that centrally apply recommended actions across member accounts.

###### Note

Only the management account or delegated administrator can create organization rules. You can only select member accounts with Automation enabled and organization rules allowed can be selected for the rule to apply. Member accounts can view the details of organization rules that apply to their account but cannot edit them. Organization rules can be configured to apply before or after member account rules.

## Rule criteria

When configuring a rule, choose the recommended action types you want your rule to implement, such as snapshot and delete unattached Amazon EBS volumes and upgrade Amazon EBS volume type. Refine your selection using criteria such as AWS Region and Resource Tags. Then preview the current matching recommended actions to validate your criteria.

###### Important

If you don't specify rule criteria, Compute Optimizer applies all the selected recommended actions types in the accounts you select in your rule scope, including recommended actions in all AWS Regions where Compute Optimizer Automation is available.

The following recommended action attributes are currently supported as criteria for automation rules:

| Attribute                 | Operator       | Field type       |
| ------------------------- | -------------- | ---------------- | ---------------------- | ------------------------- | ------------------ | ------------------------- | ------------ |
| Current volume size (GiB) | `NumericEquals | NumericNotEquals | NumericLessThan        | NumericLessThanEquals     | NumericGreaterThan | NumericGreaterThanEquals` | Integer      |
| Current volume type       | `StringEquals  | StringNotEquals  | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike         | StringNotLike`            | String       |
| Estimated savings ($)     | `NumericEquals | NumericNotEquals | NumericLessThan        | NumericLessThanEquals     | NumericGreaterThan | NumericGreaterThanEquals` | Double       |
| Lookback period (days)    | `NumericEquals | NumericNotEquals | NumericLessThan        | NumericLessThanEquals     | NumericGreaterThan | NumericGreaterThanEquals` | Integer      |
| AWS Region                | `StringEquals  | StringNotEquals  | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike         | StringNotLike`            | String       |
| Resource ARN              | `StringEquals  | StringNotEquals  | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike         | StringNotLike`            | String       |
| Resource tags             | `StringEquals  | StringNotEquals  | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike         | StringNotLike`            | Resource Tag |
| Restart needed            | `StringEquals  | StringNotEquals  | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike         | StringNotLike`            | String       |

You can specify up to 20 conditions per attribute and 20 values per condition. For more information, see [Criteria](../APIReference/API_automation_Criteria.md "../APIReference/API_automation_Criteria.md") in the AWS Compute Optimizer Automation API Reference.

## Schedule

Set a schedule for when your rule runs by specifying the frequency (daily, weekly, or monthly), start time, end time, and timezone. During this window, Compute Optimizer will start implementing recommended actions that match your specified criteria. The number of actions that get initiated depends on the duration of your scheduled time window, Compute Optimizer Automation's concurrency limit, and the time required to complete each action. Automated actions will show as "In-Progress" until all steps in the automation workflow are fully completed. Up to 100 actions can be in-progress concurrently per account per AWS Region.

## Rule order

By default, rules are created with rule order 1 (highest priority) within their rule group. For example, when a management account creates an organization rule configured to apply after member account rules, it receives a rule order of 1, the highest priority among all rules in that group. Rule group and rule order determine which rule applies when a recommended action in an account matches multiple rules. Compute Optimizer assigns the action to the active rule with the lowest rule order value (highest priority), regardless of when that rule is scheduled to run.

For example, if a recommended action matches all of the rules in the following table, Compute Optimizer assigns it to Rule-C and implements it according to Rule-C's schedule.

| Rule group                                               | Rule order | Rule name | Status                                  | Schedule                                  |
| -------------------------------------------------------- | ---------- | --------- | --------------------------------------- | ----------------------------------------- |
| Organization rules evaluated before member account rules | 1          | Rule-A    | Inactive                                | Weekly on Mondays from 12:00 to 13:00 UTC |
| 2                                                        | Rule-B     | Inactive  | Daily from 12:00 to 13:00 UTC           |
| Member account rules                                     | 1          | Rule-C    | Active                                  | Monthly on 15th from 12:00 to 13:00 UTC   |
| 2                                                        | Rule-D     | Inactive  | Monthly on 15th from 12:00 to 13:00 UTC |
| Organization rules after before member account rules     | 1          | Rule-E    | Inactive                                | Weekly on Mondays from 12:00 to 13:00 UTC |
| 2                                                        | Rule-F     | Active    | Daily from 12:00 to 13:00 UTC           |
