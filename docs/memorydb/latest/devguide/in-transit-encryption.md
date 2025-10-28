# In-transit encryption (TLS) in MemoryDB

To help keep your data secure, MemoryDB and Amazon EC2 provide mechanisms to guard against
unauthorized access of your data on the server. By providing in-transit encryption
capability, MemoryDB gives you a tool you can use to help protect your data when it is moving
from one location to another. For example, you might move data from a primary node to a read
replica node within a cluster, or between your cluster and your application.

###### Topics

- [In-transit encryption overview](#in-transit-encryption-overview "#in-transit-encryption-overview")
- [See also](#in-transit-encryption-see-also "#in-transit-encryption-see-also")

## In-transit encryption overview

MemoryDB in-transit encryption is a feature that increases the
security of your data at its most vulnerable points—when it is in transit from
one location to another.

MemoryDB in-transit encryption implements the following features:

- Encrypted connections—both the server and client
  connections are Transport Layer Security (TLS) encrypted.
- Encrypted replication—data moving between a primary node
  and replica nodes is encrypted.
- Server authentication—clients can authenticate that they
  are connecting to the right server.

From 07/20/2023, TLS 1.2 is the minimum supported version for new and existing clusters.
Use this [link](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/ "https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/") to learn more about TLS 1.2 at AWS.

For more information on connecting to MemoryDB clusters, see [Connecting to MemoryDB nodes using
redis-cli](getting-started.md#connect-tls "getting-started.md#connect-tls").

## See also

- [At-Rest Encryption in MemoryDB](at-rest-encryption.md "at-rest-encryption.md")
- [Authenticating Users with Access Control Lists (ACLs)](clusters.md "clusters.md")
- [MemoryDB and Amazon VPC](vpcs.md "vpcs.md")
- [Identity and access management in MemoryDB](iam.md "iam.md")
