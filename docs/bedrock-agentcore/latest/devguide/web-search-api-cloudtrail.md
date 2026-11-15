

# Log AgentCore Web Search API calls with AWS CloudTrail
<a name="web-search-api-cloudtrail"></a>

 AWS CloudTrail records `InvokeWebSearch` requests as data events with the event name `InvokeWebSearch`, the event source `bedrock-agentcore.amazonaws.com`, and the resource type `AWS::BedrockAgentCore::WebSearch`. Each event lists the web search tool that the request named as its resource.

By default, CloudTrail doesn’t log data events, and they don’t appear in CloudTrail **Event history**. To record `InvokeWebSearch` requests, create a trail or event data store and add an advanced event selector for the `AWS::BedrockAgentCore::WebSearch` resource type.

CloudTrail records each request that Amazon Bedrock AgentCore authenticates. These include requests that are throttled, that an AWS Identity and Access Management (IAM) policy denies, or that have a field that isn’t valid. CloudTrail doesn’t record a request that is rejected before authentication, such as a request that is unsigned, that fails authentication, or whose body is too large. It also doesn’t record a request that only a virtual private cloud (VPC) endpoint policy denies. For an `AccessDeniedException`, the event’s `errorCode` is `AccessDenied`.

The `requestParameters` field of an event holds only `webSearchId` and, if the request sets it, `maxResults`. CloudTrail doesn’t record the search text or the filters.

**Important**  
Additional charges apply for data events. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/) on the AWS website.