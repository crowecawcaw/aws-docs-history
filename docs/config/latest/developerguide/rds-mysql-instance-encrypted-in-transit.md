# rds-mysql-instance-encrypted-in-transit

Checks if connections to Amazon RDS for MySQL database instances are configured to use encryption in transit. The rule is NON\_COMPLIANT if the associated database parameter group is not in-sync or if the require\_secure\_transport parameter is not set to 1.

###### Note

The rule returns `NOT_APPLICABLE` if the Amazon RDS instance is part of an RDS cluster.

**Identifier:** RDS\_MYSQL\_INSTANCE\_ENCRYPTED\_IN\_TRANSIT

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
