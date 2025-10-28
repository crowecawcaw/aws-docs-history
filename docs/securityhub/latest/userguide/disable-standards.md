# Disabling a security standard

When you disable a security standard in AWS Security Hub CSPM, the following occurs:

- All the controls that apply to the standard are disabled, unless they're
  associated with another standard that's currently enabled.
- Security checks for the disabled controls are no longer performed, and no additional findings are generated for the disabled controls.
- Existing findings for the disabled controls are archived automatically after approximately 3‐5 days.
- AWS Config rules that Security Hub CSPM created for the disabled controls are deleted.
  Deletion of the appropriate AWS Config rules typically occurs within a few minutes of disabling
  a standard. However, it might take longer. If the first request fails to delete the rules,
  Security Hub CSPM tries again every 12 hours. However, if you disabled Security Hub CSPM or don't have any other
  standards enabled, Security Hub CSPM can't try again, which means that it can't delete the rules. If
  this occurs and you need to delete the rules, contact AWS Support.

###### Topics

- [Disabling a standard in multiple accounts and AWS Regions](#disable-standards-central-configuration "#disable-standards-central-configuration")
- [Disabling a standard in a single account and AWS Region](#securityhub-standard-disable-console "#securityhub-standard-disable-console")

## Disabling a standard in multiple accounts and AWS Regions

To disable a security standard across multiple accounts and AWS Regions, use [central configuration](central-configuration-intro.md "central-configuration-intro.md"). With central configuration, the delegated Security Hub CSPM administrator can create Security Hub CSPM configuration policies that disable one or more standards. The administrator can then associate a configuration policy with individual accounts, organizational units (OUs), or the root. A configuration policy affects the home Region, also referred to as an _aggregation Region_, and all linked Regions.

Configuration policies offer customization options. For example, you might choose to
disable the Payment Card Industry Data Security Standard (PCI DSS) in one OU. For
another OU, you might choose to disable both the PCI DSS and the National Institute of
Standards and Technology (NIST) SP 800-53 Rev. 5 standard. For information about
creating a configuration policy that enables or disables individual standards that you
specify, see [Creating and associating configuration policies](create-associate-policy.md "create-associate-policy.md").

###### Note

The Security Hub CSPM administrator can use configuration policies to disable any standard
except the [AWS Control Tower
service-managed standard](service-managed-standard-aws-control-tower.md "service-managed-standard-aws-control-tower.md"). To disable this standard, the administrator
must use AWS Control Tower directly. They must also use AWS Control Tower to disable or enable
individual controls in this standard for a centrally managed account.

If you want some accounts to configure or disable standards for their own accounts, the Security Hub CSPM administrator can designate those accounts as _self-managed accounts_. Self-managed accounts must disable standards separately in each Region.

## Disabling a standard in a single account and AWS Region

If you don't use central configuration or you have a self-managed account, you can't
use configuration policies to centrally disable security standards in multiple accounts
or AWS Regions. However, you can disable a standard in a single account and Region.
You can do this by using the Security Hub CSPM console or the Security Hub CSPM API.

Security Hub CSPM console
Follow these steps to disable a standard in one account and Region by using the Security Hub CSPM console.

###### To disable a standard in one account and Region

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to disable the standard.
3. In the navigation pane, choose **Security standards**.
4. In the section for the standard that you want to disable, choose **Disable standard**.

To disable the standard in additional Regions, repeat the preceding steps in each additional Region.

Security Hub CSPM API
To disable a standard programmatically in a single account and Region, use the [BatchDisableStandards](../../1.0/APIReference/API_BatchDisableStandards.md "../../1.0/APIReference/API_BatchDisableStandards.md") operation. Or, if you're using the AWS Command Line Interface (AWS CLI), run the [batch-disable-standards](../../../cli/latest/reference/securityhub/batch-disable-standards.md "../../../cli/latest/reference/securityhub/batch-disable-standards.md") command.

In your request, use the `StandardsSubscriptionArns` parameter
to specify the Amazon Resource Name (ARN) of the standard that you want to
disable. If you're using the AWS CLI, use the
`standards-subscription-arns` parameter to specify the ARN.
Also specify the Region that your request applies to. For example, the
following command disables the AWS Foundational Security Best Practices (FSBP) standard for an account
(`123456789012`):

```
`$` `aws securityhub batch-disable-standards \
--standards-subscription-arns "`arn:aws:securityhub:us-east-1:123456789012:subscription/aws-foundational-security-best-practices/v/1.0.0`" \
--region `us-east-1``
```

Where
`arn:aws:securityhub:us-east-1:123456789012:subscription/aws-foundational-security-best-practices/v/1.0.0`
is the ARN of the FSBP standard for the account in the US East (N. Virginia)
Region, and `us-east-1` is the Region in which to
disable it.

To obtain the ARN for a standard, you can use the [GetEnabledStandards](../../1.0/APIReference/API_GetEnabledStandards.md "../../1.0/APIReference/API_GetEnabledStandards.md") operation. This
operation retrieves information about the standards that are currently
enabled in your account. If you're using the AWS CLI, you can run the [get-enabled-standards](../../../cli/latest/reference/securityhub/get-enabled-standards.md "../../../cli/latest/reference/securityhub/get-enabled-standards.md") command to retrieve this
information.

After you disable a standard, Security Hub CSPM begins performing tasks to disable the standard in
the account and the specified Region. This includes disabling all the controls that
apply to the standard. To monitor the status of these tasks, you can [check the status of the standard](enable-standards.md#standard-subscription-status "enable-standards.md#standard-subscription-status") for
the account and Region.
