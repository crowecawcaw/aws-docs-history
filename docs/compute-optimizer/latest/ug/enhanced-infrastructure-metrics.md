# Enhanced infrastructure metrics

Enhanced infrastructure metrics is a paid feature of Compute Optimizer that applies to
Amazon EC2 instances, instances that are part of EC2 Auto Scaling groups, and Amazon RDS DB instances. This
recommendation preference extends the utilization metrics analysis lookback period to up to 93
days, compared to the default 14-day period. This gives Compute Optimizer a longer history of utilization
metrics data to analyze. You need to activate the enhanced infrastructure metrics preference.
For more information, see [Organization, account, and resource level](#activating-enhanced-infrastructure-metrics "#activating-enhanced-infrastructure-metrics").

## Required

permissions

You must have the appropriate permissions to activate and deactivate enhanced
infrastructure metrics. For more information, see [Policies to grant access
to manage Compute Optimizer recommendation preferences](security-iam.md#enhanced-infrastructure-metrics-permissions "security-iam.md#enhanced-infrastructure-metrics-permissions").

## Organization, account, and resource level

You can activate enhanced infrastructure metrics using the Compute Optimizer console, AWS Command Line Interface
(AWS CLI), and AWS SDKs. In the console, you can activate the feature in the following three
areas, with each providing a different level of activation.

- At the resource level, you can activate enhanced infrastructure
  metrics for the individual resource that you're viewing. For example, the
  **Instance details** page for an individual EC2 instance provides the
  option to activate the enhanced infrastructure metrics feature only for that EC2
  instance. For more information, see [Activating enhanced infrastructure metrics
  at the resource level](activating-eim-resource-level.md "activating-eim-resource-level.md") later in this guide.

###### Note

Resource-level preferences override account-level preferences, and account-level
preferences override organization-level preferences. For an EC2 instance that is part
of an EC2 Auto Scaling group, the EC2 Auto Scaling group recommendation preference overrides that of the
individual instance.

- For an individual AWS account holder, you can activate
  the enhanced infrastructure metrics feature for all EC2 instances in the account that
  meet your resource type and AWS Region criteria. EC2 instance preferences at the
  account level apply to standalone instances and instances that are part of EC2 Auto Scaling groups.
  For more information, see [Activating enhanced infrastructure metrics
  at the organization or account level](activating-eim-level.md "activating-eim-level.md") later in this guide.
- The account manager or the delegated administrator of an AWS Organization
  can activate the enhanced infrastructure metrics feature for all resources in all member
  accounts of the organization that meet your resource type and AWS Region criteria. EC2
  instance preferences at the organization level apply to standalone instances and
  instances that are part of EC2 Auto Scaling groups in all member accounts. For more information, see
  [Activating enhanced infrastructure metrics
  at the organization or account level](activating-eim-level.md "activating-eim-level.md") later in this guide.

After you activate the enhanced infrastructure metrics feature, Compute Optimizer applies the
preference the next time recommendations are refreshed. This can take up to 24 hours. To
confirm that your resource recommendations have enhanced infrastructure metrics enabled, see
[Confirming the status of enhanced infrastructure
metrics](#confirm-eim-status "#confirm-eim-status").

Compute Optimizer considers updated preferences the next time that it generates recommendations.
Until then, a **pending** status is affixed to your update preference (for
example, **Active-pending** or **Inactive-pending**). To
confirm if your resource recommendations are taking enhanced infrastructure metrics into
consideration, see [Confirming the status of enhanced infrastructure
metrics](#confirm-eim-status "#confirm-eim-status").

### Confirming the status of enhanced infrastructure

metrics

After you activate the enhanced infrastructure metrics recommendation preference, Compute Optimizer
applies the preference the next time that recommendations are refreshed. This can take up to
24 hours. The **Effective enhanced infrastructure metrics** column in the
Resource Recommendations page confirms that the recommendations listed are taking the
three-month look-back period into consideration. An **Active** status
confirms the recommendation listed is considering the longer look-back period. An
**Inactive** status confirms that the recommendation isn't yet
considering the longer look-back period.

## Next steps

For instructions on how activate or deactivate enhanced infrastructure metrics at the resource level, see [Activating enhanced infrastructure metrics
at the resource level](activating-eim-resource-level.md "activating-eim-resource-level.md").

For instructions on how activate or deactivate enhanced infrastructure metrics at the organization or account level, see [Activating enhanced infrastructure metrics
at the organization or account level](activating-eim-level.md "activating-eim-level.md").
