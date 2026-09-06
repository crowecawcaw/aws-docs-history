

# Enabling a control across standards
<a name="enable-controls-overview"></a>

We recommend enabling a AWS Security Hub CSPM control across all of the standards that the control applies to. If you turn on consolidated control findings, you receive one finding per control check even if a control belongs to more than one standard.

## Cross-standard enablement in multi-account, multi-Region environments
<a name="enable-controls-all-standards-central-configuration"></a>

To enable a security control across multiple AWS accounts and AWS Regions, you must be signed in to the delegated Security Hub CSPM administrator account and use [central configuration](central-configuration-intro.md).

Under central configuration, the delegated administrator can create Security Hub CSPM configuration policies that enable specified controls across enabled standards. You can then associate the configuration policy with specific accounts and organizational units (OUs) or the root. A configuration policy takes effect in your home Region (also called an aggregation Region) and all linked Regions.

Configuration policies offer customization. For example, you can choose to enable all controls in one OU, and you can choose to enable only Amazon Elastic Compute Cloud (EC2) controls in another OU. The level of granularity depends on your intended goals for security coverage in your organization. For instructions on creating a configuration policy that enables specified controls across standards, see [Creating and associating configuration policies](create-associate-policy.md).

**Note**  
The delegated administrator can create configuration policies to manage controls in all standards except the [Service-Managed Standard: AWS Control Tower](https://docs.aws.amazon.com/securityhub/latest/userguide/service-managed-standard-aws-control-tower.html). Controls for this standard should be configured in the AWS Control Tower service.

If you want some accounts to configure their own controls rather than the delegated administrator, the delegated administrator can designate those accounts as self-managed. Self-managed accounts must configure controls separately in each Region.

## Cross-standard enablement in single account and Region
<a name="enable-controls-all-standards"></a>

If you don't use central configuration or are a self-managed account, you can't use configuration policies to centrally enable controls in multiple accounts and Regions. However, you can use the following steps to enable a control in a single account and Region.

------
#### [ Security Hub CSPM console ]

**To enable a control across standards in one account and Region**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. Choose **Controls** from the navigation pane.

1. Choose the **Disabled** tab.

1. Choose the option next to a control.

1. Choose **Enable Control** (this option doesn't appear for a control that's already enabled).

1. Repeat in each Region in which you want to enable the control.

------
#### [ Security Hub CSPM API ]

**To enable a control across standards in one account and Region**

1. Invoke the [ListStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListStandardsControlAssociations.html) API. Provide a security control ID.

   **Example request:**

   ```
   {
       "SecurityControlId": "{{IAM.1}}"
   }
   ```

1. Invoke the [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html) API. Provide the Amazon Resource Name (ARN) of any standards that the control isn't enabled in. To obtain standard ARNs, run [`DescribeStandards`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html).

1. Set the `AssociationStatus` parameter equal to `ENABLED`. If you follow these steps for a control that's already enabled, the API returns an HTTP status code 200 response.

   **Example request:**

   ```
   {
       "StandardsControlAssociationUpdates": [{"SecurityControlId": "{{IAM.1}}", "StandardsArn": "arn:aws:securityhub:::{{ruleset/cis-aws-foundations-benchmark/v/1.2.0}}", "AssociationStatus": "ENABLED"}, {"SecurityControlId": "{{IAM.1}}", "StandardsArn": "arn:aws:securityhub:::{{standards/aws-foundational-security-best-practices/v/1.0.0}}", "AssociationStatus": "ENABLED"}]
   }
   ```

1. Repeat in each Region in which you want to enable the control.

------
#### [ AWS CLI ]

**To enable a control across standards in one account and Region**

1. Run the [list-standards-control-associations](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-standards-control-associations.html) command. Provide a security control ID.

   ```
   aws securityhub  --region {{us-east-1}} [`list-standards-control-associations`](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-standards-control-associations.html) --security-control-id {{CloudTrail.1}}
   ```

1. Run the [batch-update-standards-control-associations](https://docs.aws.amazon.com/cli/latest/reference/securityhub/batch-update-standards-control-associations.html) command. Provide the Amazon Resource Name (ARN) of any standards that the control isn't enabled in. To obtain standard ARNs, run the `describe-standards` command.

1. Set the `AssociationStatus` parameter equal to `ENABLED`. If you follow these steps for a control that's already enabled, the command returns an HTTP status code 200 response.

   ```
   aws securityhub  --region {{us-east-1}} batch-update-standards-control-associations --standards-control-association-updates '[{"SecurityControlId": "{{CloudTrail.1}}", "StandardsArn": "{{arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0}}", "AssociationStatus": "ENABLED"}, {"SecurityControlId": "{{CloudTrail.1}}", "StandardsArn": "{{arn:aws:securityhub:::standards/cis-aws-foundations-benchmark/v/1.4.0}}", "AssociationStatus": "ENABLED"}]'
   ```

1. Repeat in each Region in which you want to enable the control.

------