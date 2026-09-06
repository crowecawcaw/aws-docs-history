

# vpc-endpoint-enabled
<a name="vpc-endpoint-enabled"></a>

Checks if each service specified in the parameter has an Amazon VPC endpoint. The rule is NON\_COMPLIANT if Amazon VPC does not have a VPC endpoint created for each specified service. Optionally, you can specify certain VPCs for the rule to check. 



**Identifier:** VPC\_ENDPOINT\_ENABLED

**Resource Types:** AWS::EC2::VPC

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

serviceNamesType: CSV  
Comma-separated list of service names or endpoints. Example: "ec2, ecr.api" or "com.amazonaws.region.ec2". Use DescribeVpcEndpointServices for available names. The rule considers FIPS version of the endpoint to be compliant as well.

vpcIds (Optional)Type: CSV  
Comma-separated list of Amazon VPC IDs for VPC endpoints. If provided, the rule is NON\_COMPLIANT if the services specified in the serviceName parameter do not have one of these VPC endpoints.

scopeConfigResourceTypes (Optional)Type: CSV  
Comma-separated list of AWS Config resource types for the rule to check. If specified, the rule returns a compliance status only if at least one specified resource is recorded in the account. For example: "AWS::SNS::Topic".

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1601c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).