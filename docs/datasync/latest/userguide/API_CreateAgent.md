# CreateAgent

Activates an AWS DataSync agent that you deploy in your storage environment.
The activation process associates the agent with your AWS account.

If you haven't deployed an agent yet, see [Do I need a DataSync
agent?](do-i-need-datasync-agent.md "do-i-need-datasync-agent.md")

## Request Syntax

```
{
   "ActivationKey": "`string`",
   "AgentName": "`string`",
   "SecurityGroupArns": [ "`string`" ],
   "SubnetArns": [ "`string`" ],
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "VpcEndpointId": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[ActivationKey](#API_CreateAgent_RequestSyntax "#API_CreateAgent_RequestSyntax")**

Specifies your DataSync agent's activation key. If you don't have an
activation key, see [Activating your agent](activate-agent.md "activate-agent.md").

Type: String

Length Constraints: Maximum length of 29.

Pattern: `[A-Z0-9]{5}(-[A-Z0-9]{5}){4}`

Required: Yes

**[AgentName](#API_CreateAgent_RequestSyntax "#API_CreateAgent_RequestSyntax")**

Specifies a name for your agent. We recommend specifying a name that you can
remember.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

Required: No

**[SecurityGroupArns](#API_CreateAgent_RequestSyntax "#API_CreateAgent_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the security group that allows traffic between
your agent and VPC service endpoint. You can only specify one ARN.

Type: Array of strings

Array Members: Fixed number of 1 item.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

Required: No

**[SubnetArns](#API_CreateAgent_RequestSyntax "#API_CreateAgent_RequestSyntax")**

Specifies the ARN of the subnet where your VPC service endpoint is located. You can only
specify one ARN.

Type: Array of strings

Array Members: Fixed number of 1 item.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:subnet/.*$`

Required: No

**[Tags](#API_CreateAgent_RequestSyntax "#API_CreateAgent_RequestSyntax")**

Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least one tag for your agent.

Type: Array of [TagListEntry](API_TagListEntry.md "API_TagListEntry.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Required: No

**[VpcEndpointId](#API_CreateAgent_RequestSyntax "#API_CreateAgent_RequestSyntax")**

Specifies the ID of the [VPC service
endpoint](choose-service-endpoint.md#datasync-in-vpc "choose-service-endpoint.md#datasync-in-vpc") that you're using. For example, a VPC endpoint ID looks like
`vpce-01234d5aff67890e1`.

###### Important

The VPC service endpoint you use must include the DataSync service name (for
example, `com.amazonaws.us-east-2.datasync`).

Type: String

Pattern: `^vpce-[0-9a-f]{17}$`

Required: No

## Response Syntax

```
{
   "AgentArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AgentArn](#API_CreateAgent_ResponseSyntax "#API_CreateAgent_ResponseSyntax")**

The ARN of the agent that you just activated. Use the [ListAgents](API_ListAgents.md "API_ListAgents.md") operation to return a
list of agents in your AWS account and AWS Region.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

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

The following example activates a DataSync agent.

```
{
    "ActivationKey": "AAAAA-1AAAA-BB1CC-33333-EEEEE",
    "AgentName": "MyAgent",
    "Tags": [{
        "Key": "Job",
        "Value": "TransferJob-1"
    }]
}
```

### Sample Response

The response returns the ARN of the activated agent.

```
{
    "AgentArn": "arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44baca3"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateAgent.md "../../../goto/cli2/datasync-2018-11-09/CreateAgent.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateAgent.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateAgent.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateAgent.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateAgent.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateAgent.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateAgent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateAgent.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateAgent.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateAgent.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateAgent.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateAgent.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateAgent.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateAgent.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateAgent.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateAgent.md "../../../goto/boto3/datasync-2018-11-09/CreateAgent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateAgent.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateAgent.md")
