

# dynamodb-table-cross-region-replication-enabled
<a name="dynamodb-table-cross-region-replication-enabled"></a>

Checks if an Amazon DynamoDB table has an active cross-Region replica through global tables. The rule is NON\_COMPLIANT if configuration.replicas is empty or if no replica has a regionName other than the table's awsRegion and replicaStatus ACTIVE. 



**Identifier:** DYNAMODB\_TABLE\_CROSS\_REGION\_REPLICATION\_ENABLED

**Resource Types:** AWS::DynamoDB::Table

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Middle East (UAE), AWS GovCloud (US-East), AWS GovCloud (US-West) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d513c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).