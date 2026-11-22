

# Updating a Next Generation policy in AWS Network Firewall

You can change your policy's settings after you create it, with the following constraints:
+ You can't change the name of the firewall policy.
+ You can't change a Classic Network Firewall policy into a Next Generation policy, or the reverse. The policy type is fixed when you create the policy.
+ You can change the policy mode, the firewall default action, the rules in both sections, and the other policy settings.

**Warning**  
Changing the policy mode or the rules in a policy that's in use affects the traffic that the firewall allows and blocks. Review your changes before you save them.

In the console, the **Firewall policies** page lists all of your firewall policies with the following columns: **Name**, **Policy version** (**Next Generation** or **Classic**), **Policy mode** (**Enforce** or **Monitor** for Next Generation policies, and **-** for Classic policies), **Firewall default action** (**Accept**, **Drop**, **Alert**, or **Reject** for Next Generation policies, and **-** for Classic policies), and **Stateful rule evaluation order** (**Action order** or **Strict order** for Classic policies, and **-** for Next Generation policies).

When you choose the name of a Next Generation policy, the policy's page opens with four tabs. You can review the policy on these tabs and make changes from them. To delete the policy, choose **Delete** at the top of the page and confirm your request.

**Details**  
Shows the policy's resource details (name, Region, description, account ID, ARN, and status), advanced settings (`HOME_NET`, TCP idle timeout, and encryption); a monitor-mode warning when the policy is in monitor mode; and policy behavior (policy mode, firewall default action, and the stream exception setting, which this page labels **inspection failure behavior**). It also shows the evaluation stages, split into a firewall stage and an IPS stage, each with the action taken on no match; the consumed capacity for firewall rule groups, IPS rule groups, and IPS domain lists, against each limit; the deployment impact (the firewalls that use the policy, and when the policy was last updated); and any tags. You can choose **Edit** on the **Resource details**, **Advanced settings**, or **Policy behavior** sections to change those values, and choose **Manage tags** to change the policy's tags.

**Traffic inspection**  
Shows the **Route 53 Resolved IP validation** section (status, DNS firewall rule group, source IP ranges, action, DNS expiry exception policy, and bypass destination validation IP ranges) and the **TLS inspection configuration** section. Choose **Edit** on the **Route 53 Resolved IP validation** section to update the Route 53 Resolved IP validation settings, or manage the attached TLS inspection configuration from the **TLS inspection configuration** section. For more information about TLS inspection in a Next Generation policy, see [TLS inspection with a Next Generation policy in AWS Network Firewall](tls-inspection-policy-v2.md).

**Firewall rules**  
Shows the policy's firewall rule groups in a table with the columns **Priority**, **Name**, **Protocol**, **Connection state**, **Source**, **Source port**, **Destination**, **Destination port**, **Action**, **Keyword**, and **Actions**. Choose **Edit** to change the firewall section, then choose **Add rule group** and one of the following:  
+ **Add existing rule group** – Select a firewall rule group that you've already created, and assign it a priority. The priority sets the rule group's evaluation order within the policy.
+ **Add embedded rules** – Author rules directly in the policy. In the panel that opens, enter a priority and choose **Visual rule builder** or **Text rule builder**, and add rules in the **Firewall rules** section. Choosing **Add rule** opens the same visual rule builder as the firewall rule group creation flow. For more information, see [Creating a rule group for a Next Generation policy](rule-groups-v2-creating.md).

**IPS rules and packages**  
Shows the policy's IPS rule groups in a table with the columns **Name**, **Description**, **Signature**, and **Override action** (the action that a rule group override applies—for example, overriding a rule group to **Alert** so that its rules only generate alerts instead of dropping or rejecting traffic). IPS rule groups don't have a priority. The IPS engine evaluates all of its rules in the default action order (pass, then drop, then reject, then alert), regardless of the order of the rule groups. You can still change the order in which the rule groups are loaded: choose **Edit** to change the IPS section, and on the edit page, reorder a rule group with the up and down arrows next to it. Choose a rule group to view its rule details. Choose **Add rule group** and one of the following:  
+ **Add existing rule group** – Select an IPS rule group that you've already created.
+ **Add embedded rules** – Author rules directly in the policy. In the panel that opens, you can optionally define rule group variables, and you enter your rules in the text box as a Suricata-compatible rule string. IPS rules have no structured authoring form.
+ **Add managed rule group** – Choose from the available AWS managed rule groups. For more information, see [Using managed rule groups](nwfw-managed-rule-groups.md).

**To update a Next Generation policy**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.

1. In the **Firewall policies** page, choose the name of the Next Generation policy that you want to update.

1. On the policy's page, go to the tab for what you want to change—**Details**, **Traffic inspection**, **Firewall rules**, or **IPS rules and packages**—and choose **Edit** for the section you want to change. You can change the policy mode, the firewall default action, the firewall section and IPS section rule groups, and the other policy settings, within the constraints listed earlier.

1. Choose **Save** to save your changes.

To update the policy with the AWS CLI, use `update-firewall-policy-v2` and provide a current `UpdateToken` from a preceding create or describe call. The token changes with every update. The following example changes the policy to monitor mode with an accept default action, using an updated `policy.json`:

```sh
aws network-firewall update-firewall-policy-v2 \
--firewall-policy-v2-name example-policy \
--update-token 3e965e1d-2b9f-40c2-a218-5aabe88b4b2e \
--firewall-policy-v2 file://policy.json \
--region us-west-2
```

**How Network Firewall propagates your changes**  
When you make any changes to a firewall, including changes to any of the firewall's components, like rule groups, TLS inspection configurations, and firewall policies, Network Firewall propagates the changes everywhere that the firewall is used. Your changes are normally applied within minutes, but there might be a brief period of inconsistency when the changes have arrived in some places and not in others. For example, if you modify a rule group so that it drops an additional type of packet, for a firewall that uses the rule group, the new packet type might briefly be dropped by one firewall endpoint while still being allowed by another. 

This temporary inconsistency can occur when you first create a firewall and when you make changes to an existing firewall. Generally, any inconsistencies of this type last only a few seconds. 

When you add a TLS inspection configuration to an existing firewall, Network Firewall interrupts traffic flows that match the criteria defined by the TLS inspection configuration scope configuration. Network Firewall will begin SSL/TLS decryption and inspection for new connections to the firewall.

Changes to firewall engine rules and IPS engine rules are applied only to new traffic flows. Traffic flows that are already established keep the verdict that they were given. Other firewall changes are applied to all network packets. 

Adding, removing, or changing rules doesn't interrupt established traffic flows. Changing a policy's firewall default action or policy mode, or associating a firewall with a policy of the other type (a classic firewall policy instead of a Next Generation policy, or the reverse), restarts stateful inspection for the firewall. This interrupts the firewall's established traffic flows, and open connections can be reset.