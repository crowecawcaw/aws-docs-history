#

Guidelines and restrictions for client IP address preservation in Global Accelerator

As you prepare for and use client IP address preservation in AWS Global Accelerator, be aware of the following guidelines
and restrictions.

**General caveats**
When you plan for adding client IP address preservation, be aware of the following. Make sure
that you also review the overall requirements for endpoints in Global Accelerator. For more information, see
[Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md "about-endpoints-caveats.md").

###### Important

When client IP address preservation is enabled, traffic bypasses the following security controls:

- **Gateway Load Balancer (GWLB) inspection:** Traffic does not flow
  through GWLB endpoints, preventing inspection by third-party security appliances.
- **AWS Network Firewall:** Network traffic filtering and
  intrusion prevention rules are not applied to this traffic.
- **Network Access Control Lists (NACLs):** Subnet-level allow and deny
  rules are not evaluated for this traffic.

- VPC Block Public Access is supported with client IP address preservation.
- Before you add and begin to route traffic to endpoints that preserve the client IP address, make sure
  that all your required security configurations, for example, security groups, are updated to include the user client
  IP address on allow lists.
- You might see client IP addresses in AWS WAF, instead of Global Accelerator IP addresses. Client IP addresses appear in
  AWS WAF when you configure Global Accelerator for client IP address preservation and you enable AWS WAF to block connections from your
  Application Load Balancers that don't come from Global Accelerator.
- Client IP address preservation is supported in all AWS Regions where Global Accelerator is supported. For a list of
  supported Regions, see [AWS Region availability for AWS Global Accelerator](preserve-client-ip-address.md "preserve-client-ip-address.md").

**Defaults for client IP address preservation**
When you create a new accelerator using the console, client IP address preservation is enabled, by default,
for supported endpoints. You can choose to disable the option for some endpoints, depending on the endpoint type:

- When you use an internet-facing Application Load Balancer or a Network Load Balancer with security groups as an endpoint with Global Accelerator, client IP address
  preservation is enabled by default for new accelerators. You can choose to disable
  the option when you create the accelerator or by editing the accelerator later.
- When you use an internal Application Load Balancer or an EC2 instance with Global Accelerator, the endpoint always has client IP
  address preservation enabled.

Be aware of the following:

- Internal Application Load Balancers and EC2 instances always have client IP address preservation
  enabled. You can't disable the option for these endpoints.
- When you use the AWS console to create a new accelerator, the option for
  client IP address preservation is enabled by default for Application Load Balancer endpoints.
  The option is not enabled by default for Network Load Balancer with security groups endpoints.
  You can update the option for client IP address preservation for these endpoints at any time
  after you add it.
- When you use the AWS CLI or an API action to create a new accelerator and
  you don't specify the option for client IP address preservation, the following is the
  default setting for client IP address preservation:
  - Internet-facing Application Load Balancer endpoints have client IP address preservation enabled by default.
  - Network Load Balancer with security group endpoints do _not_ have client IP address
    preservation enabled by default.

**Transitioning endpoints without client IP address preservation**
For existing accelerators, you can transition endpoints without client IP address preservation
to endpoints that do preserve the client IP address. For example, existing Application Load Balancer endpoints can be transitioned to
new Application Load Balancer endpoints. To transition to the new endpoints,
we recommend that you move traffic slowly from an existing endpoint to a new endpoint that has client
IP address preservation by doing the following:

- For existing Application Load Balancer or Network Load Balancer with security groups endpoints, first add to Global Accelerator a duplicate load balancer
  endpoint that targets the same backends, and make sure that client IP address preservation is enabled for it.
  Then adjust the weights on the endpoints to slowly move traffic from the load balancer that does
  _not_ have client IP address preservation enabled to the load balancer _with_
  client IP address preservation.
- For an existing Elastic IP address endpoint, you can move traffic to an EC2 instance endpoint
  with client IP address preservation.
  First add an EC2 instance endpoint to Global Accelerator, and then adjust the weights on the endpoints to slowly move traffic
  from the Elastic IP address endpoint to the EC2 instance endpoint.

For step-by-step transition guidance, see [Transitioning endpoints to use client IP address preservation](about-endpoints.md#about-endpoints.transition-to-IP-preservation "about-endpoints.md#about-endpoints.transition-to-IP-preservation").
