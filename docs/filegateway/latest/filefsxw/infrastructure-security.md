Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Infrastructure security in

AWS Storage Gateway

As a managed service, AWS Storage Gateway is protected by the AWS global network security
procedures that are described in [Security Pillar - AWS Well-Architected Framework](../../../wellarchitected/latest/security-pillar/welcome.md "../../../wellarchitected/latest/security-pillar/welcome.md").

You use AWS published API calls to access Storage Gateway through the network. Clients
must support Transport Layer Security (TLS) 1.2. Clients must also support cipher suites
with perfect forward secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve
Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support these
modes.

Additionally, requests must be signed by using an access key ID and a secret access key
that is associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.

###### Note

You should treat the AWS Storage Gateway appliance as a managed virtual machine, and
should not attempt to access or modify its installation in any way. Attempting to
install scanning software or update any software packages using methods other than the
normal gateway update mechanism, may cause the gateway to malfunction and could impact
our ability to support or fix the gateway.

AWS reviews, analyzes, and remediates CVEs on a regular basis. We incorporate fixes
for these issues into Storage Gateway as part of our normal software release cycle. These fixes
are typically applied as part of the normal gateway update process during scheduled
maintenance windows. For more information about gateway updates, see [Managing
gateway updates using the AWS Storage Gateway console](MaintenanceManagingUpdate-common.md "MaintenanceManagingUpdate-common.md").
