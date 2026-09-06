

# Enabling a control in a specific standard
<a name="controls-configure"></a>

When you enable a standard in AWS Security Hub CSPM, all of the controls that apply to it are automatically enabled in that standard (the exception to this is service-managed standards). You can then disable and re-enable specific controls in the standard. However, we recommend aligning the enablement status of a control across all of your enabled standards. For instructions on enabling a control across all standards, see [Enabling a control across standards](enable-controls-overview.md).

The details page for a standard contains the list of applicable controls for the standard, and information about which controls are currently enabled in and disabled in that standard.

On the standards details page, you can also enable controls in specific standards. You must enable controls in specific standards separately in each AWS account and AWS Region. When you enable a control in specific standards, it only impacts the current account and Region.

To enable a control in a standard, you must first enable at least one standard to which the control applies. For instructions on enabling a standard, see [Enabling a security standard](enable-standards.md). When you enable a control in one or more standards, Security Hub CSPM starts to generate findings for that control. Security Hub CSPM includes the [control status](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-overall-status.html#controls-overall-status-values) in the calculation of the overall security score and standard security scores. Even if you enable a control in multiple standards, you'll receive a single finding per security check across standards if you turn on consolidated control findings. For more information, see [Consolidated control findings](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#consolidated-control-findings).

To enable a control in a standard, the control must be available in your current Region. For more information, see [Availability of controls by Region](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-regions.html#securityhub-regions-control-support).

Follow these steps to enable a Security Hub CSPM control in a *specific* standard. In lieu of the following steps, you can also use the [`UpdateStandardsControl`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html) API action to enable controls in a specific standard. For instructions on enabling a control in *all* standards, see [Cross-standard enablement in single account and Region](enable-controls-overview.md#enable-controls-all-standards).

------
#### [ Security Hub CSPM console ]

**To enable a control in a specific standard**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. Choose **Security standards** from the navigation pane.

1. Choose **View results** for the relevant standard.

1. Select a control.

1. Choose **Enable Control** (this option doesn't appear for a control that's already enabled). Confirm by choosing **Enable**.

------
#### [ Security Hub CSPM API ]

**To enable a control in a specific standard**

1. Run `[`ListSecurityControlDefinitions`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListSecurityControlDefinitions.html)`, and provide a standard ARN to get a list of available controls for a specific standard. To obtain a standard ARN, run [`DescribeStandards`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html). This API returns standard-agnostic security control IDs, not standard-specific control IDs.

   **Example request:**

   ```
   {
       "StandardsArn": "arn:aws:securityhub:::{{standards/aws-foundational-security-best-practices/v/1.0.0}}"
   }
   ```

1. Run `[`ListStandardsControlAssociations`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListStandardsControlAssociations.html)`, and provide a specific control ID to return the current enablement status of a control in each standard.

   **Example request:**

   ```
   {
       "SecurityControlId": "{{IAM.1}}"
   }
   ```

1. Run `[`BatchUpdateStandardsControlAssociations`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html)`. Provide the ARN of the standard that you want to enable the control in.

1. Set the `AssociationStatus` parameter equal to `ENABLED`.

   **Example request:**

   ```
   {
       "StandardsControlAssociationUpdates": [{"SecurityControlId": "{{IAM.1}}", "StandardsArn": "arn:aws:securityhub:::{{ruleset/cis-aws-foundations-benchmark/v/1.2.0}}", "AssociationStatus": "ENABLED"}]
   }
   ```

------
#### [ AWS CLI ]

**To enable a control in a specific standard**

1. Run the `[`list-security-control-definitions`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-security-control-definitions.html)` command, and provide a standard ARN to get a list of available controls for a specific standard. To obtain a standard ARN, run `describe-standards`. This command returns standard-agnostic security control IDs, not standard-specific control IDs.

   ```
   aws securityhub --region {{us-east-1}} list-security-control-definitions --standards-arn "arn:aws:securityhub:{{us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0}}"
   ```

1. Run the `[`list-standards-control-associations`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-standards-control-associations.html)` command, and provide a specific control ID to return the current enablement status of a control in each standard.

   ```
   aws securityhub  --region {{us-east-1}} list-standards-control-associations --security-control-id {{CloudTrail.1}}
   ```

1. Run the `[`batch-update-standards-control-associations`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/batch-update-standards-control-associations.html)` command. Provide the ARN of the standard that you want to enable the control in.

1. Set the `AssociationStatus` parameter equal to `ENABLED`.

   ```
   aws securityhub  --region {{us-east-1}} batch-update-standards-control-associations --standards-control-association-updates '[{"SecurityControlId": "{{CloudTrail.1}}", "StandardsArn": "arn:aws:securityhub:{{us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0}}", "AssociationStatus": "ENABLED"}]'
   ```

------