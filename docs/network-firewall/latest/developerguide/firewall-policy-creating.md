# Creating a firewall policy in AWS Network Firewall

To create a firewall policy in Network Firewall, you need rule groups that you've already defined to
use in the policy. You can create new rule groups and reuse existing ones. For
information about creating and managing rule groups, see [Managing your own rule groups in AWS Network Firewall](rule-groups.md "rule-groups.md").

If you want to use TLS inspection, you need to first create a TLS inspection configuration to use in the policy. For information about working with TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md "tls-inspection-configurations.md").

###### To create a firewall policy

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.
3. Choose **Create firewall policy**.
4. Enter a **Name** to identify this firewall policy.

###### Note

You can't change the name after you create the firewall policy. 5. (Optional) Enter a **Description** for the policy to help you identify if among your other resources. 6. **Enable Active Threat Defense - optional** gives you visibility into threat activity and indicator groups, types, and threat names you are protected against. You can add the appropriate Active Threat Defense rule groups to your firewall policy to block these threats. See the [AWS active threat defense for AWS Network Firewall](aws-managed-rule-groups-atd.md "aws-managed-rule-groups-atd.md") for more details. 7. For **Stream exception policy**, choose how Network Firewall handles traffic when a network connection breaks midstream. Network connections can break due to disruptions in external networks or within the firewall itself. Choose from the following options:

    * **Drop** - Network Firewall fails closed and drops all subsequent traffic going to the firewall. This is the default behavior.
    * **Continue** - Network Firewall continues to apply rules to the subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on this context. For example, if you have a stateful rule to drop httptraffic, Network Firewall won't match the traffic for this rule because the service won't have the context from session initialization defining the application layer protocol as HTTP. However, this behavior is rule dependent—a TCP-layer rule using a `flow:stateless` rule would still match, as would the `aws:drop_strict` default action.
    * **Reject** - Network Firewall fails closed and drops all subsequent traffic going to the firewall. Network Firewall also sends a TCP reject packet back to your client so that the client can immediately establish a new session. Network Firewall will have context about the new session and will apply rules to the subsequent traffic.

8.  Choose **Next** to go to the firewall policy's **Add rule
    groups** page.
9.  To choose the actions to take on packets that don't match any stateless
    rules, in the **Stateless default actions** section, first choose
    how to treat fragmented packets. You can choose **Use the same actions
    for all packets** or **Use different actions for full packets
    and fragmented packets**. You can then choose **Pass**,
    **Drop**, or **Forward to stateful rule groups**
    for all packets, or choose individually for full and fragmented packets. You also
    have the option to enable a custom action that lets you publish custom Amazon CloudWatch metrics
    to monitor the usage of stateless rules in your rule group.
10. To choose the way that your stateful rules are ordered for evaluation, and the
    actions to take on packets that don't match any stateful rules, in the
    **Stateful rule evaluation order and default action** section, first choose
    a rule evaluation order:

        * Choose **Strict order** (recommended) to provide your rules in the order that you want them
         to be evaluated. You can then choose one or more default actions for packets that don't match any rules.
        * Choose **Action order** to have the stateful rules engine determine the evaluation order of your rules. The default action for this rule order is **Pass**, followed by **Drop**, **Reject**, and **Alert** actions. This option was previously named **Default** order.

    For more information about stateful default actions for rule groups, see
    [Action order](suricata-rule-evaluation-order.md#suricata-default-rule-evaluation-order "suricata-rule-evaluation-order.md#suricata-default-rule-evaluation-order").

11. To add stateless rule groups, in the **Stateless rule
    groups** section, choose **Add rule groups**,
    then select the check boxes for the rule groups that you want to add and
    choose **Add rule groups**.
12. If your firewall policy has multiple stateless rule groups, in the **Stateless
    rule group** section, update the processing order as needed.
    Network Firewall processes stateless rule groups by order of priority, starting
    from the lowest. To move a rule group in the list, select the check box next
    to its name and then move it up or down. For more information, see [How AWS Network Firewall filters network traffic](firewall-policy-processing.md "firewall-policy-processing.md").
13. Choose the stateless default actions for the firewall policy to take if a full packet or
    UDP packet fragment doesn't match any of the stateless rule groups.
    Network Firewall silently drops packet fragments for other protocols.
    For information about the action options, see [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").

Network Firewall doesn't automatically forward packets to stateful rule groups. It forwards
only for the following situations:

    * The packet matches a stateless rule whose action specifies forward to stateful rule
     groups.
    * The packet doesn't match any stateless rule and the applicable default action setting
     specifies forward to stateful rule groups.

14. To add stateful rule groups, in the **Stateful rule
    groups** section, choose **Add rule groups**,
    then select the check boxes for the rule groups that you want to add and
    choose **Add rule groups**.
15. Choose **Next**.
16. On the **Configure advanced settings** page, optionally customize encryption and policy variables, and set the stream exception policy.
17. (Optional) Under **Customer managed key**, toggle the **Customize encryption settings** option to use a AWS Key Management Service customer managed key to encrypt your resources. For more information about this option, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md "kms-encryption-at-rest.md").
18. (Optional) For **Policy variables** enter one or more IPv4 or IPv6 addresses in CIDR notation to override the default value of Suricata `HOME_NET`. If your firewall is deployed using a centralized deployment model, you might want to override `HOME_NET` with the CIDRs of your home network. Otherwise, Network Firewall uses the CIDR of your inspection VPC.
19. Choose **Next**.
20. (Optional) Under **Idle Timeouts**, toggle the **Customize TCP idle timeout settings** option. This lets you define the number of seconds a TCP connection can remain idle
    before Network Firewall drops the traffic. For information about the idle timeout setting, see [Firewall policy settings in AWS Network Firewall](firewall-policy-settings.md "firewall-policy-settings.md").
21. (Optional) On the **Add TLS inspection configuration** page, choose **Add TLS inspection configuration** to turn on decryption and re-encryption of incoming SSL/TLS traffic for the firewalls associated with this policy. You can't add or remove a TLS inspection configuration after firewall policy creation. For information about TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md "tls-inspection-configurations.md").
22. Choose **Next**.
23. (Optional) On the **Add tags** page, enter a key and optional value for any
    tag that you want added to this firewall policy. Tags help you organize and
    manage your AWS resources. For more information about tagging your
    resources, see [Tagging AWS Network Firewall resources](tagging.md "tagging.md").
24. Choose **Next**.
25. In the **Review and create** page, check over your firewall policy
    settings. If you want to change any section, choose
    **Edit** for the section. This returns you to the page
    in the firewall policy wizard. Make your changes, then choose
    **Next** on each page until you come back to the review
    and create page.
26. Choose **Create firewall policy**.
    Your new firewall policy is added to the list in the **Firewall policies**
    page.
