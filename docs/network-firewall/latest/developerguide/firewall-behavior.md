# Firewall behavior in AWS Network Firewall

This section describes how AWS Network Firewall virtual firewalls behave and protect your VPC from attacks.
You define and create a firewall, then use it to monitor and protect your subnets. The
firewall monitors incoming and outgoing traffic and allows it to pass or drops it,
according to your specifications. The firewall only allows packets to pass that pass
inspection.

###### Network Firewall monitors and controls traffic to and from your protected

subnets

The following figure shows the basic interaction of your firewall with traffic
coming into your customer subnet and with traffic going out from your customer
subnet.

![The figure shows a firewall subnet directly above a customer subnet. Inside the firewall subnet is a rules engines container for packet inspection. From above the left half of the firewall subnet, a vertical grey arrow labeled "incoming packets" points down to the rules engines inside the firewall subnet. From the left side of the rules engines, a horizontal red arrow labeled "drop incoming" points left to a large red X that sits outside the firewall subnet. From the bottom left of the rules engine, a vertical green arrow labeled "pass" points down from the firewall subnet rules engines to the customer subnet. From the upper right of the customer subnet, a grey arrow labeled "outgoing packets" points up to the rules engines in the firewall subnet. From the right side of the rules engines, a horizontal red arrow labeled "drop ourgoing" points right to a large red X that sits outside the firewall subnet. From the top right of the rules engine, a vertical green arrow labeled "pass" points up from the rules engines to outside the firewall subnet.](images/firewall-pass-drop.png)

###### Topics

- [Network Firewall stateless and stateful rules engines](firewall-rules-engines.md "firewall-rules-engines.md")
- [How AWS Network Firewall filters network traffic](firewall-policy-processing.md "firewall-policy-processing.md")
