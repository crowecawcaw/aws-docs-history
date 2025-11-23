# Updating a resource group in AWS Network Firewall

You can change your resource group settings in the Network Firewall console or the AWS Resource Groups [UpdateGroup](../../../ARG/latest/APIReference/API_UpdateGroup.md "../../../ARG/latest/APIReference/API_UpdateGroup.md") API. To change your resource group settings in the Network Firewall console, use the following procedure:

###### To update a resource group

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Network Firewall resource groups**.
3. In the **Resource group** page, select the name of the resource group you want to update.
4. Make your changes. You can't change the name of a resource group after creation, but you can change other details and you can change
   the rule groups.
5. Choose **Save** to save your changes.

###### How Network Firewall propagates your changes

When you make any changes to a firewall, including changes to any of the firewall's components, like rule groups, TLS inspection configurations, and firewall policies, Network Firewall propagates the changes everywhere that the firewall is used. Your changes are normally applied within minutes, but there might be a brief period of inconsistency when the changes have arrived in some places and not in others. For example, if you modify a rule group so that it drops an additional type of packet, for a firewall that uses the rule group, the new packet type might briefly be dropped by one firewall endpoint while still being allowed by another.

This temporary inconsistency can occur when you first create a firewall and when you make changes to an existing firewall. Generally, any inconsistencies of this type last only a few seconds.

When you add a TLS inspection configuration to an existing firewall, Network Firewall interrupts traffic flows that match the criteria defined by the TLS inspection configuration scope configuration. Network Firewall will begin SSL/TLS decryption and inspection for new connections to the firewall.

Changes to stateful rules are applied only to new traffic flows. Other firewall changes, including changes to stateless rules, are applied to all network packets.
