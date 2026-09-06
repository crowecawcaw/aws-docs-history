

# neptune-cluster-encrypted
<a name="neptune-cluster-encrypted"></a>

Checks if storage encryption is enabled for your Amazon Neptune DB clusters. The rule is NON\_COMPLIANT if storage encryption is not enabled. 



**Identifier:** NEPTUNE\_CLUSTER\_ENCRYPTED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

KmsKeyArns (Optional)Type: CSV  
A comma-separated list of KMS key ARNs to compare with the KmsKeyId of the encrypted cluster.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1147c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).