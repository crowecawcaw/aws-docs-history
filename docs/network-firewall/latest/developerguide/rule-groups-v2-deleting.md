

# Deleting a rule group for a Next Generation policy

To delete a rule group, use the guidance in this section.

**Deleting a rule group, TLS inspection configuration, or firewall policy**  
When you delete a rule group, TLS inspection configuration, or a firewall policy, AWS Network Firewall checks to see if it's currently being referenced. A rule group and TLS inspection configuration can be referenced by a firewall policy, and a firewall policy can be referenced by a firewall. If Network Firewall determines that the resource is being referenced, it warns you. Network Firewall is almost always able to determine whether a resource is being referenced. However, in rare cases, it might not be able to do so. If you need to be sure that the resource that you want to delete isn't in use, check all of your firewalls or firewall policies before deleting it. Note that policies that have associations can't be deleted.

**To delete a rule group for a Next Generation policy**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.

1. In the **Network Firewall rule groups** page, select the name of the rule group that you want to delete, and then choose **Delete**.

To delete a rule group with the AWS CLI, use `delete-rule-group` with the matching `--type`. A firewall or IPS rule group that's still referenced by a policy can't be deleted—remove the reference first.

**How Network Firewall propagates your changes**  
When you make any changes to a firewall, including changes to any of the firewall's components, like rule groups, TLS inspection configurations, and firewall policies, Network Firewall propagates the changes everywhere that the firewall is used. Your changes are normally applied within minutes, but there might be a brief period of inconsistency when the changes have arrived in some places and not in others. For example, if you modify a rule group so that it drops an additional type of packet, for a firewall that uses the rule group, the new packet type might briefly be dropped by one firewall endpoint while still being allowed by another. 

This temporary inconsistency can occur when you first create a firewall and when you make changes to an existing firewall. Generally, any inconsistencies of this type last only a few seconds. 

Changes to firewall engine rules and IPS engine rules are applied only to new traffic flows. Traffic flows that are already established keep the verdict that they were given. Other firewall changes are applied to all network packets. 

Adding, removing, or changing rules doesn't interrupt established traffic flows. Changing a policy's firewall default action or policy mode, or associating a firewall with a policy of the other type (a classic firewall policy instead of a Next Generation policy, or the reverse), restarts stateful inspection for the firewall. This interrupts the firewall's established traffic flows, and open connections can be reset.