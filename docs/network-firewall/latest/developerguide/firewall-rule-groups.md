

# Working with firewall rule groups in AWS Network Firewall
<a name="firewall-rule-groups"></a>

A *firewall rule group* holds the access-control rules that the firewall engine evaluates. Firewall rules are drop by default and are evaluated at connection-state hooks as a connection progresses. You use them to define which traffic is allowed into your network. The firewall engine is built on Suricata's firewall mode. For more information, see the [Suricata firewall mode documentation](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html).

**Note**  
Firewall rule groups don't support IP set references—references to IP addresses or CIDR blocks held in another resource, such as an Amazon Virtual Private Cloud managed prefix list, a resource group, an address list, or a container association. To use CIDR ranges in firewall rules, use rule variables instead. IP set references are available for IPS rule groups and for Classic Network Firewall stateful rule groups; for the Classic version, see [IP set references in Suricata compatible AWS Network Firewall rule groups](rule-groups-ip-set-references.md).

**Topics**
+ [Authoring firewall rules](firewall-rule-groups-authoring.md)
+ [Fields of a modeled firewall rule](firewall-rule-groups-modeled.md)
+ [Firewall engine hooks](firewall-rule-groups-hooks.md)
+ [Firewall engine actions and scopes](firewall-rule-groups-verdicts.md)
+ [Accepting prior hooks automatically](firewall-rule-groups-accept-prior-hooks.md)
+ [Bypassing the IPS engine for accepted traffic](firewall-rule-ips-bypass.md)
+ [Generating firewall rules from domain names](firewall-rule-groups-fqdn.md)
+ [Geographic IP filtering](firewall-rule-groups-geo-ip.md)
+ [Dropping at an application-layer hook under a drop-by-default policy](firewall-rule-app-layer-drop-prior-hooks.md)
+ [URL and domain category filtering](firewall-rule-groups-url-category.md)
+ [Example firewall rules](firewall-rule-groups-examples.md)
+ [Best practices for firewall rules](firewall-rule-groups-best-practices.md)
+ [Valid combinations and constraints for firewall rules](firewall-rule-constraints.md)
+ [Managing evaluation order for firewall rules](firewall-rule-evaluation-order.md)