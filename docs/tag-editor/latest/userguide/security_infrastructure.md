# Infrastructure security in Tag Editor

Tag Editor doesn't provide additional ways of isolating service or network traffic. If
applicable, use AWS specific isolation. You can use the Tag Editor API and console in a
virtual private cloud (VPC) to help maximize privacy and infrastructure security.

You use AWS published API calls to access Tag Editor through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TSL 1.2 and recommend TSL 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern
  systems such as Java 7 and later support these modes.
  Additionally, requests must be signed by using an access key ID and a secret access key
  that is associated with an AWS Identity and Access Management (IAM) principal. Or, you can use the [AWS Security Token Service](../../../STS/latest/APIReference.md "../../../STS/latest/APIReference.md") (AWS STS) to generate
  temporary security credentials to sign requests.

Tag Editor does not support resource-based policies.

You can call Tag Editor API operations from any network location, but Tag Editor does support
resource-based access policies, which can include restrictions based on the source IP
address. You can also use Tag Editor policies to control access from specific Amazon Virtual Private Cloud (Amazon VPC)
endpoints or specific VPCs. Effectively, this approach isolates network access to a given
resource from only the specific VPC within the AWS network.
