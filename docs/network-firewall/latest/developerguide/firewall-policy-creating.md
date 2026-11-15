

# Creating a firewall policy in AWS Network Firewall
<a name="firewall-policy-creating"></a>

To create a firewall policy in Network Firewall, you need rule groups that you've already defined to use in the policy. You can create new rule groups and reuse existing ones. For information about creating and managing rule groups, see [Managing your own rule groups in AWS Network Firewall](rule-groups.md). 

If you want to use TLS inspection, you need to first create a TLS inspection configuration to use in the policy. For information about working with TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md).

**To create a firewall policy**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.

1. Choose **Create firewall policy**.

1. On the **Firewall policy details** page, provide the following information:

   1. For **Policy version**, select **Classic**. The **Next Generation** version is recommended and selected by default; to create a Next Generation policy instead, see [Creating a Next Generation policy in AWS Network Firewall](firewall-policy-v2-creating.md). If you change the version after entering settings, the console prompts you to confirm and clears the version-specific settings.

   1. Enter a **Name** to identify this firewall policy.
**Note**  
You can't change the name after you create the firewall policy.

   1. (Optional) Enter a **Description** for the policy to help you identify it among your other resources.

   1. **Enable Active Threat Defense** gives you visibility into threat activity and indicator groups, types, and threat names you are protected against. You can add the appropriate Active Threat Defense rule groups to your firewall policy to block these threats. See the [AWS active threat defense for AWS Network Firewall](aws-managed-rule-groups-atd.md) for more details.

   1. For **Stream exception policy**, select how Network Firewall handles traffic when a network connection breaks midstream. Network connections can break due to disruptions in external networks or within the firewall itself. Select from the following options:
      + **Reject** – Network Firewall fails closed and drops all subsequent traffic going to the firewall. Network Firewall also sends a TCP reject packet back to your client so that the client can immediately establish a new session. Network Firewall has context about the new session and applies rules to the subsequent traffic. The console pre-selects this option.
      + **Drop** – Network Firewall fails closed and drops all subsequent traffic going to the firewall.
      + **Continue** – Network Firewall continues to apply rules to the subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on this context. For example, if you have a stateful rule to drop HTTP traffic, Network Firewall won't match the traffic for this rule because the service won't have the context from session initialization defining the application layer protocol as HTTP. However, this behavior is rule dependent—a TCP-layer rule using a `flow:stateless` rule would still match, as would the `aws:drop_strict` default action.

   1. (Optional) Under **Tags**, enter a key and optional value for any tag that you want added to this firewall policy. Tags help you organize and manage your AWS resources. For more information about tagging your resources, see [Tagging AWS Network Firewall resources](tagging.md).

1. Choose **Next**.

1. (Optional) On the **Traffic inspection** page, configure the following settings:

   1. (Optional) Under **Route 53 Resolved IP validation**, select **Enable Route 53 Resolved IP validation** to validate destination IP addresses against the IP addresses that Amazon Route 53 Resolver resolved. Then select an **Action** (**Reject**, **Drop**, or **Alert**), a **DNS Firewall rule group**, and a **DNS expiry exception policy** (**Reject**, **Drop**, or **Continue**). Optionally, enter **Source IP ranges** and **Bypass destination validation IP ranges**.

   1. Under **TLS inspection configurations**, choose **Add TLS inspection configuration** to turn on decryption and re-encryption of incoming SSL/TLS traffic for the firewalls associated with this policy. You can't add or remove a TLS inspection configuration after firewall policy creation. For information about TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md).

   1. (Optional) Under **Idle timeouts**, toggle the **Customize TCP idle timeout settings** option. Use this option to define the number of seconds a TCP connection can remain idle before Network Firewall drops the traffic. For information about the idle timeout setting, see [Firewall policy settings in AWS Network Firewall](firewall-policy-settings.md).

1. Choose **Next**.

1. (Optional) On the **Add rule groups** page, add rule groups to your firewall policy:

   1. In the **Stateful rule evaluation order and default actions** section, for the rule evaluation order, select one of the following:
      + Select **Strict order** (recommended) to provide your rules in the order that you want them to be evaluated. You can then select one or more default actions for packets that don't match any rules.
      + Select **Action order** to have the stateful rules engine determine the evaluation order of your rules. The default action for this rule order is **Pass**, followed by **Drop**, **Reject**, and **Alert** actions. This option was previously named **Default** order.

      You can't change the rule evaluation order after you add a stateful rule group to the policy. For more information about stateful default actions, see [Action order](suricata-rule-evaluation-order.md#suricata-default-rule-evaluation-order).

   1. To add stateful rule groups, in the **Stateful rule group** section, choose **Add stateful rule groups**, select the check boxes for the rule groups that you want to add, and then choose **Add rule groups**. If you use strict order, select a rule group and choose **Move up** or **Move down** to set its evaluation priority.

   1. In the **Stateless default actions** section, under **Fragmented packets**, select **Use the same actions for all packets** or **Use different actions for full packets and fragmented packets**. Then, for **Rule action**, select **Forward to stateful rule groups**, **Pass**, or **Drop**. Optionally, under **Publish metrics**, select **Enable** and enter an action name and dimension value to publish custom Amazon CloudWatch metrics.

   1. To add stateless rule groups, in the **Stateless rule group** section, choose **Add stateless rule groups**, select the check boxes for the rule groups that you want to add, and then choose **Add rule groups**. Network Firewall processes stateless rule groups by order of priority, starting from the lowest; to reorder, select a rule group and move it up or down. For more information, see [How AWS Network Firewall filters network traffic](firewall-policy-processing.md).

1. Choose **Next**.

1. (Optional) On the **Network and encryption** page, configure the following settings:

   1. For **Policy variables**, enter one or more IPv4 or IPv6 addresses in CIDR notation to override the default value of Suricata `HOME_NET`. If your firewall is deployed using a centralized deployment model, you might want to override `HOME_NET` with the CIDRs of your home network. Otherwise, Network Firewall uses the CIDR of your inspection VPC.

   1. Under **Customer managed key**, toggle the **Customize encryption settings** option to use a AWS Key Management Service customer managed key to encrypt your resources. For more information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md).

1. Choose **Next**.

1. In the **Review and create** page, check over your firewall policy settings. If you want to change any section, choose **Edit** for the section. This returns you to the page in the firewall policy wizard. Make your changes, then choose **Next** on each page until you come back to the review and create page.

1. Choose **Create firewall policy**. 

Your new firewall policy is added to the list in the **Firewall policies** page.