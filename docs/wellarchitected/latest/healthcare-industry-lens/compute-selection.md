# Compute selection

| HCL_PERF2. How do you select your<br>compute solution? |
| ------------------------------------------------------ |
|                                                        |

**Select compute services
that meet regulatory and performance requirements**

Healthcare requirements for compute are generally consistent
with other industries. Guidance from the
[Well-Architected
Framework Compute Architecture Selection](../performance-efficiency-pillar/compute-architecture-selection.md "../performance-efficiency-pillar/compute-architecture-selection.md") still applies.
Healthcare applications can take advantage of virtual
machines, containers, or serverless technologies.

Healthcare applications should enable encryption in-transit at
one of the OSI layers. Some legacy communication protocols,
such as Minimal Lower Layer Protocol (MLLP) for healthcare
interoperability, may not natively support encryption
in-transit. A common industry solution has been to overlay a
VPN or create an IPsec mesh on top of virtual machines in a
VPC to encrypt sensitive data in transit; however, such
approaches can create performance penalties. Instead, where
possible, use
[Amazon EC2 instances with encryption in-transit](../../../AWSEC2/latest/UserGuide/data-protection.md "../../../AWSEC2/latest/UserGuide/data-protection.md") handled by the
underlying Amazon EC2 Nitro System to reduce any performance
penalties associated with inter-Amazon EC2 communication.

You can get a full list of Amazon EC2 instance types that
support this feature with the following CLI command:

```
AWS ec2 describe-instance-types –filters
          Name=network-info.encryption-in-transit-supported,Values=true
          –query “InstanceTypes[*].[InstanceType]” –output text
```
