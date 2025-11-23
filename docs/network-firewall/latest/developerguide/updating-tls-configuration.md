# Updating a TLS inspection configuration in Network Firewall

To change your TLS inspection configuration settings, use the following procedure:

###### To update a TLS inspection configuration

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **TLS inspection configurations**.
3. In the **TLS inspection configuration** page, select the name of the TLS inspection configuration that you
   want to update.
4. On the TLS inspection configuration page, make your changes. You can't update the name of a TLS inspection configuration
   after creation, but you can change other details. If you want to update the
   name, you must create a new TLS inspection configuration.
5. Choose **Save** to save your changes.

###### How Network Firewall propagates your changes

When you make any changes to a firewall, including changes to any of the firewall's components, like rule groups, TLS inspection configurations, and firewall policies, Network Firewall propagates the changes everywhere that the firewall is used. Your changes are normally applied within minutes, but there might be a brief period of inconsistency when the changes have arrived in some places and not in others. For example, if you modify a rule group so that it drops an additional type of packet, for a firewall that uses the rule group, the new packet type might briefly be dropped by one firewall endpoint while still being allowed by another.

This temporary inconsistency can occur when you first create a firewall and when you make changes to an existing firewall. Generally, any inconsistencies of this type last only a few seconds.
