

# rds-instance-deletion-protection-enabled
<a name="rds-instance-deletion-protection-enabled"></a>

Checks if an Amazon Relational Database Service (Amazon RDS) instance has deletion protection enabled. The rule is NON\_COMPLIANT if an Amazon RDS instance does not have deletion protection enabled; for example, deletionProtection is set to false. 

**Warning**  
Some RDS DB instances within a Cluster (Aurora/DocumentDB) will show as not applicable because deletion protection is set at the cluster level.

**Identifier:** RDS\_INSTANCE\_DELETION\_PROTECTION\_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

databaseEngines (Optional)Type: CSV  
Comma-separated list of RDS database engines to include in the evaluation of the rule. For example, 'mysql, postgres, mariadb'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1245c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).