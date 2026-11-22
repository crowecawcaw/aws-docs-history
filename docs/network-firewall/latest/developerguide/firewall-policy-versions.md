

# AWS Network Firewall firewall policy versions

Network Firewall offers two kinds of firewall policy. You can associate either a Classic Network Firewall policy or a Next Generation policy with a firewall, but not both. We recommend a Next Generation policy for new firewalls. Classic Network Firewall remains fully supported, so you can keep using it for existing firewalls.
+ **Next Generation policy** (recommended) – Filters traffic using two engines: a *firewall engine* for access control and an *IPS engine* for threat detection and prevention. For more information, see [Next Generation policies](firewall-policies-v2.md).
+ **Classic Network Firewall policy** – Filters traffic using a stateless rules engine and a stateful rules engine. Classic policies remain fully supported for existing firewalls. For more information, see [Classic Network Firewall policies](firewall-policies-classic.md).

Within a Next Generation policy, the clearest difference between its two engines is their default behavior. The firewall engine is *drop by default*—it blocks traffic that you don't explicitly allow, so you use it as an access-control layer. The IPS engine is *pass by default*—it allows traffic that doesn't match a rule, so you use it to detect and block known threats. This separation gives Network Firewall one engine of each kind and keeps access control and threat detection cleanly separated. A Next Generation policy also provides a simplified rule-authoring model and dynamic rule capacity, and it doesn't use stateless rule groups.