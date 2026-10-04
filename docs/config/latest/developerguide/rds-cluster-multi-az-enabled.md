

# rds-cluster-multi-az-enabled
<a name="rds-cluster-multi-az-enabled"></a>

Checks if Amazon Aurora DB clusters have DB instances deployed across multiple Availability Zones. The rule is NON\_COMPLIANT if the cluster's multiAZ property is false. 



**Identifier:** RDS\_CLUSTER\_MULTI\_AZ\_ENABLED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1241c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).