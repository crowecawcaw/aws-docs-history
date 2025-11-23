# Activating enhanced infrastructure metrics

at the resource level

This section provides you with instructions on how to activate or deactivate enhanced infrastructure metrics at the
resource level. Recommendation preferences activated at the resource level apply only to
the individual resource.

## Prerequisites

Make sure that you have the appropriate permissions to activate and deactivate enhanced
infrastructure metrics. For more information, see [Policies to grant
access to manage Compute Optimizer recommendation preferences](security-iam.md#enhanced-infrastructure-metrics-permissions "security-iam.md#enhanced-infrastructure-metrics-permissions").

## Procedure

###### To activate or deactivate enhanced infrastructure metrics at the

resource level

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. In the left navigation pane under **Recommendations** and **Rightsizing**,
   choose the resource type that you want to activate or deactivate enhanced infrastructure metrics.

###### Note

For an EC2 instance that's part of an EC2 Amazon EC2 Auto Scaling group, the EC2 Amazon EC2 Auto Scaling group
recommendation preference overrides the preference of the individual
instance. 3. In the resource recommendations page, select the resource for which you
want to activate or deactivate enhanced infrastructure metrics.
Then, choose **View details**. 4. In the **Recommendation preferences** section of the **Resource
details** page, choose **Enhanced infrastructure metrics**. 5. In the prompt that appears, select the **Enhanced infrastructure
metrics - paid feature** checkbox. Then, choose **Save** to activate
enhanced infrastructure metrics for the resource. 6. (Optional) If you want to deactivate the the enhanced infrastructure metrics,
unselect the **Enhanced infrastructure metrics - paid feature** checkbox.
Then, choose **Save**.

###### Note

Saving the preference initiates metering for enhanced infrastructure metrics for
the individual resource. For more information about pricing for this feature, see
[Compute Optimizer
pricing](https://aws.amazon.com/compute-optimizer/pricing/ "https://aws.amazon.com/compute-optimizer/pricing/").

Compute Optimizer considers updated preferences the next time that it generates recommendations.
Until then, a **pending** status is affixed to your updated preference
(for example, **Active-pending** or
**Inactive-pending**). To confirm if your resource recommendations are
taking enhanced infrastructure metrics into consideration, see [Confirming the status of enhanced infrastructure
metrics](enhanced-infrastructure-metrics.md#confirm-eim-status "enhanced-infrastructure-metrics.md#confirm-eim-status").

## Additional resources

- Troubleshooting — [Failed to get or update enhanced
  infrastructure metrics recommendation preferences](troubleshooting-account-opt-in.md#accounts-eim-missing-permissions "troubleshooting-account-opt-in.md#accounts-eim-missing-permissions")
- [Activating enhanced infrastructure metrics
  at the organization or account level](activating-eim-level.md "activating-eim-level.md")
