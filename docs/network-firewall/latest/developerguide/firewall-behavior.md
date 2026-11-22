

# Firewall behavior in AWS Network Firewall

This section describes how AWS Network Firewall virtual firewalls behave and protect your VPC from attacks. You define and create a firewall, then use it to monitor and protect your subnets. The firewall monitors incoming and outgoing traffic and allows it to pass or drops it, according to your specifications. The firewall only allows packets to pass that pass inspection. 

How a firewall inspects traffic depends on the kind of policy it uses. We recommend **Next Generation** policies for new firewalls, which inspect traffic with a firewall engine and an IPS engine—see [Firewall behavior with a Next Generation policy](firewall-behavior-v2.md). A **Classic Network Firewall** policy inspects traffic with a stateless rules engine and a stateful rules engine—see [Firewall behavior with a Classic Network Firewall policy](firewall-behavior-classic.md).

**Topics**
+ [Firewall behavior with a Next Generation policy](firewall-behavior-v2.md)
+ [Firewall behavior with a Classic Network Firewall policy](firewall-behavior-classic.md)