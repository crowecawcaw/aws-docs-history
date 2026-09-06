

# apigateway-domain-name-tls-check
<a name="apigateway-domain-name-tls-check"></a>

Checks if Amazon API Gateway domain names are configured with TLS 1.2 or higher. The rule is NON\_COMPLIANT if configuration.SecurityPolicy is 'TLS\_1\_0', or if the '`allowedSecurityPolicies`' parameter is provided and the security policy does not match. 



**Identifier:** APIGATEWAY\_DOMAIN\_NAME\_TLS\_CHECK

**Resource Types:** AWS::ApiGateway::DomainName

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

allowedSecurityPolicies (Optional)Type: CSV  
Comma-separated list of allowed security policies for the rule to check. If provided, the rule is NON\_COMPLIANT if configuration.SecurityPolicy is configured with a value not specified in this parameter. Valid values include: 'TLS\_1\_0', 'TLS\_1\_2', 'SecurityPolicy\_TLS13\_1\_3\_2025\_09', 'SecurityPolicy\_TLS13\_1\_3\_FIPS\_2025\_09', 'SecurityPolicy\_TLS13\_1\_2\_PFS\_PQ\_2025\_09', 'SecurityPolicy\_TLS13\_1\_2\_FIPS\_PQ\_2025\_09', 'SecurityPolicy\_TLS13\_1\_2\_PQ\_2025\_09', 'SecurityPolicy\_TLS13\_1\_2\_2021\_06', 'SecurityPolicy\_TLS13\_2025\_EDGE', 'SecurityPolicy\_TLS12\_PFS\_2025\_EDGE', and 'SecurityPolicy\_TLS12\_2018\_EDGE'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7c61c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).