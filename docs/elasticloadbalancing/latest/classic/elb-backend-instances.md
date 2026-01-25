# Registered instances for your Classic Load Balancer

After you've created your Classic Load Balancer, you must register your EC2 instances with the
load balancer. You can select EC2 instances from a single Availability Zone or multiple
Availability Zones within the same Region as the load balancer. Elastic Load Balancing routinely performs
health checks on registered EC2 instances, and automatically distributes incoming requests
to the DNS name of your load balancer across the registered, healthy EC2 instances.

###### Contents

- [Best practices for your instances](#backend-instance-best-practices "#backend-instance-best-practices")
- [Recommendations for your VPC](#set-up-ec2 "#set-up-ec2")
- [Register instances with your load balancer](elb-deregister-register-instances.md "elb-deregister-register-instances.md")
- [Health checks](elb-healthchecks.md "elb-healthchecks.md")
- [Security groups](elb-instances-security-groups.md "elb-instances-security-groups.md")
- [Network ACLs](elb-instances-network-acls.md "elb-instances-network-acls.md")

## Best practices for your instances

- You must ensure that the load balancer can communicate with your
  instances on both the listener port and the health check port. For more information, see
  [Configure security groups for your Classic Load Balancer](elb-vpc-security-groups.md "elb-vpc-security-groups.md").
  The security group for your instances must allow traffic in both directions
  on both ports for each subnet for your load balancer.
- Install a web server, such as Apache or Internet Information Services (IIS),
  on all instances that you plan to register with your load balancer.
- For HTTP and HTTPS listeners, we recommend that you enable the keep-alive
  option in your EC2 instances, which enables the load balancer to re-use the
  connections to your instances for multiple client requests. This reduces the load
  on your web server and improves the throughput of the load balancer. The
  keep-alive timeout should be at least 60 seconds to ensure that the load
  balancer is responsible for closing the connection to your instance.
- Elastic Load Balancing supports Path Maximum Transmission Unit (MTU) Discovery. To ensure that
  Path MTU Discovery can function correctly, you must ensure that the security group
  for your instance allows ICMP fragmentation required (type 3, code 4) messages.
  For more information, see [Path MTU Discovery](../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery "../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery") in the _Amazon EC2 User Guide_.

## Recommendations for your VPC

###### Virtual private cloud (VPC)

Unless you created your AWS account before 2014, you have a default VPC in each Region.
You can use a default VPC for your load balancer, if you have one, or you can create a new VPC.
For more information, see the _[Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md")_.

###### Subnets for your load balancer

To ensure that your load balancer can scale properly, verify that each subnet for
your load balancer has a CIDR block with at least a `/27` bitmask (for
example, `10.0.0.0/27`) and has at least 8 free IP addresses. Your load
balancer uses these IP addresses to establish connections with the instances, and to
scale out when necessary. If there are insufficient IP addresses, the load balancer
might be unable to scale, causing 503 errors due to insufficient capacity.

Create a subnet in each Availability Zone where you want to launch instances. Depending
on your application, you can launch your instances in public subnets, private subnets,
or a combination of public and private subnets. A public subnet has a route to an
internet gateway. Note that default VPCs have one public subnet per Availability Zone
by default.

When you create a load balancer, you must add one or more public subnets to the load
balancer. If your instances are in private subnets, create public subnets in the same
Availability Zones as the subnets with your instances; you will add these public subnets
to the load balancer.

###### Network ACLs

The network ACLs for your VPC must allow traffic in both directions on the listener port
and the health check port. For more information, see [Network ACLs for the instances for your Classic Load Balancer](elb-instances-network-acls.md "elb-instances-network-acls.md").
