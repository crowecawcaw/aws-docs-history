# Using AWS Organizations upgrade rollout policy

for automatic minor version upgrades

Amazon RDS supports AWS Organizations upgrade rollout policy to manage automatic minor version upgrades across
multiple database resources and AWS accounts. This policy helps you implement a controlled upgrade strategy for your instances by:

**How upgrade rollout policy works**

When a new minor engine version becomes eligible for automatic upgrade,
the policy controls the upgrade sequence based on defined orders:

- Resources marked as [first] (typically development environments) become eligible for upgrades during their maintenance windows.
- After a designated bake time, resources marked as [second] become eligible.
- After another designated bake time, resources marked as [last] (typically production environments) become eligible.
- Monitoring upgrade progress through AWS Health notifications.
  You can define your upgrade orders by:

- Account-level policies – Apply to all eligible resources in specified accounts.
- Resource tags – Apply to specific resources based on tags.

###### Note

Resources not configured with an upgrade policy or excluded from the policy automatically receive an upgrade order of [second].

**Prerequisites**

- Your AWS account must be part of an organization in Organizations with upgrade rollout policy enabled
- Enable automatic minor version upgrades for your instances
- Tags are not strictly required for upgrade rollout policy.
  If you want to define specific upgrade orders for different environments
  (for example, development, test, QA, production), you can use tags.
  If you don't include tag settings in your policy, all resources under
  that policy follow the default upgrade order.
  **Prerequisites**

- Your AWS account must be part of an organization in Organizations with upgrade rollout policy enabled
- Enable automatic minor version upgrades for your instances
- Tag your resources to identify their environment (for example, development, test, production)

###### To tag your resources

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the instance you want to tag.
4. Choose **Actions**, then choose **Manage tags**.
5. Choose **Add tag**.
6. Enter your tag key (for example, 'Environment') and value (for example, 'Development')
7. Choose **Add tag**, then **Save**.
   You can also add tags using the AWS CLI:

```
aws rds add-tags-to-resource \
    --resource-name arn:aws:rds:region:account-number:db:instance-name \
    --tags Key=Environment,Value=Development
```

## Upgrade order and phases

The upgrade rollout policy supports three upgrade orders:

- [first] - Typically used for development or testing environments
- [second] - Typically used for QA environments. Default order for resources not specifically configured
- [last] - Usually reserved for production environments

When a new minor engine version becomes eligible for automatic upgrade:

- Resources with upgrade order [first] become eligible for upgrades during their configured maintenance windows.
- After a designated bake time, resources with upgrade order [second] become eligible for upgrades during their maintenance windows.
- After another designated bake time, resources with upgrade order [last] become eligible for upgrades during their maintenance windows.
- The automatic minor version upgrade campaign closes after all eligible resources with upgrade orders
  [first], [second], and [last] have been upgraded, or when the campaign reaches its scheduled end date, whichever comes first.

###### Note

All automatic minor version upgrades are performed during each instance's configured maintenance window to minimize potential impact to your applications.

## Observability

### AWS Health and monitoring

You receive AWS health notifications:

- Before the start of an automatic minor version upgrade campaign
- Between each phase transition to help track and monitor upgrade progress
- Progress updates showing the number of resources upgraded across your fleet in the AWS Health console

Amazon RDS event notifications:

- Notifications for resources enabled for automatic minor version upgrades, including:
  - When your resource becomes eligible for upgrade based on its upgrade order ([first], [second], or [last])
  - Scheduled upgrade timeline during the maintenance window
  - Individual database upgrade start and completion status

- Subscribe to these events through Amazon EventBridge0 for automated monitoring

### Considerations

Some considerations to keep in mind:

- The policy applies to all future automatic minor version upgrade campaigns, including policy changes made during active campaigns.
- If you join an ongoing upgrade campaign, your resources follow the current running upgrade order and do not wait for a configured policy.
- Resources not configured with an upgrade policy automatically receive an upgrade order of [second].
- The policy provides validation periods between upgrade phases before proceeding to the next phase.
- Changes to either the policy or resource tags require time to propagate before the new upgrade order is applied.
- The policy applies only to Amazon RDS resources with automatic minor version upgrades enabled.
- If you detect an issue within an environment, you can turn off automatic minor version upgrades
  for subsequent environments or use the validation period to resolve issues before upgrades proceed to the
  next upgrade order.

###### Note

This feature supports automatic minor version upgrades for Oracle Database engine versions released after January 2026.

For more information about tagging RDS resources, see [Tagging Amazon RDS resources](USER_Tagging.md "USER_Tagging.md").
For detailed instructions on setting up and using upgrade rollout policy,
see [Getting started with AWS Organizations](../../../organizations/latest/userguide/orgs_getting-started.md "../../../organizations/latest/userguide/orgs_getting-started.md") in the _AWS Organizations User Guide_.
