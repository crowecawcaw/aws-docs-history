# Enabling a security standard

When you enable a security standard in AWS Security Hub CSPM, Security Hub CSPM automatically creates and enables all the controls that apply to the standard. Security Hub CSPM also starts running security checks and generating findings for the controls.

To optimize coverage and the accuracy of findings, enable and configure resource recording
in AWS Config before you enable a standard. When you configure resource recording, also be sure to
enable it for all the types of resources that are checked by controls that apply to the
standard. Otherwise, Security Hub CSPM might not be able to evaluate the appropriate resources, and
generate accurate findings for controls that apply to the standard. For more information,
see [Enabling and configuring AWS Config for Security Hub CSPM](securityhub-setup-prereqs.md "securityhub-setup-prereqs.md").

After you enable a standard, you can disable or later re-enable individual controls that
apply to the standard. If you disable a control for a standard, Security Hub CSPM stops generating
findings for the control. In addition, Security Hub CSPM ignores the control when it calculates the
security score for the standard. The security score is the percentage of controls that
passed evaluation, relative to the total number of controls that apply to the standard, are
enabled, and have evaluation data.

When you enable a standard, Security Hub CSPM generates a preliminary security score for the standard,
typically within 30 minutes of your first visit to the **Summary** or
**Security standards** page on the Security Hub CSPM console. Security scores are
generated only for standards that are enabled when you visit those pages on the console. In
addition, resource recording must be configured in AWS Config for the scores to appear. In the
China Regions and AWS GovCloud (US) Regions, it can take up to 24 hours for Security Hub CSPM to generate a
preliminary security score for a standard. After Security Hub CSPM generates a preliminary score, it
updates the score every 24 hours. To determine when a security score was last updated, you
can refer to a timestamp that Security Hub CSPM provides for the score. For more information, see [Calculating security scores](standards-security-score.md "standards-security-score.md").

How you enable a standard depends on whether you use [central configuration](central-configuration-intro.md "central-configuration-intro.md") to manage Security Hub CSPM for
multiple accounts and AWS Regions. We recommend using central configuration if you want to
enable standards in multi-account, multi-Region environments. You can use central
configuration if you integrate Security Hub CSPM with AWS Organizations. If you don't use central configuration,
you must enable each standard separately in each account and each Region.

###### Topics

