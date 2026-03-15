# apigateway-domain-name-tls-check

Checks if Amazon API Gateway domain names are configured with TLS 1.2 or higher. The rule is NON_COMPLIANT if configuration.SecurityPolicy is 'TLS_1_0'.

**Identifier:** APIGATEWAY_DOMAIN_NAME_TLS_CHECK

**Resource Types:** AWS::ApiGateway::DomainName

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

allowedSecurityPolicies (Optional)
Type: CSV

Comma-separated list of allowed security policies for the rule to check. If provided, the rule is NON_COMPLIANT if configuration.SecurityPolicy is configured with a value not specified in this parameter. Valid values include: 'TLS_1_0', 'TLS_1_2', 'SecurityPolicy_TLS13_1_3_2025_09', 'SecurityPolicy_TLS13_1_3_FIPS_2025_09', 'SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_PQ_2025_09', 'SecurityPolicy_TLS13_1_2_2021_06', 'SecurityPolicy_TLS13_2025_EDGE', 'SecurityPolicy_TLS12_PFS_2025_EDGE', and 'SecurityPolicy_TLS12_2018_EDGE'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
