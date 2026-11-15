

# Best practices for using Security Hub CSPM policies
<a name="orgs_manage_policies_security_hub_cspm_best_practices"></a>

Following these best practices helps you deploy and maintain Security Hub CSPM policies successfully across your organization. These guidelines cover Security Hub CSPM policy management and enforcement within AWS Organizations, including its complete-governance model, Region-specific configurations, and inheritance behavior.

## Policy design principles
<a name="policy-design-principles-cspm"></a>

Establish clear principles for your policy structure before you create Security Hub CSPM policies. Keep policies simple. Start with a broad baseline at the organization root, and refine it through child policies or Region-specific configurations only where an OU or Region needs a different configuration.

Before you write a policy, understand how Security Hub CSPM resolves it:
+ A policy governs Security Hub CSPM completely in each Region it enables. The policy disables any standard that it doesn't list as enabled. Control parameters that the policy doesn't specify use their default values.
+ A Region-specific configuration fully replaces the `default` configuration for that Region. It isn't merged with the default. List every standard, control setting, and parameter that you want in that Region.
+ A Region that appears in neither `enable_in_regions` nor `disable_in_regions` is unmanaged, not disabled. The policy leaves existing settings in that Region unchanged.
+ `default_control_association_status` also determines whether Security Hub CSPM automatically enables new controls in enabled standards. Choose `ENABLED` if you want new controls to be enabled as Security Hub CSPM releases them. Choose `DISABLED` if you want to opt in to each control explicitly.
+ Use empty Region lists deliberately. You can leave `enable_in_regions` empty when you only need to disable Security Hub CSPM in specific Regions, or leave `disable_in_regions` empty to keep Regions outside your enable list ungoverned.

## Region management strategies
<a name="region-management-strategies-cspm"></a>

Use `ALL_SUPPORTED` in `enable_in_regions` when you want your coverage to include future Regions automatically. Use explicit Region lists when you need precise control, for example to keep development Regions ungoverned.

Favor a clear `default` configuration plus a small number of Region-specific configurations over many one-off Regional blocks. Add a Region-specific configuration only when a Region needs a different set of standards, controls, or parameters.

Security Hub CSPM policies don't have a home Region. Controls that evaluate global resources, such as many IAM controls, produce the same findings in every Region where they're enabled. To avoid duplicate findings and AWS Config costs, enable these controls in one Region by using a Region-specific configuration. Then disable them in the `default` configuration. For an example of this configuration, see [Security Hub CSPM policy syntax and examples](orgs_manage_policies_security_hub_cspm_syntax.md).

Document your Region-specific requirements, particularly for:
+ Compliance-mandated Regions that require specific standards
+ Regions where you aggregate findings
+ Opt-in Regions with special considerations
+ Regions where Security Hub CSPM must remain disabled

## Policy inheritance planning
<a name="policy-inheritance-planning-cspm"></a>

Plan your inheritance structure so that you keep effective control while allowing the flexibility you need. Document which OUs can modify inherited policies and which changes they can make. To enforce a baseline that child policies can't change, restrict inheritance operators at the parent level with `@@operators_allowed_for_child_policies`. For example, set `["@@none"]` on `disable_in_regions` to prevent child policies from disabling Security Hub CSPM.

## Delegated administrator strategy
<a name="delegated-administrator-strategy-cspm"></a>

Designate a dedicated security or compliance account as the Security Hub CSPM delegated administrator rather than operating from the management account. Before you attach Security Hub CSPM policies, designate the delegated administrator and attach the delegation policy. Security Hub CSPM uses the delegated administrator to automatically associate governed accounts as members in each Region. This gives you one place to review findings and keeps administration separate from the management account.

Avoid attaching a policy that disables Security Hub CSPM to the delegated administrator account. If a policy disables Security Hub CSPM for the delegated administrator in a Region, Security Hub CSPM removes its member associations and its administrator designation in that Region.

## Migrating from central configuration
<a name="migrating-from-central-configuration-cspm"></a>

If you use Security Hub CSPM central configuration, migrate by using the import tool in the Security Hub console. The tool creates and attaches equivalent Security Hub CSPM policies for your existing configuration policies and associations. Attaching any Security Hub CSPM policy outside the tool disables central configuration for your entire organization. Accounts that central configuration previously governed might then have no policy.

## Communicate and train
<a name="communicate-and-train-cspm"></a>

Tell account owners that the organization policy now drives their Security Hub CSPM configuration. Explain three points: they can't change policy-managed settings from their accounts, a policy can change which standards and controls are active in their accounts, and ungoverned Regions keep their existing settings. Clear communication helps account owners understand the findings they receive and the controls that apply to them.

## Monitoring and validation
<a name="monitoring-validation-cspm"></a>

After you attach or modify a policy, run `DescribeEffectivePolicy` for representative accounts to confirm that the policy resolves as intended. A Region-specific configuration fully replaces the `default`, so `DescribeEffectivePolicy` is the most reliable way to catch a Region that unexpectedly lost a standard or control. Confirm that new accounts inherit the intended configuration. Review policy attachments periodically, and after any organizational change, to make sure coverage matches your structure and requirements.

## Troubleshooting strategies
<a name="troubleshooting-strategies-cspm"></a>

Use the following strategies when you troubleshoot Security Hub CSPM policies:
+ Disable takes precedence over enable. If a Region appears in both Region lists, the policy disables it. The same applies to a control that appears in both control lists.
+ A Region-specific configuration fully replaces the `default`. If a standard or control seems to be missing in one Region, check whether a Region-specific configuration omitted it.
+ A Region in neither Region list is ungoverned, not disabled. If a Region shows no policy effect, confirm whether you intended to govern it.
+ Enforcement is eventually consistent. A policy change applies asynchronously, and Security Hub CSPM periodically corrects drift. Allow time before you conclude that a change didn't take effect.
+ Trace the inheritance chain from the root down to understand how parent and child policies combine into each account's effective policy, and validate the result with `DescribeEffectivePolicy`.