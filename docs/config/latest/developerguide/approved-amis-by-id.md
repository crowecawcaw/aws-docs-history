

# approved-amis-by-id
<a name="approved-amis-by-id"></a>

Checks if EC2 instances are using specified Amazon Machine Images (AMIs). Specify a list of approved AMI IDs. Running instances with AMIs that are not on this list are NON\_COMPLIANT. 



**Identifier:** APPROVED\_AMIS\_BY\_ID

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

amiIdsType: CSV  
Comma-separated list of AMI IDs. There is a 1024 characters limit.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d165c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).