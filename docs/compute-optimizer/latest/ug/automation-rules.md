

# Automation rules

Automation rules automatically implement recommended actions based on your defined criteria and schedule. Automation rules are global resources that manage automated actions across all AWS Regions where Compute Optimizer Automation is available. You can create, update, and delete automation rules from any AWS Region where Compute Optimizer Automation is available.

You can also create automation rules with CloudFormation. For more information, see [Creating automation rules with CloudFormation](creating-automation-rules-with-cloudformation.md). For more information about viewing your rules, see [Viewing automation rules](automation-rules-view.md). To review the actions that your rules implement, see [View automation events](automation-events-view-details.md).

## Rule type
<a name="automation-rules-type"></a>

There are two types of rules:
+ Account rules: Rules that apply recommended actions only to your account.
+ Organization rules: Rules that centrally apply recommended actions across member accounts. 

**Note**  
Only the management account or delegated administrator can create organization rules. You can scope an organization rule to member accounts, organizational units (OUs), or the organization root. The rule applies only to accounts in its scope that have Automation enabled and the organization rule mode **Any allowed**. Member accounts can view the details of organization rules that apply to their account but cannot edit them. Organization rules can be configured to apply before or after member account rules.

## Rule scope
<a name="automation-rules-scope"></a>

An organization rule applies to the accounts in its scope. You can scope a rule to specific accounts, to organizational units (OUs), or to your whole organization. In the console, you choose accounts and OUs from the same list in the **Include** and **Exclude** fields. The following table lists the API fields that define a rule scope and the console field for each.


| Field | Console | Maximum | 
| --- | --- | --- | 
| `accountIds` | **Include** | Up to 50 account IDs | 
| `organizationalUnitIds` | **Include** | Up to 150 OU or root IDs | 
| `excludedAccountIds` | **Exclude** | Up to 50 account IDs | 
| `excludedOrganizationalUnitIds` | **Exclude** | Up to 150 OU or root IDs | 
+ A rule that includes an OU applies to every account in the OU and in all of its child OUs, including accounts added later. An included OU can contain any number of accounts.
+ Each OU or root that you include must have the organization rule mode **Any allowed**, from an enrollment configuration on it or on a parent. For more information, see [Organization enrollment configurations](automation-org-enrollment.md).
+ You must include at least one account or OU. To apply a rule to your whole organization, include the root.
+ A rule never applies to the management account, even when you include the root.
+ An exclusion takes precedence. An account in an excluded OU is out of scope, even if you also include the account.
+ An ID can't appear in both an include list and an exclude list.
+ You can exclude an account or OU that is outside the included scope. The exclusion applies if the account or OU moves into scope later.
+ Compute Optimizer checks OU membership each time the rule runs. When an account moves into or out of an included OU, the rule scope changes to match.
+ To see the recommended actions that a rule would apply, preview the rule before you activate it. The preview shows only accounts that have matching recommended actions.

## Rule criteria
<a name="automation-rules-criteria"></a>

When configuring a rule, choose the recommended action types you want your rule to implement, such as snapshot and delete unattached Amazon Elastic Block Store (Amazon EBS) volumes and upgrade Amazon EBS volume type. Refine your selection using criteria such as AWS Region and Resource Tags. Then preview the current matching recommended actions to validate your criteria.

**Important**  
If you don't specify rule criteria, Compute Optimizer applies all the selected recommended action types to the accounts in your rule scope. This includes recommended actions in all AWS Regions where Compute Optimizer Automation is available.

The following recommended action attributes and comparison operators are supported for automation rules:


**Recommended action attributes and supported operators**  

