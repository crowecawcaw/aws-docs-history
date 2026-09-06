

# vpc-flow-logs-enabled
<a name="vpc-flow-logs-enabled"></a>

Checks if Amazon Virtual Private Cloud (Amazon VPC) flow logs are found and enabled for all Amazon VPCs. The rule is NON\_COMPLIANT if flow logs are not enabled for at least one Amazon VPC. 



**Identifier:** VPC\_FLOW\_LOGS\_ENABLED

**Resource Types:** AWS::EC2::VPC

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

trafficType (Optional)Type: String  
TrafficType of flow logs

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1603c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).