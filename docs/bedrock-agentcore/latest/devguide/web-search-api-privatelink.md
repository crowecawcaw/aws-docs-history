

# Call AgentCore Web Search through AWS PrivateLink
<a name="web-search-api-privatelink"></a>

You can call the `InvokeWebSearch` API from your virtual private cloud (VPC) without going through the internet. To do so, create an interface VPC endpoint for the Amazon Bedrock AgentCore data plane service, `com.amazonaws.region.bedrock-agentcore`. If you enable private DNS for the endpoint, the AWS SDKs and the AWS Command Line Interface (AWS CLI) reach the API through the endpoint without any change to your code.

If you attach an endpoint policy to the interface endpoint, the policy applies to `InvokeWebSearch` requests in addition to your AWS Identity and Access Management (IAM) policies. For more information about interface endpoints for Amazon Bedrock AgentCore, see [Use AWS PrivateLink to create a private connection](vpc-interface-endpoints.md).