| Attribute | Operator | Field type | 
| --- | --- | --- | 
| Current volume size (GiB) | `NumericEquals \| NumericNotEquals \| NumericLessThan \| NumericLessThanEquals \| NumericGreaterThan \| NumericGreaterThanEquals \| NumericEqualsIfExists \| NumericNotEqualsIfExists \| NumericLessThanIfExists \| NumericLessThanEqualsIfExists \| NumericGreaterThanIfExists \| NumericGreaterThanEqualsIfExists` | Integer | 
| Current volume type | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | String | 
| Estimated savings ($) | `NumericEquals \| NumericNotEquals \| NumericLessThan \| NumericLessThanEquals \| NumericGreaterThan \| NumericGreaterThanEquals \| NumericEqualsIfExists \| NumericNotEqualsIfExists \| NumericLessThanIfExists \| NumericLessThanEqualsIfExists \| NumericGreaterThanIfExists \| NumericGreaterThanEqualsIfExists` | Double | 
| Lookback period (days) | `NumericEquals \| NumericNotEquals \| NumericLessThan \| NumericLessThanEquals \| NumericGreaterThan \| NumericGreaterThanEquals \| NumericEqualsIfExists \| NumericNotEqualsIfExists \| NumericLessThanIfExists \| NumericLessThanEqualsIfExists \| NumericGreaterThanIfExists \| NumericGreaterThanEqualsIfExists` | Integer | 
| AWS Region | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | String | 
| Resource ARN | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | String | 
| Resource tags | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | Resource Tag | 
| Restart needed | `StringEquals \| StringNotEquals \| StringEqualsIgnoreCase \| StringNotEqualsIgnoreCase \| StringLike \| StringNotLike \| StringEqualsIfExists \| StringNotEqualsIfExists \| StringEqualsIgnoreCaseIfExists \| StringNotEqualsIgnoreCaseIfExists \| StringLikeIfExists \| StringNotLikeIfExists` | String | 

You can specify up to 20 conditions per attribute and 20 values per condition. For more information, see [Criteria](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Criteria.html) in the AWS Compute Optimizer Automation API Reference.

### Comparison operators
<a name="automation-rules-comparison-operators"></a>

Use comparison operators in rule criteria to match recommended action attributes against the values you specify.

**Important**  
If the attribute that you specify in your rule criteria is not present on the recommended action, the values do not match, the condition is false, and the recommended action is excluded from the rule. This logic applies to all comparison operators except those with the `IfExists` suffix, which evaluate to true when the attribute is not present. Operators with the `IfExists` suffix test whether the attribute is present (exists) on the recommended action.

#### String condition operators
<a name="automation-rules-string-operators"></a>

String condition operators let you define rule criteria that compare a recommended action attribute to a string you specify.


**String condition operators**  

| Condition operator | Description | 
| --- | --- | 
| `StringEquals` | Exact matching, case sensitive. | 
| `StringNotEquals` | Negated exact matching, case sensitive. | 
| `StringEqualsIgnoreCase` | Exact matching, ignoring case. | 
| `StringNotEqualsIgnoreCase` | Negated matching, ignoring case. | 
| `StringLike` | Case-sensitive matching. The values can include multi-character match wildcards (`*`) anywhere in the string. You must specify wildcards to achieve partial string matches. | 
| `StringNotLike` | Negated case-sensitive matching. The values can include multi-character match wildcards (`*`) anywhere in the string. | 

**Note**  
Using `*` alone as a value with `StringLike` matches any value that is present. When combined with `StringNotLike`, a value of `*` means "does not match anything" — effectively excluding all recommended actions where the attribute is present. For example, using `StringNotLike` on a tag key `Application` with value `*` excludes any recommended action that has the `Application` tag, regardless of the tag's value.

#### Numeric condition operators
<a name="automation-rules-numeric-operators"></a>

Numeric condition operators let you define rule criteria that compare a recommended action attribute to an integer or decimal number.


**Numeric condition operators**  

| Condition operator | Description | 
| --- | --- | 
| `NumericEquals` | Exact numeric matching. | 
| `NumericNotEquals` | Negated numeric matching. | 
| `NumericLessThan` | "Less than" matching. | 
| `NumericLessThanEquals` | "Less than or equals" matching. | 
| `NumericGreaterThan` | "Greater than" matching. | 
| `NumericGreaterThanEquals` | "Greater than or equals" matching. | 

