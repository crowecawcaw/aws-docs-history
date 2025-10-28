# rds-db-security-group-not-allowed

Checks if there are any Amazon Relational Database Service (Amazon RDS)
DB security groups that are not the default DB security group. The rule is NON_COMPLIANT if there are any DB security groups that are not the default DB security group.

**Identifier:** RDS_DB_SECURITY_GROUP_NOT_ALLOWED

**Resource Types:** AWS::RDS::DBSecurityGroup

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Ireland), South America (Sao Paulo), US East (N. Virginia), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
