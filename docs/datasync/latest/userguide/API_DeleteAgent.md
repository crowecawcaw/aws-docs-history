# DeleteAgent

Removes an AWS DataSync agent resource from your AWS account.

Keep in mind that this operation (which can't be undone) doesn't remove the agent's
virtual machine (VM) or Amazon EC2 instance from your storage environment. For next
steps, you can delete the VM or instance from your storage environment or reuse it to [activate a new
agent](activate-agent.md "activate-agent.md").

## Request Syntax

```
{
   "AgentArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[AgentArn](#API_DeleteAgent_RequestSyntax "#API_DeleteAgent_RequestSyntax")**

The Amazon Resource Name (ARN) of the agent to delete. Use the `ListAgents`
operation to return a list of agents for your account and AWS Region.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DeleteAgent.md "../../../goto/cli2/datasync-2018-11-09/DeleteAgent.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DeleteAgent.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DeleteAgent.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DeleteAgent.md "../../../goto/SdkForCpp/datasync-2018-11-09/DeleteAgent.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DeleteAgent.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DeleteAgent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DeleteAgent.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DeleteAgent.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DeleteAgent.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DeleteAgent.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DeleteAgent.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DeleteAgent.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DeleteAgent.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DeleteAgent.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DeleteAgent.md "../../../goto/boto3/datasync-2018-11-09/DeleteAgent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DeleteAgent.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DeleteAgent.md")
