

# neptune-cluster-copy-tags-to-snapshot-enabled
<a name="neptune-cluster-copy-tags-to-snapshot-enabled"></a>

Checks if an Amazon Neptune cluster is configured to copy all tags to snapshots when the snapshots are created. The rule is NON\_COMPLIANT if 'copyTagsToSnapshot' is set to false. 



**Identifier:** NEPTUNE\_CLUSTER\_COPY\_TAGS\_TO\_SNAPSHOT\_ENABLED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1143c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).