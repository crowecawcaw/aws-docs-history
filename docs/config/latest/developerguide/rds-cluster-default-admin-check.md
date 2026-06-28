# rds-cluster-default-admin-check

Checks if an Amazon Relational Database Service (Amazon RDS) database cluster has changed the admin username from its default value. The rule is NON\_COMPLIANT if the admin username is set to the default value.

**Identifier:** RDS\_CLUSTER\_DEFAULT\_ADMIN\_CHECK

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

validAdminUserNames (Optional)
Type: CSV

Comma-separated list of admin username(s) that Amazon RDS clusters can use. Cannot include 'postgres' or 'admin' as valid username(s) as these are default values.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
