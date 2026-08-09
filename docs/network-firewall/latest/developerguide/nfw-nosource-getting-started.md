# Getting started with no-source-preservation mode

This section walks you through creating a Network Firewall firewall in no-source-preservation
mode using the AWS Management Console.

## Before you begin

To follow this tutorial, you need the following:

- An egress VPC where your NAT gateway is hosted. If you do not have a NAT
  gateway, create one using the steps in [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") in
  the _Amazon Virtual Private Cloud User Guide_. When creating a
  no-source-preservation Network Firewall, you need this NAT gateway ID as input.
  The firewall uses this NAT gateway's IP address to establish connectivity
  with the destination.
- A client VPC (where your applications reside) with a subnet to host the
  firewall endpoint. This subnet must be in the same Availability Zone as the
  NAT gateway. The client VPC can be the same as the egress VPC or a different
  VPC.

## Step 1: Create rule groups

Rule groups are reusable collections of network filtering rules that you use to
configure firewall behavior. Create your stateful rule groups. For
information, see [Managing your rule groups](rule-groups.md "rule-groups.md").

## Step 2: Create a firewall policy

Firewall policies define the traffic filtering behavior for a firewall. Create a
firewall policy and attach your stateful rule groups. Stateless rule groups do not apply
to no-source-preservation mode traffic.

###### To create a firewall policy

1. In the navigation pane, under **Network Firewall**, choose
   **Firewall policies**.
2. Choose **Create firewall policy**.
3. Enter a name for the firewall policy.
4. Choose **Next** to go to the Add rule groups page.
5. In the Stateful rule groups section, choose **Add rule groups**,
   then select your stateful rule group. Choose **Add rule groups**.
6. Choose **Next** then **Next** again to proceed
   to the Review and create page.
7. Choose **Create firewall policy**.

## Step 3: Create the firewall

Create the firewall in no-source-preservation mode using the AWS Management Console.

###### To create a firewall in no-source-preservation mode

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   `https://console.aws.amazon.com/vpc/`.
2. In the navigation pane, under **Network Firewall**, choose
   **Firewalls**.
3. Choose **Create firewall**.
4. For **Name**, enter the name that you want to use to identify
   this firewall. You cannot change the name of a firewall after you create it.
5. For **Deployment mode**, select **No source
   preservation**.
6. For **NAT Gateway**, select an existing NAT gateway from the
   dropdown. The console displays the NAT gateway's subnet and Availability Zone. If you
   do not have a NAT gateway, create one first.
7. For **VPC endpoint subnet**, select a VPC and subnet for the
   firewall endpoint. You can only create the endpoint in the Availability Zone that
   your NAT gateway resides in. The endpoint subnet must be different from the NAT gateway
   subnet. The console only shows options for the subnets where you are allowed to create
   the endpoint.
8. (Optional) Configure advanced settings: delete protection, traffic analysis mode
   (enabled by default), customer managed KMS key, explicit proxy listener ports
   (defaults to HTTP/3128 and HTTPS/8443), logging configuration (Alert, Flow, TLS),
   and firewall monitoring dashboard.
9. For **Associated firewall policy**, choose **Associate an
   existing firewall policy**, then select the firewall policy that you
   created in Step 2.
10. (Optional) Add tags.
11. Review and choose **Create firewall**.

Your new firewall is listed in the **Firewalls** page.

## Step 4: Verify the firewall and configure workloads

After creation, the firewall details page displays the deployment mode, the attached
NAT gateway ID, and the status. Once the status transitions from PROVISIONING to READY,
the proxy FQDN (`DnsName`) appears in the **Endpoints and
identity** section.

Point your application's proxy environment variables to the firewall's
`DnsName` on the configured listener port. No route table changes are
required – applications connect to the firewall through VPC endpoints using the
proxy's FQDN.

## Step 5: Clean up

To remove the firewall and prevent your account from accruing charges, delete the
firewall, firewall policy, and rule groups you created for the tutorial. Navigate to
each resource in the Network Firewall console and choose **Delete**.
