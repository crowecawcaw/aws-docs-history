

# Security Hub CSPM policies
<a name="orgs_manage_policies_security_hub_cspm"></a>

AWS Security Hub CSPM policies let you centrally enable and configure Security Hub CSPM across the accounts and Regions in your organization. With a Security Hub CSPM policy, you specify the organization targets (the root, organizational units (OUs), or individual accounts) where Security Hub CSPM is enabled or disabled. You also specify which security standards, controls, and custom control parameters apply in each Region. Accounts that join your organization, or move into an OU that has an attached policy, automatically inherit the policy. This keeps your security posture management consistent as your organization grows.

Security Hub CSPM policies are fully integrated with AWS Organizations. The management account, or a delegated administrator that has permission to manage the policy type, creates and attaches the policies. Security Hub CSPM then applies the effective policy to each account and Region in scope, and keeps the account in that state.

## Key features and benefits
<a name="security-hub-cspm-policies-features"></a>

With Security Hub CSPM policies, you get the following capabilities for managing cloud security posture across a multi-account environment:
+ Centrally [enable](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) or disable Security Hub CSPM across accounts and Regions in your organization.
+ Define which security standards are enabled, which controls are enabled or disabled, and which custom control parameter values apply, all in a single policy.
+ Apply a uniform configuration to every Region in scope, or give specific Regions their own configuration to meet Regional compliance requirements.
+ Automatically apply your configuration to new accounts when they join your organization.
+ Prevent accounts that have a policy attached to them from changing Security Hub CSPM settings that are defined in the policy.
+ Automatically associate governed accounts as members of the Security Hub CSPM delegated administrator in each Region, so you don't need to send or accept invitations.

## What are Security Hub CSPM policies?
<a name="security-hub-cspm-policies-what-are"></a>

Security Hub CSPM policies are AWS Organizations declarative policies that provide centralized control over Security Hub CSPM configuration across multiple accounts in your organization. A policy describes the complete desired state of Security Hub CSPM in each Region that it governs: whether Security Hub CSPM is enabled, which standards are enabled, the enablement status of each control, and the values of customizable control parameters.

When a policy governs an account in a Region, the policy is the source of truth for that account's Security Hub CSPM configuration in that Region. Standards that the policy doesn't list as enabled are disabled in Security Hub CSPM. Customizable control parameters that the policy doesn't specify use their default values. This model is the same complete-governance model that Security Hub CSPM [ central configuration](https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html) uses, so you can move existing central configuration policies to AWS Organizations without changing the resulting configuration.

Security Hub CSPM policies replace Security Hub CSPM central configuration as the recommended way to manage Security Hub CSPM across an organization. The two mechanisms are mutually exclusive. For more information about moving from central configuration, see [Managing accounts using organization policies in Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/accounts-orgs-policies.html) in the AWS Security Hub CSPM User Guide.

## How Security Hub CSPM policies work
<a name="security-hub-cspm-policies-how-works"></a>

When you attach a Security Hub CSPM policy to your organization root, an OU, or an account, AWS Organizations calculates the effective policy for each account in scope. Security Hub CSPM then applies the effective policy in each Region that the policy governs. The following rules determine the result:

Regional enablement  
The `enable_in_regions` and `disable_in_regions` lists determine where Security Hub CSPM is enabled or disabled. When a Region appears in both lists, the disable configuration takes precedence. Regions that appear in neither list remain ungoverned by the policy, and their existing settings are left unchanged.

Future Regions  
When you specify `ALL_SUPPORTED`, the list includes all current Regions where Security Hub CSPM is available and any Regions added in the future.

Standards and controls  
In each Region where the policy enables Security Hub CSPM, the policy also applies the standards, controls, and custom control parameters from the `cspm_standards_controls` object. A `default` configuration applies to every enabled Region. An optional Region-specific configuration fully replaces the `default` for that Region.

