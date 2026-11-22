

# Next Generation policies in AWS Network Firewall

An AWS Network Firewall *Next Generation* policy (the `FirewallPolicyV2` resource) is a firewall policy that filters traffic using two separate inspection engines: a *firewall engine* for access control and an *IPS engine* for intrusion detection and prevention. Next Generation policies are a separate resource type from the Classic Network Firewall policies described in [Classic Network Firewall policies](firewall-policies-classic.md). The two policy types exist side by side, and a firewall uses one or the other. For an overview of how the two policy types compare, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).

Like a Classic Network Firewall policy, a Next Generation policy defines the monitoring and protection behavior for a firewall. The details of the behavior are defined in the rule groups that you add to the policy's two sections, and in the policy's default settings. Within either section, you can reference reusable rule groups or author *embedded rules* (also called inline rules) directly in the policy; for how to add rules to a section, see [The firewall section and the IPS section](firewall-policy-v2-sections.md). To use a firewall policy, you associate it with one or more firewall endpoints or firewall endpoint associations.

**Topics**
+ [The firewall engine and the IPS engine](firewall-policy-v2-engines.md)
+ [Next Generation policy settings in AWS Network Firewall](firewall-policy-v2-settings.md)
+ [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md)
+ [Stream exception policy for Next Generation policies](stream-exception-policy-v2.md)
+ [Firewall default action](firewall-policy-v2-default-action.md)
+ [The firewall section and the IPS section](firewall-policy-v2-sections.md)
+ [Embedded rules in a Next Generation policy](firewall-policy-v2-embedded-rules.md)
+ [Signature ID uniqueness](firewall-policy-v2-sid-uniqueness.md)
+ [Managing your Next Generation policy in AWS Network Firewall](firewall-policy-v2-managing.md)