

# AWS Network Firewall quotas

AWS Network Firewall is subject to the following quotas (formerly referred to as limits). These quotas are the same for all AWS Regions in which Network Firewall is available. Each Region is subject to these quotas individually. The quotas are not cumulative across Regions.

Network Firewall has the following default quotas on the maximum number of entities you can have per account per Region. You can request an increase in these adjustable quotas through the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/network-firewall/quotas).


| Resource | Default quota | 
| --- | --- | 
| Maximum number of firewalls per account per Region. | 5 | 
| Maximum number of firewall policies per account per Region. | 20 | 
| Maximum number of stateful rule groups per account per Region. <br />You can't use all of these rule groups in a single firewall policy. See the immutable maximum number of stateful rule groups per firewall policy in the table that follows this one.  | 50 | 
| Maximum number of VPC endpoint associations per account per Region. | 300 | 
| Maximum number of stateless rule groups per account per Region.<br />You can't use all of these rule groups in a single firewall policy. See the immutable maximum number of stateless rule groups per firewall policy in the table that follows this one.  | 50 | 
| Maximum number of stateful rules per firewall policy per account per Region. This is the total across all rule groups that are referenced by the policy. | 30,000 | 
| Maximum number of TLS inspection configurations per account per Region. | 20 | 
| Maximum number of container associations per account per Region. | 100 | 

Network Firewall has the following quotas that can't be changed.


| Resource | Quota | 
| --- | --- | 
| Maximum number of VPC endpoint associations allowed per firewall, per Availability Zone. | 50 | 
| Maximum character length of a Suricata rule. Each variable value in the rule counts towards this limit. | 8,192 | 
| Maximum size of a Suricata-compatible rules string for a rule group, in bytes. | 2,000,000 | 
| Maximum number of VPC IDs per aws\_firewall\_endpoint\_vpc rule option. | 4,096 | 
| Size reserved per aws\_firewall\_endpoint\_vpc option during rule validation. | 992 bytes | 
| Maximum stateful rule group capacity. For more information, see [Setting rule group capacity in AWS Network Firewall](nwfw-rule-group-capacity.md). | 30,000 | 
| Maximum number of IP set references per Suricata compatible stateful rule group. For information about IP set references, see [IP set references in Suricata compatible AWS Network Firewall rule groups](rule-groups-ip-set-references.md). | 5 | 
| Maximum number of context sets per rule group. For information about context sets, see [Context-aware rules in AWS Network Firewall](context-aware-rules.md). | 100 | 
| Maximum number of resource IDs per context set. A rule that references a context set must also stay within the maximum character length of a rule after Network Firewall expands the variable references in it. | 1,000 | 
| Maximum number of monitoring configurations per container association. | 5 | 
| Maximum number of container association references per rule group. | 30 | 
| Maximum number of stateful rule groups per firewall policy. | 20 | 
| Maximum number of stateless rule groups per firewall policy. | 20 | 
| Maximum stateless rule group capacity. For more information, see [Setting rule group capacity in AWS Network Firewall](nwfw-rule-group-capacity.md).  | 30,000 | 
| Maximum number of custom actions per stateless rule group. | 10 | 
| Maximum number of stateless rules per firewall policy. This is the total across all rule groups that are referenced by the policy. | 30,000 | 
| Maximum number of firewall rules per Next Generation policy. This is the total across the embedded rules and all rule groups that are referenced in the policy's firewall section. This is a fixed limit; every policy has this full capacity and it can't be increased. The firewall engine and the IPS engine have dedicated, separate rule capacity, for a combined total of 80,000 rules per policy. For more information, see [Next Generation policies](firewall-policies-v2.md) and [Setting rule group capacity in AWS Network Firewall](rule-group-capacity-v2.md).IPS engine domain list rule groups use a separate capacity pool. Their capacity is tracked independently from the firewall engine and IPS rule pools and doesn't count toward the combined 80,000 firewall and IPS total. This pool allows a maximum of 10,000,000 domain name specifications per policy. | 30,000 | 
| Maximum number of IPS rules per Next Generation policy. This is the total across the embedded rules and all rule groups that are referenced in the policy's IPS section. This is a fixed limit; every policy has this full capacity and it can't be increased. For more information, see [Next Generation policies](firewall-policies-v2.md) and [Setting rule group capacity in AWS Network Firewall](rule-group-capacity-v2.md). | 50,000 | 
| Maximum number of embedded rules per Next Generation policy. This is the combined total of the embedded rules that you author directly in the policy's firewall engine section and IPS engine section. This count includes disabled rules. Rules in referenced rule groups don't count toward this limit. | 30,000 | 
| Maximum combined size of embedded rules per Next Generation policy. This is the combined size of the embedded rule strings across the policy's firewall engine section and IPS engine section. | 5 MB | 
| Maximum number of firewall rule groups per Next Generation policy. The maximum number of rule group entries in the policy's firewall engine section, counting both referenced rule groups and embedded rules. | 20 | 
| Maximum number of IPS rule groups per Next Generation policy. The maximum number of rule group entries in the policy's IPS engine section, counting both referenced rule groups and embedded rules. | 20 | 
| Maximum network traffic bandwidth for a firewall's endpoints in any single Availability Zone. Endpoints can be defined in the firewall and in VPC endpoint associations that use the firewall. Network Firewall drops any traffic over the limit.  | 100 Gbps | 
| Maximum number of IP addresses per NAT gateway that Network Firewall creates for a NAT/Proxy firewall. For a public NAT gateway, an Elastic IP address and its paired private IP address count as one address. Amazon EC2 quotas for NAT gateways and Elastic IP addresses also apply. For information, see [Amazon VPC quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) in the Amazon Virtual Private Cloud User Guide. | 8 | 
| Maximum number of NAT gateways and firewall endpoints per Availability Zone for a NAT/Proxy firewall. | 1 | 
| Required number of firewall policies per firewall. | 1 | 
| Maximum consumed domain capacity per firewall policy. This is the total number of domain name specifications across all AWS Marketplace managed rule groups in the firewall policy that use the stateful-domain-rulegroup resource type. | 10,000,000 | 
| Maximum number of firewalls that can use the same firewall policy. | 1,000 | 
| Maximum number of firewall policies that can use the same rule group. | 1,000 | 
| Maximum number of TLS inspection configurations per firewall policy. | 1 | 
| Maximum number of firewall policies that can use the same TLS inspection configuration. | 1,000 | 
| Maximum number of certificate authority (CA) certificates per TLS inspection configuration. CA certificates are used for outbound SSL/TLS inspection. | 1 | 
| Maximum number of server certificates per TLS inspection configuration. Server certificates are used for inbound SSL/TLS inspection. | 10 | 