Control status precedence  
The `enabled_controls` and `disabled_controls` lists determine which security controls are enabled in the relevant Regions. When a control appears in both lists, the disable configuration takes precedence. Any other control in an enabled standard uses the `default_control_association_status` value.

Inheritance  
Child policies can modify parent policy settings using inheritance operators, unless the parent policy restricts those operators.

When a Security Hub CSPM policy governs an account in a Region, you can't use the Security Hub CSPM console or API in that account to change the settings that the policy manages. To change those settings, update the policy.

## Terminology
<a name="security-hub-cspm-policies-terminology"></a>

This topic uses the following terms when discussing Security Hub CSPM policies.


**Security Hub CSPM policy terminology**  

| Term | Definition | 
| --- | --- | 
| Effective policy | The final policy that applies to an account after AWS Organizations combines all inherited policies and any policies attached directly to the account. | 
| Policy inheritance | The process by which accounts inherit policies from the organization root and parent organizational units. | 
| Governed Region | A Region that appears in the enable\_in\_regions or disable\_in\_regions list of an account's effective policy. | 
| Ungoverned Region | A Region that appears in neither list. The policy doesn't change or manage Security Hub CSPM settings in that Region. | 
| Management account | The account that creates the organization. It enables trusted access and the policy type, and can designate a delegated administrator. | 
| Delegated administrator | The account designated to manage Security Hub CSPM on behalf of the organization. With a delegation policy, it can also create and manage Security Hub CSPM policies. | 
| Delegation policy | The AWS Organizations resource-based policy that grants a delegated administrator permission to manage Security Hub CSPM policies. | 
| Central Configuration | The earlier Security Hub CSPM feature for configuring Security Hub CSPM across an organization by using configuration policies. It is mutually exclusive with Security Hub CSPM policies. | 

## Use cases for Security Hub CSPM policies
<a name="security-hub-cspm-policies-use-cases"></a>

With Security Hub CSPM policies, you can address common posture management challenges in multi-account environments. The following use cases show how organizations typically use them.

### Organization-wide security baseline
<a name="security-hub-cspm-policies-use-case-1"></a>

A security team wants every account to run the [AWS Foundational Security Best Practices standard](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html) in every Region. They attach a policy to the organization root that enables Security Hub CSPM in `ALL_SUPPORTED` Regions and enables the standard with all of its controls. New accounts and new Regions are covered automatically.

### Regional compliance requirements
<a name="security-hub-cspm-policies-use-case-2"></a>

A multinational company must run the PCI DSS standard only in the Regions that process cardholder data. They use a `default` configuration for the organization-wide baseline, and add Region-specific configurations that also enable PCI DSS in the affected Regions.

### Cost-conscious control selection
<a name="security-hub-cspm-policies-use-case-3"></a>

An organization wants findings only for a curated set of controls. They set `default_control_association_status` to `DISABLED` and list only the controls they want in `enabled_controls`. Controls that Security Hub CSPM releases later remain disabled until the policy enables them.

### Workload-specific configuration by OU
<a name="security-hub-cspm-policies-use-case-4"></a>

A platform team attaches a baseline policy at the root, then attaches child policies to specific OUs to add standards or adjust control parameters for workloads with stricter requirements.

## Policy inheritance and enforcement
<a name="security-hub-cspm-policies-inheritance"></a>

The inheritance model follows the AWS Organizations hierarchy, so policy application is predictable and consistent.
+ Policies attached at the root apply to all accounts.
+ Accounts inherit policies from their parent organizational units.
+ Multiple policies can apply to a single account. AWS Organizations merges them into one effective policy.
+ More specific policies (closer to the account in the hierarchy) take precedence, subject to the inheritance operators that parent policies allow.
+ Policy enforcement is eventually consistent. Security Hub CSPM applies changes asynchronously and periodically corrects any configuration drift in governed accounts.

## Policy validation
<a name="security-hub-cspm-policies-validation"></a>

