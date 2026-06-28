# Third-party data sources

CloudWatch extends monitoring capabilities beyond AWS with direct integrations for
24 third-party security, identity, and endpoint platforms. These integrations
consolidate security events, audit logs, and telemetry data from external sources
into CloudWatch Logs for unified analysis.

The following table lists the supported direct third-party integrations:

Direct third-party integrations| Source | Integration pattern | Category |
| --- | --- | --- |
| Akamai DataStream 2 | S3 Delivery | CDN and edge security |
| Cisco Meraki | API | Network security |
| Cisco Umbrella | S3 Delivery | DNS and network security |
| CrowdStrike Falcon | S3 Delivery | Endpoint security |
| Drupal Core | API | Content management |
| Entrust IDaaS | API | Identity and access management |
| F5 BIG-IP | S3 Delivery | Network security |
| GitHub | API | Source code and audit logs |
| Microsoft Entra ID | API | Identity and access management |
| Microsoft Office 365 | API | Productivity and audit logs |
| Microsoft Windows Event Logs | API | Operating system events |
| Netskope | API | Network security and CASB |
| Okta Auth0 | API | Identity and access management |
| Okta SSO | API | Identity and access management |
| OneLogin Identity | API | Identity and access management |
| Palo Alto Networks NGFW | API | Network security |
| PingIdentity PingOne | API | Identity and access management |
| Slack Audit Log | API | Collaboration and audit logs |
| SentinelOne | S3 Delivery | Endpoint security |
| ServiceNow CMDB | API | IT service management |
| Tanium Endpoint Management | S3 Delivery | Endpoint security and management |
| Wiz CNAPP | API | Cloud security |
| Zeek | S3 Delivery | Network security monitoring |
| Zscaler ZIA/ZPA | S3 Delivery | Network security |

For detailed setup procedures, prerequisites, and configuration steps for each
integration, see [Third-party data sources integration](third-party-integration-setup.md "third-party-integration-setup.md").

###### Additional third-party sources through Security Hub CSPM

Beyond the 24 direct integrations, 49+ additional third-party sources are
available through AWS Security Hub CSPM integration. Security Hub CSPM partner
providers that send findings to Security Hub are automatically available as data
sources. For the full list of supported partners, see the [Security Hub CSPM partner providers](../../../securityhub/latest/userguide/securityhub-partner-providers.md "../../../securityhub/latest/userguide/securityhub-partner-providers.md") documentation.

###### Additional third-party sources through Security Hub

AWS Security Hub (distinct from Security Hub CSPM) provides its own set of
third-party integrations. These integrations that send findings to Security Hub are
automatically available as data sources. For the full list of supported
integrations, see the [Security Hub third-party integrations](../../../securityhub/latest/userguide/securityhub-v2-integrations.md "../../../securityhub/latest/userguide/securityhub-v2-integrations.md") documentation.
