# rds-proxy-tls-encryption

Checks if Amazon RDS proxies enforce TLS for all connections. The rule is NON\_COMPLIANT if an Amazon RDS proxy does not have TLS enforced for all connections.

**Identifier:** RDS\_PROXY\_TLS\_ENCRYPTION

**Resource Types:** AWS::RDS::DBProxy

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
