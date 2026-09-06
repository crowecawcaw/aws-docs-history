

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

1. Enter a name for the firewall policy.

1. Choose **Next** to go to the Add rule groups page.

1. In the Stateful rule groups section, choose **Add rule groups**, then select your stateful rule group. Choose **Add rule groups**.

1. Choose **Next** then **Next** again to proceed to the Review and create page.

1. Choose **Create firewall policy**.

## Step 3: Create the firewall
<a name="nfw-nosource-step3-firewall"></a>

Create the firewall in no-source-preservation mode using the AWS Management Console.

**To create a firewall in no-source-preservation mode**

1. Sign in to the AWS Management Console and open the Amazon VPC console at `https://console.aws.amazon.com/vpc/`.

1. In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. Choose **Create firewall**.

1. For **Name**, enter the name that you want to use to identify this firewall. You cannot change the name of a firewall after you create it.

1. For **Deployment mode**, select **No source preservation**.

1. For **NAT Gateway**, select an existing NAT gateway from the dropdown. The console displays the NAT gateway's subnet and Availability Zone. If you do not have a NAT gateway, create one first.

1. For **VPC endpoint subnet**, select a VPC and subnet for the firewall endpoint. You can only create the endpoint in the Availability Zone that your NAT gateway resides in. The endpoint subnet must be different from the NAT gateway subnet. The console only shows options for the subnets where you are allowed to create the endpoint.

1. (Optional) Configure advanced settings: delete protection, traffic analysis mode (enabled by default), customer managed KMS key, explicit proxy listener ports (defaults to HTTP/3128 and HTTPS/8443), logging configuration (Alert, Flow, TLS), and firewall monitoring dashboard.

1. For **Associated firewall policy**, choose **Associate an existing firewall policy**, then select the firewall policy that you created in Step 2.

1. (Optional) Add tags.

1. Review and choose **Create firewall**.

Your new firewall is listed in the **Firewalls** page.

## Step 4: Verify the firewall and configure workloads
<a name="nfw-nosource-step4-verify"></a>

After creation, the firewall details page displays the deployment mode, the attached NAT gateway ID, and the status. Once the status transitions from PROVISIONING to READY, the proxy FQDN (`DnsName`) appears in the **Endpoints and identity** section.

Point your application's proxy environment variables to the firewall's `DnsName` on the configured listener port. No route table changes are required – applications connect to the firewall through VPC endpoints using the proxy's FQDN.

## Step 5: Clean up
<a name="nfw-nosource-step5-cleanup"></a>

To remove the firewall and prevent your account from accruing charges, delete the firewall, firewall policy, and rule groups you created for the tutorial. Navigate to each resource in the Network Firewall console and choose **Delete**.