For example, you can use `NumericGreaterThanEquals` with the **Lookback period** attribute to create a rule that only automates recommended actions where the lookback period used to generate the recommendation is at least 32 days.

### IfExists operators
<a name="automation-rules-ifexists-operators"></a>

Append `IfExists` to any comparison operator (for example, `StringLikeIfExists`) to change how a condition is evaluated when the attribute you specify is **absent** from a recommended action:
+ With a base operator, an absent attribute evaluates to **false**, and the recommended action is **excluded** from the rule.
+ With the `IfExists` variant, an absent attribute evaluates to **true**, and the recommended action is **included**.

`IfExists` is helpful when you want to exclude a specific group of resources from a rule but still include the resources that don't carry the tag you're filtering on. For example, you might want to include everything except the resources owned by one team. A base `StringNotEquals` on `team` = `TeamA` excludes TeamA's resources, but it also excludes every resource that doesn't carry the `team` tag at all — leaving out resources you intended to include. Add `IfExists` to keep those untagged resources in scope:
+ **StringNotEquals** matches only resources that have the `team` tag set to a value other than `TeamA`. Untagged resources are excluded.
+ **StringNotEqualsIfExists** matches resources without the `team` tag *and* resources where it is set to any value other than `TeamA`. Only resources tagged `team` = `TeamA` are excluded.

`IfExists` is also helpful when you want to let resource owners exclude their own resources from automation. You can designate a dedicated opt-out tag, such as `automation-opt-out`, that an owner applies to any resource they want to leave out. In this case, the presence of the tag matters, not its value, so use `StringNotLikeIfExists` with the value `*` on the `automation-opt-out` tag key. The `*` wildcard matches any value, so Compute Optimizer excludes every resource that carries the tag. The `IfExists` variant keeps the resources that don't carry the tag in scope; without it, every untagged resource would be excluded as well.

### Rule criteria examples
<a name="automation-rules-criteria-examples"></a>

#### Example: Include only recommended actions in specific Regions
<a name="automation-rules-criteria-examples-regions"></a>

The following rule criteria uses `StringEquals` on the **AWS Region** attribute to match recommended actions for resources in `us-east-1` or `us-west-2`. When you specify more than one value for a condition, the values have an OR relationship — a recommended action matches the condition if its attribute value matches any one of the values.

Criteria configuration:


**Region criteria: configuration**  

| Attribute | Operator | Values | 
| --- | --- | --- | 
| AWS Region | `StringEquals` | `us-east-1`, `us-west-2` | 

Evaluation:


**Region criteria: evaluation**  

| Attribute value | Result | 
| --- | --- | 
| `us-east-1` | Match | 
| `us-west-2` | Match | 
| `eu-west-1` | No match | 

#### Example: Include only recommended actions generated with a minimum lookback period
<a name="automation-rules-criteria-examples-lookback"></a>

The following rule criteria uses `NumericGreaterThanEquals` on the **Lookback period (days)** attribute to only automate recommended actions where the lookback period used to generate the recommendation is at least 32 days. This lets you require a longer observation window before a recommended action is automated.

Criteria configuration:


**Lookback period criteria: configuration**  

| Attribute | Operator | Values | 
| --- | --- | --- | 
| Lookback period (days) | `NumericGreaterThanEquals` | `32` | 

Evaluation:


**Lookback period criteria: evaluation**  

| Attribute value | Result | 
| --- | --- | 
| `32` | Match | 
| `14` | No match | 

#### Example: Include recommended actions unless the resource belongs to a specific team
<a name="automation-rules-criteria-examples-team"></a>

Consider a platform team that enables Compute Optimizer Automation across many accounts but wants to leave one team's resources out of the rule. The team already tags resources with a `team` tag for other purposes, but not every resource carries it. They want automation applied broadly while excluding any resource tagged `team` = `TeamA`.

