# Describe your VPC network architecture

Amazon VPC enables you to define a logically isolated virtual network in the AWS Cloud,
known as a virtual private cloud (VPC). Create separate VPCs to isolate infrastructure
by workload or organizational entity. You can configure your VPCs by selecting
IP address ranges, configuring routing, and adding network gateways to connect
your VPCs to each other, the internet, or to your own corporate network. You
launch AWS resources, such as EC2 instances or RDS instances, in your VPCs.

The following table describes the key characteristics of a VPC network. A network
administrator can use this guidance to describe the architecture and configuration of
your VPC network. Having this information enables them to configure a functionally
equivalent network on premises or using another Cloud Provider.

| Characteristic                                                                             | Description                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Geographic location](#vpc-network-geographic-location "#vpc-network-geographic-location") | Amazon VPC is hosted in all AWS Regions world-wide. You can select the Regions<br>for your VPC network that put your AWS resources closest to your customers.                                                                                                            |
| [Subnets](#vpc-network-subnets "#vpc-network-subnets")                                     | The subnets that you define for your VPCs define network boundaries and<br>determine the IP addresses for your AWS resources. You can add subnets in<br>multiple Availability Zones to increase the availability of your resources.                                      |
| [Network connectivity](#vpc-network-connectivity "#vpc-network-connectivity")              | The gateways that you attach to your VPCs or subnets to provide connectivity<br>between your VPC network and other networks, such as other VPCs or subnets,<br>the internet, or your on-premises networks.                                                               |
| [Security controls](#vpc-network-security-controls "#vpc-network-security-controls")       | The security groups that you create for your VPCs control traffic<br>to and from the associated resources, such as compute resources,<br>database resources, and load balancers. Each subnet has a network ACL<br>that controls traffic entering and leaving the subnet. |
| [Traffic management](#vpc-network-traffic-management "#vpc-network-traffic-management")    | Routing rules control the traffic flow between subnets, VPCs, and external<br>locations. The load balancers provided by Elastic Load Balancing distribute incoming traffic<br>across multiple targets, such as EC2 instances, containers, and Lambda functions.          |

## Geographic location

Amazon VPC is available in every AWS Region world-wide. Each Region is a separate geographic
area. You can lower network latency when you create VPCs for your resources in Regions
that are close to the majority of your users.

You can use Amazon EC2 Global View to list your VPCs across all Regions using a graphical user
interface (there is no equivalent programmatic interface). With the Amazon VPC console, AWS API,
and AWS command line interfaces, you must list the VPCs and VPC resources for each Region
individually.

###### Why this matters

After you determine where your VPCs are located, you can decide whether
to configure a functionally equivalent network in the same locations or
different locations, depending on your needs.

###### To get a summary of your VPCs across all Regions

1. Open the Amazon EC2 Global View console at [https://console.aws.amazon.com/ec2globalview/home](https://console.aws.amazon.com/ec2globalview/home "https://console.aws.amazon.com/ec2globalview/home").
2. On the **Region explorer** tab, under **Summary**,
   check the resource count for **VPCs**, which includes
   the number of VPCs and the number of Regions. This includes both default
   VPCs that AWS creates on your behalf and nondefault VPCs that you create.
   Click the underlined text to see how the VPC count is spread across Regions.
   If a Region has only one VPC, it is most likely the default VPC for the Region.
3. On the **Global search** tab, select the client filter
   **Resource type = Vpc**. You can filter the results
   further by specifying a Region or a tag.

###### To get the VPCs in a Region using the AWS CLI

Use the following [describe-vpcs](../../../cli/latest/reference/ec2/describe-vpcs.md "../../../cli/latest/reference/ec2/describe-vpcs.md") command. You must run this command in each Region
where you have VPCs. The `--query` parameter includes only the
VPC IDs in the output. You can include additional fields as needed.

```
aws ec2 describe-vpcs \
    --region `us-east-2` \
    --query "Vpcs[*].VpcId"
```

Each Region comes with a default VPC. If you aren't using the default VPCs, you
can exclude them from the results by adding the following filter.

```
--filters Name=is-default,Values=false
```

## Subnets

A subnet is a logical network boundary in a VPC. When you create a subnet, you
assign a block of IP address. Resources that you launch into a subnet are
assigned IP addresses from the block of IP addresses for the subnet. IP addresses
allow resources to communicate with each other over a local network or the internet.

The resource map in the Amazon VPC console provides a visual representation of the
subnets for your VPC.

###### Why this matters

Subnets enables network administrators to implement security boundaries
and control traffic between application tiers. By noting the IP addresses of
your subnets, you can help to ensure that resources in a functionally equivalent
network can communicate with the same clients or applications that they can in
your VPC network.

###### To view the subnets for a VPC using the resource map

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **VPCs**.
3. Select the checkbox for the VPC.
4. Choose the **Resource map** tab.
5. In the VPC pane, choose **Show details**. The
   **Subnets** pane lists all subnets in the VPC
   and shows their IP address ranges. Hover over a subnet to highlight
   its associated route table and network connections. For more detail,
   click the link to open the subnet detail page.

###### To describe the subnets for a VPC using the AWS CLI

Use the following [describe-subnets](../../../cli/latest/reference/ec2/describe-subnets.md "../../../cli/latest/reference/ec2/describe-subnets.md") command. The `--filters` parameter scopes
the search to describe the subnets for the specified VPC. The `--query`
parameter includes only the specified fields in the output. You can include
additional fields as needed.

```
aws ec2 describe-subnets \
    --filters Name=vpc-id,Values=`vpc-1234567890abcdef0` \
    --query Subnets[*].[SubnetId,AvailabilityZoneId,CidrBlock,Ipv6CidrBlockAssociationSet[0].Ipv6CidrBlock] \
    --output table
```

The following is example output. The columns are subnet ID, AZ ID, IPv4 address range,
and the first IPv6 address range (if any).

```
---------------------------------------------------------------------------------------
|                                   DescribeSubnets                                   |
+---------------------------+-----------+----------------+----------------------------+
|  subnet-0d2d1b81e0bc9c6d4 |  usw2-az1 |  10.0.144.0/20 |  2600:1f14:1e6e:a003::/64  |
|  subnet-0e01d500780bb7468 |  usw2-az1 |  10.0.16.0/20  |  2600:1f14:1e6e:a001::/64  |
|  subnet-0eb17d85f5dfd33b1 |  usw2-az2 |  10.0.128.0/20 |  2600:1f14:1e6e:a002::/64  |
|  subnet-0e990c67809773b19 |  usw2-az2 |  10.0.0.0/20   |  2600:1f14:1e6e:a000::/64  |
+---------------------------+-----------+----------------+----------------------------+
```

## Network connectivity

The connectivity options provided by Amazon VPC enable you to create a network that
spans VPCs in multiple accounts and Regions and remote networks.

You can use the resource map in the Amazon VPC console to discover whether your VPCs
use internet gateways, egress-only internet gateways, NAT gateways, or gateway
VPC endpoints. The resource map does not show any transit gateways, peering
connections, virtual private gateways, or other types of VPC endpoints that
are in use. You can get the complete list of gateways and peering connections for
a VPC by describing them one at a time using the console, the API, or a command-line
interface.

###### Why this matters

After you understand the connectivity provided by your VPC network,
you can ensure that resources in a functionally equivalent network
can communicate with the same local and remote resources.

###### To view the network connections for a VPC using the resource map

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **VPCs**.
3. Select the checkbox for the VPC.
4. Choose the **Resource map** tab.
5. In the VPC pane, choose **Show details**. The
   **Network connections** pane lists any internet
   gateways, egress-only internet gateways, NAT gateways, and gateway
   VPC endpoints. If the resource type isn't clear, hover over the
   link icon for the network connection and examine the resulting
   URL. This URL is a link to the resource in the console, and it
   contains the resource type and resource ID (for example,
   internetGatewayId=igw-0123456780abcdef).

###### To get the network connections for your VPCs using the AWS CLI

1. Use the following [describe-internet-gateways](../../../cli/latest/reference/ec2/describe-internet-gateways.md "../../../cli/latest/reference/ec2/describe-internet-gateways.md") command to get the
   internet gateways for the specified Region. The `--query` parameter
   includes only the specified fields in the output. You can include additional
   fields as needed.

```
aws ec2 describe-internet-gateways \
    --region `us-east-2` \
    --query InternetGateways[*].[Attachments[0].VpcId,InternetGatewayId] \
    --output table
```

The following is example output. The columns show the VPC IDs and internet gateway
IDs.

```
----------------------------------------------------
|             DescribeInternetGateways             |
+------------------------+-------------------------+
|  None                  |  igw-04c61dba10EXAMPLE  |
|  vpc-0bf4c2739bEXAMPLE |  igw-09737a4029EXAMPLE  |
|  vpc-060415a18fEXAMPLE |  igw-0c562bd22aEXAMPLE  |
|  vpc-0ea9d41094EXAMPLE |  igw-0e06f7033dEXAMPLE  |
|  vpc-03b86de356EXAMPLE |  igw-0a9ff72d05EXAMPLE  |
+------------------------+-------------------------+
```

2. Use the following [describe-egress-only-internet-gateways](../../../cli/latest/reference/ec2/describe-egress-only-internet-gateways.md "../../../cli/latest/reference/ec2/describe-egress-only-internet-gateways.md") command to get the
   egress-only internet gateways for the specified Region. The `--query`
   parameter includes only the specified fields in the output. You can include
   additional fields as needed.

```
aws ec2 describe-egress-only-internet-gateways \
    --region `us-east-2` \
    --query EgressOnlyInternetGateways[*].[Attachments[0].VpcId,EgressOnlyInternetGatewayId] \
    --output table
```

The following is example output. The columns show the VPC IDs and the egress-only internet
gateway IDs.

```
-----------------------------------------------------
|        DescribeEgressOnlyInternetGateways         |
+------------------------+--------------------------+
|  vpc-060415a18fEXAMPLE |  eigw-0b8ca558acEXAMPLE  |
+------------------------+--------------------------+
```

3. Use the following [describe-nat-gateways](../../../cli/latest/reference/ec2/describe-nat-gateways.md "../../../cli/latest/reference/ec2/describe-nat-gateways.md") command to get the NAT gateways for the
   specified Region. The `--query` parameter includes only the specified
   fields in the output. You can include additional fields as needed.

```
aws ec2 describe-nat-gateways \
    --region `us-east-2` \
    --query NatGateways[*].[VpcId,NatGatewayId,SubnetId] \
    --output table
```

The following is example output. The columns show the VPC IDs, NAT gateway IDs, and subnet
IDs.

```
---------------------------------------------------------------------------------
|                              DescribeNatGateways                              |
+------------------------+-------------------------+----------------------------+
|  vpc-060415a18fEXAMPLE |  nat-026316334aEXAMPLE  |  subnet-0eb17d85f5EXAMPLE  |
|  vpc-060415a18fEXAMPLE |  nat-0f08bc5f52EXAMPLE  |  subnet-0d2d1b81e0EXAMPLE  |
+------------------------+-------------------------+----------------------------+
```

4. Use the following [describe-transit-gateway-vpc-attachments](../../../cli/latest/reference/ec2/describe-transit-gateway-vpc-attachments.md "../../../cli/latest/reference/ec2/describe-transit-gateway-vpc-attachments.md") command to get the transit
   gateway VPC attachments for the specified Region. The `--query`
   parameter includes only the specified fields in the output. You can include
   additional fields as needed.

```
aws ec2 describe-transit-gateway-vpc-attachments \
    --region `us-east-2` \
    --query TransitGatewayVpcAttachments[*].[VpcId,TransitGatewayId,length(SubnetIds[])] \
    --output table
```

The following is example output. The columns show the VPC IDs, transit gateway IDs, and
the count of subnets.

```
---------------------------------------------------------
|         DescribeTransitGatewayVpcAttachments          |
+------------------------+-------------------------+----+
|  vpc-0bf4c2739bEXAMPLE |  tgw-055dc4e47bEXAMPLE  |  4 |
|  vpc-0ea9d41094EXAMPLE |  tgw-055dc4e47bEXAMPLE  |  2 |
+------------------------+-------------------------+----+
```

5. Use the following [describe-vpc-peering-connections](../../../cli/latest/reference/ec2/describe-vpc-peering-connections.md "../../../cli/latest/reference/ec2/describe-vpc-peering-connections.md") command to get the
   peering connections for the VPCs in the specified Region. The `--query`
   parameter includes only the specified fields in the output. You can include
   additional fields as needed.

```
aws ec2 describe-vpc-peering-connections \
    --region `us-east-2` \
    --query VpcPeeringConnections[*].[AccepterVpcInfo.VpcId,RequesterVpcInfo.VpcId] \
    --output table
```

The following is example output. The columns show the accepter VPC IDs, accepter VPC
owners, requester VPC IDs, and requester VPC owners.

```
------------------------------------------------------------------------------------
|                          DescribeVpcPeeringConnections                           |
+------------------------+---------------+------------------------+----------------+
|  vpc-0ea9d41094EXAMPLE |  123456789012 |  vpc-03b86de356EXAMPLE |  123456789012  |
+------------------------+---------------+------------------------+----------------+
```

6. Use the following [describe-vpn-gateways](../../../cli/latest/reference/ec2/describe-vpn-gateways.md "../../../cli/latest/reference/ec2/describe-vpn-gateways.md") command to get the virtual private gateways
   for the specified Region. The `--query` parameter includes only the
   specified fields in the output. You can include additional fields as needed.

```
aws ec2 describe-vpn-gateways \
    --region `us-east-2` \
    --query VpnGateways[*].[VpcAttachments[0].VpcId,VpnGatewayId] \
    --output table
```

The following is example output. The columns show the VPC IDs and virtual
private gateway IDs.

```
----------------------------------------------------
|                DescribeVpnGateways               |
+------------------------+-------------------------+
|  vpc-0bf4c2739bEXAMPLE |  vgw-0cb3226c4aEXAMPLE  |
+------------------------+-------------------------+
```

7. Use the following [describe-vpc-endpoints](../../../cli/latest/reference/ec2/describe-vpc-endpoints.md "../../../cli/latest/reference/ec2/describe-vpc-endpoints.md") command to get the VPC endpoints for the
   specified Region. The `--query` parameter includes only the specified
   fields in the output. You can include additional fields as needed.

```
aws ec2 describe-vpc-endpoints \
    --region `us-east-2` \
    --query 'VpcEndpoints[*].[VpcId,VpcEndpointType,ServiceName||ServiceNetworkArn||ResourceConfigurationArn]' \
    --output table
```

The following is example output. The first column shows the VPC ID and the second column
shows the VPC endpoint type. The third column depends on the endpoint type, and
shows either the service name, resource configuration ARN, or service network
ARN.

```
----------------------------------------------------------------------------------------------------------------------------------------
|                                                         DescribeVpcEndpoints                                                         |
+------------------------+-----------------+-------------------------------------------------------------------------------------------+
|  vpc-060415a18fcc9afde |  Interface      |  com.amazonaws.vpce.us-west-2.vpce-svc-007832a03d60fc387                                  |
|  vpc-060415a18fcc9afde |  Interface      |  com.amazonaws.vpce.us-west-2.vpce-svc-007832a03d60fc387                                  |
|  vpc-0bf4c2739bc05a694 |  Gateway        |  com.amazonaws.us-west-2.s3                                                               |
|  vpc-0ea9d410947d27b7d |  Interface      |  com.amazonaws.us-west-2.logs                                                             |
|  vpc-0bf4c2739bc05a694 |  Resource       |  arn:aws:vpc-lattice:us-east-2:123456789012:resourceconfiguration/rcfg-07129f3acded87625  |
|  vpc-0bf4c2739bc05a694 |  ServiceNetwork |  arn:aws:vpc-lattice:us-east-2:123456789012:servicenetwork/sn-0808d1748faee0c1e           |
|  vpc-0bf4c2739bc05a694 |  ServiceNetwork |  arn:aws:vpc-lattice:us-east-2:123456789012:servicenetwork/sn-0808d1748faee0c1e           |
+------------------------+-----------------+-------------------------------------------------------------------------------------------+
```

## Security controls

The security controls provided by Amazon VPC determine network access to your VPCs
and the resources deployed in your VPCs.

###### Why this matters

After you determine the inbound traffic allowed to reach your subnets and
resources and the output traffic allowed to leave your subnets and resources,
you can plan the firewall rules needed for a functionally equivalent network.

###### Security controls

- [Security groups](#vpc-network-security-groups "#vpc-network-security-groups")
- [Network ACLs](#vpc-network-acls-subnet "#vpc-network-acls-subnet")

### Security groups

A security group allows specific inbound and outbound traffic at the resource level.
Security groups are the primary mechanism to control access to resources in your VPCs.

###### To get the security groups for your VPCs

Use the following [describe-security-groups](../../../cli/latest/reference/ec2/describe-security-groups.md "../../../cli/latest/reference/ec2/describe-security-groups.md") command to display the security groups
for the specified VPC.

```
aws ec2 describe-security-groups \
    --filters Name=vpc-id,Values=`vpc-1234567890abcdef0` \
    --query SecurityGroups[*].GroupId
```

###### To get the inbound rules for a security group

Use the following [describe-security-group-rules](../../../cli/latest/reference/ec2/describe-security-group-rules.md "../../../cli/latest/reference/ec2/describe-security-group-rules.md") command to display the rules for the
specified security group where `IsEgress` is `false`.

```
aws ec2 describe-security-group-rules \
    --filters Name=group-id,Values=`sg-0abcdef1234567890` \
    --query 'SecurityGroupRules[?IsEgress==`false`]'
```

###### To get the outbound rules for a security group

Use the following [describe-security-group-rules](../../../cli/latest/reference/ec2/describe-security-group-rules.md "../../../cli/latest/reference/ec2/describe-security-group-rules.md") command to display the rules for the
specified security group where `IsEgress` is `true`.

```
aws ec2 describe-security-group-rules \
    --filters Name=group-id,Values=`sg-0abcdef1234567890` \
    --query 'SecurityGroupRules[?IsEgress==`true`]'
```

### Network ACLs

A network access control list (ACL) allows or denies specific inbound and outbound
traffic at the subnet level. You can use network ACLs as defense-in-depth in case a
resource is deployed without the correct security group.

###### To get the network ACLs for your subnets

Use the following [describe-network-acls](../../../cli/latest/reference/ec2/describe-network-acls.md "../../../cli/latest/reference/ec2/describe-network-acls.md") command to display the network ACLs
for the specified VPC and their subnet associations.

```
aws ec2 describe-network-acls \
    --filters Name=vpc-id,Values=`vpc-1234567890abcdef0` \
    --query "NetworkAcls[*].{ID:NetworkAclId,Subnets:Associations[].SubnetId}"
```

###### To get the inbound rules for a network ACL

Use the following [describe-network-acls](../../../cli/latest/reference/ec2/describe-network-acls.md "../../../cli/latest/reference/ec2/describe-network-acls.md") command to display the rules for the
specified network ACL where `Egress` is `false`.

```
aws ec2 describe-network-acls \
    --network-acl-ids `acl-0abcdef1234567890` \
    --query 'NetworkAcls[*].Entries[?Egress==`false`]'
```

###### To get the outbound rules for a network ACL

Use the following [describe-network-acls](../../../cli/latest/reference/ec2/describe-network-acls.md "../../../cli/latest/reference/ec2/describe-network-acls.md") command to display the rules for the
specified network ACL where `Egress` is `true`.

```
aws ec2 describe-network-acls \
    --network-acl-ids `acl-0abcdef1234567890` \
    --query 'NetworkAcls[*].Entries[?Egress==`true`]'
```

## Traffic management

Effective traffic management combines the network-level routing decisions provided by
route tables with the application-level distribution strategies provided by load balancing.

###### Why this matters

Network administrators must design subnets, routing, DNS resolution, and load balancing
to optimize traffic flow while maintaining security boundaries and performance requirements.
By noting the configuration of these components in your VPC network, you can help to ensure
that resources in a functionally equivalent network can communicate with the same clients
or devices that they can in your VPC network.

###### Traffic management

- [Route tables](#vpc-network-traffic-routing "#vpc-network-traffic-routing")
- [DHCP option set](#vpc-network-dhcp-options "#vpc-network-dhcp-options")
- [Load balancers](#vpc-network-traffic-elb "#vpc-network-traffic-elb")

### Route tables

Route tables determine how network traffic flows across network boundaries such as
subnets, VPCs, on-premises networks, and the internet.

The resource map in the Amazon VPC console provides a visual representation of the
route tables for your VPC.

###### To view the route tables for a VPC using the resource map

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **VPCs**.
3. Select the checkbox for the VPC.
4. Choose the **Resource map** tab.
5. The **Route tables** pane lists all route tables for the VPC.
   Hover over a route table to highlight its associated subnets and network
   connections. For more detail, click the link to open the route table detail page.

###### To describe your route tables

Use the [describe-route-tables](../../../cli/latest/reference/ec2/describe-route-tables.md "../../../cli/latest/reference/ec2/describe-route-tables.md") command to describe the route tables
for the specified VPC and their subnet associations.

```
aws ec2 describe-route-tables \
    --filters Name=vpc-id,Values=`vpc-1234567890abcdef0` \
    --query "RouteTables[*].{ID:RouteTableId,Subnets:Associations[].SubnetId}"
```

###### To get the routes for a route table

Use the [describe-route-tables](../../../cli/latest/reference/ec2/describe-route-tables.md "../../../cli/latest/reference/ec2/describe-route-tables.md") command to describe the routes for
the specified route table.

```
aws ec2 describe-route-tables \
    --route-table-ids `rtb-02ec01715bEXAMPLE` \
    --query RouteTables[*].Routes
```

### DHCP option set

Your VPC has a DHCP option set that you can use to configure various network
settings. For example, you can configure custom DNS servers so that your EC2
instances can resolve internal host names using your existing DNS infrastructure.
For more information, see [DHCP option set concepts](DHCPOptionSetConcepts.md "DHCPOptionSetConcepts.md").

###### To describe the DHCP options for your VPC

Use the [describe-dhcp-options](../../../cli/latest/reference/ec2/describe-dhcp-options.md "../../../cli/latest/reference/ec2/describe-dhcp-options.md") command to describe the specified
DHCP options. The example also gets the ID of the DHCP options for the
specified VPC using the [describe-vpcs](../../../cli/latest/reference/ec2/describe-vpcs.md "../../../cli/latest/reference/ec2/describe-vpcs.md") command.

```
aws ec2 describe-dhcp-options \
    --dhcp-options-id "$(aws ec2 describe-vpcs \
        --vpc-id `vpc-1234567890abcdef0` \
        --query Vpcs[].DhcpOptionsId --output text)"
```

The following is example output for a VPC that uses the default DHCP options.

```
{
    "DhcpOptions": [
        {
            "OwnerId": "415546850671",
            "Tags": [],
            "DhcpOptionsId": "dopt-1234567890abcdef0",
            "DhcpConfigurations": [
                {
                    "Key": "domain-name",
                    "Values": [
                        {
                            "Value": "us-west-2.compute.internal"
                        }
                    ]
                },
                {
                    "Key": "domain-name-servers",
                    "Values": [
                        {
                            "Value": "AmazonProvidedDNS"
                        }
                    ]
                }
            ]
        }
    ]
}
```

### Load balancers

Load balancing distributes incoming traffic from clients across multiple targets.
Load balancers monitor the health of targets and automatically remove unhealthy
targets from traffic distribution, ensuring that only healthy targets are used. This
improves the availability and performance of your application and optimizes resource
utilization. For more information, see the [Elastic Load Balancing User Guide](../../../elasticloadbalancing/latest/userguide.md "../../../elasticloadbalancing/latest/userguide.md").

###### To describe your load balancers

Use the [describe-load-balancers](../../../cli/latest/reference/elbv2/describe-load-balancers.md "../../../cli/latest/reference/elbv2/describe-load-balancers.md") command to display the load balancers for the
specified VPC.

```
aws elbv2 describe-load-balancers \
    --query 'LoadBalancers[?VpcId==``vpc-1234567890abcdef0``].LoadBalancerArn'
```

## Related resources

The following are optional services or features that you might be using in your
VPC network:

- [Direct Connect](../../../directconnect/latest/UserGuide.md "../../../directconnect/latest/UserGuide.md")
- [AWS Network Firewall](../../../network-firewall/latest/developerguide.md "../../../network-firewall/latest/developerguide.md")
- [IPAM](../ipam.md "../ipam.md")
- [Traffic mirroring](../mirroring.md "../mirroring.md")
- [VPC flow logs](flow-logs.md "flow-logs.md")
