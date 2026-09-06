

# rds-cluster-multi-az-enabled
<a name="rds-cluster-multi-az-enabled"></a>

Checks if Multi-Availability Zone (Multi-AZ) replication is enabled on Amazon Aurora and Multi-AZ DB clusters managed by Amazon Relational Database Service (Amazon RDS). The rule is NON\_COMPLIANT if an Amazon RDS instance is not configured with Multi-AZ. 



**Identifier:** RDS\_CLUSTER\_MULTI\_AZ\_ENABLED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1233c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).