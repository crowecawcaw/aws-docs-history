

# Getting started with no-source-preservation mode
<a name="nfw-nosource-getting-started"></a>

This section walks you through creating a Network Firewall firewall in no-source-preservation mode using the AWS Management Console.

## Before you begin
<a name="nfw-nosource-prerequisites"></a>

To follow this tutorial, you need the following:
+ An egress VPC where your NAT gateway is hosted. If you do not have a NAT gateway, create one using the steps in [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon Virtual Private Cloud User Guide*. When creating a no-source-preservation Network Firewall, you need this NAT gateway ID as input. The firewall uses this NAT gateway's IP address to establish connectivity with the destination.
+ A client VPC (where your applications reside) with a subnet to host the firewall endpoint. This subnet must be in the same Availability Zone as the NAT gateway. The client VPC can be the same as the egress VPC or a different VPC.

## Step 1: Create rule groups
<a name="nfw-nosource-step1-rule-groups"></a>

Rule groups are reusable collections of network filtering rules that you use to configure firewall behavior. Create your stateful rule groups. For information, see [Managing your rule groups](rule-groups.md).

## Step 2: Create a firewall policy
<a name="nfw-nosource-step2-policy"></a>

Firewall policies define the traffic filtering behavior for a firewall. Create a firewall policy and attach your stateful rule groups. Stateless rule groups do not apply to no-source-preservation mode traffic.

**To create a firewall policy**

1. In the navigation pane, under **Network Firewall**, choose **Firewall policies**.

1. Choose **Create firewall policy**.

1. For **Policy version**, select **Classic**. No-source-preservation mode requires a Classic Network Firewall policy. For information about the policy types, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).

1. Enter a name for the firewall policy.

1. Choose **Next** to go to the **Traffic inspection** page. For this tutorial, leave its settings unset and choose **Next** to go to the **Add rule groups** page.

1. In the Stateful rule groups section, choose **Add rule groups**, then select your stateful rule group. Choose **Add rule groups**.

1. Choose **Next** to go to the **Network and encryption** page, then choose **Next** again to go to the **Review and create** page.

1. Choose **Create firewall policy**.

## Step 3: Create the firewall
<a name="nfw-nosource-step3-firewall"></a>

Create the firewall in no-source-preservation mode using the AWS Management Console.

**To create a firewall in no-source-preservation mode**

1. Sign in to the AWS Management Console and open the Amazon VPC console at `https://console.aws.amazon.com/vpc/`.

1. In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. Choose **Create firewall**.

1. On the **Describe firewall** page, for **Name**, enter the name that you want to use to identify this firewall. You cannot change the name of a firewall after you create it. Choose **Next**.

1. On the **Deployment mode** page, select **No source preservation**.

1. For **NAT Gateway**, select an existing NAT gateway from the dropdown list. The console displays the selected NAT gateway's VPC, subnet, and Availability Zone. If you don't have a NAT gateway, choose **Create NAT gateway** to create one in the Amazon VPC console, and then refresh the list.

1. For **VPC endpoint subnet**, select a VPC and a subnet for the firewall endpoint. The subnet must be in the same Availability Zone as the NAT gateway, and it can't be the NAT gateway's own subnet. To add more subnets, choose **Add subnet**; all subnets must be in the same VPC. You must specify at least one subnet.

1. (Optional) On the **Configure advanced settings** page, configure settings such as delete protection, traffic analysis mode, a customer managed key, **Explicit proxy listeners**, logging configuration (Alert, Flow, and TLS logs), and the firewall monitoring dashboard. Under **Explicit proxy listeners**, you can set an **HTTP port** and an **HTTPS port**. If you leave a port blank, the firewall uses the default port—3128 for HTTP and 8443 for HTTPS.

1. On the **Associate firewall policy** page, select **Associate an existing firewall policy**, then select the firewall policy that you created in Step 2.

1. (Optional) On the **Add tags** page, add any tags that you want.

1. On the **Review and create** page, review the firewall configuration, and then choose **Create firewall**.

Your new firewall is listed in the **Firewalls** page.

## Step 4: Verify the firewall and configure workloads
<a name="nfw-nosource-step4-verify"></a>

After creation, the firewall details page displays the deployment mode, the attached NAT gateway ID, and the status. After the status transitions from PROVISIONING to READY, the proxy FQDN (`DnsName`) appears in the **Endpoints and identity** section.

Point your application's proxy environment variables to the firewall's `DnsName` on the configured listener port. No route table changes are required – applications connect to the firewall through VPC endpoints using the proxy's FQDN.

## Step 5: Clean up
<a name="nfw-nosource-step5-cleanup"></a>

To remove the firewall and prevent your account from accruing charges, delete the firewall, firewall policy, and rule groups you created for the tutorial. Navigate to each resource in the Network Firewall console and choose **Delete**.