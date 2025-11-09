# Security Hub controls for AWS Config

These Security Hub controls evaluate the AWS Config service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Config.1] AWS Config should be enabled and use the service-linked role for resource recording

**Related requirements:** CIS AWS Foundations Benchmark v5.0.0/3.3, CIS AWS Foundations Benchmark v1.2.0/2.5, CIS AWS Foundations Benchmark v1.4.0/3.5, CIS AWS Foundations Benchmark v3.0.0/3.3, NIST.800-53.r5 CM-3, NIST.800-53.r5 CM-6(1), NIST.800-53.r5 CM-8, NIST.800-53.r5 CM-8(2), PCI DSS v3.2.1/10.5.2, PCI DSS v3.2.1/11.5

**Category:** Identify > Inventory

**Severity:** Critical

**Resource type:** `AWS::::Account`

**AWS Config rule:** None (custom Security Hub rule)

**Schedule type:** Periodic

**Parameters:**

| Parameter                             | Description                                                                                                      | Type    | Allowed custom values | Security Hub default value |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------- | --------------------- | -------------------------- |
| `includeConfigServiceLinkedRoleCheck` | The control doesn’t evaluate whether AWS Config uses the service-linked role if the parameter is set to `false`. | Boolean | `true` or `false`     | `true`                     |

This control checks whether AWS Config is enabled in your account in the current AWS Region, records all
resources that correspond to controls that are enabled in the current Region, and uses the [service-linked AWS Config role](../../../config/latest/developerguide/using-service-linked-roles.md "../../../config/latest/developerguide/using-service-linked-roles.md").
The name of the service-linked role is **AWSServiceRoleForConfig**. If you don't use the service-linked role and don't set the `includeConfigServiceLinkedRoleCheck` parameter to
`false`, the control fails because other roles might not have the necessary permissions for AWS Config to
accurately record your resources.

The AWS Config service performs configuration management of supported AWS resources in your account and
delivers log files to you. The recorded information includes the configuration item (AWS resource),
relationships between configuration items, and any configuration changes within resources. Global resources are
resources that are available in any Region.

The control is evaluated as follows:

- If the current Region is set as your [aggregation Region](finding-aggregation.md "finding-aggregation.md"),
  the control produces `PASSED` findings only if AWS Identity and Access Management (IAM) global resources are recorded (if you have enabled
  controls that require them).
- If the current Region is set as a linked Region, the control doesn’t evaluate whether
  IAM global resources are recorded.
- If the current Region isn’t in your aggregator, or if cross-Region aggregation isn’t set up in your account, the
  control produces `PASSED` findings only if IAM global resources are recorded (if you have enabled
  controls that require them).

Control results aren't impacted by whether you choose daily or continuous recording of changes in resource state in AWS Config.
However, the results of this control can change when new controls are released if you have configured
automatic enablement of new controls or have a central configuration policy that
automatically enables new controls. In these cases, if you don't record all resources, you must
configure recording for resources that are associated with new controls in order to receive a `PASSED` finding.

Security Hub security checks work as intended only if you enable AWS Config in all Regions and configure resource recording for
controls that require it.

###### Note

Config.1 requires that AWS Config is enabled in all Regions in which you use Security Hub.

Since Security Hub is a Regional service, the check performed for this control evaluates only the
current Region for the account.

To allow security checks against IAM global resources in a Region, you must record IAM
global resources in that Region. Regions that don’t have IAM global resources recorded will receive a
default `PASSED` finding for controls that check IAM global resources. Since IAM global resources are
identical across AWS Regions, we recommend that you record IAM global resources in only the home Region
(if cross-Region aggregation is enabled in your account). IAM resources will be recorded only in the Region in which
global resource recording is turned on.

The IAM globally recorded resource types that AWS Config supports are IAM users, groups, roles, and
customer managed policies. You can consider disabling Security Hub controls that check these resource types in Regions where global
resource recording is turned off. For more information, see [Suggested controls to disable in Security Hub CSPM](controls-to-disable.md "controls-to-disable.md").

### Remediation

In the home Region and Regions that aren’t part of an aggregator, record all resources that are required for
controls that are enabled in the current Region, including IAM global resources if you have enabled controls that require IAM global
resources.

In linked Regions, you can use any AWS Config recording mode, as long as you are recording all resources that correspond
to controls that are enabled in the current Region. In linked Regions, if you have enabled controls that require recording of IAM
global resources, you won’t receive a `FAILED` finding (your recording of other resources is sufficient).

The `StatusReasons` field in the `Compliance` object of your finding can help you determine
why you have a failed finding for this control. For more information, see [Compliance details for control
findings](controls-findings-create-update.md#control-findings-asff-compliance "controls-findings-create-update.md#control-findings-asff-compliance").

For a list of which resources must be recorded for each control, see [Required AWS Config resources for control
findings](controls-config-resources.md "controls-config-resources.md").
For general information about enabling AWS Config and configuring resource recording, see [Enabling and configuring AWS Config for Security Hub CSPM](securityhub-setup-prereqs.md "securityhub-setup-prereqs.md").
