# Viewing AWS managed rule groups in Network Firewall using the console

You can view the managed rule groups that are available for your use in your Network Firewall policy.

###### To view the list of managed rule groups

- **Console** – You can view the list of managed rule groups either in the **Network Firewall rule groups** page in the **AWS managed rule groups** tab, or in the policy details page. When you add managed rule groups to a policy, you’ll see only the managed rule groups that fit your policy type. For example, if your policy type is default ordered, you’ll see only the managed rule groups that have a type of default ordered.
- **API** – [ListRuleGroups](../APIReference/API_ListRuleGroups.md "../APIReference/API_ListRuleGroups.md") with the parameter `Scope`.
- **CLI** – `aws network-firewall list-rule-groups --scope MANAGED`. To filter by managed rule group type, you can include the parameter `managed-type` and filter by `AWS_MANAGED_THREAT_SIGNATURES` and `AWS_MANAGED_DOMAIN_LISTS`.
