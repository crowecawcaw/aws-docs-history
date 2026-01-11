# rds-snapshots-public-prohibited

Checks if Amazon Relational Database Service (Amazon RDS) snapshots are public. The rule is NON_COMPLIANT if any existing and new Amazon RDS snapshots are public.

###### Note

It can take up to 12 hours for compliance results to be captured.

**Identifier:** RDS_SNAPSHOTS_PUBLIC_PROHIBITED

**Resource Types:** AWS::RDS::DBClusterSnapshot, AWS::RDS::DBSnapshot

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Africa (Cape Town), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
