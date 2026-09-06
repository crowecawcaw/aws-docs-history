

# ec2-transit-gateway-multicast-domain-tagged
<a name="ec2-transit-gateway-multicast-domain-tagged"></a>

Checks if Amazon EC2 transit gateway multicast domains have tags. Optionally, you can specify tag keys. The rule is NON\_COMPLIANT if there are no tags or if the specified tag keys are not present. The rule does not check for tags starting with 'aws:'. 



**Identifier:** EC2\_TRANSIT\_GATEWAY\_MULTICAST\_DOMAIN\_TAGGED

**Resource Types:** AWS::EC2::TransitGatewayMulticastDomain

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

requiredKeyTags (Optional)Type: CSV  
Comma-separated list of tag keys for the rule to check. If provided, the rule is NON\_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d635c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).