

# Getting started with resolved IP validation
<a name="route53-resolved-ip-validation-getting-started"></a>

This topic walks you through enabling and enforcing resolved IP validation on an existing firewall, using the Amazon Route 53 Resolver DNS Firewall and Network Firewall consoles. To configure the feature programmatically instead, use the `Route53ResolvedIPValidation` setting in [UpdateFirewallPolicy](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateFirewallPolicy.html).

**Prerequisites**  
Before you begin, make sure that you have the following:
+ A firewall with an associated firewall policy.
+ VPCs behind the firewall that use the Amazon Route 53 Resolver for Domain Name System (DNS) resolution. Resolved IP validation can only validate against resolutions that the Route 53 Resolver recorded.
+ Flow logging enabled on the firewall, so that you can observe validation results before you enforce them. For more information about firewall logging, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).

You create and manage the DNS Firewall rule group in Amazon Route 53 Resolver DNS Firewall, not in Network Firewall. The rule group doesn't need any rules. Its purpose is to define which VPCs' resolutions are in scope for validation, so associate it only with the VPCs behind this firewall. For more information, see the scoping recommendation in [Recommendations for configuring resolved IP validation](route53-resolved-ip-validation-recommendations.md). For instructions on creating and managing DNS Firewall rule groups, see [Using DNS Firewall to filter outbound DNS traffic](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) in the *Amazon Route 53 Developer Guide*.

You turn on resolved IP validation in alert mode first, so that you can observe its effect before you enforce it. After you verify the results, you change the action to drop or reject connections that fail validation. Alert mode logs failed validations without blocking them.

First, create the DNS Firewall rule group and associate it with your VPCs:

**To create the DNS Firewall rule group and associate it with your VPCs**

1. Open the DNS Firewall rule groups page of the Amazon Virtual Private Cloud (Amazon VPC) console at [https://console.aws.amazon.com/vpcconsole/home#DNSFirewallRuleGroups:](https://console.aws.amazon.com/vpcconsole/home#DNSFirewallRuleGroups:).

1. On the navigation bar, choose the AWS Region where your firewall is deployed.

1. Choose **Add rule group**, enter a name for the rule group, and choose **Add rule group**.

1. Note the rule group ID (`rslvr-frg-<id>`) on the rule group's details page.

1. Choose the **Associated VPCs** tab, and then choose **Associate VPC**.

1. Select a VPC that sends traffic through your firewall, and then choose **Associate**. Repeat for each VPC behind the firewall. The association's **Status** shows **Updating** and then **Complete**. This can take a few minutes.

Next, enable resolved IP validation on the firewall policy. Start in alert mode so that you can see which connections would fail validation before any traffic is affected:

**To enable resolved IP validation in your firewall policy**

1. Open the firewall policies page of the Network Firewall console at [https://console.aws.amazon.com/vpcconsole/home#NetworkFirewallPolicies:](https://console.aws.amazon.com/vpcconsole/home#NetworkFirewallPolicies:), and then choose the name of the firewall policy that your firewall uses.

1. In the **Route 53 Resolved IP validation** section, choose **Edit**, and then turn on **Enable Route 53 Resolved IP validation**.

1. For **Action**, select **Alert**.

1. For **DNS expiry exception policy**, select **Continue**, **Drop**, or **Reject**. For more information about these settings, see [Configuring resolved IP validation on the firewall policy](route53-resolved-ip-validation-policy-setting.md).

1. For **DNS Firewall rule group**, select the rule group that you created in the previous procedure. If the rule group isn't listed yet, refresh the list.

1. (Optional) Narrow the scope of validation.

   1. For **Source IP ranges**, enter the client address ranges to validate, one per line. If you don't specify any ranges, validation applies to the firewall's VPC CIDR ranges.

   1. For **Bypass destination validation IP ranges**, enter any destination ranges to exempt from the check.

1. Choose **Save**. On the policy's details page, the **Route 53 Resolved IP validation** section now shows a **Status** of **Enabled**. If the firewall already uses this policy, the change deploys to it automatically.

After you enable resolved IP validation in alert mode, verify that it behaves as you expect before you enforce it. Resolved IP validation checks each connection's destination IP address against the resolutions that the Route 53 Resolver returned in your associated VPCs, so unexpected failures usually point to clients that resolve DNS elsewhere.

(Optional) Add resolved-domain rules to a stateful rule group in the policy. With these rules, you allow or deny specific domains based on how the Amazon Route 53 Resolver resolved their destination IP addresses. In a domain list rule group, select **DNS (Route 53 resolved domains)** as one of the protocols. For more information about resolved-domain rules, see [Matching specific domains with resolved-domain rules](route53-resolved-ip-validation-rules.md).

Allow about 24 hours for clients to refresh their DNS caches. During that time, watch the `route53_resolved_ip` log field in your firewall's flow logs and the `DnsUnresolvedFlows` and `DnsAzUnavailableFlows` metrics in CloudWatch. Investigate anything that fails validation unexpectedly. For more information about troubleshooting resolved IP validation, see [Monitoring and troubleshooting resolved IP validation](route53-resolved-ip-validation-troubleshooting.md).

When the rate of unresolved flows reaches a level that's acceptable for your environment, enforce validation:

**To enforce resolved IP validation**

1. Open the firewall policies page of the Network Firewall console at [https://console.aws.amazon.com/vpcconsole/home#NetworkFirewallPolicies:](https://console.aws.amazon.com/vpcconsole/home#NetworkFirewallPolicies:).

1. Choose the name of your firewall policy.

1. In the **Route 53 Resolved IP validation** section, choose **Edit**.

1. Set **Action** to **Drop** or **Reject**.

1. Choose **Save**.

After the change deploys, the firewall drops or resets connections whose destination IP address the Route 53 Resolver didn't resolve in an associated VPC. Connections to destinations in the bypass ranges, and connections from sources outside the configured source ranges, are not affected.