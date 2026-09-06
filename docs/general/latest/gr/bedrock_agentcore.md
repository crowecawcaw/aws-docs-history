

# Amazon Bedrock AgentCore endpoints and quotas
<a name="bedrock_agentcore"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="bedrock_agentcore_region"></a>

### Amazon Bedrock AgentCore control plane APIs
<a name="bedrock_agentcore_cp"></a>

The following table provides a list of Region-specific endpoints that Amazon Bedrock AgentCore supports for calling control plane operations.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | bedrock-agentcore-control.us-east-1.amazonaws.com | HTTPS | 
| US East (Ohio) | us-east-2 | bedrock-agentcore-control.us-east-2.amazonaws.com | HTTPS | 
| US West (Oregon) | us-west-2 | bedrock-agentcore-control.us-west-2.amazonaws.com | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | bedrock-agentcore-control. ap-southeast-1.amazonaws.com | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | bedrock-agentcore-control.ap-southeast-2.amazonaws.com | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 | bedrock-agentcore-control.ap-south-1.amazonaws.com | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | bedrock-agentcore-control.ap-northeast-1.amazonaws.com | HTTPS | 
| Europe (Ireland) | eu-west-1 | bedrock-agentcore-control.eu-west-1.amazonaws.com | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | bedrock-agentcore-control.eu-central-1.amazonaws.com | HTTPS | 

### Amazon Bedrock AgentCore data plane APIs
<a name="bedrock_agentcore_dp"></a>

The following table provides a list of Region-specific endpoints that Amazon Bedrock AgentCore supports for calling data plane operations.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | bedrock-agentcore.us-east-1.amazonaws.com | HTTPS | 
| US East (Ohio) | us-east-2 | bedrock-agentcore.us-east-2.amazonaws.com | HTTPS | 
| US West (Oregon) | us-west-2 | bedrock-agentcore.us-west-2.amazonaws.com | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | bedrock-agentcore.ap-southeast-1.amazonaws.com | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | bedrock-agentcore.ap-southeast-2.amazonaws.com | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 | bedrock-agentcore.ap-south-1.amazonaws.com | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | bedrock-agentcore.ap-northeast-1.amazonaws.com | HTTPS | 
| Europe (Ireland) | eu-west-1 | bedrock-agentcore.eu-west-1.amazonaws.com | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | bedrock-agentcore.eu-central-1.amazonaws.com | HTTPS | 

### Amazon Bedrock AgentCore Gateway data plane APIs
<a name="bedrock_agentcore_gateway_dp"></a>

The following table provides a list of Region-specific endpoints that Amazon Bedrock AgentCore Gateway supports for invoking a gateway.

Replace {{gatewayId}} with the ID of your gateway.


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | {{gatewayId}}.gateway.bedrock-agentcore.us-east-1.amazonaws.com | HTTPS | 
| US East (Ohio) | us-east-2 | {{gatewayId}}.gateway.bedrock-agentcore.us-east-2.amazonaws.com | HTTPS | 
| US West (Oregon) | us-west-2 | {{gatewayId}}.gateway.bedrock-agentcore.us-west-2.amazonaws.com | HTTPS | 
| Europe (Frankfurt) | eu-central-1 | {{gatewayId}}.gateway.bedrock-agentcore.eu-central-1.amazonaws.com | HTTPS | 
| Europe (Ireland) | eu-west-1 | {{gatewayId}}.gateway.bedrock-agentcore.eu-west-1.amazonaws.com | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | {{gatewayId}}.gateway.bedrock-agentcore.ap-northeast-1.amazonaws.com | HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 | {{gatewayId}}.gateway.bedrock-agentcore.ap-south-1.amazonaws.com | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 | {{gatewayId}}.gateway.bedrock-agentcore.ap-southeast-1.amazonaws.com | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 | {{gatewayId}}.gateway.bedrock-agentcore.ap-southeast-2.amazonaws.com | HTTPS | 
| US West (N. California) | us-west-1 | {{gatewayId}}.gateway.bedrock-agentcore.us-west-1.amazonaws.com | HTTPS | 
| Europe (London) | eu-west-2 | {{gatewayId}}.gateway.bedrock-agentcore.eu-west-2.amazonaws.com | HTTPS | 
| Europe (Paris) | eu-west-3 | {{gatewayId}}.gateway.bedrock-agentcore.eu-west-3.amazonaws.com | HTTPS | 
| Europe (Milan) | eu-south-1 | {{gatewayId}}.gateway.bedrock-agentcore.eu-south-1.amazonaws.com | HTTPS | 
| Europe (Spain) | eu-south-2 | {{gatewayId}}.gateway.bedrock-agentcore.eu-south-2.amazonaws.com | HTTPS | 
| Europe (Stockholm) | eu-north-1 | {{gatewayId}}.gateway.bedrock-agentcore.eu-north-1.amazonaws.com | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 | {{gatewayId}}.gateway.bedrock-agentcore.ap-northeast-2.amazonaws.com | HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 | {{gatewayId}}.gateway.bedrock-agentcore.ap-south-2.amazonaws.com | HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 | {{gatewayId}}.gateway.bedrock-agentcore.ap-southeast-5.amazonaws.com | HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 | {{gatewayId}}.gateway.bedrock-agentcore.ap-southeast-7.amazonaws.com | HTTPS | 
| Canada (Central) | ca-central-1 | {{gatewayId}}.gateway.bedrock-agentcore.ca-central-1.amazonaws.com | HTTPS | 
| South America (São Paulo) | sa-east-1 | {{gatewayId}}.gateway.bedrock-agentcore.sa-east-1.amazonaws.com | HTTPS | 

## Service quotas
<a name="limits_bedrock_agentcore"></a>

For information about Amazon Bedrock AgentCore service quotas, see [Quotas for Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html).