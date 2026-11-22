

# Firewall behavior with a Classic Network Firewall policy

When a firewall uses a Classic Network Firewall policy, it inspects traffic with a stateless rules engine and a stateful rules engine. For new firewalls, we recommend a Next Generation policy instead; see [Firewall behavior with a Next Generation policy](firewall-behavior-v2.md).

**Network Firewall monitors and controls traffic to and from your protected subnets**  
The following figure shows the basic interaction of your firewall with traffic coming into your customer subnet and with traffic going out from your customer subnet.

![The figure shows a firewall subnet directly above a customer subnet. Inside the firewall subnet is a rules engines container for packet inspection. From above the left half of the firewall subnet, a vertical grey arrow labeled "incoming packets" points down to the rules engines inside the firewall subnet. From the left side of the rules engines, a horizontal red arrow labeled "drop incoming" points left to a large red X that sits outside the firewall subnet. From the bottom left of the rules engine, a vertical green arrow labeled "pass" points down from the firewall subnet rules engines to the customer subnet. From the upper right of the customer subnet, a grey arrow labeled "outgoing packets" points up to the rules engines in the firewall subnet. From the right side of the rules engines, a horizontal red arrow labeled "drop outgoing" points right to a large red X that sits outside the firewall subnet. From the top right of the rules engine, a vertical green arrow labeled "pass" points up from the rules engines to outside the firewall subnet.](https://docs.aws.amazon.com/network-firewall/latest/developerguide/images/firewall-pass-drop.png)


**Topics**
+ [Network Firewall stateless and stateful rules engines](firewall-rules-engines.md)
+ [How AWS Network Firewall filters network traffic](firewall-policy-processing.md)