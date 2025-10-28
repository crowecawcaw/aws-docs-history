# Getting started with AWS Network Firewall

AWS Network Firewall provides network traffic filtering protection for your Amazon Virtual Private Cloud VPCs. This
tutorial provides steps for getting started with Network Firewall using the AWS Management Console. You can
also use Network Firewall API operations to create and manage your firewalls.
For
more information about working with Network Firewall API operations, see the
[AWS Network Firewall API Reference](../APIReference.md "../APIReference.md").

###### Topics

- [Before you begin](#getting-started-prerequisites "#getting-started-prerequisites")
- [Step 1: Create rule groups](#getting-started-add-rule-groups "#getting-started-add-rule-groups")
- [Step 2: Create a firewall
  policy](#getting-started-configure-firewall-policy "#getting-started-configure-firewall-policy")
- [Step 3: Create a firewall](#getting-started-create-firewall "#getting-started-create-firewall")
- [Step 4: Update your Amazon VPC route
  tables](#getting-started-update-route-tables "#getting-started-update-route-tables")
- [Step 5: Remove the firewall and clean up your
  resources](#getting-started-clean-up "#getting-started-clean-up")

## Before you begin

This tutorial walks you through configuring and implementing an AWS Network Firewall firewall
for a VPC with a basic internet gateway architecture, like the one depicted at [Simple single zone architecture with an internet gateway using AWS Network Firewall](arch-single-zone-igw.md "arch-single-zone-igw.md").

To follow this tutorial, you'll need a test VPC where you want to implement a network
firewall. Additionally, you must know how to manage the subnets and route tables in your
VPC.

- For information about managing subnets in your VPC, see
  [VPCs and subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md")
  in the _Amazon Virtual Private Cloud User Guide_.
- For information about managing route tables for your VPC, see
  [Route
  tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon Virtual Private Cloud User
  Guide_.

The test VPC that you use for this tutorial must have the following configuration in one
Region:

- An internet gateway.
- A customer subnet.
- Routing configured to send inbound traffic from the internet gateway to the subnet and to
  send the subnet's outbound traffic to the internet gateway.
- A second subnet to use as the firewall subnet. This subnet must not be used for other purposes
  and must have at least one available IP address. You'll select the Availability
  Zone and subnet ID when you create the firewall.

If you have a different architecture that you'd like to add a firewall to, you can adjust
the guidance in this tutorial accordingly. Network Firewall doesn't support some VPC
architectures. For information, see [AWS Network Firewall example architectures with routing](architectures.md "architectures.md").

## Step 1: Create rule groups

Rule groups are reusable collections of network filtering rules that you use to configure
firewall behavior. In this step, you create a stateless rule group and a stateful rule
group. For information about rule groups, see [Managing your rule groups](rule-groups.md "rule-groups.md").

###### To create a stateless rule group

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.
3. Choose **Create rule group**.
4. In the **Create rule group** page, for the **Rule
   group type**, choose **Stateless rule group**.
5. Enter the name that you want for the rule group. You'll use the name to identify the rule
   group when you add it to your firewall policy later in the tutorial. You can't
   change the name of a rule group after you create it.
6. For **Capacity**, enter `10`.
7. Enter the following rule specifications to create a stateless rule that blocks all packets coming from the source IP address CIDR range `192.0.2.0/24`:
   1. Set the priority to **10**.
   2. Leave the protocol setting at **All**.
   3. For the source address, specify `192.0.2.0/24`.
   4. Leave the source port at **Any**.
   5. Set the destination address to **Any**.
   6. For the action, choose **Drop**.
   7. Choose **Add rule**. Your rule is added to the
      **Rules** list.

8. Review the settings for the rule group, then choose **Create rule
   group**.

Your new rule group is added to the list in the **Rule groups**
page.

###### To create a stateful rule group

1. From the **Rule groups** page, choose **Create rule
   group**.
2. In the **Create rule group** page, for the **Rule
   group type**, choose **Stateful rule group**.
3. Enter a name for the stateful rule group.
4. For **Capacity**, enter `10`.
5. Choose the stateful rule group configuration option **Import Suricata compatible
   rules**. The entry form for Suricata compatible rule string appears.
   Copy and paste the following Suricata rule into the text box. This rule drops TLS traffic for a specific target domain:

```
drop tls $HOME_NET any -> $EXTERNAL_NET any (ssl_state:client_hello; tls.sni; content:"evil.com"; startswith; nocase; endswith; msg:"matching TLS denylisted FQDNs"; priority:1; flow:to_server, established; sid:1; rev:1;)
```

6. Choose **Add rule**. Your rule is added to the
   **Rules** list for the rule group.
7. Review the settings for the rule group, then choose **Create rule
   group**.

Your stateless rule group and your stateful rule group are listed in the
**Rule groups** page. You can now use these rule groups in your
firewall policies.

## Step 2: Create a firewall

policy

Firewall policies use rule groups and other settings to define the traffic filtering
behavior for a firewall. In this procedure, you'll create a policy using the rule groups
that you created in the previous step. For information about firewall policies, see
[Firewall policies in AWS Network Firewall](firewall-policies.md "firewall-policies.md").

###### To configure a firewall policy

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.
3. In the **Firewall policies** page, choose **Create
   firewall policy**.
4. Enter the name that you want to use for the firewall policy. You'll use the
   name to identify the policy when you associate it with your firewall later in
   the tutorial. You can't change the name of a firewall policy after you create
   it.
5. Choose **Next** to go to the firewall policy's **Add rule
   groups** page.
6. In the **Stateless rule groups** section, choose **Add rule
   groups**, then select the check box for the stateless rule group
   that you created in the prior procedure. Choose **Add rule groups**. At the
   bottom of the page, the firewall policy's capacity counter shows the capacity
   consumed by adding this rule group next to the maximum capacity allowed for a
   firewall policy.
7. Your stateless rule group blocks some incoming traffic. In the stateless default actions,
   you choose what to do with the rest of the traffic. For this tutorial, we'll forward it to the
   stateful engine. Use the same default action for packets and packet fragments.
   Network Firewall only manages UDP packet fragments and silently drops packet fragments for other protocols.
   Set the action to **Forward to stateful rules**.
8. In the **Stateful rule groups** section, choose **Add rule
   groups**, then select the check box for the stateful rule group
   that you created in the prior procedure. Choose **Add rule groups**.
9. Choose **Next** then **Next** again to proceed through
   the tagging option and to the **Review and create** page. From
   this page, you can choose **Edit** for any area to return to
   the corresponding page in the firewall policy creation wizard.
10. Choose **Create firewall policy**.

Your new firewall policy is added to the list in the **Firewall policies**
page. You can now use your firewall policy in your firewalls.

## Step 3: Create a firewall

Firewalls associate the traffic filtering behavior of a firewall policy with the primary VPC where
you want to filter traffic. In this procedure, you'll create a firewall using the
firewall policy that you created in the previous step. For information about firewalls,
see [Firewalls and firewall endpoints in AWS Network Firewall](firewalls.md "firewalls.md").

###### To create a firewall

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. Choose **Create firewall**.
4. For **Name**, enter the name that you want to use to identify this
   firewall. You can't change the name of a firewall after you create it.
5. For **VPC**, select your VPC from the dropdown.
6. For **Availability Zone** and **Subnet**, select the zone and
   firewall subnet that you identified in [Before you begin](#getting-started-prerequisites "#getting-started-prerequisites").
7. For **Associated firewall policy**, choose **Associate an
   existing firewall policy**, then select the firewall policy that
   you created in the prior procedure.
8. Choose **Create firewall**.

Your new firewall is listed in the **Firewalls** page. You've configured
the firewall's behavior with the firewall policy and rule groups, and your firewall has an endpoint
that's running in your VPC, ready to filter network traffic.

###### Note

Network Firewall supports up to 100 Gbps of network traffic per firewall endpoint. If you require more traffic
bandwidth, you can split your resources into subnets and create a Network Firewall firewall in
each subnet.

The next step is to route the VPC's network traffic through the firewall endpoint. You'll insert it into the
traffic flow between the internet gateway and your customer subnet.

## Step 4: Update your Amazon VPC route

tables

After you create your firewall, you insert its firewall endpoint into your Amazon Virtual Private Cloud
network traffic flow, in between your internet gateway and your customer subnet. You
create routing for the firewall endpoint so that it forwards traffic between the
internet gateway and your subnet. Then, you update the route tables for your internet
gateway and your subnet, to send traffic to the firewall endpoint instead of to each
other.

This procedure covers the high-level steps for route table management.
For information about managing route tables for your VPC, see
[Route
tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon Virtual Private Cloud User
Guide_.

###### To modify your route tables to insert a firewall endpoint between your internet

gateway and your subnet

1. Review your routing for the internet gateway and for your customer subnet, to
   determine the components used to route traffic between the two.

Record the current settings. You'll use them to reverse your changes at the
end of the tutorial.

    * The internet gateway's route table typically has an entry with a
     destination set to your customer subnet's CIDR block and a target of
     `local`.
    * The subnet's route table typically has an entry with a destination set
     to `0.0.0.0/0` and a target set to the internet gateway ID.

2.  Create a route table configuration for the firewall endpoint with the
    following two routes:

        * An entry that matches the internet gateway's route specification for
         traffic going to the customer subnet's CIDR block.
        * An entry that matches the subnet's route specification for traffic
         going to the internet gateway.

    The firewall endpoint is now ready to filter and forward traffic between the
    internet gateway and the customer subnet. The endpoint only forwards traffic to
    its intended destination if it passes the inspection criteria that you defined
    in the rule groups and firewall policy.

3.  Update the internet gateway's routing to modify the entry with a destination
    set to your customer subnet's CIDR block. Change the target to the firewall
    endpoint ID.
4.  Update the customer subnet routing to modify the entry with a destination set
    to the internet gateway ID. Change the target to the firewall endpoint ID.

The firewall endpoint is now
filtering
all traffic between your internet gateway and customer subnet.

## Step 5: Remove the firewall and clean up your

resources

You've now successfully completed the tutorial. To remove the firewall endpoint from your
VPC and prevent your account from accruing AWS Network Firewall charges for the tutorial
resources, revert your route table changes and clean up the Network Firewall resources that
you created.

###### To modify your route tables to remove the firewall

1. Return the internet gateway and subnet route tables to the configurations they had at the
   start of the prior procedure. This stops traffic from routing to the firewall
   endpoint.
2. Remove the route table configuration for the firewall endpoint.

###### To remove the Network Firewall resources

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. In the **Firewalls** page, select the firewall that you created for the
   tutorial.
4. Choose **Delete**, and then confirm your request.
5. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.
6. In the **Firewall policies** page, select the firewall policy
   that you created for the tutorial.
7. Choose **Delete**, and confirm your request.
8. In the navigation pane, under **Network Firewall**, choose **Network Firewall rule groups**.
9. In the **Rule group** page, select the name of the rule
   groups that you created for the tutorial, and then choose
   **Delete**.

You've successfully removed the firewall from your VPC traffic flow and removed all of the
Network Firewall resources that you created for this tutorial.
