

# Working with stateful rule groups in AWS Network Firewall
<a name="stateful-rule-groups-ips"></a>

A stateful rule group is a rule group that uses Suricata compatible intrusion prevention system (IPS) specifications. Suricata is an open source network IPS that includes a standard rule-based language for stateful network traffic inspection. 

Stateful rule groups have a configurable top-level setting called `StatefulRuleOptions`, which contains the `RuleOrder` attribute. You can set this in the console when you create a rule group, or in the API under `StatefulRuleOptions`. You can't change the `RuleOrder` after the rule group is created. 

You can enter any stateful rule in Suricata compatible strings. For standard Suricata rules specifications and for domain list inspection, you can alternately provide specifications to Network Firewall and have Network Firewall create the Suricata compatible strings for you. 

As needed, depending on the rules that you provide, the stateful engine performs deep packet inspection (DPI) of your traffic flows. DPI inspects and processes the payload data within your packets, rather than just the header information. 

The rest of this section provides requirements and additional information for using Suricata compatible rules with Network Firewall. 

**Note**  
This section and others that describe Suricata-based concepts are not intended to replace or duplicate information from the Suricata documentation. For more Suricata-specific information, see the [Suricata documentation](https://docs.suricata.io/en/suricata-8.0.3/).

**Previous Suricata major version upgrade**  
When Network Firewall upgrades to a new major version of Suricata, related changes are tracked here.

Network Firewall upgraded from Suricata version 7.0 to 8.0.3. For full information about the upgrade from version 7.0, see [Upgrading 7.0 to 8.0](https://docs.suricata.io/en/latest/upgrade.html#upgrading-7-0-to-8-0) on the Suricata website. 

The following are examples of the changes in that upgrade: 
+ WebSocket is now identified as its own protocol, separate from HTTP. After an HTTP `Upgrade` to WebSocket completes, the flow is reclassified from `http` to `websocket`. 
+ As a result, rules that use `app-layer-protocol:!http` to detect non-HTTP traffic on HTTP ports now match WebSocket traffic. To continue allowing WebSocket connections, add a pass rule that matches the HTTP Upgrade handshake before those rules. For an example, see [Stateful rules examples: allow traffic](suricata-examples.md#suricata-example-allow-rules). 
+ You might see an increase in alerts for the same rules, because the stateful engine can trigger TCP stream reassembly earlier. 
+ The `stream.checksum-validation` setting no longer affects the checksum rule keywords. For example, `ipv4-csum:valid` now matches only when the checksum is actually valid. 

**Topics**
+ [Creating a stateful rule group](rule-group-stateful-creating.md)
+ [Updating a stateful rule group](rule-group-stateful-updating.md)
+ [Deleting a stateful rule group](rule-group-stateful-deleting.md)
+ [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md)
+ [Limitations and caveats for stateful rules in AWS Network Firewall](suricata-limitations-caveats.md)
+ [Best practices for writing Suricata compatible rules for AWS Network Firewall](suricata-best-practices.md)
+ [Examples of stateful rules for Network Firewall](suricata-examples.md)