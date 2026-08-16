# Troubleshooting telemetry configuration

This section describes common issues you might encounter when using telemetry
configuration and how to resolve them.

## Resources not appearing

If resources are not appearing in discovery, verify the following:

- The resource type is supported by telemetry configuration. For a list of supported
  data sources, see [Supported data sources](telemetry-config-rules.md#telemetry-config-troubleshoot-service "telemetry-config-rules.md#telemetry-config-troubleshoot-service").
- The AWS Config recorder is enabled in your account. Telemetry configuration requires AWS Config
  service-linked recorders to discover resources.
- You have appropriate IAM permissions to view the resources.
- Sufficient time has elapsed since enabling telemetry configuration. The initial
  discovery of resources may take up to 24 hours to complete in some cases.

## Rules not applying

If enablement rules are not applying to your resources, check the following:

- Verify the rule scope configuration. Make sure the rule targets the correct
  organization, OU, or account.
- Check tag filters. If the rule uses tag-based filtering, verify that the target
  resources have the expected tags.
- Check for rule conflicts. If multiple conflicting rules exist, none of the
  conflicting rules are applied. For more information, see [Rule evaluation hierarchy](telemetry-config-rules.md#telemetry-config-rules-hierarchy "telemetry-config-rules.md#telemetry-config-rules-hierarchy").

###### Note

When you create an enablement rule, we discover non-compliant resources (those without
telemetry enabled) through AWS Config Configuration Items (CIs) before turning them on
based on your enablement rule scope. The initial discovery of the resources may take up to
24 hours to complete in some cases.

## Multi-Region issues

When using multi-Region telemetry configuration, you might encounter the following
issues:

- **Spoke Region failures** – If a rule fails to
  replicate to a spoke Region, the failure is visible in the rule status dashboard. The
  system automatically retries failed replications. Check the per-Region status in the
  console or by using the API to identify which Regions are affected.
- **Delayed resource discovery** – Resources from
  spoke Regions may take longer to appear in the home Region view because CloudWatch uses a AWS Config
  aggregator to collect resource data across Regions.
- **Reconciliation drift** – The system
  periodically reconciles rules across Regions to correct drift. If you notice
  inconsistencies between the home Region and spoke Regions, allow time for the
  reconciliation process to complete.

## Home Region conflicts

You might encounter errors when attempting to edit or delete a rule from a Region that
is not the home Region for that rule. Replicated rules can only be modified in the home
Region where they were originally created.

To resolve home Region conflicts:

- Check the informational alert displayed on the rule in the console. The alert
  identifies the home Region for the rule.
- Navigate to the home Region in the CloudWatch console to edit or delete the rule.
- If you need to create a different rule in the spoke Region, create a new rule with a
  different name and scope that does not conflict with the replicated rule.
