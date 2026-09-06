

# redshift-enhanced-vpc-routing-enabled
<a name="redshift-enhanced-vpc-routing-enabled"></a>

Checks if Amazon Redshift cluster has 'enhancedVpcRouting' enabled. The rule is NON\_COMPLIANT if 'enhancedVpcRouting' is not enabled or if the configuration.enhancedVpcRouting field is 'false'. 



**Identifier:** REDSHIFT\_ENHANCED\_VPC\_ROUTING\_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1313c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).