When you create or update a Security Hub CSPM policy, AWS Organizations validates it. The following validations occur:
+ Region names must be valid AWS Region identifiers where Security Hub CSPM is available.
+ Policy structure must follow AWS Organizations policy syntax rules.
+ Both `enable_in_regions` and `disable_in_regions` lists must be present, though they can be empty.
+ The `cspm_standards_controls` object must contain a `default` object with a `default_control_association_status` value.
+ Standards, control IDs, and custom control parameter names must be valid. Control parameter values must be within the allowed range for the parameter.
+ Each control in `enabled_controls` and `disabled_controls` must belong to a standard that the same policy enables.
+ A policy must not list `enabled_controls` when `default_control_association_status` is `ENABLED`, or `disabled_controls` when it is `DISABLED`.

Some conditions can arise only in the effective policy, after AWS Organizations merges several individually valid policies.
+ A policy can list some controls in both the `enabled_controls` and `disabled_controls` lists. When a control appears in both lists, the disable configuration takes precedence.
+ An effective policy can enable a control without enabling any standard that contains it. In this case, Security Hub CSPM enables the control by using the AWS Organizations service-managed standard in Security Hub CSPM rather than failing the policy.

## Regional considerations and supported Regions
<a name="security-hub-cspm-policies-regions"></a>

Security Hub CSPM policies operate in each Region independently. Understanding Regional behavior helps you design policies for your organization's global footprint.
+ Policy enforcement occurs in each Region independently.
+ You can specify which Regions to enable, disable, or leave ungoverned.
+ A Region-specific configuration in `cspm_standards_controls` completely replaces the `default` configuration for that Region.
+ New Regions are automatically included when you use `ALL_SUPPORTED`.
+ Policies apply only in Regions where Security Hub CSPM is available. A standard or control that isn't available in a Region has no effect in that Region.
+ Security Hub CSPM policies are available in the commercial AWS Regions, the AWS GovCloud (US) Regions, and the China Regions.

## Detachment behavior
<a name="security-hub-cspm-policies-detachment"></a>

If you detach a Security Hub CSPM policy and no other policy applies to an account, Security Hub CSPM and its standards and controls stay in their current state in that account. The account becomes self-managed and can change its own settings again. Future changes to the organization, such as new accounts joining an OU, no longer configure Security Hub CSPM automatically unless another attached policy covers them.

## Delegated administrator
<a name="security-hub-cspm-policies-delegated-admin"></a>

The Security Hub CSPM delegated administrator manages Security Hub CSPM for the organization. To let the [ delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html) create and attach Security Hub CSPM policies, the management account attaches a delegation policy. This resource-based policy grants permission to manage the `SECURITYHUB_CSPM_POLICY` policy type. Security Hub and Security Hub CSPM share the same delegated administrator.

## Prerequisites
<a name="security-hub-cspm-policies-prerequisites"></a>

Before you use Security Hub CSPM policies, complete the following prerequisites:
+ Enable trusted access for Security Hub CSPM in AWS Organizations.
+ Designate a delegated administrator for Security Hub CSPM (recommended).
+ Attach a delegation policy for the delegated administrator, if the delegated administrator will manage policies.
+ Enable the Security Hub CSPM policy type on the organization root.

## Next steps
<a name="security-hub-cspm-policies-next-steps"></a>

To get started with Security Hub CSPM policies:

1. Complete the prerequisites in [Getting started with Security Hub CSPM policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub_cspm_getting_started.html).

1. Plan your policy strategy. For more information, see [Best practices for using Security Hub CSPM policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub_cspm_best_practices.html).

1. Review the policy syntax and example policies in [Security Hub CSPM policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub_cspm_syntax.html).

1. If you use central configuration, review [Managing accounts using organization policies](https://docs.aws.amazon.com/securityhub/latest/userguide/accounts-orgs-policies.html) in the AWS Security Hub CSPM User Guide before you attach your first policy.