

# Best practices for using Amazon GuardDuty policies
<a name="orgs_manage_policies_guardduty_best_practices"></a>

When implementing Amazon GuardDuty policies across your organization, following established best practices helps ensure successful deployment and maintenance of your threat-detection configuration. These guidelines address the aspects of GuardDuty policy management and enforcement within AWS Organizations, including its per-Region enablement model and inheritance behavior.

## Policy design principles
<a name="guardduty-policy-design-principles"></a>

Before creating GuardDuty policies, establish clear principles for your policy structure. Keep policies simple and avoid complex nested or per-Region overrides where a single default suffices, because they make the effective outcome harder to reason about. Start with a broad default at the organization root and refine it through child policies or Regional overrides only where a specific Region genuinely needs a different configuration.

Understand how the enablement model resolves before you author a policy:
+ The `default` block is the baseline applied to every Region where GuardDuty is available. It is optional.
+ A Region-keyed block fully replaces the default for that Region; it is not merged. List every feature you want in that Region, because features omitted from a Regional block are not inherited from `default`.
+ A Region with no default and no Regional block is unmanaged, not disabled. The policy neither enables nor disables it, and existing settings are left unchanged.
+ Within any block, foundational threat detection must be enabled if any other feature in that same block is enabled.

## Region management strategies
<a name="guardduty-region-management-strategies"></a>

When managing Regions through GuardDuty policies, favor a clear default plus a small number of explicit Regional overrides over many one-off blocks. Rely on the `default` block to cover future Regions automatically, and add a Region-keyed block only when a Region requires a configuration that differs from the default.

## Delegated administrator strategy
<a name="guardduty-delegated-administrator-strategy"></a>

Designate a dedicated security or compliance account as the GuardDuty delegated administrator, rather than operating from the management account. Set the delegated administrator from the GuardDuty console or through AWS Organizations APIs before you attach policies. Centralizing administration in one account gives you consistent management, a single place to review findings, and a clear separation from the management account.

## Communicate and train
<a name="guardduty-communicate-and-train"></a>

Educate account owners that GuardDuty enablement is now driven by the organization policy and might change the features active in their accounts. Explain that a policy manages features per Region, enabling or disabling them, and that an unmanaged Region leaves their existing settings untouched. Clear communication helps account owners understand the monitoring in place and respond appropriately to findings surfaced through the delegated administrator.

## Monitoring and validation
<a name="guardduty-monitoring-validation"></a>

After attaching or modifying a policy, run `DescribeEffectivePolicy` for representative accounts and Regions to confirm the enablement resolves as intended. Because a Regional block fully replaces the default, this is the reliable way to catch a Region that unexpectedly dropped a feature. Monitor for new accounts joining the organization and confirm they inherit the intended GuardDuty enablement automatically. Review policy attachment scopes periodically, at least quarterly and after any organizational change, to ensure coverage stays aligned with your structure and security requirements.

## Troubleshooting strategies
<a name="guardduty-troubleshooting-strategies"></a>

Use the following strategies when troubleshooting GuardDuty policies:
+ A Region-keyed block fully replaces the default for that Region. If a feature seems missing in one Region, check whether a Regional override omitted it rather than assuming it was inherited.
+ A Region with no default and no override is unmanaged, not disabled. If a Region shows no policy effect, confirm whether it is genuinely unmanaged.
+ Enforcement is eventually consistent, not instant. A policy change propagates asynchronously and is reconciled by periodic drift correction, so allow time before concluding a change did not take effect.
+ Walk the inheritance chain from the root down to understand how parent and child policies combine into the effective policy for each account, and validate the result with `DescribeEffectivePolicy`.