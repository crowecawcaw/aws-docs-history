# Infrastructure security in Elastic Load Balancing

As a managed service, ELB is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access ELB through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.

## Network isolation

A virtual private cloud (VPC) is a virtual network in your own logically isolated area
in the AWS Cloud. A subnet is a range of IP addresses in a VPC. When you create a load
balancer, you can specify one or more subnets for the load balancer nodes. You can deploy
EC2 instances in the subnets of your VPC and register them with your load balancer. For
more information about VPC and subnets, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

When you create a load balancer in a VPC, it can be either internet-facing or internal.
An internal load balancer can only route requests that come from clients with access to
the VPC for the load balancer.

Your load balancer sends requests to its registered targets using private IP addresses.
Therefore, your targets do not need public IP addresses in order to receive requests from
a load balancer.

To call the ELB API from your VPC using private IP addresses, use AWS PrivateLink. For
more information, see [Access ELB using an interface endpoint (AWS PrivateLink)](load-balancer-vpc-endpoints.md "load-balancer-vpc-endpoints.md").

## Controlling network traffic

Consider the following options for securing network traffic when you use a load
balancer:

- Use secure listeners to support encrypted communication between clients
  and your load balancers. Application Load Balancers support HTTPS listeners. Network Load Balancers support TLS
  listeners. Classic Load Balancers support both HTTPS and TLS listeners. You can choose from
  predefined security policies for your load balancer to specify the cipher
  suites and protocol versions that are supported by your application. You can
  use AWS Certificate Manager (ACM) or AWS Identity and Access Management (IAM) to manage the server certificates
  installed on your load balancer. You can use the Server Name Indication
  (SNI) protocol to serve multiple secure websites using a single secure
  listener. SNI is automatically enabled for your load balancer when you
  associate more than one server certificate with a secure listener.
- Configure the security groups for your Application Load Balancers and Classic Load Balancers to accept traffic only
  from specific clients. These security groups must allow inbound traffic from clients
  on the listener ports and outbound traffic to the clients.
- Configure the security groups for your Amazon EC2 instances to accept traffic only from
  the load balancer. These security groups must allow inbound traffic from the load
  balancer on the listener ports and the health check ports.
- Configure your Application Load Balancer to securely authenticate users through an identity
  provider or using corporate identities. For more information, see [Authenticate users
  using an Application Load Balancer](../application/listener-authenticate-users.md "../application/listener-authenticate-users.md").
- Use [AWS WAF](../../../waf/latest/developerguide/waf-chapter.md "../../../waf/latest/developerguide/waf-chapter.md") with your
  Application Load Balancers to allow or block requests based on the rules in a web access control
  list (web ACL).