The following rule criteria uses `StringNotEqualsIfExists` on the **Resource tags** attribute, with the tag key `team` and the value `TeamA`. A recommended action is included when the resource doesn't have the `team` tag at all, or when the tag is set to any value other than `TeamA`. Because many resources won't carry the tag, `IfExists` is what keeps them in scope — without it, every untagged resource would be excluded.

Criteria configuration:


**Team exclusion criteria: configuration**  

| Attribute | Operator | Tag key | Values | 
| --- | --- | --- | --- | 
| Resource tags | `StringNotEqualsIfExists` | `team` | `TeamA` | 

Evaluation:


**Team exclusion criteria: evaluation**  

| Recommended action state | Result | Explanation | 
| --- | --- | --- | 
| The resource does not have the `team` tag | Match | The attribute is absent, and `IfExists` evaluates absent attributes as true. | 
| The resource has tag `team` = `web` | Match | The tag is present and the value does not match `TeamA`. | 
| The resource has tag `team` = `TeamA` | No match | The tag is present and the value matches `TeamA`, so the recommended action is excluded. | 

#### Example: Include recommended actions unless the resource has an opt-out tag
<a name="automation-rules-criteria-examples-optout"></a>

You can let resource owners exclude individual resources from automation by applying a dedicated opt-out tag. In this example, an owner adds the `automation-opt-out` tag to any resource they want to leave out.

The following rule criteria uses `StringNotLikeIfExists` on the **Resource tags** attribute, with the tag key `automation-opt-out` and the value `*`. The `*` wildcard matches any value, so any resource that carries the tag is excluded. A recommended action is included when the resource doesn't have the `automation-opt-out` tag.

Criteria configuration:


**Opt-out tag criteria: configuration**  

| Attribute | Operator | Tag key | Values | 
| --- | --- | --- | --- | 
| Resource tags | `StringNotLikeIfExists` | `automation-opt-out` | `*` | 

Evaluation:


**Opt-out tag criteria: evaluation**  

| Recommended action state | Result | Explanation | 
| --- | --- | --- | 
| The resource does not have the `automation-opt-out` tag | Match | The attribute is absent, and `IfExists` evaluates absent attributes as true. | 
| The resource has tag `automation-opt-out` = `true` | No match | The tag is present, and `*` matches any value, so the recommended action is excluded. | 
| The resource has tag `automation-opt-out` = `temporary` | No match | The tag is present, and `*` matches any value, so the recommended action is excluded. | 

#### Example: Exclude recommended actions on infrastructure-as-code (IaC) managed resources
<a name="automation-rules-criteria-examples-iac"></a>

If you manage resources using an infrastructure-as-code (IaC) tool such as CloudFormation or Terraform, you can create an exclusion rule that filters out IaC-managed resources based on resource tags.

##### CloudFormation
<a name="automation-rules-criteria-examples-iac-cfn"></a>

Resources managed using CloudFormation have the system tags `aws:cloudformation:stack-id`, `aws:cloudformation:stack-name`, and `aws:cloudformation:logical-id`. You can filter on one of these tags to identify CloudFormation-managed resources. This example filters on `aws:cloudformation:stack-id`.

The following rule criteria uses `StringNotLikeIfExists` on the **Resource tags** attribute, with the tag key `aws:cloudformation:stack-id` and the value `*`. The `*` wildcard matches any value, so any resource that carries the tag is excluded. A recommended action is included when the resource does not have the `aws:cloudformation:stack-id` tag.

Criteria configuration:


**CloudFormation exclusion criteria: configuration**  

| Attribute | Operator | Tag key | Values | 
| --- | --- | --- | --- | 
| Resource tags | `StringNotLikeIfExists` | `aws:cloudformation:stack-id` | `*` | 

Evaluation:


**CloudFormation exclusion criteria: evaluation**  

