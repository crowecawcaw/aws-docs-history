

# Reachability Analyzer explanation codes
<a name="explanation-codes"></a>

If a destination is not reachable, Reachability Analyzer provides one or more explanation codes to help you diagnose and address network misconfiguration.

**Topics**
+ [Path is not reachable](#path-not-reachable-codes)
+ [Configuration](#configuration-codes)
+ [Search filter codes](#search-filter-codes)

## Path is not reachable
<a name="path-not-reachable-codes"></a>

The following explanation codes indicate that the path analysis determined that the path is not reachable.

**BAD\_STATE**  
This component is not in a functional state.

**BAD\_STATE\_ATTACHMENT**  
The attachment between these components is not in a functional state.

**BAD\_STATE\_ROUTE**  
This route is not in a functional state.

**BAD\_STATE\_VPN**  
This VPN connection is not in a functional state.

**CANNOT\_ROUTE**  
This route can't transmit traffic because its destination CIDR or prefix list does not match the destination address of the packet.

**ELB\_ACL\_RESTRICTION**  
Classic Load Balancers apply network ACLs to outbound traffic, even if it's destined for a target in the same subnet as the load balancer.

**ELB\_INSTALLED\_AZ\_RESTRICTION**  
This load balancer can send traffic only to targets in Availability Zones that are enabled for the load balancer.

**ELB\_LISTENER\_PORT\_RESTRICTION**  
This Classic Load Balancer listener allows only inbound traffic destined for the specified port, and outbound traffic with the specified destination port.

**ELB\_LISTENERS\_MISMATCH**  
This Classic Load Balancer does not have a listener that accepts the traffic.

**ELB\_NOT\_CROSSZONE**  
This load balancer can't send traffic to some targets because cross-zone load balancing is disabled.

**ELBV2\_LISTENER\_HAS\_NO\_TG**  
This listener is associated with target groups that have no targets.

**ELBV2\_LISTENER\_PORT\_RESTRICTION**  
This listener does not accept traffic unless it has the specified destination port.

**ELBV2\_LISTENER\_REQUIRES\_TG\_ACCEPT**  
This listener does not have a target group that accepts the traffic.

**ELBV2\_LISTENERS\_MISMATCH**  
This load balancer does not have a listener that accepts the traffic.

**ELBV2\_NO\_TARGETS\_IN\_AZ**  
The load balancer does not have targets in the specified Availability Zones.

**ELBV2\_SOURCE\_ADDRESS\_PRESERVATION**  
If source address preservation is enabled, the outgoing source address is unaltered while traversing the Network Load Balancer.

**ENI\_ADDRESS\_RESTRICTION**  
This network interface does not allow inbound or outbound traffic unless the source or destination address matches its private IP address.

**ENI\_SG\_RULES\_MISMATCH**  
This security group has no inbound or outbound rules that apply.

**ENI\_SOURCE\_DEST\_CHECK\_RESTRICTION**  
Network interfaces with source/destination check enabled reject inbound traffic if the destination address does not match one of its private IP addresses, and reject outbound traffic if the source address does not match one of their private IP addresses.

**FIREWALL\_RULES\_RESTRICTION**  
The traffic is blocked by a matching Network Firewall firewall rule.

**GATEWAY\_REJECTS\_SPOOFED\_TRAFFIC**  
Gateways reject traffic with spoofed addresses from the VPC.

**GWLB\_DESTINATION\_PORT\_RESTRICTION**  
Traffic between a Gateway Load Balancer and its targets must use port 6081 as the destination port. To analyze connectivity through a Gateway Load Balancer, specify port 6081 in the path definition.

**GWLB\_PROTOCOL\_RESTRICTION**  
Traffic between a Gateway Load Balancer and its targets must use the GENEVE protocol, which is UDP-based. To analyze connectivity through a Gateway Load Balancer, specify the UDP protocol in the path definition.

**HIGHER\_PRIORITY\_ROUTE**  
This route table contains a route to the destination that can't be used because there is a higher priority route with the same destination CIDR.

**IGW\_DESTINATION\_ADDRESS\_IN\_VPC\_CIDRS**  
Internet gateways accept traffic only if the destination address is within the VPC CIDR block.

**IGW\_DESTINATION\_ADDRESS\_NOT\_IN\_RFC1918\_EGRESS**  
Internet gateways reject outbound traffic with destination addresses in the private IP address range (see [RFC1918](https://www.rfc-editor.org/rfc/rfc1918)).

**IGW\_DESTINATION\_ADDRESS\_NOT\_IN\_RFC6598\_EGRESS**  
Internet gateways reject outbound traffic with destination addresses in the shared IP address range (see [RFC6598](https://www.rfc-editor.org/rfc/rfc6598)).

**IGW\_NAT\_REFLECTION**  
The path has an internet gateway as an intermediate component, which Reachability Analyzer does not support. Instead, analyze the path from the source to the internet gateway and then analyze the path from the internet gateway to the destination.

**IGW\_PRIVATE\_IP\_ASSOCIATION\_FOR\_INGRESS**  
Internet gateways reject inbound traffic with a destination address that is not the public IP address of a network interface in the VPC with an available attachment.

**IGW\_PUBLIC\_IP\_ASSOCIATION\_FOR\_EGRESS**  
Traffic can't reach the internet through the internet gateway if the source address is not paired with a public IP address or if the source address does not belong to a network interface in the VPC with an available attachment.

**IGW\_SOURCE\_ADDRESS\_NOT\_IN\_RFC1918\_INGRESS**  
Internet gateways reject inbound traffic with source addresses in the private IP address range (see [RFC1918](https://www.rfc-editor.org/rfc/rfc1918)).

**IGW\_SOURCE\_ADDRESS\_NOT\_IN\_RFC6598\_INGRESS**  
Internet gateways reject inbound traffic with source addresses in the shared IP address range (see [RFC6598](https://www.rfc-editor.org/rfc/rfc6598)).

**INGRESS\_RTB\_NO\_PUBLIC\_IP**  
A middlebox appliance can't receive traffic from the internet through an ingress route table if it does not have a public IP address.

**INGRESS\_RTB\_TRAFFIC\_REDIRECTION**  
Subnets whose traffic is redirected to a middlebox appliance can't use a direct route to the internet gateway even when the subnet route table provides one.

**MORE\_SPECIFIC\_ROUTE**  
The specified route can't be used to transmit traffic because there is a more specific route that matches. You can use filters to require that a path include a specific intermediate component.

**NGW\_DEST\_ADDRESS\_PRESERVATION**  
NAT gateways do not alter destination addresses.

**NGW\_REQUIRES\_SOURCE\_IN\_VPC**  
NAT gateways can only transmit traffic that originates from network interfaces within the same VPC. NAT gateways can't transmit traffic that originates from peering connections, VPN connections, or Direct Connect.

**NGW\_SOURCE\_ADDRESS\_REASSIGN**  
NAT gateways transform the source's addresses in outbound traffic to match its private IP address.

**NO\_POSSIBLE\_DESTINATION**  
The network component can't deliver the packet to any possible destination, or the network component sent traffic to a destination in another account or Region. If the destination is in another account, [enable cross-account analyses](multi-account.md).

**NO\_ROUTE\_TO\_DESTINATION**  
The route table does not have an applicable route to the destination resource.

**PCX\_REQUIRES\_ADDRESS\_IN\_VPC\_CIDR**  
Traffic can traverse this peering connection only if the destination or source address is within the CIDR block of the destination VPC.

**PROTOCOL\_RESTRICTION**  
This component only accepts traffic with specific protocols.

**REGIONAL\_NGW\_ROUTE\_AZ\_RESTRICTION**  
The regional NAT gateway is not registered in the Availability Zone where the traffic originates.

**REMAP\_EPHEMERAL\_PORT**  
Outbound traffic from a NAT gateway or load balancer has the source port remapped to an ephemeral port in the range [1024–65535].

**SG\_HAS\_NO\_RULES**  
This security group has no inbound or outbound rules.

**SG\_REFERENCES\_NOT\_PRESERVED**  
The network component discards security group information about forwarded traffic. This prevents traffic from being accepted by security group rules that accept traffic only from a source or destination that belongs to a security group.

**SG\_REFERENCING\_SUPPORT**  
The transit gateway VPC attachment does not have security group referencing support enabled. Therefore, we discard security group information about forwarded traffic.

**SUBNET\_ACL\_RESTRICTION**  
Inbound or outbound traffic for a subnet must be admitted by the network ACL for the subnet.

**TARGET\_ADDRESS\_RESTRICTION**  
A load balancer can only route traffic that is destined for the address of one of its targets.

**TARGET\_PORT\_RESTRICTION**  
A load balancer can only route traffic to a target using its registered port.

**TGW\_ATTACH\_MISSING\_TGW\_RTB\_ASSOCIATION**  
This transit gateway attachment doesn't have a valid transit gateway route table association.

**TGW\_ATTACH\_VPC\_AZ\_RESTRICTION**  
Traffic from a VPC attachment in the default mode can't be forwarded to the network interface in this Availability Zone because it comes from an Availability Zone where the attachment has a different network interface. Traffic from a VPC attachment in appliance mode can't be forwarded to the network interface in this Availability Zone because on the forward path it used a different Availability Zone.

**TGW\_BAD\_STATE\_VPN**  
This VPN connection is in a non-functional state.

**TGW\_ROUTE\_AZ\_RESTRICTION**  
This transit gateway is not registered in the Availability Zone where the traffic originates. The VPC attachment must have a subnet association in the Availability Zone.

**TGW\_RTB\_BAD\_STATE\_ROUTE**  
This transit gateway route table has a route to the destination that is in a bad state.

**TGW\_RTB\_CANNOT\_ROUTE**  
This transit gateway route table has a route to the intended destination, but the route does not match the packet destination address.

**TGW\_RTB\_HIGHER\_PRIORITY\_ROUTE**  
This transit gateway route table contains a route to the intended destination that can't be used because there is a higher-priority route with the same destination CIDR.

**TGW\_RTB\_MORE\_SPECIFIC\_ROUTE**  
This transit gateway route table has a route to the destination, but there is a more specific route.

**TGW\_RTB\_NO\_ROUTE\_TO\_TGW\_ATTACHMENT**  
This transit gateway route table has no route to this transit gateway attachment.

**TGW\_RTB\_ROUTES\_ARE\_UNKNOWN**  
The routes of this transit gateway route table are not known. This might be due to an internal error or because the transit gateway route table does not belong to the account running the analysis.

**UNKNOWN\_DESTINATION**  
The path can't be extended because the information about the destination is insufficient.

**UNKNOWN\_PEERED\_SGS**  
One of the VPCs in the VPC peering connection is unknown. This is typically because the VPC is in a different account. Access controls referencing security groups are treated as inaccessible and deny traffic crossing this peering connection.

**UNKNOWN\_RESOURCE**  
Reachability Analyzer can't analyze this resource because it can't describe the resource.

**VGW\_PRIVATE\_IP\_ASSOCIATION\_FOR\_EGRESS**  
Virtual private gateways can't accept outbound traffic if the source address does not belong to a network interface in the VPC with an available attachment.

**VGW\_PRIVATE\_IP\_ASSOCIATION\_FOR\_INGRESS**  
Virtual private gateways can't accept inbound traffic if the destination address is not the private IP address of a network interface in the VPC with an available attachment.

**VPC\_BLOCK\_PUBLIC\_ACCESS\_ENABLED**  
Internet traffic is blocked because [VPC Block Public Access](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) (BPA) is enabled.

**VPC\_LOCAL\_ROUTE\_CIDR\_RESTRICTION**  
Local routes apply only to packets with a destination address within the VPC CIDR block.

**VPCE\_GATEWAY\_EGRESS\_SOURCE\_ADDRESS\_RESTRICTION**  
VPC gateway endpoints emit only traffic with source addresses within the CIDRs of their corresponding prefix lists.

**VPCE\_GATEWAY\_PROTOCOL\_RESTRICTION**  
VPC gateway endpoints accept only TCP or ICMP ECHO traffic, and emit only TCP or ICMP ECHO reply traffic.

**VPCE\_INTRA\_VPC\_TRAFFIC**  
A VPC endpoint can't initiate connections to resources in the same VPC where it is deployed. Instead, analyze the path in the reverse direction.

**VPCE\_SERVICE\_NOT\_INSTALLED\_IN\_AZ**  
The VPC endpoint service is not installed in the specified Availability Zone.

## Configuration
<a name="configuration-codes"></a>

The following explanation codes indicate that the path analysis determined that no path is possible.

**DISCONNECTED\_VPCS**  
The source and destination are in separate VPCs that are not connected by a supported resource.

**NO\_PATH**  
Reachability Analyzer was unable to find a path from the source to the destination. The following are the most common causes:  
+ The path does not meet the optional configuration details, such as an IP address, port, or filter.
+ The source or destination components are temporarily isolated from the network (for example, a newly started instance that does not yet have a network interface).
+ The source can't initiate traffic to the destination (for example, an interface VPC endpoint or gateway VPC endpoint can't initiate connections with components in the same VPC as the VPC endpoint).
+ The path requires the ability to analyze an unsupported feature (for example, IPv6) or an unsupported network component.

**NO\_SOURCE\_OR\_DESTINATION**  
The source or destination resource does not exist.

**UNASSOCIATED\_COMPONENT**  
The component is not associated with a VPC in your account (for example, a recently terminated instance), or none of its network interfaces has an IPv4 address.

**UNSUPPORTED\_COMPONENT**  
The component is not supported by Reachability Analyzer.

## Search filter codes
<a name="search-filter-codes"></a>

The following explanation codes indicate that the path analysis couldn't find a path from the source to the destination that matched the specified filters. However, there might be a path that matches some of the specified filters. Verify that the filters are as intended. Otherwise, remove the filters that didn't match.

**COMPONENT\_FILTER\_RESTRICTION**  
There is no path that traverses the specified component.

**COMPONENT\_FILTER\_RESTRICTION\_REMOVED\_COMPONENT**  
There is no path that traverses the specified component because of an intermediate component filter.

**FILTER\_AT\_DESTINATION\_DESTINATION\_ADDRESS**  
There is no path that matches the specified destination IP address at the destination.

**FILTER\_AT\_DESTINATION\_DESTINATION\_PORT\_RANGE**  
There is no path that matches the specified destination port range at the destination.

**FILTER\_AT\_DESTINATION\_PROTOCOL**  
There is no path that matches the specified destination protocol.

**FILTER\_AT\_DESTINATION\_SOURCE\_ADDRESS**  
There is no path that matches the specified source address at the destination.

**FILTER\_AT\_DESTINATION\_SOURCE\_PORT\_RANGE**  
There is no path that matches the specified source port range at the destination.

**FILTER\_AT\_SOURCE\_DESTINATION\_ADDRESS**  
There is no path that matches the specified destination IP address at the source.

**FILTER\_AT\_SOURCE\_DESTINATION\_PORT\_RANGE**  
There is no path that matches the specified destination port range at the source.

**FILTER\_AT\_SOURCE\_PROTOCOL**  
There is no path that matches the specified protocol.

**FILTER\_AT\_SOURCE\_SOURCE\_ADDRESS**  
There is no path that matches the specified source IP address at the source.

**FILTER\_AT\_SOURCE\_SOURCE\_PORT\_RANGE**  
There is no path that matches the specified source port range at the source.

**IGW\_EXPECTS\_PUBLIC\_ADDRESS**  
IP addresses must be public IP addresses when the resource is an internet gateway.