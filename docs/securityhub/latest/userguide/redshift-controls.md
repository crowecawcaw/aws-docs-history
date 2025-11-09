# Security Hub controls for Amazon Redshift

These AWS Security Hub controls evaluate the Amazon Redshift service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Redshift.1] Amazon Redshift clusters should prohibit public access

**Related requirements:** NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9), PCI DSS v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.4, PCI DSS v3.2.1/1.3.6, PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration >
Resources not publicly accessible

**Severity:** Critical

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
[redshift-cluster-public-access-check](../../../config/latest/developerguide/redshift-cluster-public-access-check.md "../../../config/latest/developerguide/redshift-cluster-public-access-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon Redshift clusters are publicly accessible. It evaluates the
`PubliclyAccessible` field in the cluster configuration item.

The `PubliclyAccessible` attribute of the Amazon Redshift cluster configuration indicates
whether the cluster is publicly accessible. When the cluster is configured with
`PubliclyAccessible` set to `true`, it is an Internet-facing instance
that has a publicly resolvable DNS name, which resolves to a public IP address.

When the cluster is not publicly accessible, it is an internal instance with a DNS name
that resolves to a private IP address. Unless you intend for your cluster to be publicly
accessible, the cluster should not be configured with `PubliclyAccessible` set to
`true`.

### Remediation

To update an Amazon Redshift cluster to disable public access, see [Modifying a cluster](../../../redshift/latest/mgmt/managing-clusters-console.md#modify-cluster "../../../redshift/latest/mgmt/managing-clusters-console.md#modify-cluster") in the _Amazon Redshift Management Guide_.
Set **Publicly accessible** to **No**.

## [Redshift.2] Connections to Amazon Redshift clusters should be encrypted in transit

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::Redshift::Cluster` `AWS::Redshift::ClusterParameterGroup`

**AWS Config rule:**
[redshift-require-tls-ssl](../../../config/latest/developerguide/redshift-require-tls-ssl.md "../../../config/latest/developerguide/redshift-require-tls-ssl.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether connections to Amazon Redshift clusters are required to use encryption in
transit. The check fails if the Amazon Redshift cluster parameter `require_SSL` isn't set to
`True`.

TLS can be used to help prevent potential attackers from using person-in-the-middle or
similar attacks to eavesdrop on or manipulate network traffic. Only encrypted connections over
TLS should be allowed. Encrypting data in transit can affect performance. You should test your
application with this feature to understand the performance profile and the impact of TLS.

### Remediation

To update an Amazon Redshift parameter group to require encryption, see [Modifying a parameter group](../../../redshift/latest/mgmt/managing-parameter-groups-console.md#parameter-group-modify "../../../redshift/latest/mgmt/managing-parameter-groups-console.md#parameter-group-modify") in the _Amazon Redshift Management Guide_.
Set `require_ssl` to **True**.

## [Redshift.3] Amazon Redshift clusters should have automatic snapshots enabled

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6, NIST.800-53.r5 CP-6(1), NIST.800-53.r5 CP-6(2), NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > Backups enabled

**Severity:** Medium

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
[redshift-backup-enabled](../../../config/latest/developerguide/redshift-backup-enabled.md "../../../config/latest/developerguide/redshift-backup-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter             | Description                               | Type    | Allowed custom values | Security Hub default value |
| --------------------- | ----------------------------------------- | ------- | --------------------- | -------------------------- |
| `​MinRetentionPeriod` | Minimum snapshot retention period in days | Integer | `7` to `35`           | `7`                        |

This control checks whether an Amazon Redshift cluster has automated snapshots enabled, and a retention period greater
than or equal to the specified time frame. The control fails if automated snapshots aren't enabled for the cluster, or if
the retention period is less than the specified time frame. Unless you provide a custom parameter value for the snapshot retention
period, Security Hub uses a default value of 7 days.

Backups help you to recover more quickly from a security incident. They strengthen the
resilience of your systems. Amazon Redshift takes periodic snapshots by default. This control checks
whether automatic snapshots are enabled and retained for at least seven days. For more details
on Amazon Redshift automated snapshots, see [Automated
snapshots](../../../redshift/latest/mgmt/working-with-snapshots.md#about-automated-snapshots "../../../redshift/latest/mgmt/working-with-snapshots.md#about-automated-snapshots") in the _Amazon Redshift Management Guide_.

### Remediation

To update the snapshot retention period for an Amazon Redshift cluster, see [Modifying a cluster](../../../redshift/latest/mgmt/managing-clusters-console.md#modify-cluster "../../../redshift/latest/mgmt/managing-clusters-console.md#modify-cluster") in the _Amazon Redshift Management Guide_.
For **Backup**, set **Snapshot retention** to a value of 7 or greater.

## [Redshift.4] Amazon Redshift clusters should have audit logging enabled

**Related requirements:** NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.2.1

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
`redshift-cluster-audit-logging-enabled` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

- `loggingEnabled = true` (not customizable)

This control checks whether an Amazon Redshift cluster has audit logging enabled.

Amazon Redshift audit logging provides additional information about connections and user activities in
your cluster. This data can be stored and secured in Amazon S3 and can be helpful in security audits
and investigations. For more information, see [Database audit logging](../../../redshift/latest/mgmt/db-auditing.md "../../../redshift/latest/mgmt/db-auditing.md") in the _Amazon Redshift Management Guide_.

### Remediation

To configure audit logging for an Amazon Redshift cluster, see [Configuring auditing using the console](../../../redshift/latest/mgmt/db-auditing-console.md "../../../redshift/latest/mgmt/db-auditing-console.md") in the _Amazon Redshift Management Guide_.

## [Redshift.6] Amazon Redshift should have automatic upgrades to major versions enabled

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CP-9, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-2(2), NIST.800-53.r5 SI-2(4), NIST.800-53.r5 SI-2(5)

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** Medium

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
[redshift-cluster-maintenancesettings-check](../../../config/latest/developerguide/redshift-cluster-maintenancesettings-check.md "../../../config/latest/developerguide/redshift-cluster-maintenancesettings-check.md")

**Schedule type:** Change triggered

**Parameters:**

- `allowVersionUpgrade = true` (not customizable)

This control checks whether automatic major version upgrades are enabled for the Amazon Redshift
cluster.

Enabling automatic major version upgrades ensures that the latest major version updates to
Amazon Redshift clusters are installed during the maintenance window. These updates might include security
patches and bug fixes. Keeping up to date with patch installation is an important step in
securing systems.

### Remediation

To remediate this issue from the AWS CLI, use the Amazon Redshift `modify-cluster` command,
and set the `--allow-version-upgrade` attribute. `clustername` is the name of your Amazon Redshift
cluster.

```
aws redshift modify-cluster --cluster-identifier `clustername` --allow-version-upgrade
```

## [Redshift.7] Redshift clusters should use enhanced VPC routing

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network configuration > API private access

**Severity:** Medium

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
[redshift-enhanced-vpc-routing-enabled](../../../config/latest/developerguide/redshift-enhanced-vpc-routing-enabled.md "../../../config/latest/developerguide/redshift-enhanced-vpc-routing-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Redshift cluster has `EnhancedVpcRouting`
enabled.

Enhanced VPC routing forces all `COPY` and `UNLOAD` traffic between
the cluster and data repositories to go through your VPC. You can then use VPC features such as
security groups and network access control lists to secure network traffic. You can also use VPC
Flow Logs to monitor network traffic.

### Remediation

For detailed remediation instructions, see [Enabling enhanced VPC
routing](../../../redshift/latest/mgmt/enhanced-vpc-enabling-cluster.md "../../../redshift/latest/mgmt/enhanced-vpc-enabling-cluster.md") in the _Amazon Redshift Management Guide_.

## [Redshift.8] Amazon Redshift clusters should not use the default Admin username

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Identify > Resource Configuration

**Severity:** Medium

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
[redshift-default-admin-check](../../../config/latest/developerguide/redshift-default-admin-check.md "../../../config/latest/developerguide/redshift-default-admin-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Redshift cluster has changed the admin username from its default value. This control will fail if the admin username for a Redshift cluster is set to `awsuser`.

When creating a Redshift cluster, you should change the default admin username to a unique value. Default usernames are public knowledge and should be changed upon configuration. Changing the default usernames reduces the risk of unintended access.

### Remediation

You can't change the admin username for your Amazon Redshift cluster after creating it. To create a new cluster with a non-default
username, see [Step 1: Create a sample Amazon Redshift cluster](../../../redshift/latest/gsg/rs-gsg-prereq.md "../../../redshift/latest/gsg/rs-gsg-prereq.md")
in the _Amazon Redshift Getting Started Guide_.

## [Redshift.10] Redshift clusters should be encrypted at rest

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-3(6),
NIST.800-53.r5 SC-13,
NIST.800-53.r5 SC-28,
NIST.800-53.r5 SC-28(1),
NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
[redshift-cluster-kms-enabled](../../../config/latest/developerguide/redshift-cluster-kms-enabled.md "../../../config/latest/developerguide/redshift-cluster-kms-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Amazon Redshift clusters are encrypted at rest.
The control fails if a Redshift cluster isn't encrypted at rest or if the encryption key is different from the provided key in the rule parameter.

In Amazon Redshift, you can turn on database encryption for your clusters to help protect data at rest. When you turn on encryption
for a cluster, the data blocks and system metadata are encrypted for the cluster and its snapshots. Encryption of data at rest
is a recommended best practice because it adds a layer of access management to your data. Encrypting Redshift clusters at rest
reduces the risk that an unauthorized user can access the data stored on disk.

### Remediation

To modify a Redshift cluster to use KMS encryption, see [Changing cluster encryption](../../../redshift/latest/mgmt/changing-cluster-encryption.md "../../../redshift/latest/mgmt/changing-cluster-encryption.md") in the _Amazon Redshift Management Guide_.

## [Redshift.11] Redshift clusters should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
`tagged-redshift-cluster` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`         |

This control checks whether an Amazon Redshift cluster has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the cluster doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the cluster isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to a Redshift cluster, see [Tagging resources in Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-tagging.md "../../../redshift/latest/mgmt/amazon-redshift-tagging.md") in the _Amazon Redshift Management Guide_.

## [Redshift.12] Redshift event notification subscriptions should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Redshift::EventSubscription`

**AWS Config rule:**
`tagged-redshift-eventsubscription` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`         |

This control checks whether an Amazon Redshift cluster snapshot has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the cluster snapshot doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the cluster snapshot isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to a Redshift event notification subscription, see [Tagging resources in Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-tagging.md "../../../redshift/latest/mgmt/amazon-redshift-tagging.md") in the _Amazon Redshift Management Guide_.

## [Redshift.13] Redshift cluster snapshots should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Redshift::ClusterSnapshot`

**AWS Config rule:**
`tagged-redshift-clustersnapshot` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`         |

This control checks whether an Amazon Redshift cluster snapshot has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the cluster snapshot doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the cluster snapshot isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to a Redshift cluster snapshot, see [Tagging resources in Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-tagging.md "../../../redshift/latest/mgmt/amazon-redshift-tagging.md") in the _Amazon Redshift Management Guide_.

## [Redshift.14] Redshift cluster subnet groups should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Redshift::ClusterSubnetGroup`

**AWS Config rule:**
`tagged-redshift-clustersubnetgroup` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`         |

This control checks whether an Amazon Redshift cluster subnet group has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the cluster subnet group doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the cluster subnet group isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to a Redshift cluster subnet group, see [Tagging resources in Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-tagging.md "../../../redshift/latest/mgmt/amazon-redshift-tagging.md") in the _Amazon Redshift Management Guide_.

## [Redshift.15] Redshift security groups should allow ingress on the cluster port only from restricted origins

**Related requirements:** PCI DSS v4.0.1/1.3.1

**Category:** Protect > Secure network configuration > Security group configuration

**Severity:** High

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
[redshift-unrestricted-port-access](../../../config/latest/developerguide/redshift-unrestricted-port-access.md "../../../config/latest/developerguide/redshift-unrestricted-port-access.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether a security group associated with an Amazon Redshift cluster has ingress rules that permit access to
the cluster port from the internet (0.0.0.0/0 or ::/0). The control fails if the security group ingress rules permit access to the cluster
port from the internet.

Permitting unrestricted inbound access to the Redshift cluster port (IP address with a /0 suffix) can result in
unauthorized access or security incidents. We recommend applying the principal of least privilege access when creating security
groups and configuring inbound rules.

### Remediation

To restrict ingress on the Redshift cluster port to restricted origins, see [Work with security group rules](../../../vpc/latest/userguide/security-group-rules.md#working-with-security-group-rules "../../../vpc/latest/userguide/security-group-rules.md#working-with-security-group-rules")
in the _Amazon VPC User Guide_. Update rules where the port range matches the Redshift cluster port and the IP port range is 0.0.0.0/0.

## [Redshift.16] Redshift cluster subnet groups should have subnets from multiple Availability Zones

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::Redshift::ClusterSubnetGroup`

**AWS Config rule:**
[redshift-cluster-subnet-group-multi-az](../../../config/latest/developerguide/redshift-cluster-subnet-group-multi-az.md "../../../config/latest/developerguide/redshift-cluster-subnet-group-multi-az.md")

**Schedule type:** Change triggered

**Parameters:** None

The control checks whether an Amazon Redshift cluster subnet group has subnets from more than one Availability Zone (AZ). The control fails if the cluster subnet group doesn't have
subnets from at least two different AZs.

Configuring subnets across multiple AZs help ensure that your Redshift data warehouse can continue operating even when failure events occur.

### Remediation

To modify a Redshift cluster subnet group to span multiple AZs, see [Modifying a cluster subnet group](../../../redshift/latest/mgmt/modify-cluster-subnet-group.md "../../../redshift/latest/mgmt/modify-cluster-subnet-group.md")
in the _Amazon Redshift Management Guide_.

## [Redshift.17] Redshift cluster parameter groups should be

tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::Redshift::ClusterParameterGroup`

**AWS Config rule:** [redshift-cluster-parameter-group-tagged](../../../config/latest/developerguide/redshift-cluster-parameter-group-tagged.md "../../../config/latest/developerguide/redshift-cluster-parameter-group-tagged.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                                | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredKeyTags` | A list of non-system tag keys that must be assigned to an evaluated resource. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an Amazon Redshift cluster parameter group has the tag keys
specified by the `requiredKeyTags` parameter. The control fails if
the parameter group doesn't have any tag keys, or it doesn't have all the keys specified
by the `requiredKeyTags` parameter. If you don't specify any values
for the `requiredKeyTags` parameter, the control checks only for the
existence of a tag key and fails if the parameter group doesn't have any tag keys. The
control ignores system tags, which are applied automatically and have the
`aws:` prefix.

A tag is a label that you create and assign to an AWS resource. Each tag consists of
a required tag key and an optional tag value. You can use tags to categorize resources
by purpose, owner, environment, or other criteria. They can help you identify, organize,
search for, and filter resources. They can also help you track resource owners for
actions and notifications. You can also use tags to implement attribute-based access
control (ABAC) as an authorization strategy. For more information about ABAC strategies,
see [Define
permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. For more information about tags, see the
[Tagging AWS Resources and Tag Editor User
Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

###### Note

Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are
accessible from many AWS services. They aren't intended to be used for private or sensitive data.

### Remediation

For information about adding tags to an Amazon Redshift cluster parameter group, see
[Tag resources in Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-tagging.md "../../../redshift/latest/mgmt/amazon-redshift-tagging.md") in the
_Amazon Redshift Management Guide_.

## [Redshift.18] Redshift clusters should have Multi-AZ

deployments enabled

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::Redshift::Cluster`

**AWS Config rule:**
[redshift-cluster-multi-az-enabled](../../../config/latest/developerguide/redshift-cluster-multi-az-enabled.md "../../../config/latest/developerguide/redshift-cluster-multi-az-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether multiple Availability Zones (Multi-AZ) deployments are enabled for
an Amazon Redshift cluster. The control fails if Multi-AZ deployments aren't enabled for the
Amazon Redshift cluster.

Amazon Redshift supports multiple Availability Zones (Multi-AZ) deployments for provisioned clusters.
If Multi-AZ deployments are enabled for a cluster, an Amazon Redshift data warehouse can continue
operating in failure scenarios when an unexpected event happens in an Availability Zone
(AZ). A Multi-AZ deployment deploys compute resources in more than one AZ and these
compute resources can be accessed through a single endpoint. In the event of an entire
AZ failure, the remaining compute resources in another AZ are available to continue
processing workloads. You can convert an existing Single-AZ data warehouse to a Multi-AZ
data warehouse. Additional compute resources are then provisioned in a second AZ.

### Remediation

For information about configuring Multi-AZ deployments for an Amazon Redshift cluster,
see [Converting a Single-AZ
data warehouse to a Multi-AZ data warehouse](../../../redshift/latest/mgmt/convert-saz-to-maz.md "../../../redshift/latest/mgmt/convert-saz-to-maz.md") in the _Amazon Redshift Management Guide_.
