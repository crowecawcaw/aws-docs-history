

# docdb-cluster-encrypted
<a name="docdb-cluster-encrypted"></a>

Checks if storage encryption is enabled for your Amazon DocumentDB (with MongoDB compatibility) clusters. The rule is NON\_COMPLIANT if storage encryption is not enabled. 



**Identifier:** DOCDB\_CLUSTER\_ENCRYPTED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Africa (Cape Town), Asia Pacific (Osaka), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), US West (N. California), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

kmsKeyArns (Optional)Type: CSV  
A comma-separated list of KMS key ARNs to compare with the KmsKeyID of the encrypted cluster.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d489c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).