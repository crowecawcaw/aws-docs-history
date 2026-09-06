

# service-vpc-endpoint-enabled
<a name="service-vpc-endpoint-enabled"></a>

Checks if Service Endpoint for the service provided in rule parameter is created for each Amazon Virtual Private Cloud (Amazon VPC). The rule is NON\_COMPLIANT if an Amazon VPC doesn't have an Amazon VPC endpoint created for the service. 



**Identifier:** SERVICE\_VPC\_ENDPOINT\_ENABLED

**Resource Types:** AWS::EC2::VPC

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

serviceNameType: String  
The short name or suffix for the service. Note: To get a list of available service names or valid suffix list, use DescribeVpcEndpointServices.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1523c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).