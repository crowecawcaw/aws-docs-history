# DescribeAgent

Returns information about an AWS DataSync agent, such as its name, service
endpoint type, and status.

## Request Syntax

```
{
   "AgentArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[AgentArn](#API_DescribeAgent_RequestSyntax "#API_DescribeAgent_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the DataSync agent that you want
information about.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "AgentArn": "***string***",
   "CreationTime": ***number***,
   "EndpointType": "***string***",
   "LastConnectionTime": ***number***,
   "Name": "***string***",
   "Platform": {
      "Version": "***string***"
   },
   "PrivateLinkConfig": {
      "PrivateLinkEndpoint": "***string***",
      "SecurityGroupArns": [ "***string***" ],
      "SubnetArns": [ "***string***" ],
      "VpcEndpointId": "***string***"
   },
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AgentArn](#API_DescribeAgent_ResponseSyntax "#API_DescribeAgent_ResponseSyntax")**

The ARN of the agent.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

**[CreationTime](#API_DescribeAgent_ResponseSyntax "#API_DescribeAgent_ResponseSyntax")**

The time that the agent was [activated](activate-agent.md "activate-agent.md").

Type: Timestamp

**[EndpointType](#API_DescribeAgent_ResponseSyntax "#API_DescribeAgent_ResponseSyntax")**

The type of [service endpoint](choose-service-endpoint.md "choose-service-endpoint.md") that your agent is connected to.

Type: String

Valid Values: `PUBLIC | PRIVATE_LINK | FIPS | FIPS_PRIVATE_LINK`

**[LastConnectionTime](#API_DescribeAgent_ResponseSyntax "#API_DescribeAgent_ResponseSyntax")**

The last time that the agent was communicating with the DataSync
service.

Type: Timestamp

**[Name](#API_DescribeAgent_ResponseSyntax "#API_DescribeAgent_ResponseSyntax")**

The name of the agent.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

**[Platform](#API_DescribeAgent_ResponseSyntax "#API_DescribeAgent_ResponseSyntax")**

The platform-related details about the agent, such as the version number.

Type: [Platform](API_Platform.md "API_Platform.md") object

**[PrivateLinkConfig](#API_DescribeAgent_ResponseSyntax "#API_DescribeAgent_ResponseSyntax")**

The network configuration that the agent uses when connecting to a [VPC
service endpoint](choose-service-endpoint.md#choose-service-endpoint-vpc "choose-service-endpoint.md#choose-service-endpoint-vpc").

Type: [PrivateLinkConfig](API_PrivateLinkConfig.md "API_PrivateLinkConfig.md") object

**[Status](#API_DescribeAgent_ResponseSyntax "#API_DescribeAgent_ResponseSyntax")**

The status of the agent.

- If the status is `ONLINE`, the agent is configured properly and ready to
  use.
- If the status is `OFFLINE`, the agent has been out of contact with
  DataSync for five minutes or longer. This can happen for a few reasons. For
  more information, see [What do I do if my agent is offline?](troubleshooting-datasync-agents.md#troubleshoot-agent-offline "troubleshooting-datasync-agents.md#troubleshoot-agent-offline")

Type: String

Valid Values: `ONLINE | OFFLINE`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## Examples

### Sample Request

The following example returns information about an agent specified in a
request.

```
{
  "AgentArn": "arn:aws:datasync:us-east-2:111122223333:agent/agent-1234567890abcdef0"
}
```

### Sample Response

The following example response describes an agent that uses a public service
endpoint.

```
{
    "AgentArn": "arn:aws:datasync:us-east-2:111122223333:agent/agent-1234567890abcdef0",
    "Name": "Data center migration agent",
    "Status": "ONLINE",
    "LastConnectionTime": "2022-10-17T17:21:35.540000+00:00",
    "CreationTime": "2022-10-05T20:52:29.499000+00:00",
    "EndpointType": "PUBLIC",
    "Platform": {
        "Version": "2"
    }
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeAgent.md "../../../goto/cli2/datasync-2018-11-09/DescribeAgent.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeAgent.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeAgent.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeAgent.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeAgent.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeAgent.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeAgent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeAgent.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeAgent.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeAgent.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeAgent.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeAgent.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeAgent.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeAgent.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeAgent.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeAgent.md "../../../goto/boto3/datasync-2018-11-09/DescribeAgent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeAgent.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeAgent.md")
