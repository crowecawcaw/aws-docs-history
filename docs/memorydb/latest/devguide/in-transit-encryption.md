

# In-transit encryption (TLS) in MemoryDB
<a name="in-transit-encryption"></a>

To help keep your data secure, MemoryDB and Amazon EC2 provide mechanisms to guard against unauthorized access of your data on the server. By providing in-transit encryption capability, MemoryDB gives you a tool you can use to help protect your data when it is moving from one location to another. For example, you might move data from a primary node to a read replica node within a cluster, or between your cluster and your application.

**Topics**
+ [In-transit encryption overview](#in-transit-encryption-overview)
+ [See also](#in-transit-encryption-see-also)

## In-transit encryption overview
<a name="in-transit-encryption-overview"></a>

MemoryDB in-transit encryption is a feature that increases the security of your data at its most vulnerable points—when it is in transit from one location to another.

MemoryDB in-transit encryption implements the following features:
+ **Encrypted connections**—both the server and client connections are Transport Layer Security (TLS) encrypted.
+ **Encrypted replication—**data moving between a primary node and replica nodes is encrypted.
+ **Server authentication**—clients can authenticate that they are connecting to the right server.

From 07/20/2023, TLS 1.2 is the minimum supported version for new and existing clusters. Use this [link](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/) to learn more about TLS 1.2 at AWS.

**Certificate Transparency logging**  
MemoryDB provisions a TLS certificate that includes the cluster name for every cluster endpoint. AWS Certificate Manager records publicly trusted TLS certificates in public, append-only Certificate Transparency logs. As a result, every MemoryDB cluster name appears in public Certificate Transparency logs. Don't include confidential or sensitive information in cluster names. For more information about Certificate Transparency logging, see [Certificate Transparency logging](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency) in the *AWS Certificate Manager User Guide*.

For more information on connecting to MemoryDB clusters, see [Connecting to MemoryDB nodes using redis-cli](getting-started.md#connect-tls).

## See also
<a name="in-transit-encryption-see-also"></a>
+ [At-Rest Encryption in MemoryDB](at-rest-encryption.md)
+ [Authenticating Users with Access Control Lists (ACLs)](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html)
+ [MemoryDB and Amazon VPC](vpcs.md)
+ [Identity and access management in MemoryDB](iam.md)