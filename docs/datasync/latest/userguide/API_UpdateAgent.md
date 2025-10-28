# UpdateAgent

Updates the name of an AWS DataSync agent.

## Request Syntax

```
{
   "AgentArn": "`string`",
   "Name": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[AgentArn](#API_UpdateAgent_RequestSyntax "#API_UpdateAgent_RequestSyntax")**

The Amazon Resource Name (ARN) of the agent to update.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: Yes

**[Name](#API_UpdateAgent_RequestSyntax "#API_UpdateAgent_RequestSyntax")**

The name that you want to use to configure the agent.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

Required: No

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateAgent.md "../../../goto/cli2/datasync-2018-11-09/UpdateAgent.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateAgent.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateAgent.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateAgent.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateAgent.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateAgent.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateAgent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateAgent.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateAgent.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateAgent.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateAgent.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateAgent.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateAgent.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateAgent.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateAgent.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateAgent.md "../../../goto/boto3/datasync-2018-11-09/UpdateAgent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateAgent.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateAgent.md")
