

# Disabling a control in a specific standard
<a name="disable-controls-standard"></a>

You can disable a control in only specific security standards, instead of across all standards. If the control applies to other enabled standards, AWS Security Hub CSPM continues to run security checks for the control and you continue to receive findings for the control.

We recommend aligning the enablement status of a control across all of the enabled standards that the control applies to. For information about disabling a control across all of the standards that it applies to, see [Disabling a control across standards](disable-controls-across-standards.md).

On the standards details page, you can also disable controls in specific standards. You must disable controls in specific standards separately in each AWS account and AWS Region. When you disable a control in specific standards, it affects only the current account and Region.

Choose your preferred method, and follow these steps to disable a control in one or more specific standards.

------
#### [ Security Hub CSPM console ]

**To disable a control in a specific standard**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. Choose **Security standards** from the navigation pane. Choose **View results** for the relevant standard.

1. Select a control.

1. Choose **Disable Control**. This option doesn't appear for a control that's already disabled.

1. Provide a reason for disabling the control, and confirm by choosing **Disable**.

------
#### [ Security Hub CSPM API ]

**To disable a control in a specific standard**

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

1. Run `[`BatchUpdateStandardsControlAssociations`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html)`. Provide the ARN of the standard in which you want to disable the control.

1. Set the `AssociationStatus` parameter equal to `DISABLED`. If you follow these steps for a control that's already disabled, the API returns an HTTP status code 200 response.

   **Example request:**

   ```
   {
       "StandardsControlAssociationUpdates": [{"SecurityControlId": "{{IAM.1}}", "StandardsArn": "arn:aws:securityhub:::{{ruleset/cis-aws-foundations-benchmark/v/1.2.0}}", "AssociationStatus": "DISABLED",  "UpdatedReason": "{{Not applicable to environment}}"}]
   }
   ```

------
#### [ AWS CLI ]

**To disable a control in a specific standard**

1. Run the `[`list-security-control-definitions`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-security-control-definitions.html)` command, and provide a standard ARN to get a list of available controls for a specific standard. To obtain a standard ARN, run `describe-standards`. This command returns standard-agnostic security control IDs, not standard-specific control IDs.

   ```
   aws securityhub --region {{us-east-1}} list-security-control-definitions --standards-arn "arn:aws:securityhub:{{us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0}}"
   ```

1. Run the `[`list-standards-control-associations`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-standards-control-associations.html)` command, and provide a specific control ID to return the current enablement status of a control in each standard.

   ```
   aws securityhub  --region {{us-east-1}} list-standards-control-associations --security-control-id {{CloudTrail.1}}
   ```

1. Run the `[`batch-update-standards-control-associations`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/batch-update-standards-control-associations.html)` command. Provide the ARN of the standard in which you want to disable the control.

1. Set the `AssociationStatus` parameter equal to `DISABLED`. If you follow these steps for a control that's already enabled, the command returns an HTTP status code 200 response.

   ```
   aws securityhub  --region {{us-east-1}} batch-update-standards-control-associations --standards-control-association-updates '[{"SecurityControlId": "{{CloudTrail.1}}", "StandardsArn": "arn:aws:securityhub:{{us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0}}", "AssociationStatus": "DISABLED", "UpdatedReason": "{{Not applicable to environment}}"}]'
   ```

------