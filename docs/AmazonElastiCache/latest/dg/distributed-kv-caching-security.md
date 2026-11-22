

# Security in distributed KV caching

Distributed key-value (KV) caching uses the same security model as ElastiCache for Valkey. For the security of ElastiCache, see [Security in Amazon ElastiCache](security.md). The following sections describe only the security settings that are specific to distributed KV caching.

**Topics**
+ [Infrastructure security](#distributed-kv-caching-security.efa-security-group)
+ [Access control](#distributed-kv-caching-security.access)
+ [Data protection](#distributed-kv-caching-security.encryption)
+ [Security best practices for distributed KV caching](#distributed-kv-caching-security.best-practices)
+ [Compliance validation](#distributed-kv-caching-security.compliance)

## Infrastructure security
<a name="distributed-kv-caching-security.efa-security-group"></a>

For infrastructure security in ElastiCache, see [Infrastructure security in AWS ElastiCache](infrastructure-security.md).

Elastic Fabric Adapter (EFA) requires a security group with a self-referencing inbound rule and a self-referencing outbound rule. Attach it to the cluster, and to the primary interface and every `efa` and `efa-only` interface of each client host. For the commands, see [Step 2: Create a security group](distributed-kv-caching-getting-started.md#distributed-kv-caching-getting-started.security-group).

## Access control
<a name="distributed-kv-caching-security.access"></a>

Role-based access control (RBAC) users and user groups control data access. To add a user group when you create the cluster, use `--user-group-ids`. For more information, see [Role-Based Access Control (RBAC)](Clusters.RBAC.md).

AWS Identity and Access Management (IAM) authentication is available for Valkey clients. For more information, see [Authenticating with IAM in ElastiCache](auth-iam.md). LMCache doesn't support IAM authentication. LMCache connects with an RBAC user and a password.

The `@largeobj` access control list (ACL) category contains all large object commands. For the categories of each command, see [Large object ACLs](large-objects.md#large-objects-acl).

### Valkey user for LMCache
<a name="distributed-kv-caching-security.lmcache-user"></a>

Limit the Valkey user of LMCache to the LMCache keys and to the commands of its transport. Replace {{key-prefix}} with the `key_prefix` value that LMCache uses. For the access string of the `rdma` transport, see [Step 8: Connect your inference engine](distributed-kv-caching-getting-started.md#distributed-kv-caching-getting-started.configure).

For the `blob-tcp` transport, use the following access string. Each LMCache worker sends `BLOB.INFO __lmcache_blob_tcp_probe__` when it connects. Without the probe key in the access string, LMCache doesn't start.

```
on ~{{key-prefix}}@* ~__lmcache_blob_tcp_probe__ +@largeobj +EXISTS +DEL +EXPIRE +INFO +PING +client|setinfo +client|setname +cluster|slots +cluster|info
```

For the `tcp` transport, use the following access string. The `tcp` transport sets the time to live (TTL) in the same `SET` command, so it doesn't need `@largeobj` or `+EXPIRE`.

```
on ~{{key-prefix}}@* +GET +SET +EXISTS +DEL +INFO +PING +client|setinfo +client|setname +cluster|slots +cluster|info
```

## Data protection
<a name="distributed-kv-caching-security.encryption"></a>

For more information about encryption in ElastiCache, see [Data security in Amazon ElastiCache](encryption.md).

### Encryption in transit
<a name="distributed-kv-caching-security.in-transit"></a>

A distributed KV caching cluster requires encryption in transit, with `TransitEncryptionMode` set to `required`. You can't turn off encryption in transit or change this mode. Transport Layer Security (TLS) protects all commands and replies, the data that `BLOB.TCP_SET` and `BLOB.TCP_GET` send, and the `SET` and `GET` data of the LMCache `tcp` transport.

With `BLOB.RDMA_SET` and `BLOB.RDMA_GET`, the object data moves over EFA, and TLS doesn't protect it. The AWS Nitro System hardware automatically encrypts traffic between `cache.i8ge.48xlarge` nodes and supported client instance types in the same VPC with 256-bit authenticated encryption with associated data (AEAD). To check whether your client instance type is supported, see [Encryption in transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) in the Amazon EC2 User Guide. For more information about how remote direct memory access (RDMA) data and client memory regions are handled, see [Security](https://valkey.io/topics/large-object-configuration/#security) on the valkey.io website.

### Encryption at rest
<a name="distributed-kv-caching-security.at-rest"></a>

A hardware module on the instance always encrypts data on the Non-Volatile Memory Express (NVMe) instance storage of the node with an XTS-AES-256 cipher, and destroys the keys when the node is replaced or terminated. ElastiCache also removes all data from NVMe storage when a node starts or shuts down.

Encryption at rest is always on, and you can't turn it off. Data on NVMe storage is also encrypted at rest with a key from AWS Key Management Service (AWS KMS). By default, ElastiCache uses an AWS owned key. To use a customer managed key, specify it with `--kms-key-id` when you create the cluster. For more information, see [Using customer managed keys from AWS KMS](at-rest-encryption.md#using-customer-managed-keys-for-elasticache-security).

## Security best practices for distributed KV caching
<a name="distributed-kv-caching-security.best-practices"></a>

In addition to the security practices for ElastiCache (see [Security in Amazon ElastiCache](security.md)), use the following practices for a distributed KV caching cluster:
+ Remove the `@largeobj` category (`-@largeobj`) from users that don't need the large object commands.
+ Use a dedicated EFA security group that contains only the cluster and its client hosts.
+ Use client instance types that support Nitro encryption in transit for RDMA traffic.
+ Check the RDMA error counters in `INFO largeobj`. For more information, see [Node-level detail with INFO largeobj](distributed-kv-caching-monitoring.md#distributed-kv-caching-monitoring.info).

## Compliance validation
<a name="distributed-kv-caching-security.compliance"></a>

For all security topics for ElastiCache, see [Security in Amazon ElastiCache](security.md), and for compliance information, see [Compliance validation for Amazon ElastiCache](elasticache-compliance.md).