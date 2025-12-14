# Sending findings from Resolver DNS Firewall to Security Hub CSPM

[AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") provides you with a comprehensive view of your security state in AWS and
helps you to check your environment against security industry standards and best practices. Security Hub CSPM
collects security data from across AWS accounts, AWS services, and supported third-party partner
products, and helps you to analyze security trends and identify the highest priority security
issues.

By integrating Resolver DNS Firewall with Security Hub CSPM, you can send findings from DNS Firewall to
Security Hub CSPM. Security Hub CSPM then includes those findings in its analysis of your security posture.

###### Contents

- [How findings work in Security Hub CSPM](securityhub-integration.md#securityhub-integration-sending-findings "securityhub-integration.md#securityhub-integration-sending-findings")
  - [Types of findings that DNS Firewall sends](securityhub-integration.md#securityhub-integration-finding-types "securityhub-integration.md#securityhub-integration-finding-types")
  - [Retrying when Security Hub CSPM is unavailable](securityhub-integration.md#securityhub-integration-retry-send "securityhub-integration.md#securityhub-integration-retry-send")
  - [Updating existing findings in
    Security Hub CSPM](securityhub-integration.md#securityhub-integration-finding-updates "securityhub-integration.md#securityhub-integration-finding-updates")

- [Typical finding from DNS Firewall](securityhub-integration.md#securityhub-integration-finding-example "securityhub-integration.md#securityhub-integration-finding-example")
- [Enabling and configuring the integration](securityhub-integration.md#securityhub-integration-enable "securityhub-integration.md#securityhub-integration-enable")
- [Stopping the delivery of findings to Security Hub CSPM](securityhub-integration.md#securityhub-integration-disable "securityhub-integration.md#securityhub-integration-disable")

## How findings work in Security Hub CSPM

In Security Hub CSPM, a finding is an observable record of a security check or security-related detection.
Some findings come from issues that are detected by other AWS services or by third-party partners.
Security Hub CSPM also has its own security controls that it uses to detect security issues and generate findings.

Security Hub CSPM provides tools to manage findings from across all of these sources. You can view and
filter lists of findings and view details of a finding. For information, see [Reviewing finding details and finding history in Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-findings-viewing.md "../../../securityhub/latest/userguide/securityhub-findings-viewing.md") in
the _AWS Security Hub CSPM User Guide_. You can also automatically update findings or send them to a custom action.
For more information, see [Automatically modifying and taking action on Security Hub CSPM findings](../../../securityhub/latest/userguide/automations.md "../../../securityhub/latest/userguide/automations.md")
in the _AWS Security Hub CSPM User Guide_.

All findings in Security Hub CSPM use a standard JSON format called the AWS Security Finding Format
(ASFF). The ASFF includes details about the source of the security issue, the affected resources, and
the current status of the finding. For more information, see [AWS Security Finding
Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md") in the _AWS Security Hub CSPM User Guide_.

DNS Firewall is one of the AWS services that sends findings to Security Hub CSPM.

### Types of findings that DNS Firewall sends

DNS Firewall has the following integrations:

- **Managed Domain Lists**: security findings related to queries
  blocked or alerted on for domains associated with AWS Managed Domain
  Lists.
- **Custom domain lists**: security findings related to queries blocked or alerted on for domains associated with the customer’s domain list.
- **DNS Firewall Advanced**: security findings related to queries blocked or alerted on by DNS Firewall Advanced.

Security Hub CSPM ingests findings from DNS Firewall in the [AWS Security Finding
Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md"). In ASFF, the `Types` field provides the finding type.
Findings from DNS Firewall can have the following values for `Types`.

- `TTPs/Impact/Impact:Runtime-MaliciousDomainRequest.Reputation`

### Retrying when Security Hub CSPM is unavailable

If Security Hub CSPM is unavailable, DNS Firewall retries sending the findings until they are received.

### Updating existing findings in

Security Hub CSPM

DNS Firewall will update the existing findings if the same finding is observed again.

## Typical finding from DNS Firewall

Security Hub CSPM ingests DNS Firewall findings in the [AWS Security Finding
Format (ASFF)](../../../securityhub/latest/userguide/securityhub-findings-format.md "../../../securityhub/latest/userguide/securityhub-findings-format.md").

Here is an example of a typical finding from DNS Firewall in ASFF.

```
{
            "SchemaVersion": "2018-10-08",
            "Id": "00000000-0000-0000-0000-example1",
            "ProductArn": "arn:aws:securityhub:us-east-1::product/amazon/route-53-resolver-dns-firewall-aws-list",
            "ProductName": "Route 53 Resolver DNS Firewall - AWS List",
            "CompanyName": "Amazon",
            "Region": "us-east-1",
            "GeneratorId": "arn:aws:route53resolver:us-east-1:000000000000:firewall-rule-group/rslvr-frg-example1",
            "AwsAccountId": "000000000000",
            "Types": [
                "TTPs/Impact/Impact:Runtime-MaliciousDomainRequest.Reputation"
            ],
            "FirstObservedAt": "2024-12-06T19:58:49.000Z",
            "LastObservedAt": "2024-12-06T19:58:49.000Z",
            "CreatedAt": "2024-12-06T19:58:49.000Z",
            "UpdatedAt": "2024-12-06T19:58:49.000Z",
            "Severity": {
                "Label": "HIGH",
                "Normalized": 70
            },
            "Title": "DNS Firewall ALERT generated for domain example1.com. from VPC vpc-example1",
            "Description": "DNS Firewall ALERT",
            "ProductFields": {
                "aws/route53resolver/dnsfirewall/queryName": "example1.com.",
                "aws/route53resolver/dnsfirewall/firewallRuleGroupId": "rslvr-frg-example1",
                "aws/route53resolver/dnsfirewall/queryType": "A",
                "aws/route53resolver/dnsfirewall/queryClass": "IN",
                "aws/route53resolver/dnsfirewall/firewallDomainListId": "rslvr-fdl-example1",
                "aws/route53resolver/dnsfirewall/transport": "UDP",
                "aws/route53resolver/dnsfirewall/firewallRuleAction": "ALERT",
                "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-1::product/amazon/route-53-resolver-dns-firewall-aws-list/00000000-0000-0000-0000-example1",
                "aws/securityhub/ProductName": "Route 53 Resolver DNS Firewall - AWS List",
                "aws/securityhub/CompanyName": "Amazon"
            },
            "Resources": [
                {
                    "Type": "Other",
                    "Id": "rslvr-in-example1",
                    "Partition": "aws",
                    "Region": "us-east-1",
                    "Details": {
                        "Other": {
                            "ResourceType": "ResolverEndpoint",
                            "EndpointId": "rslvr-in-example1"
                        }
                    }
                },
                {
                    "Type": "Other",
                    "Id": "rni-example1",
                    "Partition": "aws",
                    "Region": "us-east-1",
                    "Details": {
                        "Other": {
                            "NetworkInterfaceId": "rni-example1",
                            "ResourceType": "ResolverNetworkInterface"
                        }
                    }
                }
            ],
            "WorkflowState": "NEW",
            "Workflow": {
                "Status": "NEW"
            },
            "RecordState": "ACTIVE",
            "FindingProviderFields": {
                "Severity": {
                    "Label": "HIGH"
                },
                "Types": [
                    "TTPs/Impact/Impact:Runtime-MaliciousDomainRequest.Reputation"
                ]
            },
            "ProcessedAt": "2024-12-11T19:33:35.494Z"
        }
```

## Enabling and configuring the integration

To integrate DNS Firewall with Security Hub CSPM, you must first enable Security Hub CSPM. For information about enabling
Security Hub CSPM, see [Enabling Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") in the _AWS Security Hub CSPM User Guide_.

## Stopping the delivery of findings to Security Hub CSPM

To stop sending DNS Firewall findings to Security Hub CSPM, you can use the Security Hub CSPM console or the Security Hub CSPM API.

For instructions, see [Disabling the flow of findings from an integration](../../../securityhub/latest/userguide/securityhub-findings-providers.md#securityhub-integration-disable "../../../securityhub/latest/userguide/securityhub-findings-providers.md#securityhub-integration-disable") in the _AWS Security Hub CSPM User Guide_.
