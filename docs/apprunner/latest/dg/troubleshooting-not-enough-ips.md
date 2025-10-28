# When there are not enough IP addresses for launching instances or scaling

###### Note

For public services, App Runner does not create an Elastic Network Interface (ENI) in your VPCs, so your public services are not affected
by this change.

This guide helps you resolve IP exhaustion errors you may encounter on App Runner services with VPC access for outgoing traffic enabled.

App Runner will launch instances in the subnets associated with your VPC connector. App Runner creates 1 ENI per
instance in the subnet where your instance is launched. Each ENI uses a private IP in that subnet. Subnets have
fixed number of IPs available, depending on the CIDR block associated with that subnet. If App Runner is unable
to find subnet(s) with sufficient IPs to create an ENI, it will fail to launch new instances for your App Runner
service. This may lead to issues with scaling up your services. In such cases you will see App Runner event
logs indicating that App Runner is unable to find subnets with available IPs. You can update your services with
instructions below to resolve such errors.

## How to update your services to have more available IPs

Number of IP addresses available in a subnet is based on the CIDR block associated with that subnet. CIDR
blocks associated with a subnet cannot be updated after creation. App Runner VPC connectors can also not be
updated once they are created. To provide more IPs to your App Runner services with VPC access for outgoing traffic enabled :

1. Create new subnet(s) with a larger CIDR block.
2. Create a new VPC connector with the new subnet(s).
3. Update your App Runner service to use the new VPC connector.

## Calculating IPs needed for your services

Before attempting to create new subnet(s) with larger CIDR blocks, determine the number of IPs you will need
across your App Runner services. We recommend calculating number of IPs needed in your connector as follows :

1. For each services with VPC access for outgoing traffic enabled, note the
   [max size (maximum instances)](manage-autoscaling.md "manage-autoscaling.md") in the auto scaling configuration.
2. Sum the values across all services.
3. Double this sum to account for the new instances launched during blue-green deployments.

### Example

Consider two services A and B using the same VPC connector.

1. Service A has the max size configured as 25.
2. Service B has max size configured as 15.

**Required IPs** = 2 × (25 + 15) = 80

Ensure your subnets have at least 80 available IPs combined.

## Create new subnet(s)

1. Determine the CIDR block size needed for IPv4 using this formula (Note that 5 IPs are reserved by AWS:
   [Subnet Sizing](../../../vpc/latest/userguide/subnet-sizing.md "../../../vpc/latest/userguide/subnet-sizing.md"))

```
Number of available IP addresses = 2^(32 - prefix length) - 5
```

```
Example :
For 192.168.1.0/24:
Prefix length is 24
Number of available IP addresses = 2^(32 - 24) - 5 = 2^8-5 = 251 IP addresses

For 10.0.0.0/16:
Prefix length is 16
Number of available IP addresses = 2^(32 - 16) - 5 = 2^16-5 = 65,531 IP addresses

Quick reference:
/24 = 251 IP addresses
/16 = 65,531 IP addresses
```

2. Create a new subnet by using the AWS EC2 CLI.

```
aws ec2 create-subnet --vpc-id <my-vpc-id> --cidr-block <cidr-block>
```

Example (creates a subnet with 4,096 IPs) :

```
aws ec2 create-subnet --vpc-id my-vpc-id --cidr-block 10.0.0.0/20
```

3. Create a new VPC connector. See : [Manage VPC Access](network-vpc.md "network-vpc.md")
4. Update your services with outgoing traffic to VPC enabled to use this new VPC connector.App Runner
   will start using the new subnets once your service is updated.

###### Note

VPCs are also limited with number of available IPs that can be allocated to the subnets by CIDR
blocks. If you are unable to create subnets with larger CIDR blocks, you might need to update your VPC
with secondary CIDR blocks before creating the new subnet(s).

## Attaching Secondary CIDR blocks to your VPC

Associate secondary CIDR block to this VPC.

```
 aws ec2 associate-vpc-cidr-block --vpc-id <my-vpc-id> --cidr-block <cidr-block>
```

Example :

```
aws ec2 associate-vpc-cidr-block --vpc-id my-vpc-id --cidr-block 10.1.0.0/16
```

## Verification

Once you have updated your service. You can use the following to perform verification of your fix

1. **Monitor event logs :** Monitor your App Runner service event [logs](monitor-cwl.md "monitor-cwl.md")
   to validate no new IP or ENI unavailability errors show up
2. **Check Service Scaling:**
   1. Fully scale up service by changing the min instance count in your autoscaling configuration
   2. Verify that all new instances are launched without any IP-related errors
   3. Monitor through several scaling events to ensure consistent performance

3. **Console Banner:** If you're using the AWS Management Console, confirm that
   App Runner no longer displays a banner warning about insufficient IPs.
4. **VPC and Subnet IP Utilization:**
   1. Use the VPC Dashboard or CLI commands to check IP address utilization in your new subnets.
   2. Confirm that there's still a healthy margin of available IPs after your service has scaled up

## Common Pitfalls

When addressing IP exhaustion in App Runner services, be aware of these potential issues:

1. **Inadequate IP Address Planning:** Underestimating future IP needs can lead to
   recurring exhaustion issues. Conduct thorough capacity planning, considering potential service
   growth and peak usage scenarios.
2. **Overlooking VPC-wide IP Usage:** Remember that other AWS services within the
   same VPC also consume IP addresses. Consider the IP requirements of all services when planning your
   VPC and subnet configurations.
3. **Neglecting to Update Services:** After creating new subnets or VPC connectors,
   ensure you update your App Runner services to use the new configurations. Failure to do so will result in
   continued use of the exhausted IP range.
4. **Misunderstanding CIDR Block Overlaps:** When adding secondary CIDR blocks to a
   VPC, ensure they don't overlap with existing blocks. Overlapping CIDR blocks can cause routing
   conflicts and IP address ambiguity.
5. **Exceeding VPC Limits:** Be aware that a VPC can have a maximum of 5
   CIDR blocks (1 primary and 4 secondary). Plan your IP address space expansion within these constraints.
6. **Ignoring Subnet AZ Distribution:** When creating new subnets, ensure they are
   distributed across multiple Availability Zones for high availability and fault tolerance.
7. **Overlooking ENI Limits:** Remember that there are limits to the number of ENIs
   that can be attached to instances. Verify that your AWS account limits align with your
   planned network interface usage.

By being aware of these pitfalls, you can more effectively manage your VPC resources and avoid IP
exhaustion issues in your App Runner services.

## Additional Resources

1. [AWS VPC Documentation](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")
2. [Understanding CIDR Blocks](../../../vpc/latest/userguide/how-it-works.md#VPC_Sizing "../../../vpc/latest/userguide/how-it-works.md#VPC_Sizing")
3. [App Runner VPC Connectors](network-vpc.md "network-vpc.md")

## Glossary

1. **ENI:**Elastic Network Interface, a virtual network interface in AWS.
2. **CIDR:**Classless Inter-Domain Routing, a method for allocating IP addresses.
3. **VPC Connector:** A resource that enables App Runner to connect to your VPC.
