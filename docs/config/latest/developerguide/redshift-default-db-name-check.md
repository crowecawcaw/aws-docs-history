

# redshift-default-db-name-check
<a name="redshift-default-db-name-check"></a>

Checks if a Redshift cluster has changed its database name from the default value. The rule is NON\_COMPLIANT if the database name for a Redshift cluster is set to “dev”, or if the optional parameter is provided and the database name does not match. 



**Identifier:** REDSHIFT\_DEFAULT\_DB\_NAME\_CHECK

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

validDatabaseNames (Optional)Type: CSV  
Comma-separated list of database name(s) for Redshift clusters.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1311c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).