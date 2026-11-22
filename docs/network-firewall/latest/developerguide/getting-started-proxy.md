

# Getting started with a NAT/Proxy firewall

This section walks you through creating an AWS Network Firewall NAT/Proxy firewall using the AWS Management Console.

With a NAT/Proxy firewall, Network Firewall creates a NAT gateway so that the firewall can perform network address translation (NAT) and act as an explicit forward proxy. You use the firewall to filter egress-only connections and their responses. Clients send traffic to the firewall through the firewall endpoint. The firewall filters the traffic and sends it out through the NAT gateway, which uses its own IP address as the source. You can also turn off NAT on non-proxy traffic, so that the firewall returns filtered traffic to the firewall endpoint without address translation. For more information, see [NAT/Proxy firewall in AWS Network Firewall](nfw-proxy.md).

If you want the firewall to preserve the client source IP address, choose a routed firewall instead. With that capability, you steer traffic to the firewall through your VPC route tables and route outbound traffic through your own NAT gateway or internet gateway. For information about creating a routed firewall, see [Getting started with a Next Generation policy](getting-started-v2.md) or [Getting started with a Classic AWS Network Firewall policy](getting-started-classic.md).

**Topics**
+ [Before you begin](#getting-started-proxy-prerequisites)
+ [Step 1: Create rule groups](#getting-started-proxy-rule-groups)
+ [Step 2: Create a firewall policy](#getting-started-proxy-policy)
+ [Step 3: Create the firewall](#getting-started-proxy-create-firewall)
+ [Step 4: Verify the firewall and configure workloads](#getting-started-proxy-verify)
+ [Step 5: Clean up](#getting-started-proxy-clean-up)

## Before you begin
<a name="getting-started-proxy-prerequisites"></a>

To follow this tutorial, you need the following:
+ A VPC for the firewall. Network Firewall creates the firewall's NAT gateways and firewall endpoints in this one VPC. After you create the firewall, you can add firewall endpoints in other VPCs with VPC endpoint associations.
+ Two subnets in each Availability Zone that you want the firewall to run in. In each Availability Zone, you need:
  + A *NAT subnet*, where Network Firewall creates the NAT gateway. For a public NAT gateway, this subnet needs a route to an internet gateway.
  + A *firewall endpoint subnet*, where Network Firewall creates the firewall endpoint. This subnet must be in the same Availability Zone as the NAT subnet, and it can't be the NAT subnet. Use a subnet dedicated to the firewall endpoint.
+ IP addresses for each NAT gateway. Choose the NAT gateway connectivity type before you start:
  + **Public** – The NAT gateways use Elastic IP addresses to reach the internet. Allocate at least one Elastic IP address for each NAT gateway, and pick one available private IP address from the NAT subnet for each Elastic IP address. The Elastic IP addresses must not be associated with another resource. For information, see [Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html) in the *Amazon Virtual Private Cloud User Guide*.
  + **Private** – The NAT gateways use only private IP addresses to reach other VPCs or your on-premises network. Pick at least one available private IP address from each NAT subnet.

  Each NAT gateway can have up to 8 IP addresses. For a public NAT gateway, an Elastic IP address and its paired private IP address count as one address. Private IP addresses must be in the NAT subnet's IPv4 CIDR block. AWS reserves the first four IP addresses and the last IP address in each subnet, so you can't use those.

## Step 1: Create rule groups
<a name="getting-started-proxy-rule-groups"></a>

Rule groups are reusable collections of network filtering rules that you use to configure firewall behavior. Create your rule groups. For a Next Generation policy, see [Rule groups for Next Generation policies](rule-groups-v2.md). For a Classic Network Firewall policy, create stateful rule groups; stateless rules don't inspect explicit proxy traffic. For information about creating rule groups, see [Managing your rule groups](rule-groups.md).

## Step 2: Create a firewall policy
<a name="getting-started-proxy-policy"></a>

Firewall policies define the traffic filtering behavior for a firewall. Create a firewall policy and attach your rule groups. You can use a Next Generation policy or a Classic Network Firewall policy. For information about creating a firewall policy, see [Creating a Next Generation policy in AWS Network Firewall](firewall-policy-v2-creating.md) or [Creating a firewall policy in AWS Network Firewall](firewall-policy-creating.md).

You can also skip this step and create an empty firewall policy while you create the firewall in Step 3. You can configure the associated firewall policy after you create the firewall.

## Step 3: Create the firewall
<a name="getting-started-proxy-create-firewall"></a>

**To create a NAT/Proxy firewall (part 1): specify the VPC, NAT gateways, and endpoints**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

   In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. Choose **Create firewall**.

1. On the **Describe firewall** page, for **Firewall name**, enter a name to identify this firewall. You can't change the name of a firewall after you create it. Optionally, enter a description. Choose **Next**.

1. On the **Firewall capability** page, for **Firewall capability**, choose **NAT/Proxy firewall**. This option is selected by default.

1. In the **NAT gateway details** section, configure the VPC, the NAT gateways, and the firewall endpoints. Network Firewall creates the NAT gateway and the firewall endpoint in each Availability Zone that you specify. You can't change these details after you create the firewall. Configure the following:

   1. For **VPC**, choose the VPC for the firewall's NAT gateways and firewall endpoints.

   1. For **Connectivity type**, choose **Public** or **Private**. This setting applies to the NAT gateway in every Availability Zone.

   1. Under **NAT gateway 1**, for **NAT subnet**, choose the subnet where Network Firewall creates the NAT gateway. The subnet's Availability Zone becomes the Availability Zone for this NAT gateway and firewall endpoint.

   1. Under **NAT IP addresses**, enter the IP addresses for this NAT gateway:
      + For a public NAT gateway, for **Elastic IP allocations**, choose one or more Elastic IP addresses. For **Private IP addresses**, enter one private IP address from the NAT subnet for each Elastic IP address. Separate addresses with commas. If the console can't list your Elastic IP addresses, or you have no unassociated Elastic IP addresses, enter the allocation IDs (for example, `eipalloc-0123456789abcdef0`) instead.
      + For a private NAT gateway, for **Private IP addresses**, enter one or more private IP addresses from the NAT subnet. Separate addresses with commas. **Elastic IP allocations** doesn't apply to a private NAT gateway.

   1. For **Firewall endpoint subnet**, choose the subnet where Network Firewall creates the firewall endpoint. The list shows only other subnets in the NAT gateway's Availability Zone.

   1. To run the firewall in another Availability Zone, choose **Add NAT gateway** and repeat the previous three substeps. Each NAT gateway must use a subnet in a different Availability Zone. To remove a NAT gateway, choose **Remove**.

1. Choose **Next**.

After you configure the NAT gateways and firewall endpoints, configure the firewall's advanced settings, associate a firewall policy, and create the firewall.

**To create a NAT/Proxy firewall (part 2): configure settings and create the firewall**

1. (Optional) On the **Configure advanced settings** page, configure the following settings, and then choose **Next**:
   + **Protection against changes** – Turn on delete protection and subnet change protection.
   + **Customer managed key** – Choose an AWS KMS key to encrypt and decrypt your firewall resources. For information about encrypting your firewall resources, see [Encryption at rest with AWS Key Management Service](kms-encryption-at-rest.md).
   + **Explicit proxy listeners** – Set an **HTTP port** and an **HTTPS port** for the proxy. If you leave a port blank, the firewall uses the default port: 3128 for HTTP and 8443 for HTTPS. Each port must be between 1 and 65535, and you can't use the same port for both HTTP and HTTPS.
   + **Certificate** – To give the proxy your own hostname, choose an AWS Certificate Manager (ACM) certificate for your custom hostname. The proxy presents this certificate to clients that connect using that hostname. To use the default hostname, choose **No certificate (use the default hostname)**. You can't change this setting after you create the firewall. For information, see [Using a custom proxy hostname and certificate](nfw-proxy-custom-hostname.md).
   + **Custom hostname** – If you chose a certificate, enter the hostname that your clients use to send HTTP and HTTPS traffic to the proxy, for example `proxy.example.com`. The hostname must be a fully qualified domain name that the certificate covers. The console lists the names on the certificate. You can't change this setting after you create the firewall.
   + **Non-proxy traffic** – **Enable NAT on non-proxy traffic** performs network address translation on traffic that doesn't use the explicit proxy, and is turned on by default. When it's turned on, filtered traffic exits through the associated NAT gateway. When it's turned off, filtered traffic exits from the firewall endpoint. You can't change this setting after you create the firewall.
   + **Logging configuration** – Choose the log types to send, their destinations, and whether to turn on the firewall monitoring dashboard. For information, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).

1. On the **Associate firewall policy** page, choose one of the following, and then choose **Next**:
   + **Associate an existing firewall policy** – Choose the firewall policy that you created in Step 2.
   + **Create and associate an empty firewall policy** – Enter a name for the new firewall policy. You can add rule groups to the policy after you create the firewall.

1. (Optional) On the **Add tags** page, add any tags that you want, and then choose **Next**.

1. On the **Review and create** page, review the firewall configuration. Under **Firewall capability**, the **NAT gateway details** table lists the Availability Zone, NAT subnet, Elastic IP allocations (public NAT gateways only), private IP addresses, and firewall endpoint subnet for each NAT gateway. To change a step, choose **Edit**. When you're ready, choose **Create firewall**.

Your new firewall is listed on the **Firewalls** page. Network Firewall creates the NAT gateways and firewall endpoints while the firewall provisions, which can take several minutes.

## Step 4: Verify the firewall and configure workloads
<a name="getting-started-proxy-verify"></a>

**To verify the firewall and configure workloads**

1. On the **Firewalls** page, choose your firewall to open its details page.
   + In the firewall details, **NAT gateway associations** lists the NAT gateways that Network Firewall created. While a NAT gateway is still being created, the console shows **NAT gateway provisioning**.
   + The **Firewall endpoints** table lists each Availability Zone's firewall endpoint, along with its NAT gateway and NAT gateway status.
   + The **Endpoints and identity** section shows the **Proxy listeners**, the **Proxy hostname**, the **Custom hostname** and **Certificate** (if you set them), and whether **Network address translation for non-proxy traffic** is enabled. The proxy hostname appears after the firewall is ready.

1. To send traffic through the explicit proxy, point your applications' proxy settings (for example, the `HTTP_PROXY` and `HTTPS_PROXY` environment variables) to the firewall's proxy hostname, or your custom hostname, on the listener port. Clients that use the explicit proxy don't need route table changes. For information, see [Configuring workloads to use the proxy](nfw-proxy-client-config.md).

1. To inspect traffic that doesn't use the explicit proxy, update your VPC route tables to send that traffic to the firewall endpoint in the same Availability Zone. For information, see [VPC route table configuration for AWS Network Firewall](vpc-config-route-tables.md).

To change the proxy listener ports later, choose **Edit** in the **Endpoints and identity** section.

## Step 5: Clean up
<a name="getting-started-proxy-clean-up"></a>

To remove the firewall and prevent your account from accruing charges, delete the resources that you created for this tutorial.

**To delete the firewall and its resources**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. Select your firewall, and then choose **Delete**. If delete protection is turned on, choose **Disable delete protection** first.

1. To delete the NAT gateways along with the firewall, select **Also delete the NAT gateways this firewall created**. If you leave this cleared, the NAT gateways are kept and keep working as regular NAT gateways, and you must delete them separately in the Amazon VPC console.

1. Confirm the deletion.

1. Delete the firewall policy and rule groups that you created for this tutorial. Navigate to each resource in the Network Firewall console and choose **Delete**.

1. If you allocated Elastic IP addresses for this tutorial, release them in the Amazon VPC console after the NAT gateways are deleted.