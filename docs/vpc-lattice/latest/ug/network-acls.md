

# Control traffic to VPC Lattice using network ACLs
<a name="network-acls"></a>

A network access control list (ACL) allows or denies specific inbound or outbound traffic at the subnet level. The default network ACL allows all inbound and outbound traffic. You can create custom network ACLs for your subnets to provide an additional layer of security. For more information, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon VPC User Guide*.

**Topics**
+ [Network ACLs for your client subnets](#network-acl-client-subnets)
+ [Network ACLs for your target subnets](#network-acl-target-subnets)

## Network ACLs for your client subnets
<a name="network-acl-client-subnets"></a>

The network ACLs for client subnets must allow traffic between clients and VPC Lattice. You can get the IP address ranges to allow from the [managed prefix list](security-groups.md#managed-prefix-list) for VPC Lattice.

The following is an example inbound rule.


| Source | Protocol | Port range | Comment | 
| --- | --- | --- | --- | 
| {{vpc\_lattice\_cidr\_block}} | TCP | 1025-65535 | Allow traffic from VPC Lattice to clients | 

The following is an example outbound rule.


| Destination | Protocol | Port range | Comment | 
| --- | --- | --- | --- | 
| {{vpc\_lattice\_cidr\_block}} | {{listener}} | {{listener}} | Allow traffic from clients to VPC Lattice | 

## Network ACLs for your target subnets
<a name="network-acl-target-subnets"></a>

The network ACLs for target subnets must allow traffic between targets and VPC Lattice on both the target port and the health check port. You can get the IP address ranges to allow from the [managed prefix list](security-groups.md#managed-prefix-list) for VPC Lattice.

The following is an example inbound rule.


| Source | Protocol | Port range | Comment | 
| --- | --- | --- | --- | 
| {{vpc\_lattice\_cidr\_block}} | {{target}} | {{target}} | Allow traffic from VPC Lattice to targets | 
| {{vpc\_lattice\_cidr\_block}} | {{health check}} | {{health check}} | Allow health check traffic from VPC Lattice to targets | 

The following is an example outbound rule.


| Destination | Protocol | Port range | Comment | 
| --- | --- | --- | --- | 
| {{vpc\_lattice\_cidr\_block}} | {{target}} | 1024-65535 | Allow traffic from targets to VPC Lattice | 
| {{vpc\_lattice\_cidr\_block}} | {{health check}} | 1024-65535 | Allow health check traffic from targets to VPC Lattice | 