- [Enabling a standard in multiple accounts and AWS Regions](#enable-standards-central-configuration "#enable-standards-central-configuration")
- [Enabling a standard in a single account and AWS Region](#securityhub-standard-enable-console "#securityhub-standard-enable-console")
- [Checking the status of a standard](#standard-subscription-status "#standard-subscription-status")

## Enabling a standard in multiple accounts and AWS Regions

To enable and configure a security standard across multiple accounts and AWS Regions, use [central configuration](central-configuration-intro.md "central-configuration-intro.md"). With central configuration, the delegated Security Hub CSPM administrator can create Security Hub CSPM configuration policies that enable one or more standards. The administrator can then associate a configuration policy with individual accounts, organizational units (OUs), or the root. A configuration policy affects the home Region, also referred to as an _aggregation Region_, and all linked Regions.

Configuration policies offer customization options. For example, you might choose to enable only the AWS Foundational Security Best Practices (FSBP) standard for one OU. For another OU, you might choose to enable both the FSBP standard and the Center for Internet Security (CIS) AWS Foundations Benchmark v1.4.0 standard. For information about creating a configuration policy that enables particular standards that you specify, see [Creating and associating configuration policies](create-associate-policy.md "create-associate-policy.md").

If you use central configuration, Security Hub CSPM doesn't automatically enable any standards in new or existing accounts. Instead, the Security Hub CSPM administrator specifies which standards to enable in different accounts when they create Security Hub CSPM configuration policies for their organization. Security Hub CSPM offers a recommended configuration policy in which only the FSBP standard is enabled. For more information, see [Types of configuration policies](configuration-policies-overview.md#policy-types "configuration-policies-overview.md#policy-types").

###### Note

The Security Hub CSPM administrator can use configuration policies to enable any standard
except the [AWS Control Tower
service-managed standard](service-managed-standard-aws-control-tower.md "service-managed-standard-aws-control-tower.md"). To enable this standard, the administrator must
use AWS Control Tower directly. They must also use AWS Control Tower to enable or disable individual
controls in this standard for a centrally managed account.

If you want some accounts to enable and configure standards for their own accounts, the Security Hub CSPM administrator can designate those accounts as _self-managed accounts_. Self-managed accounts must enable and configure standards separately in each Region.

## Enabling a standard in a single account and AWS Region

If you don't use central configuration or you have a self-managed account, you can't
use configuration policies to centrally enable security standards in multiple accounts
or AWS Regions. However, you can enable a standard in a single account and Region. You
can do this by using the Security Hub CSPM console or the Security Hub CSPM API.

Security Hub CSPM console
Follow these steps to enable a standard in one account and Region by using the Security Hub CSPM console.

###### To enable a standard in one account and Region

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to enable the standard.
3. In the navigation pane, choose **Security standards**. The **Security standards** page lists all the standards that Security Hub CSPM currently supports. If you already enabled a standard, the section for the standard includes the current security score and additional details for the standard.
4. In the section for the standard that you want to enable, choose **Enable standard**.

To enable the standard in additional Regions, repeat the preceding steps in each additional Region.

Security Hub CSPM API
To enable a standard programmatically in a single account and Region, use the [BatchEnableStandards](../../1.0/APIReference/API_BatchEnableStandards.md "../../1.0/APIReference/API_BatchEnableStandards.md") operation. Or, if you're using the AWS Command Line Interface (AWS CLI), run the [batch-enable-standards](../../../cli/latest/reference/securityhub/batch-enable-standards.md "../../../cli/latest/reference/securityhub/batch-enable-standards.md") command.

In your request, use the `StandardsArn` parameter to specify the Amazon Resource Name (ARN) of the standard that you want to enable. Also specify the Region that your request applies to. For example, the following command enables the AWS Foundational Security Best Practices (FSBP) standard:

```
`$` `aws securityhub batch-enable-standards \
--standards-subscription-requests '{"StandardsArn":"`arn:aws:securityhub:`us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0``"}' \
--region `us-east-1``
```

Where `arn:aws:securityhub:`us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0``is the ARN of the FSBP standard in the US East (N. Virginia) Region, and`us-east-1` is the Region in which to enable it.

To obtain the ARN for a standard, use the [DescribeStandards](../../1.0/APIReference/API_DescribeStandards.md "../../1.0/APIReference/API_DescribeStandards.md") operation or, if you're using the AWS CLI, run the [describe-standards](../../../cli/latest/reference/securityhub/describe-standards.md "../../../cli/latest/reference/securityhub/describe-standards.md") command.

To first review a list of standards that are currently enabled in your account, you can use the [GetEnabledStandards](../../1.0/APIReference/API_GetEnabledStandards.md "../../1.0/APIReference/API_GetEnabledStandards.md") operation. If you're using the AWS CLI, you can run the [get-enabled-standards](../../../cli/latest/reference/securityhub/get-enabled-standards.md "../../../cli/latest/reference/securityhub/get-enabled-standards.md") command to retrieve this list.

After you enable a standard, Security Hub CSPM begins performing tasks to enable the standard in
the account and the specified Region. This includes creating all the controls that apply
to the standard. To monitor the status of these tasks, you can check the status of the
standard for the account and Region.

## Checking the status of a standard

When you enable a security standard for an account, Security Hub CSPM begins creating all the controls that apply to the standard in the account. Security Hub CSPM also performs additional tasks to enable the standard for the account, such as generating a preliminary security score for the standard. While Security Hub CSPM performs these tasks, the status of the standard is _Pending_ for the account. The status of the standard then passes through additional states, which you can monitor and check.

###### Note

Changes to individual controls for a standard don't affect the overall status of
the standard. For example, if you enable a control that you previously disabled,
your change doesn't affect the status of the standard. Similarly, if you change a
parameter value for an enabled control, your change doesn't affect the status of the
standard.

To check the status of a standard by using the Security Hub CSPM console, choose **Security standards** in the navigation pane. The **Security standards** page lists all the standards that Security Hub CSPM currently supports. If Security Hub CSPM is currently performing tasks to enable the standard, the section for the standard indicates that Security Hub CSPM is still generating a security score for the standard. If a standard is enabled, the section for the standard includes the current score. Choose **View results** to review additional details, including the status of individual controls that apply to the standard. For more information, see [Schedule for running security checks](securityhub-standards-schedule.md "securityhub-standards-schedule.md").

To check the status of a standard programmatically with the Security Hub CSPM API, use the [GetEnabledStandards](../../1.0/APIReference/API_GetEnabledStandards.md "../../1.0/APIReference/API_GetEnabledStandards.md") operation. In your request, optionally use the `StandardsSubscriptionArns` parameter to specify the Amazon Resource Name (ARN) of the standard whose status you want to check. If you're using the AWS Command Line Interface (AWS CLI), you can run the [get-enabled-standards](../../../cli/latest/reference/securityhub/get-enabled-standards.md "../../../cli/latest/reference/securityhub/get-enabled-standards.md") command to check the status of a standard. To specify the ARN of the standard to check, use the `standards-subscription-arns` parameter. To determine which ARN to specify, you can use the [DescribeStandards](../../1.0/APIReference/API_DescribeStandards.md "../../1.0/APIReference/API_DescribeStandards.md") operation or, for the AWS CLI, run the [describe-standards](../../../cli/latest/reference/securityhub/describe-standards.md "../../../cli/latest/reference/securityhub/describe-standards.md") command.

If your request succeeds, Security Hub CSPM responds with an array of
`StandardsSubscription` objects. A _standard
subscription_ is an AWS resource that Security Hub CSPM creates in an account when a
standard is enabled for the account. Each `StandardsSubscription` object
provides details about a standard that is currently enabled or is being enabled or
disabled for the account. Within each object, the `StandardsStatus` field
specifies the current status of the standard for the account.

The status of a standard (`StandardsStatus`) can be one of the following.

**PENDING**

Security Hub CSPM is currently performing tasks to enable the standard for the
account. This includes creating the controls that apply to the standard, and
generating a preliminary security score for the standard. It can take
several minutes for Security Hub CSPM to complete all the tasks. A standard can also
have this status if it's already enabled for the account and Security Hub CSPM is
currently adding new controls to the standard.

If a standard has this status, you might not be able to retrieve the details of individual controls that apply to the standard. In addition, you might not be able to configure or disable individual controls for the standard. For example, if you try to disable a control by using the [UpdateStandardsControl](../../1.0/APIReference/API_UpdateStandardsControl.md "../../1.0/APIReference/API_UpdateStandardsControl.md") operation, an error occurs.

To determine whether you can configure or otherwise manage individual controls for the standard, refer to the value for the `StandardsControlsUpdatable` field. If the value for this field is `READY_FOR_UPDATES`, you can start managing individual controls for the standard. Otherwise, wait until Security Hub CSPM completes additional processing tasks to enable the standard.

**READY**

The standard is currently enabled for the account. Security Hub CSPM can run security
checks and generate findings for all the controls that apply to the standard
and are currently enabled. Security Hub CSPM can also calculate a security score for the
standard.

If a standard has this status, you can retrieve the details of individual controls that apply to the standard. In addition, you can configure, disable, or re-enable the controls. You can also disable the standard.

**INCOMPLETE**

Security Hub CSPM wasn't able to enable the standard completely for the account. Security Hub CSPM can't run security checks and generate findings for all the controls that apply to the standard and are currently enabled. In addition, Security Hub CSPM can't calculate a security score for the standard.

To determine why the standard wasn't enabled completely, refer to the information in the `StandardsStatusReason` array. This array specifies issues that prevented Security Hub CSPM from enabling the standard. If an internal error occurred, try enabling the standard for the account again. For other types of issues, [check your AWS Config settings](securityhub-setup-prereqs.md "securityhub-setup-prereqs.md"). You can also [disable individual controls](disable-controls-overview.md "disable-controls-overview.md") that you don't want to check, or disable the standard completely.

**DELETING**

Security Hub CSPM is currently processing a request to disable the standard for the account. This includes disabling the controls that apply to the standard, and removing the associated security score. It can take several minutes for Security Hub CSPM to finish processing the request.

If a standard has this status, you can't re-enable the standard or try to disable it again for the account. Security Hub CSPM must finish processing the current request first. In addition, you can't retrieve the details of individual controls that apply to the standard or manage the controls.

**FAILED**

Security Hub CSPM wasn't able to disable the standard for the account. One or more errors occurred when Security Hub CSPM attempted to disable the standard. In addition, Security Hub CSPM can't calculate a security score for the standard.

To determine why the standard wasn't disabled completely, refer to the information in the `StandardsStatusReason` array. This array specifies issues that prevented Security Hub CSPM from disabling the standard.

If a standard has this status, you can't retrieve the details of individual controls that apply to the standard or manage the controls. You can, however, re-enable the standard for the account. If you address the issues that prevented Security Hub CSPM from disabling the standard, you can also try to disable the standard again.

If the status of a standard is `READY`, Security Hub CSPM runs security checks and generates findings for all the controls that apply to the standard and are currently enabled. For other statuses, Security Hub CSPM might run checks and generate findings for some, but not all, enabled controls. It can take up to 24 hours to generate or update control findings. For more information, see [Schedule for running security checks](securityhub-standards-schedule.md "securityhub-standards-schedule.md").
