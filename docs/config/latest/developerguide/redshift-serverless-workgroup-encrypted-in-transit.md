# redshift-serverless-workgroup-encrypted-in-transit

Checks if AWS Redshift Serverless workgroups have the require\_ssl config parameter set to true. The rule is NON\_COMPLIANT if require\_ssl is set to false.

**Identifier:** REDSHIFT\_SERVERLESS\_WORKGROUP\_ENCRYPTED\_IN\_TRANSIT

**Resource Types:** AWS::RedshiftServerless::Workgroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), South America (Sao Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
