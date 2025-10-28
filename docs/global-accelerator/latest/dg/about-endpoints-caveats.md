# Requirements for resources you add as accelerator endpoints

Be aware of the following requirements and limitations for different types of resources that you can add as endpoints
for standard accelerators in AWS Global Accelerator. Some requirements apply regardless of the type of resource that you
add.

**All resource types**

- Before you enable client IP address preservation for an endpoint, there are additional requirements to keep
  in mind. For more information, see [Transition endpoints with client IP address preservation](about-endpoints.md "about-endpoints.md").
- To add an endpoint to a dual-stack accelerator, the endpoint must have client IP address preservation enabled.
- When you add resources as endpoints behind Global Accelerator, we recommend that you don't
  also send traffic directly to the same endpoints over the internet. Sending direct traffic can lead to connection
  collision issues. For more information, see
  [How to avoid connection collisions that result in TCP connection time delays](about-endpoints.md "about-endpoints.md").
- The resources that you add as endpoints for an accelerator and the accelerator itself must be owned by the
  same account, unless you configure cross-account support. However, the target instances behind a load balancer endpoint can be owned by different accounts.
  In this scenario, the accounts that own the target instances must be given permission to access a subnet owned by the
  account that owns the load balancer and accelerator. For more information, see
  [Configure cross-account access in Global Accelerator](cross-account-resources.md "cross-account-resources.md").
- Before you terminate or delete a resource that you've added as an endpoint behind an accelerator, we recommend
  that you remove the endpoint from Global Accelerator endpoint groups.

**Application Load Balancer endpoints**

- An Application Load Balancer endpoint can be internet-facing or internal.
- Dual-stack Application Load Balancers can be added as endpoints.
- Global Accelerator only supports Application Load Balancers running inside an AWS Region. Global Accelerator does not support an Application Load Balancer running
  as an endpoint in a Local Zone.

**Network Load Balancer endpoints**

- A Network Load Balancer endpoint can be internet-facing or internal.
- Client IP address preservation is only supported for Network Load Balancers that support security groups.
- Client IP address preservation is supported for Network Load Balancers with TCP and UDP listeners, but not with
  TLS termination.
- Dual-stack Network Load Balancers can be added as endpoints for IPv4 or dual-stack accelerators, but there are a few restrictions:
  - For IPv4 accelerators, when you add a dual-stack Network Load Balancer, you cannot enable client
    IP address preservation for the endpoint in Global Accelerator.
  - The Network Load Balancer must support security groups.

- Global Accelerator only supports Network Load Balancers running inside an AWS Region. Global Accelerator does not support a Network Load Balancer running
  as an endpoint in a Local Zone.
- For Network Load Balancer endpoints, we recommend that you disable cross-zone traffic for the load balancers to
  avoid connection collisions, which can result in increased TCP connection time. For more information, see
  [How to avoid connection collisions that result in TCP connection time delays](about-endpoints.md "about-endpoints.md").
- Global Accelerator does not support using shared subnets to target Network Load Balancer endpoints with client
  IP address preservation.
- Global Accelerator does not support upgrading to dual-stack an existing IPv4 accelerator
  with Network Load Balancer endpoints.

If you plan to update to dual-stack an IPv4 accelerator that has existing traffic towards
a Network Load Balancer endpoint, you must first remove the Network Load Balancer endpoint, then update the accelerator.
This will result in a period of downtime for the Network Load Balancer, during the update. Then,
after the update is complete, you can add the Network Load Balancer endpoint again so that traffic
can resume.

**Amazon EC2 instance endpoints**

- An EC2 instance endpoint can't be one of the following types: C1, CC1, CC2, CG1,
  CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, or T1.
- EC2 instances are supported as endpoints in specific AWS Regions. For more information,
  see [AWS Region availability for AWS Global Accelerator](preserve-client-ip-address.md "preserve-client-ip-address.md").

Global Accelerator only supports EC2 instances inside an AWS Region. Global Accelerator does not support routing to an Elastic
IP address as an endpoint in a Local Zone.

- We recommend that you remove an
  EC2 instance from Global Accelerator endpoint groups before you terminate the instance. If you terminate an EC2
  instance before you remove it from an endpoint group in Global Accelerator,
  and then you create another instance in the same VPC with the same private IP address, and health
  checks pass, Global Accelerator will route traffic to the new endpoint.
- Dual-stack EC2 instances can be added as endpoints. However, the instances must have a primary IPv6
  elastic network interface (ENI) attached to them. For more information, see [Work with network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md#working-with-enis "../../../AWSEC2/latest/UserGuide/using-eni.md#working-with-enis") in the Amazon Elastic Compute Cloud User Guide.

**Elastic IP addresses**

- Dual-stack Elastic IP addresses cannot be added as endpoints.
