# Data protection

| HPCSEC02: How do you manage data encryption in your HPC cluster? |
| ---------------------------------------------------------------- |
|                                                                  |

As described in the
[Data
Protection](../security-pillar/data-protection.md "../security-pillar/data-protection.md") section, classifying and protecting data are
foundational practices. The same foundational practices apply to
the data related to your HPC workloads, and once the data is
classified, there are a few additional HPC consideration for
protecting it.

###### Best practices

- [HPCSEC02-BP01 Enforce encryption at rest in your HPC environment](#hpcsec02-bp01 "#hpcsec02-bp01")
- [HPCSEC02-BP02 Enforce encryption in transit in your HPC environment](#hpcsec02-bp02 "#hpcsec02-bp02")

## HPCSEC02-BP01 Enforce encryption at rest in your HPC environment

With
[SEC08-BP01](../security-pillar/sec_protect_data_rest_key_mgmt.md "../security-pillar/sec_protect_data_rest_key_mgmt.md"),
you securely manage encryption keys to protect data at rest. You
also tightly control access through the use of
[key
policies](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") and IAM policies. AWS HPC products, such as AWS ParallelCluster, configure IAM permissions on different
components, such as cluster, queues, and login nodes. Therefore,
cluster users can unencrypt data at rest by IAM permissions
associated with the cluster or component. If your HPC
environment needs further isolation, such as by project or group
separation, consider an architecture with multiple clusters for
data separation by encryption key.

## HPCSEC02-BP02 Enforce encryption in transit in your HPC environment

When implementing
[SEC09-BP02](../security-pillar/sec_protect_data_transit_encrypt.md "../security-pillar/sec_protect_data_transit_encrypt.md"),
you enforce encryption in transit. Tightly coupled HPC
applications using EFA bypass the operating system kernel and
directly communicate with the EFA device rather than traditional
TCP/IP networking. This provides low-latency, reliable
communication between cluster instances but introduces
additional considerations when enforcing encryption in transit
compared to traditional TCP/IP approaches.

AWS provides secure and private connectivity between EC2
instances of all types. In addition, some instance types use the
offload capabilities of the underlying Nitro System hardware to
automatically encrypt in-transit traffic between instances. This
encryption uses Authenticated Encryption with Associated Data
(AEAD) algorithms with 256-bit encryption, which also helps
implement
[SEC09-BP03](../security-pillar/sec_protect_data_transit_authentication.md "../security-pillar/sec_protect_data_transit_authentication.md").
There is no impact on network performance.

Therefore, your EFA traffic is automatically encrypted between
cluster members with no impact to performance. This automatic
encryption is also used with
[FSx for Lustre](../../../fsx/latest/LustreGuide/encryption-in-transit-fsxl.md "../../../fsx/latest/LustreGuide/encryption-in-transit-fsxl.md") and enforcing encryption in transit between
cluster members and an FSx for Lustre filesystem. See
[Encryption
in transit](../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit "../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit") for additional details.
