

# rds-mariadb-instance-encrypted-in-transit
<a name="rds-mariadb-instance-encrypted-in-transit"></a>

Checks if connections to Amazon RDS for MariaDB DB instances with engine version greater than or equal to 10.5 use encryption in transit. The rule is NON\_COMPLIANT if the DB parameter group is not in-sync or if require\_secure\_transport is not set to ON. 



**Identifier:** RDS\_MARIADB\_INSTANCE\_ENCRYPTED\_IN\_TRANSIT

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1259c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).