

# Configure DNS and NTP with a DHCP option set

Amazon Elastic VMware Service reads your VPC DHCP option set. The option set provides the DNS servers for host IP address resolution, the domain name for DNS resolution, and the NTP servers for time synchronization. Create a DHCP option set with these values and associate it with your VPC, using the Amazon VPC console or the AWS CLI.

Your environment deployment fails if you don’t meet the following requirements.
+ The DHCP option set includes a primary DNS server IP address and a secondary DNS server IP address.
+ A DNS forward lookup zone has A records for each VMware Cloud Foundation (VCF) management appliance and Amazon EVS host in your deployment.
+ A DNS reverse lookup zone has PTR records for each VCF management appliance and Amazon EVS host in your deployment.
+ The VPC main route table has a route to your DNS servers.
+ Your domain name registration is valid and unexpired, and no duplicate host names or IP addresses exist.
+ Your security groups and network ACLs allow the traffic in [Required traffic](evs-env-nacl-cong.md#evs-env-nacl-rules).

## DNS server requirements
<a name="getting-started-config-dns"></a>

Both DNS server IP addresses must be reachable and must respond to queries when the Amazon EVS connector launches. All required forward A records and reverse PTR records must resolve through those servers at that time. For the host names and records that each mode needs, see [Step 2: Create DNS records](self-deployed-host-dns-records.md) for Self-deployed mode and [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md) for EVS-deployed mode.

### DNS for on-premises connectivity
<a name="getting-started-config-dns-on-prem"></a>

For on-premises connectivity, we recommend Route 53 private hosted zones with inbound resolver endpoints. This setup gives you hybrid DNS resolution, so resources in your VPC resolve names hosted on your on-premises network, and the other way around. You can also use your own DNS server with Route 53 outbound resolver endpoints. Using both Route 53 and a custom DNS server in the DHCP option set can cause unexpected behavior. For instructions, see [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) and [Forwarding inbound DNS queries to your VPC](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) in the *Amazon Route 53 Developer Guide*.

**Important**  
If you use custom DNS domain names in a Route 53 private hosted zone, you must set the `enableDnsHostnames` and `enableDnsSupport` VPC attributes to `true`. The same applies if you use private DNS with interface VPC endpoints (AWS PrivateLink). For more information, see [DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html#vpc-dns-support).

## NTP server requirements
<a name="getting-started-config-ntp"></a>

A consistent and accurate time reference is required for many VCF tasks, including system logging and auditing, security operations, distributed system management, and troubleshooting. You can enter the IPv4 addresses of up to four NTP servers in the DHCP option set.

Amazon EVS hosts use the link-local Amazon Time Sync Service address `169.254.169.123` as their NTP source. The VCF Installer specification for diskless hosts in this guide uses `time.aws.com`. Diskless hosts are available only with VCF 9.x. For the NTP validation warnings that this causes, see [Validate and deploy](deploy-diskless-spec.md#getting-started-diskless-deploy).

For more information about NTP options in DHCP, see [RFC 2132](https://datatracker.ietf.org/doc/html/rfc2132#section-8.3). For time synchronization on EC2 instances, see [Precision clock and time synchronization in your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html) in the *Amazon EC2 User Guide*.

## Create private hosted zones and a Resolver inbound endpoint
<a name="network-dhcp-dns-zones"></a>

If you don’t have DNS servers that the VPC can reach, use Route 53 private hosted zones. Create the zones and the endpoint before the DHCP option set, because the endpoint addresses become the DNS servers in the option set. You create the DNS records later. For Self-deployed mode, see [Step 2: Create DNS records](self-deployed-host-dns-records.md). For EVS-deployed mode, see [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md).

1. Create a Route 53 private hosted zone for your domain name, for example `evs.example.com`, and associate it with your VPC. This zone is the forward lookup zone.

1. Create a second private hosted zone for reverse lookup, and associate it with your VPC. The zone must cover the address range of your Amazon EVS VLAN subnets, for example `10.10.in-addr.arpa` for 10.10.0.0/16.

1. Create a security group in your VPC that allows inbound TCP and UDP port 53 from the VPC CIDR block and from any network that queries the endpoint.

1. Create a Route 53 Resolver inbound endpoint in the service access subnet with two IP addresses in that subnet, and the security group from the previous step. The two addresses can be in the same subnet, so a Single-AZ VPC doesn’t need a second Availability Zone for the endpoint.

1. Wait until the endpoint status is operational, and note its two IP addresses.

Use the two endpoint IP addresses as the primary and secondary DNS servers in the DHCP option set. For instructions, see [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) and [Forwarding inbound DNS queries to your VPC](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) in the *Amazon Route 53 Developer Guide*.

## Create and associate the DHCP option set
<a name="network-dhcp-dns-ntp-steps"></a>

Create the DHCP option set and associate it with your VPC in the Amazon VPC console or with the AWS CLI. Choose the tab for the method that you use.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc) and choose **DHCP option sets** in the navigation pane.

1. Choose **Create DHCP option set**.

1. For **Domain name**, enter your DNS domain name.

1. For **Domain name servers**, enter the primary and secondary DNS server IP addresses.

1. For **NTP servers**, enter the IPv4 addresses of up to four NTP servers.

1. Choose **Create DHCP option set**.

1. In the navigation pane, choose **Your VPCs** and select your VPC.

1. Choose **Actions**, **Edit VPC settings**.

1. For **DHCP option set**, choose the option set that you created, and then choose **Save**.

1. Create the DHCP option set and store its ID. Replace the example addresses and names with your own values.

   ```bash
   DHCP_OPTIONS_ID=$(aws ec2 create-dhcp-options \
     --dhcp-configurations \
       "Key=domain-name,Values=example.com" \
       "Key=domain-name-servers,Values=10.10.200.100,10.10.200.101" \
       "Key=ntp-servers,Values=10.10.200.20" \
     --query 'DhcpOptions.DhcpOptionsId' \
     --output text)
   ```

1. Associate the DHCP option set with your VPC. If `$VPC_ID` isn’t set in your shell, replace it in the following commands with the ID of your VPC.

   ```bash
   aws ec2 associate-dhcp-options \
     --dhcp-options-id $DHCP_OPTIONS_ID \
     --vpc-id $VPC_ID
   ```

1. Verify the association.

   ```bash
   aws ec2 describe-vpcs \
     --vpc-ids $VPC_ID \
     --query 'Vpcs[0].DhcpOptionsId'
   ```

   The output is the ID of the DHCP option set that you created.

You have configured DNS and NTP for your VPC. For more information, see [Create a DHCP option set](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html#CreatingaDHCPOptionSet) in the * Amazon VPC User Guide*.

## Launch an instance to reach the VPC
<a name="network-access-instance"></a>

Later steps need a computer with a web browser that can reach the private IP addresses of your VPC and resolve the names in your private DNS zones. For example, you verify DNS records from it and open the VMware Host Client, the VCF Installer, and the vSphere Client from it. If your on-premises network doesn’t reach the VPC yet, launch an Amazon EC2 instance in the VPC for this purpose.

Launch the instance after you associate the DHCP option set. An instance that launches before the association doesn’t get the DNS servers and the domain name of the option set.

1. Launch an Amazon EC2 instance in the service access subnet, with no public IP address. Use a Windows instance if you want a desktop web browser on it.

1. Attach an instance profile that lets AWS Systems Manager manage the instance. The instance reaches Systems Manager through the NAT gateway, or through interface VPC endpoints for Systems Manager.

1. Connect to the instance with Session Manager, or to a Windows desktop with Fleet Manager Remote Desktop.

1. From the instance, run `nslookup` with your domain name. The output names the DNS server that answered, which must be one of the DNS servers in the option set.

For instructions, see [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) and [Connecting to a Windows Server managed instance using Remote Desktop](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.html) in the * AWS Systems Manager User Guide*.

## Check DNS reachability
<a name="evs-env-dns-reachability"></a>

Amazon EVS needs a persistent connection to SDDC Manager and to the DNS servers in your DHCP option set to reach DNS records. If the connection to SDDC Manager becomes unavailable, Amazon EVS can no longer validate the environment status, and you might lose environment access. For instructions to troubleshoot this issue, see [Troubleshoot networking](troubleshoot-networking.md).

Next, set up Amazon VPC Route Server. For instructions, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).