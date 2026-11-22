

# Getting started with a Next Generation policy

This tutorial walks you through creating a firewall that uses a Next Generation policy, using the AWS Management Console. A Next Generation policy has two engines: a *firewall engine* for access control, which is drop by default, and an *IPS engine* for threat detection, which is pass by default. You create a firewall rule group and an IPS rule group, combine them in a Next Generation policy, create a firewall, and route your VPC traffic through the firewall endpoint. For a tutorial that uses a Classic policy instead, see [Getting started with a Classic AWS Network Firewall policy](getting-started-classic.md). For the differences between the two policy types, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).

This tutorial uses the same VPC prerequisites as described in [Before you begin](getting-started.md#getting-started-prerequisites).

**Tip**  
This tutorial creates the policy in monitor mode so that you can validate it against real traffic before it blocks anything. For the recommended monitor-to-enforce workflow, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md). For more detail on each policy setting, see [Next Generation policy settings in AWS Network Firewall](firewall-policy-v2-settings.md).

**Note**  
Following this tutorial creates Network Firewall resources in your account—a firewall, a firewall policy, and rule groups—that incur charges for as long as they exist. To avoid ongoing charges, complete the final step, [Step 5: Remove the firewall and clean up your resources](#getting-started-v2-clean-up), when you finish the tutorial. That step removes the resources that you create here.

**Topics**
+ [Step 1: Create rule groups](#getting-started-v2-rule-groups)
+ [Step 2: Create a firewall policy](#getting-started-v2-policy)
+ [Step 3: Create a firewall](#getting-started-v2-firewall)
+ [Step 4: Update your Amazon VPC route tables](#getting-started-v2-route-tables)
+ [Step 5: Remove the firewall and clean up your resources](#getting-started-v2-clean-up)

## Step 1: Create rule groups
<a name="getting-started-v2-rule-groups"></a>

In this step, you create two rule groups: a firewall rule group that allows outbound TLS traffic to a specific domain, and an IPS rule group that drops a known-bad host. For more information about the two kinds of rule group, see [Working with firewall rule groups in AWS Network Firewall](firewall-rule-groups.md) and [Working with IPS rule groups in AWS Network Firewall](ips-rule-groups.md). For the full create procedure and all authoring formats, see [Creating a rule group for a Next Generation policy](rule-groups-v2-creating.md).

**To describe and configure the rule group**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.

1. Choose **Create**.

1. On the **Describe rule group** page, enter a **Name** to identify the rule group, then choose **Next**. You can't change the name after you create the rule group.

1. On the **Choose rule group type** page, for **Rule group version**, leave **Next Generation** selected (the default). For the rule group type, select **Firewall rule group**. For **Rule group format**, select **Text rule builder**, then choose **Next**.

1. On the **Rule group variables** page, choose **Next** to accept the defaults.

1. On the **Configure rules** page, under **Suricata compatible rule string**, copy and paste the following rules. These rules accept the TCP layer in both directions, then allow an outbound TLS connection only when its server name indication (SNI) is a subdomain of `example.com`. The firewall engine is drop by default, so TLS traffic to any other domain isn't accepted.

   ```
   accept:hook tcp:all $HOME_NET any -> $EXTERNAL_NET any (tcp.session:setup,established; app-layer-protocol:unknown|tls; sid:1;)
   accept:hook tcp:all $EXTERNAL_NET any -> $HOME_NET any (tcp.session:setup,established; app-layer-protocol:unknown|tls; sid:2;)
   accept:flow tls:<client_hello $HOME_NET any -> $EXTERNAL_NET any (tls.sni; dotprefix; content:".example.com"; endswith; nocase; sid:3;)
   ```

Next, set the rule group's capacity and create it.

**To set capacity and create the rule group**

1. On the **Configure rules** page, under **Capacity sizing**, select how to set the rule group's capacity. The console shows the number of rules you've configured and the minimum capacity they require, with the following options:
   + **Allow room to grow** (recommended) – Sets the capacity to double the minimum, and at least 100, so that you can add rules later without re-creating the rule group.
   + **Match current rules** – Sets only enough capacity for the rules you've configured. You can't add rules later.
   + **Custom capacity** – Accepts a capacity value that you enter, from 1 to 30,000.

   For this tutorial, leave **Allow room to grow** selected. You can't change the capacity after you create the rule group.

1. Choose **Next**, review the rule group on the **Review and create** page, then choose **Create**.

Your firewall rule group is added to the list in the **Rule groups** page.

**Note**  
IPS protection is primarily provided by AWS and partner managed rule groups. You create your own IPS rule group only when you want to add custom rules. For more information about managed rule groups, see [Managed rule groups in AWS Network Firewall](nwfw-managed-rule-groups.md).

**To create an IPS rule group**

1. From the **Rule groups** page, choose **Create**.

1. On the **Describe rule group** page, enter a **Name** to identify the rule group, then choose **Next**.

1. On the **Choose rule group type** page, for **Rule group version**, leave **Next Generation** selected. For the rule group type, select **IPS rule group**. The **Rule group format** for an IPS rule group is **Text rule builder**. Choose **Next**.

1. On the **Rule group variables** page, choose **Next** to accept the defaults.

1. On the **Configure rules** page, under **Suricata compatible rule string**, copy and paste the following rule. An IPS rule group uses the same Suricata-compatible syntax as a Classic Network Firewall stateful rule group. This rule drops TLS connections whose SNI is `evil.example.com`. The firewall engine admits this connection because its SNI is a subdomain of `example.com`, so the connection advances to the IPS engine for inspection. Because the SNI is visible in the TLS handshake, the rule works without TLS inspection.

   ```
   drop tls $HOME_NET any -> $EXTERNAL_NET any (msg:"block evil host"; tls.sni; content:"evil.example.com"; startswith; endswith; nocase; sid:2001; rev:1;)
   ```

1. On the same page, under **Capacity sizing**, leave **Allow room to grow** selected (the recommended option). The capacity options are the same as for the firewall rule group (see the previous procedure), except that the **Custom capacity** maximum for an IPS rule group is 30,000.

1. Choose **Next**, review the rule group, then choose **Create**.

Your firewall rule group and your IPS rule group are both listed in the **Rule groups** page. You can now use them in a Next Generation policy.

## Step 2: Create a firewall policy
<a name="getting-started-v2-policy"></a>

In this step, you create a Next Generation policy that uses the two rule groups from the previous step. You set the firewall default action to drop and create the policy in monitor mode, so that the policy evaluates traffic and writes logs without blocking anything while you validate it. For the full create procedure and all policy settings, see [Creating a Next Generation policy in AWS Network Firewall](firewall-policy-v2-creating.md).

**To create the firewall policy**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

   In the navigation pane, under **Network Firewall**, choose **Firewall policies**, and then choose **Create firewall policy**. On the **Firewall policy details** page, for **Policy version** leave **Next Generation** selected (the default), enter a **Name** for the policy (you can't change it later), leave **Enable Active Threat Defense** selected, set **Firewall default action** to **Drop** (so the firewall engine drops any traffic your rule group doesn't explicitly accept), set **Policy mode** to **Monitor** (so the policy evaluates traffic and writes logs without blocking while you validate it), and leave **Stream exception setting** at **Reject**. For a description of each setting, see [Next Generation policy settings in AWS Network Firewall](firewall-policy-v2-settings.md). Then choose **Next**.

1. On the **Traffic inspection** page, all settings are optional. This page is where you can turn on **Route 53 Resolved IP validation**, attach a **TLS inspection** configuration, and customize the TCP idle timeout. For this tutorial, leave these unset and choose **Next**. For more information about these settings, see [Next Generation policy settings in AWS Network Firewall](firewall-policy-v2-settings.md).

1. On the **Add firewall rule groups** page, choose **Add rule group**, then choose **Add existing rule group**. Select the firewall rule group that you created in the previous step, assign it a priority, and then choose **Next**.

1. On the **Add IPS rule groups** page, choose **Add rule group**, then choose **Add existing rule group**. Select the IPS rule group that you created, then choose **Next**.

1. On the **Network and encryption** page, the customer managed key and policy variables settings are optional. For this tutorial, choose **Next** to accept the defaults.

1. On the **Review and create** page, review the policy, then choose **Create firewall policy**. You can choose **Edit** for any section to return to the corresponding page.

Your new firewall policy is added to the list in the **Firewall policies** page. You can now use it in your firewall.

## Step 3: Create a firewall
<a name="getting-started-v2-firewall"></a>

Firewalls associate the traffic filtering behavior of a firewall policy with the primary VPC where you want to filter traffic. In this procedure, you create a firewall using the firewall policy that you created in the previous step. For information about firewalls, see [Firewalls and firewall endpoints in AWS Network Firewall](firewalls.md).

**Note**  
Creating a firewall and its firewall endpoints starts incurring AWS Network Firewall charges, and those charges continue until you remove the resources in [Step 5: Remove the firewall and clean up your resources](#getting-started-v2-clean-up). Complete the cleanup step when you finish the tutorial to avoid ongoing charges.

**To create the firewall**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

   In the navigation pane, under **Network Firewall**, choose **Firewalls**, and then choose **Create firewall**.

1. On the **Describe firewall** page, for **Name**, enter the name that you want to use to identify this firewall, and optionally enter a description. You can't change the name after you create the firewall. Choose **Next**.

1. On the **Firewall capability** page, for **Firewall capability**, choose **routed firewall**.

1. On the **Attachment type** page, under **Attachment Details**, select **VPC**, select your VPC, and then select the **Availability Zone**, **Subnet**, and **IP address type** for the firewall subnet that you identified in [Before you begin](getting-started.md#getting-started-prerequisites). Choose **Next**.

1. On the **Configure advanced settings** page, the settings are optional—they include change protection, traffic analysis mode, a customer managed key, logging configuration (alert, flow, and TLS logs), and the firewall monitoring dashboard. Because this tutorial creates the policy in monitor mode, turn on logging now so that you can review what the firewall would do before you route traffic through it. Under the logging configuration, turn on **Alert** logging and select a log destination, such as CloudWatch Logs or Amazon S3. Optionally, also turn on **Flow** logging. Then choose **Next**.
**Note**  
If you accept the defaults on this page, logging stays off and the firewall writes no alert logs. In that case, you can't review the monitor-mode results to validate the policy before you switch it to enforce mode. Turn on alert logging here, before you route traffic through the firewall in [Step 4: Update your Amazon VPC route tables](#getting-started-v2-route-tables). For more information about configuring firewall logging, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).

1. On the **Associate firewall policy** page, select **Associate an existing firewall policy**, select the firewall policy that you created in the previous step, then choose **Next**.

1. (Optional) On the **Add tags** page, add any tags that you want, then choose **Next**.

1. On the **Review and create** page, review your configuration, then choose **Create firewall**.

Your new firewall is listed in the **Firewalls** page. You've configured the firewall's behavior with the firewall policy and rule groups, and your firewall has an endpoint that's running in your VPC, ready to filter network traffic.

**Note**  
Network Firewall supports up to 100 Gbps of network traffic per firewall endpoint. If you require more traffic bandwidth, you can split your resources into subnets and create a Network Firewall in each subnet.

The next step is to route the VPC's network traffic through the firewall endpoint. You insert it into the traffic flow between the internet gateway and your customer subnet.

## Step 4: Update your Amazon VPC route tables
<a name="getting-started-v2-route-tables"></a>

After you create your firewall, you insert its firewall endpoint into your Amazon Virtual Private Cloud network traffic flow, in between your internet gateway and your customer subnet. You create routing for the firewall endpoint so that it forwards traffic between the internet gateway and your subnet. Then, you update the route tables for your internet gateway and your subnet, to send traffic to the firewall endpoint instead of to each other.

This procedure covers the high-level steps for route table management. For information about managing route tables for your VPC, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon Virtual Private Cloud User Guide*.

**To modify your route tables to insert a firewall endpoint between your internet gateway and your subnet**

1. Review your routing for the internet gateway and for your customer subnet, to determine the components used to route traffic between the two.

   Record the current settings. You use them to reverse your changes at the end of the tutorial.
   + The internet gateway's route table typically has an entry with a destination set to your customer subnet's CIDR block and a target of `local`.
   + The subnet's route table typically has an entry with a destination set to `0.0.0.0/0` and a target set to the internet gateway ID.

1. Create a route table configuration for the firewall endpoint with the following two routes:
   + An entry that matches the internet gateway's route specification for traffic going to the customer subnet's CIDR block.
   + An entry that matches the subnet's route specification for traffic going to the internet gateway.

   The firewall endpoint is now ready to filter and forward traffic between the internet gateway and the customer subnet. The endpoint only forwards traffic to its intended destination if it passes the inspection criteria that you defined in the rule groups and firewall policy.

1. Update the internet gateway's routing to modify the entry with a destination set to your customer subnet's CIDR block. Change the target to the firewall endpoint ID.

1. Update the customer subnet routing to modify the entry with a destination set to the internet gateway ID. Change the target to the firewall endpoint ID.

The firewall endpoint is now filtering all traffic between your internet gateway and customer subnet. Because the policy is in monitor mode, the firewall writes logs for the actions it would apply but doesn't block traffic yet. When you've confirmed that the policy allows the traffic you intend, change the policy mode to **Enforce** to begin blocking. For the full validation workflow, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md).

To verify the tutorial rules while the policy is in monitor mode, generate traffic from an instance in your customer subnet and review the alert logs you turned on in [Step 3: Create a firewall](#getting-started-v2-firewall):
+ Run `curl https://www.example.com`. The connection succeeds. In the alert logs, an entry with a `sid` of `3` and an `engine` field value of `fw` shows that the firewall engine accepted it. The IPS rule doesn't match this connection, so it advances to its destination.
+ Run `curl -k --connect-to evil.example.com:443:www.example.com:443 https://evil.example.com`. This sends a TLS handshake with the SNI `evil.example.com` to a reachable server, so the result of the `curl` command itself doesn't matter—the handshake is what the rule matches. The firewall engine admits the connection because the SNI is a subdomain of `example.com`, so the connection advances to the IPS engine. Because the policy is in monitor mode, the IPS rule is applied as an alert and doesn't block the connection. In the alert logs, look for an entry with the rule's `sid` of `2001`, an `engine` field value of `td` (the IPS engine), and an `action` of `allowed`. After you switch the policy to enforce mode, the IPS engine drops this connection and the entry shows an `action` of `blocked`. For more information about the `engine` field, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).

## Step 5: Remove the firewall and clean up your resources
<a name="getting-started-v2-clean-up"></a>

You've now successfully completed the tutorial. To remove the firewall endpoint from your VPC and prevent your account from accruing AWS Network Firewall charges for the tutorial resources, revert your route table changes and clean up the Network Firewall resources that you created.

**To modify your route tables to remove the firewall**

1. Return the internet gateway and subnet route tables to the configurations they had at the start of the prior procedure. This stops traffic from routing to the firewall endpoint.

1. Remove the route table configuration for the firewall endpoint.

**Important**  
The following steps permanently delete the firewall, firewall policy, and rule groups that you created for this tutorial. Make sure that you no longer need these resources before you continue, because Network Firewall can't recover them after you delete them.

**To remove the Network Firewall resources**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. In the **Firewalls** page, select the firewall that you created for the tutorial.

1. Choose **Actions**, then choose **Delete**, and confirm your request.

1. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.

1. In the **Firewall policies** page, select the firewall policy that you created for the tutorial.

1. Choose **Delete**, and confirm your request.

1. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.

1. In the **Rule group** page, select the rule groups that you created for the tutorial, and then choose **Delete**.

You've successfully removed the firewall from your VPC traffic flow and removed all of the Network Firewall resources that you created for this tutorial.