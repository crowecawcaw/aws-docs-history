# AOSSEC02-BP04 Assess your OpenSearch Service domain's configuration

with AWS Config

Use AWS Config to evaluate your OpenSearch Service domain's
configuration settings, gaining visibility into potential issues or
areas for improvement and enhancing compliance and security.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome:** You assess
OpenSearch Service domains' configuration settings using AWS Config.

**Benefits of establishing this best
practice:**

- **Improved configuration
  visibility**: Assessing OpenSearch Service domains'
  configuration settings using AWS Config provides visibility into
  domain configurations, helping you identify potential issues or
  areas for improvement.
- **Enhanced compliance and
  security**: By using AWS Config to detect security
  risks or compliance issues, organizations can take corrective
  actions to meet their requirements, which creates a more secure
  and compliant setup for their OpenSearch Service domains.

## Implementation guidance

To maintain optimal configuration and alignment with your
organization's security and compliance requirements, it's
essential to regularly assess the settings of your OpenSearch Service domains. To do this, use AWS Config, which
provides a service that automatically evaluates and reports on the
configuration of your AWS resources, including your OpenSearch Service domains.

With AWS Config, you can gain visibility into your domain
configurations, identify potential security risks or compliance
issues, and take corrective actions to meet your organization's
requirements. To set up AWS Config for compliance notifications,
see
[Getting
Started with AWS Config](../../../config/latest/developerguide/getting-started.md "../../../config/latest/developerguide/getting-started.md"),
[List
of AWS Config Managed Rules](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md") and
[Security
Best Practices for Amazon OpenSearch Service](https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Security-Best-Practices-for-Amazon-OpenSearch-Service.yaml "https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Security-Best-Practices-for-Amazon-OpenSearch-Service.yaml"). These
resources provide step-by-step instructions on how to configure
AWS Config to send compliance notifications and meet your
organization's security and compliance standards.
