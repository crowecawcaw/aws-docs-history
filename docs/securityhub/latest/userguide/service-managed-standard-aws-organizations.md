

# Service-Managed Standard: AWS Organizations

Service-Managed Standard: AWS Organizations holds controls that your AWS Security Hub CSPM declarative policies enable when no enabled standard contains them. This section explains how Security Hub CSPM creates and manages the standard, and how to view its controls and findings.

## What is Service-Managed Standard: AWS Organizations?
<a name="aws-organizations-standard-summary"></a>

Service-Managed Standard: AWS Organizations is a service-managed standard that Security Hub CSPM creates and manages for accounts that a Security Hub CSPM policy governs. The standard includes all Security Hub CSPM controls for AWS. Security Hub CSPM uses this standard to enable a control when the account's effective policy enables the control but doesn't enable any standard that contains it.

This situation can occur only in an effective policy. When you create or update a Security Hub CSPM policy, Organizations rejects the policy if a control in `enabled_controls` doesn't belong to a standard that the same policy enables. When Organizations merges several policies that are each valid on their own, the resulting effective policy can still enable a control without enabling a standard that contains it. For example:
+ A policy attached to the organization root enables standard A and lists control X in `enabled_controls`.
+ A policy attached to an organizational unit (OU) uses `@@assign` to replace the list of enabled standards with standard B, which doesn't include control X.

The effective policy for accounts in that OU enables control X, but no enabled standard contains it. Instead of failing the policy, Security Hub CSPM enables control X through Service-Managed Standard: AWS Organizations.

**Tip**  
Service-managed standards differ from other standards in AWS Security Hub CSPM. For example, you can't create, delete, or configure this standard directly in Security Hub CSPM. For more information, see [Service-managed standards in Security Hub CSPM](service-managed-standards.md).

For more information about Security Hub CSPM policies and effective policies, see [Managing accounts with declarative policies in Security Hub CSPM](accounts-orgs-policies.md) in this guide and [Security Hub CSPM policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_securityhub-cspm.html) in the *AWS Organizations User Guide*.

## Creating the standard
<a name="aws-organizations-standard-creation"></a>

You don't create this standard yourself. Security Hub CSPM creates the standard in an account and AWS Region the first time that the account's effective policy enables a control that isn't in any enabled standard. Security Hub CSPM creates the standard only in Regions where the effective policy enables Security Hub CSPM.

Until Security Hub CSPM creates the standard in an account and Region, you can't see the standard in the Security Hub CSPM console. You also can't access it through the Security Hub CSPM API or AWS CLI in that account and Region.

You can't specify this standard in the `enabled_standards` list of a Security Hub CSPM policy. Security Hub CSPM policies don't configure service-managed standards. For more information, see [Security Hub CSPM policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_securityhub-cspm_syntax.html) in the *AWS Organizations User Guide*.

This standard is available only in the Regions where Security Hub CSPM policies are available.

## Enabling and disabling controls in the standard
<a name="aws-organizations-standard-managing-controls"></a>

Security Hub CSPM enables a control in this standard only when the account's effective policy enables that control and no other enabled standard contains it. When Security Hub CSPM adds new controls to the standard, it doesn't automatically enable them.

While a Security Hub CSPM policy governs an account in a Region, the account can't directly disable this standard or change the enablement status of its controls through the Security Hub CSPM console, Security Hub CSPM API, or AWS CLI. For example, Security Hub CSPM denies [BatchDisableStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchDisableStandards.html), [UpdateStandardsControl](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html), and [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html) requests from governed accounts and Regions.

If a policy no longer governs an account in a Region, you can disable the standard or its controls in that Region. You can't enable the standard or its controls yourself.

**Note**  
You can't use [central configuration](central-configuration-intro.md) to manage Service-Managed Standard: AWS Organizations. You can manage this standard only through Security Hub CSPM policies in AWS Organizations.

## Viewing enablement status and control status
<a name="aws-organizations-standard-control-status"></a>

You can view the enablement status of this standard and its controls by using one of the following methods:
+ Security Hub CSPM console
+ Security Hub CSPM API (call the [GetEnabledStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetEnabledStandards.html) and [ListStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListStandardsControlAssociations.html) operations)
+ AWS CLI (run the [get-enabled-standards](https://docs.aws.amazon.com/cli/latest/reference/securityhub/get-enabled-standards.html) and [list-standards-control-associations](https://docs.aws.amazon.com/cli/latest/reference/securityhub/list-standards-control-associations.html) commands)

To see the configuration that Security Hub CSPM applies, view the account's effective policy in Organizations. For example, call the [DescribeEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html) API with the `SECURITYHUB_CSPM_POLICY` policy type.

Security Hub CSPM calculates control status based on the workflow status and compliance status of the control findings. For more information about enablement status and control status, see [Reviewing the details of controls in Security Hub CSPM](securityhub-standards-control-details.md).

**Note**  
When Security Hub CSPM enables controls for this standard, it can take up to 18 hours to generate findings for controls that use an existing AWS Config service-linked rule. For more information, see [Schedule for running security checks](securityhub-standards-schedule.md).

## Deleting the standard
<a name="aws-organizations-standard-deletion"></a>

While a policy governs an account in a Region, you can't delete or disable this standard in that account and Region. If an account's effective Security Hub CSPM policy no longer enables any control that's missing from the enabled standards, Security Hub CSPM automatically disables this standard.

Disabling Security Hub CSPM removes Service-Managed Standard: AWS Organizations and any other standards that you've enabled. This also applies when a Security Hub CSPM policy disables Security Hub CSPM in a Region.

## Finding field format for Service-Managed Standard: AWS Organizations
<a name="aws-organizations-standard-finding-fields"></a>

When Security Hub CSPM enables controls for this standard, you start to receive control findings in Security Hub CSPM. Security Hub CSPM reports control findings in the [AWS Security Finding Format (ASFF)](securityhub-findings-format.md). These are the ASFF values for this standard's Amazon Resource Name (ARN) and `GeneratorId`:
+ **Standard ARN** – `arn:aws:securityhub:{{us-east-1}}::standards/service-managed-aws-organizations-cspm/v/1.0.0`
+ **GeneratorId** – `service-managed-aws-organizations-cspm/v/1.0.0/{{ACM.1}}`

For a sample control finding, see [Samples of control findings](sample-control-findings.md).

## Controls that apply to Service-Managed Standard: AWS Organizations
<a name="aws-organizations-standard-controls"></a>

Service-Managed Standard: AWS Organizations supports all Security Hub CSPM controls. For information about each control, including remediation steps for failed findings, see [Control reference for Security Hub CSPM](securityhub-controls-reference.md).

Regional limits on controls apply to this standard. If a control isn't available in a Region, Security Hub CSPM doesn't enable it in that Region. For more information, see [Regional limits on Security Hub CSPM controls](regions-controls.md).