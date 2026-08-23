# redshift-serverless-workgroup-no-public-access

Checks if Amazon Redshift Serverless workgroups do not allow public access. The rule is NON\_COMPLIANT if a workgroup has 'Turn on Public Accessible' enabled.

**Identifier:** REDSHIFT\_SERVERLESS\_WORKGROUP\_NO\_PUBLIC\_ACCESS

**Resource Types:** AWS::RedshiftServerless::Workgroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Africa (Cape Town), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
