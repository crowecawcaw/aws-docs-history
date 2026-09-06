

# internet-gateway-authorized-vpc-only
<a name="internet-gateway-authorized-vpc-only"></a>

Checks if internet gateways are attached to an authorized virtual private cloud (Amazon VPC). The rule is NON\_COMPLIANT if internet gateways are attached to an unauthorized VPC. 



**Identifier:** INTERNET\_GATEWAY\_AUTHORIZED\_VPC\_ONLY

**Resource Types:** AWS::EC2::InternetGateway

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

AuthorizedVpcIds (Optional)Type: CSV  
Comma-separated list of the authorized VPC IDs with attached IGWs. If parameter is not provided all attached IGWs will be NON\_COMPLIANT.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d981c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).