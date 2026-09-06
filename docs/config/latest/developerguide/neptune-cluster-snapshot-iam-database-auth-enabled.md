

# neptune-cluster-snapshot-iam-database-auth-enabled
<a name="neptune-cluster-snapshot-iam-database-auth-enabled"></a>

Checks if Amazon Neptune cluster snapshots have IAM database authentication enabled. The rule is NON\_COMPLIANT if configuration.iamdatabaseAuthenticationEnabled is false. 



**Identifier:** NEPTUNE\_CLUSTER\_SNAPSHOT\_IAM\_DATABASE\_AUTH\_ENABLED

**Resource Types:** AWS::RDS::DBClusterSnapshot

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Hyderabad), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1155c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).