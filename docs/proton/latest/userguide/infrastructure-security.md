End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Infrastructure security in AWS Proton

As a managed service, AWS Proton is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access AWS Proton through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  To improve network isolation, you can use AWS PrivateLink as described in the following section.

## AWS Proton and interface VPC endpoints (AWS PrivateLink)

You can establish a private connection between your VPC and AWS Proton by creating an _interface VPC
endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you to privately access AWS Proton APIs without an internet gateway,
NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with AWS Proton APIs. Traffic between your VPC and AWS Proton does not leave the Amazon
network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your subnets.

For more information, see [Interface VPC endpoints
(AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.

### Considerations for AWS Proton VPC endpoints

Before you set up an interface VPC endpoint for AWS Proton, ensure that you review [Interface endpoint properties and
limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

AWS Proton supports making calls to all of its API actions from your VPC.

VPC endpoint policies are supported for AWS Proton. By default, full access to AWS Proton is allowed through the
endpoint. For more information, see [Controlling access to
services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

### Creating an interface VPC endpoint for AWS Proton

You can create a VPC endpoint for the AWS Proton service using either the Amazon VPC console or the AWS Command Line Interface
(AWS CLI). For more information, see [Creating
an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for AWS Proton using the following service name:

- com.amazonaws.`region`.proton

If you enable private DNS for the endpoint, you can make API requests to AWS Proton using its default DNS name
for the Region, for example, `proton.`region`.amazonaws.com`.

For more information, see [Accessing a service through an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the _Amazon VPC User Guide_.

### Creating a VPC endpoint policy for AWS Proton

You can attach an endpoint policy to your VPC endpoint that controls access to AWS Proton. The policy specifies
the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services
with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for AWS Proton actions

The following is an example of an endpoint policy for AWS Proton. When attached to an endpoint, this policy
grants access to the listed AWS Proton actions for all principals on all resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Principal": "*",
 "Action": [
 "proton:ListServiceTemplates",
 "proton:ListServiceTemplateMajorVersions",
 "proton:ListServiceTemplateMinorVersions",
 "proton:ListServices",
 "proton:ListServiceInstances",
 "proton:ListEnvironments",
 "proton:GetServiceTemplate",
 "proton:GetServiceTemplateMajorVersion",
 "proton:GetServiceTemplateMinorVersion",
 "proton:GetService",
 "proton:GetServiceInstance",
 "proton:GetEnvironment",
 "proton:CreateService",
 "proton:UpdateService",
 "proton:UpdateServiceInstance",
 "proton:UpdateServicePipeline",
 "proton:DeleteService"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```
