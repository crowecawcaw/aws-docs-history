#

Requirements for endpoints with client IP address preservation

There are specific requirements for endpoint types that you can use with client IP address preservation.

> You can use this feature with endpoints that are Application Load Balancers, Network Load Balancers with security groups, and Amazon EC2 instances,
> subject to the additional requirements described in this section. Endpoints on custom routing accelerators always
> have the client IP address preserved.

This section provides information that is specific to endpoints that you want to add with client IP
address preservation enabled. For information about overall requirements for endpoints,
see [Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md "about-endpoints-caveats.md").

In addition, for more information about best practices with client IP address
preservation, see [Best practices for ENIs and security groups with client IP address
preservation](best-practices-aga.md "best-practices-aga.md").

If you intend to use the client IP address preservation feature, be aware of the following
when you add endpoints to Global Accelerator, in addition to the overall requirements for
endpoints in Global Accelerator.

**Elastic IP addresses**
Client IP address preservation is not supported for Elastic IP address endpoints
in Global Accelerator.

**Network Load Balancer endpoints**
If you want to enable client IP address preservation when you add Network Load Balancer resources
as endpoints to Global Accelerator, be aware that client IP address preservation is not supported for the
following:

- Network Load Balancers without security groups
- Network Load Balancers with security groups that have TLS listeners attached
- Network Load Balancers with security groups that perform IPv4 to IPv6 NAT translation to their EC2 targets

In addition, for Network Load Balancers, client IP address preservation is supported only when targets are in
the same VPC as the Network Load Balancer. Traffic must flow directly from the Network Load Balancer to the target.

These requirements apply only to Network Load Balancer endpoints, not to other load balancing endpoints,
such as Application Load Balancers.

**Elastic network interfaces**
To support client IP address preservation, Global Accelerator creates elastic network interfaces in your
AWS account—one for each subnet where an endpoint is present. For more information about how Global Accelerator
works with elastic network interfaces, see [Best practices for ENIs and security groups with client IP address
preservation](best-practices-aga.md "best-practices-aga.md").

**Endpoints in private subnets**
You can target an Application Load Balancer, Network Load Balancer, or an EC2 instance in a private subnet using
Global Accelerator but you must have an [internet
gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") attached to the VPC that contains the endpoints. For more information, see
[Secure VPC connections in AWS Global Accelerator](secure-vpc-connections.md "secure-vpc-connections.md").

As a best practice, use private subnets if you want to ensure that traffic
is delivered only by Global Accelerator. Also, make sure that inbound security group rules are configured appropriately
to correctly allow or deny traffic for your applications.

**Add the client IP address to the allow list**
Before you add and begin to route traffic to endpoints that preserve the
client IP address, make sure that all your required security configurations, for example,
security groups, are updated to include the user client IP address on the allow list. Network
access control lists (ACLs) only apply to egress (outbound) traffic. If you need to filter ingress
(inbound) traffic, you must use security groups.

**Configure network access control lists (ACLs)**

Network ACLs associated with your VPC subnets apply to egress (outbound)
traffic when client IP address preservation is enabled on your accelerator. However, for
traffic to be allowed to exit through Global Accelerator, you must configure the ACL as both an inbound and
outbound rule.

For example, to allow TCP and UDP clients using an ephemeral source port to connect
to your endpoint through Global Accelerator, associate the subnet of your endpoint with a
Network ACL that allows outbound traffic destined to an ephemeral TCP or UDP port (port range
1024-65535, destination 0.0.0.0/0). In addition, create a matching inbound rule (port range
1024-65535, source 0.0.0.0/0).

Be aware of the following for security groups and WAF:

- Security group and AWS WAF rules are an additional set of capabilities that you can
  apply to protect your resources. For example, the inbound security group rules associated
  with your Amazon EC2 instances and Application Load Balancers allow you to control the destination ports that clients
  can connect to through Global Accelerator, such as port 80 for HTTP or port 443 for HTTPS.
- Amazon EC2 instance security groups apply to any traffic
  that arrives to your instances, including traffic from Global Accelerator and any public or Elastic IP address that
  is assigned to your instance.
