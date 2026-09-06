

# redshift-cluster-subnet-group-multi-az
<a name="redshift-cluster-subnet-group-multi-az"></a>

Checks If Amazon Redshift subnet groups contain subnets from more than one Availability Zone. The rule is NON\_COMPLIANT if an Amazon Redshift subnet group does not contain subnets from at least two different Availability Zones. 



**Identifier:** REDSHIFT\_CLUSTER\_SUBNET\_GROUP\_MULTI\_AZ

**Resource Types:** AWS::Redshift::ClusterSubnetGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1307c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).