# Security Hub controls for Amazon Redshift Serverless

These AWS Security Hub controls evaluate the Amazon Redshift Serverless service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [RedshiftServerless.1] Amazon Redshift Serverless workgroups should use enhanced VPC routing

**Category:** Protect > Secure network configuration > Resources within VPC

**Severity:** High

**Resource type:** `AWS::RedshiftServerless::Workgroup`

**AWS Config rule:**
[redshift-serverless-workgroup-routes-within-vpc](../../../config/latest/developerguide/redshift-serverless-workgroup-routes-within-vpc.md "../../../config/latest/developerguide/redshift-serverless-workgroup-routes-within-vpc.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether enhanced VPC routing is enabled for an Amazon Redshift Serverless workgroup. The control fails if enhanced VPC routing is
disabled for the workgroup.

If enhanced VPC routing is disabled for an Amazon Redshift Serverless workgroup, Amazon Redshift routes traffic through the internet, including traffic to other services within the AWS network. If you enable enhanced VPC routing for a workgroup, Amazon Redshift forces all `COPY` and `UNLOAD` traffic between your cluster and your data repositories through your virtual private cloud (VPC) based on the Amazon VPC service. With enhanced VPC routing, you can use standard VPC features to control the flow of data between your Amazon Redshift cluster and other resources. This includes features such as VPC security groups and endpoint policies, network access control lists (ACLs), and Domain Name System (DNS) servers. You can also use VPC flow logs to monitor `COPY` and `UNLOAD` traffic.

### Remediation

For more information about enhanced VPC routing and how to enable it for a workgroup, see [Controlling network traffic with Redshift enhanced VPC routing](../../../redshift/latest/mgmt/enhanced-vpc-routing.md "../../../redshift/latest/mgmt/enhanced-vpc-routing.md") in the _Amazon Redshift Management Guide_.

## [RedshiftServerless.2] Connections to Redshift Serverless workgroups should

be required to use SSL

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::RedshiftServerless::Workgroup`

**AWS Config rule:**
[redshift-serverless-workgroup-encrypted-in-transit](../../../config/latest/developerguide/redshift-serverless-workgroup-encrypted-in-transit.md "../../../config/latest/developerguide/redshift-serverless-workgroup-encrypted-in-transit.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether connections to an Amazon Redshift Serverless workgroup are required to encrypt
data in transit. The control fails if the `require_ssl` configuration parameter for
the workgroup is set to `false`.

An Amazon Redshift Serverless workgroup is a collection of compute resources that groups together compute
resources like RPUs, VPC subnet groups, and security groups. Properties of a workgroup include
network and security settings. These settings specify whether connections to a workgroup
should be required to use SSL to encrypt data in transit.

### Remediation

For information about updating the settings for an Amazon Redshift Serverless workgroup to require SSL
connections, see [Connecting to Amazon Redshift Serverless](../../../redshift/latest/mgmt/serverless-connecting.md "../../../redshift/latest/mgmt/serverless-connecting.md") in
the _Amazon Redshift Management Guide_.

## [RedshiftServerless.3] Redshift Serverless workgroups should prohibit

public access

**Category:** Protect > Secure network configuration > Resources not publicly accessible

**Severity:** High

**Resource type:** `AWS::RedshiftServerless::Workgroup`

**AWS Config rule:**
[redshift-serverless-workgroup-no-public-access](../../../config/latest/developerguide/redshift-serverless-workgroup-no-public-access.md "../../../config/latest/developerguide/redshift-serverless-workgroup-no-public-access.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether public access is disabled for an Amazon Redshift Serverless workgroup. It
evaluates the `publiclyAccessible` property of a Redshift Serverless workgroup. The control fails
if public access is enabled (`true`) for the workgroup.

The public access (`publiclyAccessible`) setting for an Amazon Redshift Serverless workgroup
specifies whether the workgroup can be accessed from a public network. If public access is
enabled (`true`) for a workgroup, Amazon Redshift creates an Elastic IP address that makes the
workgroup publicly accessible from outside the VPC. If you don't want a workgroup to be
publicly accessible, disable public access for it.

### Remediation

For information about changing the public access setting for an Amazon Redshift Serverless workgroup, see
[Viewing the properties for a workgroup](../../../redshift/latest/mgmt/serverless-console-workgroups.md "../../../redshift/latest/mgmt/serverless-console-workgroups.md") in the _Amazon Redshift
Management Guide_.

## [RedshiftServerless.4] Redshift Serverless namespaces should be encrypted

with customer managed AWS KMS keys

**Related requirements:** NIST.800-53.r5 AU-9, NIST.800-53.r5
CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SC-12(2),
NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5
SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::RedshiftServerless::Namespace`

**AWS Config rule:**
[redshift-serverless-namespace-cmk-encryption](../../../config/latest/developerguide/redshift-serverless-namespace-cmk-encryption.md "../../../config/latest/developerguide/redshift-serverless-namespace-cmk-encryption.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter    | Description                                                                                                                                                                                                        | Type                            | Allowed custom values                                                                                                         | Security Hub default value |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `kmsKeyArns` | A list of Amazon Resource Names (ARNs) of AWS KMS keys to include in the<br>evaluation. The control generates a `FAILED` finding if a Redshift Serverless namespace<br>isn't encrypted with a KMS key in the list. | StringList (maximum of 3 items) | 1–3 ARNs of existing KMS keys. For example:<br>`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`. | No default value           |

This control checks whether an Amazon Redshift Serverless namespace is encrypted at rest with a customer
managed AWS KMS key. The control fails if the Redshift Serverless namespace isn't encrypted with a
customer managed KMS key. You can optionally specify a list of KMS keys for the control to
include in the evaluation.

In Amazon Redshift Serverless, a namespace defines a logical container for database objects. This control
periodically checks whether the encryption settings for a namespace specify a customer managed
AWS KMS key, instead of an AWS managed KMS key, for encryption of data in the
namespace. With a customer managed KMS key, you have full control of the key. This includes
defining and maintaining the key policy, managing grants, rotating cryptographic material,
assigning tags, creating aliases, and enabling and disabling the key.

### Remediation

For information about updating the encryption settings for an Amazon Redshift Serverless namespace and
specifying a customer managed AWS KMS key, see [Changing the AWS KMS key for a namespace](../../../redshift/latest/mgmt/serverless-workgroups-and-namespaces-rotate-kms-key.md "../../../redshift/latest/mgmt/serverless-workgroups-and-namespaces-rotate-kms-key.md") in the _Amazon Redshift
Management Guide_.

## [RedshiftServerless.5] Redshift Serverless namespaces should not use the default admin username

**Category:** Identify > Resource configuration

**Severity:** Medium

**Resource type:**
`AWS::RedshiftServerless::Namespace`

**AWS Config rule:**
[redshift-serverless-default-admin-check](../../../config/latest/developerguide/redshift-serverless-default-admin-check.md "../../../config/latest/developerguide/redshift-serverless-default-admin-check.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether the admin username for an Amazon Redshift Serverless namespace is the default
admin username, `admin`. The control fails if the admin username for the Redshift Serverless
namespace is `admin`.

When creating an Amazon Redshift Serverless namespace, you should specify a custom admin username for the
namespace. The default admin username is public knowledge. By specifying a custom admin
username, you can, for example, help mitigate the risk or effectiveness of brute force attacks
against the namespace.

### Remediation

You can change the admin username for an Amazon Redshift Serverless namespace by using the Amazon Redshift Serverless
console or API. To change it by using the console, choose the namespace configuration, and
then choose **Edit admin credentials** on the **Actions**
menu. To change it programmatically, use the [UpdateNamespace](../../../redshift-serverless/latest/APIReference/API_UpdateNamespace.md "../../../redshift-serverless/latest/APIReference/API_UpdateNamespace.md") operation or, if you’re using the AWS CLI, run the [update-namespace](../../../cli/latest/reference/redshift-serverless/update-namespace.md "../../../cli/latest/reference/redshift-serverless/update-namespace.md") command. If you change the admin username, you must also change
the admin password at the same time.

## [RedshiftServerless.6] Redshift Serverless namespaces should export logs to

CloudWatch Logs

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::RedshiftServerless::Namespace`

**AWS Config rule:**
[redshift-serverless-publish-logs-to-cloudwatch](../../../config/latest/developerguide/redshift-serverless-publish-logs-to-cloudwatch.md "../../../config/latest/developerguide/redshift-serverless-publish-logs-to-cloudwatch.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon Redshift Serverless namespace is configured to export connection and
user logs to Amazon CloudWatch Logs. The control fails if the Redshift Serverless namespace isn't configured to export
the logs to CloudWatch Logs.

If you configure Amazon Redshift Serverless to export connection log (`connectionlog`) and user
log (`userlog`) data to a log group in Amazon CloudWatch Logs, you can collect and store your
log records in durable storage, which can support security, access, and availability reviews
and audits. With CloudWatch Logs, you can also perform real-time analysis of log data and use CloudWatch to
create alarms and review metrics.

### Remediation

To export log data for an Amazon Redshift Serverless namespace to Amazon CloudWatch Logs, the respective logs must be
selected for export in the audit logging configuration settings for the namespace. For
information about updating these settings, see [Editing security and encryption](../../../redshift/latest/mgmt/serverless-console-configuration-edit-network-settings.md "../../../redshift/latest/mgmt/serverless-console-configuration-edit-network-settings.md") in the _Amazon Redshift Management
Guide_.
