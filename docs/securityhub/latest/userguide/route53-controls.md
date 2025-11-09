# Security Hub controls for Route 53

These AWS Security Hub controls evaluate the Amazon Route 53 service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Route53.1] Route 53 health checks should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::Route53::HealthCheck`

**AWS Config rule:**`tagged-route53-healthcheck` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an Amazon Route 53 health check has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the health check doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the health check isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
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

To add tags to a Route 53 health check, see [Naming and tagging health checks](../../../Route53/latest/DeveloperGuide/health-checks-tagging.md "../../../Route53/latest/DeveloperGuide/health-checks-tagging.md") in the _Amazon Route 53 Developer Guide_.

## [Route53.2] Route 53 public hosted zones should log DNS queries

**Related requirements:** NIST.800-53.r5 AC-2(4),
NIST.800-53.r5 AC-4(26),
NIST.800-53.r5 AC-6(9),
NIST.800-53.r5 AU-10,
NIST.800-53.r5 AU-12,
NIST.800-53.r5 AU-2,
NIST.800-53.r5 AU-3,
NIST.800-53.r5 AU-6(3),
NIST.800-53.r5 AU-6(4),
NIST.800-53.r5 CA-7,
NIST.800-53.r5 SC-7(9),
NIST.800-53.r5 SI-3(8),
NIST.800-53.r5 SI-4(20),
NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::Route53::HostedZone`

**AWS Config rule:**
[`route53-query-logging-enabled`](../../../config/latest/developerguide/route53-query-logging-enabled.md "../../../config/latest/developerguide/route53-query-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if DNS query logging is enabled for an Amazon Route 53 public hosted zone. The control fails if DNS
query logging isn't enabled for a Route 53 public hosted zone.

Logging DNS queries for a Route 53 hosted zone addresses DNS security and compliance requirements and grants visibility.
The logs include information such as the domain or subdomain that was queried, the date and time of the query, the DNS record type
(for example, A or AAAA), and the DNS response code (for example, `NoError` or `ServFail`). When DNS query
logging is enabled, Route 53 publishes the log files to Amazon CloudWatch Logs.

### Remediation

To log DNS queries for Route 53 public hosted zones, see [Configuring logging for DNS queries](../../../Route53/latest/DeveloperGuide/query-logs.md#query-logs-configuring "../../../Route53/latest/DeveloperGuide/query-logs.md#query-logs-configuring") in the _Amazon Route 53 Developer Guide_.
