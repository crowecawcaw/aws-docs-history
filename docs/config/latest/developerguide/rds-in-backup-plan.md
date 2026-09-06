

# rds-in-backup-plan
<a name="rds-in-backup-plan"></a>

Checks if Amazon Relational Database Service (Amazon RDS) databases are present in AWS Backup plans. The rule is NON\_COMPLIANT if Amazon RDS databases are not included in any AWS Backup plan. 

**Note**  
The rule only applies to Amazon Aurora DB instances. DB clusters are not supported.

**Identifier:** RDS\_IN\_BACKUP\_PLAN

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1253c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).