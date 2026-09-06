

# rds-sqlserver-encrypted-in-transit
<a name="rds-sqlserver-encrypted-in-transit"></a>

Checks if connections to Amazon RDS SQL server database instances are configured to use encryption in transit. The rule is NON\_COMPLIANT if the DB parameter force\_ssl for the parameter group is not set to 1 or the ApplyStatus parameter is not 'in-sync'. 



**Identifier:** RDS\_SQLSERVER\_ENCRYPTED\_IN\_TRANSIT

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1285c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).