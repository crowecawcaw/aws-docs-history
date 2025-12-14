# Security Hub CSPM controls for Amazon EMR

These AWS Security Hub CSPM controls evaluate the Amazon EMR (previously called Amazon Elastic MapReduce) service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [EMR.1] Amazon EMR cluster primary nodes should not have public IP addresses

**Related requirements:** PCI DSS v3.2.1/1.2.1,PCI DSS v3.2.1/1.3.1,PCI DSS v3.2.1/1.3.2,PCI DSS v3.2.1/1.3.4,PCI DSS v3.2.1/1.3.6, PCI DSS v4.0.1/1.4.4, NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network configuration

**Severity:** High

**Resource type:**
`AWS::EMR::Cluster`

**AWS Config rule:**
[emr-master-no-public-ip](../../../config/latest/developerguide/emr-master-no-public-ip.md "../../../config/latest/developerguide/emr-master-no-public-ip.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether master nodes on Amazon EMR clusters have public IP addresses. The control
fails if public IP addresses are associated with any of the master node instances.

Public IP addresses are designated in the `PublicIp` field of the
`NetworkInterfaces` configuration for the instance. This control only checks Amazon EMR
clusters that are in a `RUNNING` or `WAITING` state.

### Remediation

During launch, you can control whether your instance in a default or nondefault subnet is
assigned a public IPv4 address. By default, default subnets have this attribute set to `true`. Nondefault
subnets have the IPv4 public addressing attribute set to `false`, unless it was
created by the Amazon EC2 launch instance wizard. In that case, the attribute is set to
`true`.

After launch, you can't manually disassociate a public IPv4 address from your
instance.

To remediate a failed finding, you must launch a new cluster in a VPC with a private subnet that has the
IPv4 public addressing attribute set to `false`. For instructions, see [Launch
clusters into a VPC](../../../emr/latest/ManagementGuide/emr-vpc-launching-job-flows.md "../../../emr/latest/ManagementGuide/emr-vpc-launching-job-flows.md") in the _Amazon EMR Management Guide_.

## [EMR.2] Amazon EMR block public access setting should be enabled

**Related requirements:** PCI DSS v4.0.1/1.4.4, NIST.800-53.r5 AC-21,
NIST.800-53.r5 AC-3,
NIST.800-53.r5 AC-3(7),
NIST.800-53.r5 AC-4,
NIST.800-53.r5 AC-4(21),
NIST.800-53.r5 AC-6,
NIST.800-53.r5 SC-7,
NIST.800-53.r5 SC-7(11),
NIST.800-53.r5 SC-7(16),
NIST.800-53.r5 SC-7(20),
NIST.800-53.r5 SC-7(21),
NIST.800-53.r5 SC-7(3),
NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure access management > Resource not publicly accessible

**Severity:** Critical

**Resource type:**
`AWS::::Account`

**AWS Config rule:**
[emr-block-public-access](../../../config/latest/developerguide/emr-block-public-access.md "../../../config/latest/developerguide/emr-block-public-access.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether your account is configured with Amazon EMR block public access. The control fails if the
block public access setting isn't enabled or if any port other than port 22 is allowed.

Amazon EMR block public access prevents you from launching a cluster in a public subnet if the cluster has a
security configuration that allows inbound traffic from public IP addresses on a port. When a user from your AWS account
launches a cluster, Amazon EMR checks the port rules in the security group for the cluster and compares them with your
inbound traffic rules. If the security group has an inbound rule that opens ports to the public IP addresses
IPv4 0.0.0.0/0 or IPv6 ::/0, and those ports aren't specified as exceptions for your account, Amazon EMR doesn't let the
user create the cluster.

###### Note

Block public access is enabled by default. To increase account protection, we recommend that you keep it enabled.

### Remediation

To configure block public access for Amazon EMR, see [Using Amazon EMR block public access](../../../emr/latest/ManagementGuide/emr-block-public-access.md "../../../emr/latest/ManagementGuide/emr-block-public-access.md")
in the _Amazon EMR Management Guide_.

## [EMR.3] Amazon EMR security configurations should be encrypted at rest

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CP-9(8), NIST.800-53.r5 SI-12

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::EMR::SecurityConfiguration`

**AWS Config rule:**
[emr-security-configuration-encryption-rest](../../../config/latest/developerguide/emr-security-configuration-encryption-rest.md "../../../config/latest/developerguide/emr-security-configuration-encryption-rest.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EMR security configuration has encryption at rest enabled. The control fails if the security configuration doesn't enable encryption at rest.

Data at rest refers to data that's stored in persistent, non-volatile storage for any duration. Encrypting data at rest helps you protect its confidentiality, which reduces the risk that an unauthorized user can access it.

### Remediation

To enable encryption at rest in an Amazon EMR security configuration, see [Configure data encryption](../../../emr/latest/ManagementGuide/emr-create-security-configuration.md#emr-security-configuration-encryption.html "../../../emr/latest/ManagementGuide/emr-create-security-configuration.md#emr-security-configuration-encryption.html") in the _Amazon EMR Management Guide_.

## [EMR.4] Amazon EMR security configurations should be encrypted in transit

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3)

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::EMR::SecurityConfiguration`

**AWS Config rule:**
[emr-security-configuration-encryption-transit](../../../config/latest/developerguide/emr-security-configuration-encryption-transit.md "../../../config/latest/developerguide/emr-security-configuration-encryption-transit.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon EMR security configuration has encryption in transit enabled. The control fails if the security configuration doesn't enable encryption in transit.

Data in transit refers to data that moves from one location to another, such as between nodes in your cluster or between your cluster and your application. Data may move across the internet or within a private network. Encrypting data in transit reduces the risk that an unauthorized user can eavesdrop on network traffic.

### Remediation

To enable encryption in transit in an Amazon EMR security configuration, see [Configure data encryption](../../../emr/latest/ManagementGuide/emr-create-security-configuration.md#emr-security-configuration-encryption.html "../../../emr/latest/ManagementGuide/emr-create-security-configuration.md#emr-security-configuration-encryption.html") in the _Amazon EMR Management Guide_.
