# Security Hub controls for Amazon OpenSearch Service

These AWS Security Hub controls evaluate the Amazon OpenSearch Service (OpenSearch Service) service and resources. The
controls might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Opensearch.1] OpenSearch domains should have encryption at rest enabled

**Related requirements:** PCI DSS v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.4, PCI DSS v3.2.1/7.2.1, NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-encrypted-at-rest`](../../../config/latest/developerguide/opensearch-encrypted-at-rest.md "../../../config/latest/developerguide/opensearch-encrypted-at-rest.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether OpenSearch domains have encryption-at-rest configuration
enabled. The check fails if encryption at rest is not enabled.

For an added layer of security for sensitive data, you should configure your OpenSearch Service domain
to be encrypted at rest. When you configure encryption of data at rest, AWS KMS stores
and manages your encryption keys. To perform the encryption, AWS KMS uses the Advanced
Encryption Standard algorithm with 256-bit keys (AES-256).

To learn more about OpenSearch Service encryption at rest, see [Encryption of data at rest for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/encryption-at-rest.md "../../../opensearch-service/latest/developerguide/encryption-at-rest.md") in the
_Amazon OpenSearch Service_
_Developer Guide_.

### Remediation

To enable encryption at rest for new and existing OpenSearch domains, see [Enabling encryption of data at rest](../../../opensearch-service/latest/developerguide/encryption-at-rest.md#enabling-ear "../../../opensearch-service/latest/developerguide/encryption-at-rest.md#enabling-ear") in the
_Amazon OpenSearch Service Developer Guide_.

## [Opensearch.2] OpenSearch domains should not be publicly accessible

**Related requirements:** PCI DSS v3.2.1/1.2.1, PCI DSS v3.2.1/1.3.1, PCI DSS v3.2.1/1.3.2, PCI DSS v3.2.1/1.3.4, PCI DSS v3.2.1/1.3.6, NIST.800-53.r5 AC-21, NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4, NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7, NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20), NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-7(9)

**Category:** Protect > Secure network configuration > Resources within VPC

**Severity:** Critical

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-in-vpc-only`](../../../config/latest/developerguide/opensearch-in-vpc-only.md "../../../config/latest/developerguide/opensearch-in-vpc-only.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether OpenSearch domains are in a VPC. It does not evaluate the VPC subnet routing configuration to determine public access.

You should ensure that OpenSearch domains are not attached to public subnets. See [Resource-based policies](../../../opensearch-service/latest/developerguide/ac.md#ac-types-resource "../../../opensearch-service/latest/developerguide/ac.md#ac-types-resource") in the Amazon OpenSearch Service Developer Guide. You should also ensure that your VPC is configured according to the recommended best practices. See [Security best practices for your VPC](../../../vpc/latest/userguide/vpc-security-best-practices.md "../../../vpc/latest/userguide/vpc-security-best-practices.md") in the Amazon VPC User Guide.

OpenSearch domains deployed within a VPC can communicate with VPC resources over the private AWS network, without the need to traverse the public internet. This configuration increases the security posture by limiting access to the data in transit. VPCs provide a number of network controls to secure access to OpenSearch domains, including network ACL and security groups. Security Hub recommends that you migrate public OpenSearch domains to VPCs to take advantage of these controls.

### Remediation

If you create a domain with a public endpoint, you cannot later place it within a VPC. Instead, you must create a new domain and migrate your data. The reverse is also true.
If you create a domain within a VPC, it cannot have a public endpoint. Instead, you must either
[create another domain](../../../opensearch-service/latest/developerguide/createupdatedomains.md#es-createdomains "../../../opensearch-service/latest/developerguide/createupdatedomains.md#es-createdomains") or disable this control.

For instructions, see [Launching your Amazon OpenSearch Service domains within a VPC](../../../opensearch-service/latest/developerguide/vpc.md "../../../opensearch-service/latest/developerguide/vpc.md") in the _Amazon OpenSearch Service Developer Guide_.

## [Opensearch.3] OpenSearch domains should encrypt data sent between nodes

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2)

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-node-to-node-encryption-check`](../../../config/latest/developerguide/opensearch-node-to-node-encryption-check.md "../../../config/latest/developerguide/opensearch-node-to-node-encryption-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether OpenSearch domains have node-to-node encryption enabled. This control fails if node-to-node encryption is disabled on the domain.

HTTPS (TLS) can be used to help prevent potential attackers from eavesdropping on or manipulating network traffic using person-in-the-middle or similar attacks. Only encrypted connections over HTTPS (TLS) should be allowed. Enabling node-to-node encryption for OpenSearch domains ensures that intra-cluster communications are encrypted in transit.

There can be a performance penalty associated with this configuration. You should be aware of and test the performance trade-off before enabling this option.

### Remediation

To enable node-to-node encryption on an OpenSearch domain, see [Enabling node-to-node encryption](../../../opensearch-service/latest/developerguide/ntn.md#enabling-ntn "../../../opensearch-service/latest/developerguide/ntn.md#enabling-ntn") in the _Amazon OpenSearch Service Developer Guide_.

## [Opensearch.4] OpenSearch domain error logging to CloudWatch Logs should be enabled

**Related requirements:** NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8)

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-logs-to-cloudwatch`](../../../config/latest/developerguide/opensearch-logs-to-cloudwatch.md "../../../config/latest/developerguide/opensearch-logs-to-cloudwatch.md")

**Schedule type:** Change triggered

**Parameters:**

- `logtype = 'error'` (not customizable)

This control checks whether OpenSearch domains are configured to send error logs to CloudWatch Logs. This control fails if error logging to CloudWatch is not enabled for a domain.

You should enable error logs for OpenSearch domains and send those logs to CloudWatch Logs for retention and response. Domain error logs can assist with security and access audits, and can help to diagnose availability issues.

### Remediation

To enable log publishing, see [Enabling log publishing (console)](../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md#createdomain-configure-slow-logs-console "../../../opensearch-service/latest/developerguide/createdomain-configure-slow-logs.md#createdomain-configure-slow-logs-console") in the _Amazon OpenSearch Service Developer Guide_.

## [Opensearch.5] OpenSearch domains should have audit logging enabled

**Related requirements:** NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.2.1

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-audit-logging-enabled`](../../../config/latest/developerguide/opensearch-audit-logging-enabled.md "../../../config/latest/developerguide/opensearch-audit-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

- `cloudWatchLogsLogGroupArnList` (not customizable) – Security Hub does not populate this parameter. Comma-separated list of CloudWatch Logs log groups that should be configured for audit logs.

This control checks whether OpenSearch domains have audit logging enabled. This control
fails if an OpenSearch domain does not have audit logging enabled.

Audit logs are highly customizable. They allow you to track user activity on your
OpenSearch clusters, including authentication successes and failures, requests to
OpenSearch, index changes, and incoming search queries.

### Remediation

For instructions on enabling audit logs, see [Enabling audit logs](../../../opensearch-service/latest/developerguide/audit-logs.md#audit-log-enabling "../../../opensearch-service/latest/developerguide/audit-logs.md#audit-log-enabling") in the _Amazon OpenSearch Service Developer Guide_.

## [Opensearch.6] OpenSearch domains should have at least three data nodes

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-data-node-fault-tolerance`](../../../config/latest/developerguide/opensearch-data-node-fault-tolerance.md "../../../config/latest/developerguide/opensearch-data-node-fault-tolerance.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether OpenSearch domains are configured with at least three data
nodes and `zoneAwarenessEnabled` is `true`. This control fails
for an OpenSearch domain if `instanceCount` is less than 3 or
`zoneAwarenessEnabled` is `false`.

To achieve cluster-level high availability and fault tolerance, an OpenSearch domain
should have at least three data nodes. Deploying an OpenSearch domain with at least
three data nodes ensures cluster operations if a node fails.

### Remediation

###### To modify the number of data nodes in an OpenSearch domain

1. Sign in to the AWS console and open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. Under **My domains**, choose the name of the domain to edit, and choose **Edit**.
3. Under **Data nodes** set **Number of nodes** to a number greater than `3`. If you are deploying to three Availability Zones, set the number to a multiple of three to ensure equal distribution across Availability Zones.
4. Choose **Submit**.

## [Opensearch.7] OpenSearch domains should have fine-grained access control enabled

**Related requirements:** NIST.800-53.r5 AC-2(1), NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(15), NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-5, NIST.800-53.r5 AC-6

**Category:** Protect > Secure Access Management > Sensitive API actions restricted

**Severity:** High

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-access-control-enabled`](../../../config/latest/developerguide/opensearch-access-control-enabled.md "../../../config/latest/developerguide/opensearch-access-control-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether OpenSearch domains have fine-grained access control enabled. The control fails if the fine-grained access control is
not enabled. Fine-grained access control requires `advanced-security-options`in the OpenSearch parameter `update-domain-config` to be enabled.

Fine-grained access control offers additional ways of controlling access to your data on Amazon OpenSearch Service.

### Remediation

To enable fine-grained access control, see [Fine-grained access control in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/fgac.md "../../../opensearch-service/latest/developerguide/fgac.md") in the _Amazon OpenSearch Service Developer Guide_.

## [Opensearch.8] Connections to OpenSearch domains should be encrypted using the latest TLS security policy

**Related requirements:** NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-https-required`](../../../config/latest/developerguide/opensearch-https-required.md "../../../config/latest/developerguide/opensearch-https-required.md")

**Schedule type:** Change triggered

**Parameters:**

- `tlsPolicies: Policy-Min-TLS-1-2-PFS-2023-10` (not customizable)

This controls checks whether an Amazon OpenSearch Service domain endpoint is configured to use the latest TLS security policy. The control
fails if the OpenSearch domain endpoint isn't configured to use the latest supported policy or if HTTPs isn't enabled.

HTTPS (TLS) can be used to help prevent potential attackers from using person-in-the-middle or similar attacks to eavesdrop on or manipulate network traffic. Only encrypted connections over HTTPS (TLS) should be allowed.
Encrypting data in transit can affect performance. You should test your application with this feature to understand the performance profile and the impact of TLS. TLS 1.2 provides several security enhancements over previous versions of TLS.

### Remediation

To enable TLS encryption, use the [UpdateDomainConfig](../../../opensearch-service/latest/APIReference/API_UpdateDomainConfig.md "../../../opensearch-service/latest/APIReference/API_UpdateDomainConfig.md") API operation.
Configure the [DomainEndpointOptions](../../../opensearch-service/latest/APIReference/API_DomainEndpointOptions.md "../../../opensearch-service/latest/APIReference/API_DomainEndpointOptions.md") field to specify the value for `TLSSecurityPolicy`.
For more information, see [Node-to-node encryption](../../../opensearch-service/latest/developerguide/ntn.md "../../../opensearch-service/latest/developerguide/ntn.md") in the _Amazon OpenSearch Service Developer Guide_.

## [Opensearch.9] OpenSearch domains should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:** `tagged-opensearch-domain` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | `No default value`         |

This control checks whether an Amazon OpenSearch Service domain has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the domain doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the domain isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to an OpenSearch Service domain, see [Working with tags](../../../opensearch-service/latest/developerguide/managedomains-awsresourcetagging.md#managedomains-awsresourcetagging-console "../../../opensearch-service/latest/developerguide/managedomains-awsresourcetagging.md#managedomains-awsresourcetagging-console") in the _Amazon OpenSearch Service Developer Guide_.

## [Opensearch.10] OpenSearch domains should have the latest software update installed

**Related requirements:** NIST.800-53.r5 SI-2, NIST.800-53.r5 SI-2(2), NIST.800-53.r5 SI-2(4), NIST.800-53.r5 SI-2(5), PCI DSS v4.0.1/6.3.3

**Category:** Identify > Vulnerability, patch, and version management

**Severity:** Low

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-update-check`](../../../config/latest/developerguide/opensearch-update-check.md "../../../config/latest/developerguide/opensearch-update-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon OpenSearch Service domain has the latest software update installed. The control fails if a
software update is available but not installed for the domain.

OpenSearch Service software updates provide the latest platform fixes, updates, and features available for the environment.
Keeping up-to-date with patch installation helps maintain domain security and availability. If no action is taken on
required updates, the service software is updated automatically (typically after 2 weeks). We recommend scheduling updates
during a time of low traffic to the domain to minimize service disruption.

### Remediation

To install software updates for an OpenSearch domain, see [Starting an update](../../../opensearch-service/latest/developerguide/service-software.md#service-software-requesting "../../../opensearch-service/latest/developerguide/service-software.md#service-software-requesting") in
the _Amazon OpenSearch Service Developer Guide_.

## [Opensearch.11] OpenSearch domains should have at least three dedicated primary nodes

**Related requirements:** NIST.800-53.r5 CP-10,
NIST.800-53.r5 CP-2,
NIST.800-53.r5 SC-5,
NIST.800-53.r5 SC-36,
NIST.800-53.r5 SI-13

**Category:** Recover > Resilience > High availability

**Severity:** Low

**Resource type:**
`AWS::OpenSearch::Domain`

**AWS Config rule:**
[`opensearch-primary-node-fault-tolerance`](../../../config/latest/developerguide/opensearch-primary-node-fault-tolerance.md "../../../config/latest/developerguide/opensearch-primary-node-fault-tolerance.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon OpenSearch Service domain is configured with at least three dedicated primary nodes. The
control fails if the domain has fewer than three dedicated primary nodes.

OpenSearch Service uses dedicated primary nodes to increase cluster stability. A dedicated primary node performs cluster
management tasks, but doesn't hold data or respond to data upload requests. We recommend that you use multi-AZ with standby, which
adds three dedicated primary nodes to each production OpenSearch domain.

### Remediation

To change the number of primary nodes for an OpenSearch domain, see [Creating and managing Amazon OpenSearch Service domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md "../../../opensearch-service/latest/developerguide/createupdatedomains.md") in
the _Amazon OpenSearch Service Developer Guide_.
