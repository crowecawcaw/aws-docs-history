# athena-data-catalog-description

Checks if Amazon Athena data catalogs have a description. The rule is NON_COMPLIANT if configuration.Description does not exist.

**Identifier:** ATHENA_DATA_CATALOG_DESCRIPTION

**Resource Types:** AWS::Athena::DataCatalog

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
