

# Troubleshoot networking

Network problems in an Amazon Elastic VMware Service environment might involve DNS, Amazon VPC Route Server, route tables, network ACLs, or the NSX distributed firewall. These solutions apply to both deployment modes. For BGP symptoms between the NSX Edge nodes and VPC Route Server in a Self-deployed environment, see [NSX Edge and BGP symptoms](troubleshoot-self-deployed.md#troubleshoot-sd-nsx).

## Amazon EVS can’t reach DNS servers or SDDC Manager
<a name="troubleshoot-dns-reachability"></a>

Amazon EVS needs a persistent connection to SDDC Manager and to the DNS servers in your VPC DHCP option set. When the connection fails, the reachability status check or a connector reachability check fails. Amazon EVS can then no longer validate the environment status, and you can lose environment access.

 **Cause** 

The DNS servers aren’t reachable from the service access subnet, a DNS record is missing or wrong, or a network ACL blocks the traffic.

 **Solution** 

1. Make sure that your DNS servers are reachable from the service access subnet.

1. Make sure that the DNS records are valid, and that no duplicate host names or IP addresses exist.

1. Make sure that your network ACL rules allow TCP and UDP access to the DNS servers, and HTTPS and SSH access to the host management and management VM VLAN subnets.

1. If you use custom DNS domain names in a private hosted zone in Route 53, make sure that the `enableDnsHostnames` and `enableDnsSupport` attributes of the VPC are both `true`. For more information, see [DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html#vpc-dns-support).

1. Don’t use both Route 53 and a custom DNS server in the DHCP option set, because the combination can cause unexpected behavior.

For the DNS settings, see [Configure DNS and NTP with a DHCP option set](network-dhcp-dns-ntp.md). For the status check, see [The reachability check failed](troubleshoot-status-checks.md#troubleshoot-reachability).

## The deployment fails because of the VPC Route Server configuration
<a name="troubleshoot-rs-deploy-fails"></a>

 **Cause** 

The route server configuration doesn’t meet the Amazon EVS requirements.

 **Solution** 

Check that your configuration meets each of the following requirements, and deploy again:
+ At least two route server endpoints are in the service access subnet.
+ The route server peer ASN matches the NSX Edge peer ASN of the Tier-0 gateway.
+ Each route server peer uses a unique, unused IP address from the NSX uplink VLAN CIDR block that you specify when you create the environment.
+ Every route table that the route server propagates to has at least one explicit subnet association.

For the setup, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).

## Routes don’t propagate or BGP sessions don’t come up
<a name="troubleshoot-rs-routes"></a>

After deployment, NSX routes don’t appear in your VPC route tables, or the BGP sessions with the route server stay down.

 **Cause** 

A propagated route table has no explicit subnet association, the peer ASNs don’t match, or two peers use the same IP address. BGP route advertisement fails if a propagated route table has no explicit subnet association.

 **Solution** 

1. Verify that each propagated route table has an explicit subnet association.

1. Check that the peer ASN on the route server peers matches the ASN of the NSX Tier-0 gateway.

1. Confirm that each route server peer IP address is unique.

1. Review the route propagation status in your route tables.

1. Use VPC Route Server peer logging to monitor BGP session health and find connection problems. For more information, see [Route server peer logging](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-peer-logging.html) in the * Amazon VPC User Guide*.

Amazon EVS supports only the default BGP keepalive mechanism for peer liveness detection. Amazon EVS doesn’t support multi-hop Bidirectional Forwarding Detection (BFD). For the route server setup, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).

## NSX connectivity fails after the environment is deployed
<a name="troubleshoot-rt-association"></a>

 AWS resources can’t reach virtual machines on NSX network segments.

 **Cause** 

The Amazon EVS VLAN subnets are implicitly associated with the VPC main route table, and you haven’t associated them explicitly with a route table. NSX connectivity fails if the VLAN subnets aren’t explicitly associated with a VPC route table.

 **Solution** 

Explicitly associate each Amazon EVS VLAN subnet with a route table in your VPC. A public HCX VLAN subnet needs a public route table. For the steps, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).

## On-premises systems can’t reach the environment
<a name="troubleshoot-tgw-routes"></a>

 **Cause** 

The transit gateway route tables don’t contain the VPC CIDR blocks that the Amazon EVS environment created. Transit Gateway doesn’t learn NSX overlay routes from VPC Route Server. Amazon EVS doesn’t support connectivity through an Direct Connect private virtual interface, or through an AWS Site-to-Site VPN connection that ends directly in the underlay VPC.

 **Solution** 

1. Update the transit gateway route tables with the VPC CIDR blocks that the environment created. Add static routes for the NSX overlay networks.

1. If you use Direct Connect, update your allowed prefixes so that the Direct Connect gateway sends and receives the updated routes.

For the steps, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).

## Security group rules have no effect on VLAN subnet traffic
<a name="troubleshoot-nacl"></a>

 **Cause** 

Amazon EC2 security groups don’t function on elastic network interfaces that are attached to Amazon EVS VLAN subnets. Until you change the association, the VLAN subnets use the default network ACL of the VPC.

 **Solution** 

1. Find the network ACL that a VLAN subnet uses. In the following command, replace `<subnet-id>` with the ID of the VLAN subnet.

   ```bash
   aws ec2 describe-network-acls \
     --filters Name=association.subnet-id,Values=<subnet-id> \
     --query 'NetworkAcls[0].NetworkAclId' \
     --output text
   ```

   The command returns the ID of the network ACL.

1. Make sure that the network ACL allows the traffic that Amazon EVS requires. If it doesn’t, the environment deployment fails, and an existing environment can have a degraded compliance status.

1. Associate your network ACL with the VLAN subnets, if it isn’t associated.

For the required traffic and the association steps, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).

## You can’t reach the VCF appliances after you add a distributed firewall rule
<a name="troubleshoot-dfw-lockout"></a>

You added an NSX distributed firewall rule, such as a rule that denies all traffic, and you can no longer reach your management appliances.

 **Cause** 

The distributed firewall rule applies to the traffic that you use to reach the appliances.

 **Solution** 

You configure and own the NSX distributed firewall rules in your environment. For how distributed firewall rules work, see [Add a Distributed Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/nsxt-dc/3-2/administration-guide/security/distributed-firewall/add-a-distributed-firewall.html) in the Broadcom documentation. For help with NSX configuration, you can contact Broadcom with your Broadcom support entitlement, or contact AWS Support.

If these steps don’t resolve the problem, see [Get help from AWS Support and Broadcom](get-help.md) for who to contact and what to include in a case.