| Recommended action state | Result | Explanation | 
| --- | --- | --- | 
| The resource has tag `aws:cloudformation:stack-id` = `arn:aws:cloudformation:us-east-1:123456789012:stack/my-stack/2ac98f30-5bdd-11e4-949b-50fa5262a838` | No match | The tag is present, and `*` matches any value, so the recommended action is excluded. | 
| The resource does not have the `aws:cloudformation:stack-id` tag | Match | The attribute is absent, and `IfExists` evaluates absent attributes as true. | 
| The resource has tag `Environment` = `production`, but not the `aws:cloudformation:stack-id` tag | Match | The attribute is absent, and `IfExists` evaluates absent attributes as true. | 

##### Terraform
<a name="automation-rules-criteria-examples-iac-terraform"></a>

To exclude Terraform-managed resources from automated actions, add a user tag (for example, `ManagedBy` = `terraform`) to those resources in your Terraform configuration. After tagging, you can apply tag-based rule criteria to exclude them, similar to the preceding CloudFormation example.

#### Example: Combine multiple criteria
<a name="automation-rules-criteria-examples-combine"></a>

You can combine multiple criteria to narrow the scope of your rule. All criteria must match for a recommended action to be included in the rule (AND logic).

The following configuration automates EBS volume recommended actions that:

1. Are in us-east-1 and us-west-2

1. Were generated with a lookback period of at least 32 days; and

1. Are not opted out of automation (no `automation-opt-out` tag).

This rule includes a recommended action only when all three conditions are met simultaneously.

Criteria configuration:


**Combined criteria: configuration**  

| Attribute | Operator | Values | 
| --- | --- | --- | 
| AWS Region | `StringEquals` | `us-east-1`, `us-west-2` | 
| Lookback period (days) | `NumericGreaterThanEquals` | `32` | 
| Resource tags (key: `automation-opt-out`) | `StringNotLikeIfExists` | `*` | 

## Schedule
<a name="automation-rules-schedule"></a>

Set a schedule for when your rule runs by specifying the frequency (daily, weekly, or monthly), start time, end time, and timezone. During this window, Compute Optimizer will start implementing recommended actions that match your specified criteria. The number of actions that get initiated depends on the duration of your scheduled time window, Compute Optimizer Automation's concurrency limit, and the time required to complete each action. Automated actions will show as "In-Progress" until all steps in the automation workflow are fully completed. Up to 100 actions can be in-progress concurrently per account per AWS Region.

## Rule order
<a name="automation-rules-order"></a>

By default, rules are created with rule order 1 (highest priority) within their rule group. For example, a management account might create an organization rule configured to apply after member account rules. That rule receives a rule order of 1, the highest priority among all rules in that group. Rule group and rule order determine which rule applies when a recommended action in an account matches multiple rules. Compute Optimizer assigns the action to the active rule with the lowest rule order (highest priority), regardless of when that rule is scheduled to run.

For example, if a recommended action matches all of the rules in the following table, Compute Optimizer assigns it to Rule-C and implements it according to Rule-C's schedule.


**Rule order example**  

| Rule group | Rule order | Rule name | Status | Schedule | 
| --- | --- | --- | --- | --- | 
| Organization rules evaluated before member account rules | 1 | Rule-A | Inactive | Weekly on Mondays from 12:00 to 13:00 UTC | 
| Organization rules evaluated before member account rules | 2 | Rule-B | Inactive | Daily from 12:00 to 13:00 UTC | 
| Member account rules | 1 | Rule-C | Active | Monthly on 15th from 12:00 to 13:00 UTC | 
| Member account rules | 2 | Rule-D | Inactive | Monthly on 15th from 12:00 to 13:00 UTC | 
| Organization rules evaluated after member account rules | 1 | Rule-E | Inactive | Weekly on Mondays from 12:00 to 13:00 UTC | 
| Organization rules evaluated after member account rules | 2 | Rule-F | Active | Daily from 12:00 to 13:00 UTC | 