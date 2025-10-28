# Infrastructure security in AWS Clean Rooms

As a managed service, AWS Clean Rooms is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access AWS Clean Rooms through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.

## Network security

When AWS Clean Rooms reads from your S3 bucket during query execution, the traffic between AWS Clean Rooms
and Amazon S3 is securely routed through the AWS private network. In-flight traffic is signed
using Amazon Signature Version 4 protocol (SIGv4) and encrypted using HTTPS. This traffic
is authorized based on the IAM service role which you have set up for your configured
table.

You can connect programmatically to AWS Clean Rooms through an endpoint. For a list of service
endpoints, see [AWS Clean Rooms endpoints and quotas](../../../general/latest/gr/clean-rooms.md#clean-rooms_region "../../../general/latest/gr/clean-rooms.md#clean-rooms_region") in the _AWS General Reference_.

All service endpoints are HTTPS-only. You can use Amazon Virtual Private Cloud (VPC) endpoints in case you
want to connect to AWS Clean Rooms from your VPC and do not want to have internet connectivity. For
more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

You can assign IAM policies to your IAM principals which make use of the [aws:SourceVpce context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpce "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcevpce") to restrict your IAM principal to only be able to
make calls to AWS Clean Rooms through a VPC endpoint and not over the internet.
