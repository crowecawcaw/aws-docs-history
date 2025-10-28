# ListAgents

Returns a list of AWS DataSync agents that belong to an AWS account in the AWS Region specified in the request.

With pagination, you can reduce the number of agents returned in a response. If you get
a truncated list of agents in a response, the response contains a marker that you can specify
in your next request to fetch the next page of agents.

`ListAgents` is eventually consistent. This means the result of running the
operation might not reflect that you just created or deleted an agent. For example, if you
create an agent with [CreateAgent](API_CreateAgent.md "API_CreateAgent.md") and then
immediately run `ListAgents`, that agent might not show up in the list right away.
In situations like this, you can always confirm whether an agent has been created (or deleted)
by using [DescribeAgent](API_DescribeAgent.md "API_DescribeAgent.md").

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[MaxResults](#API_ListAgents_RequestSyntax "#API_ListAgents_RequestSyntax")**

Specifies the maximum number of DataSync agents to list in a response. By
default, a response shows a maximum of 100 agents.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[NextToken](#API_ListAgents_RequestSyntax "#API_ListAgents_RequestSyntax")**

Specifies an opaque string that indicates the position to begin the next list of
results in the response.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

Required: No

## Response Syntax

```
{
   "Agents": [
      {
         "AgentArn": "***string***",
         "Name": "***string***",
         "Platform": {
            "Version": "***string***"
         },
         "Status": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Agents](#API_ListAgents_ResponseSyntax "#API_ListAgents_ResponseSyntax")**

A list of DataSync agents in your AWS account in the AWS Region specified in the request. The list is ordered by the agents' Amazon
Resource Names (ARNs).

Type: Array of [AgentListEntry](API_AgentListEntry.md "API_AgentListEntry.md") objects

**[NextToken](#API_ListAgents_ResponseSyntax "#API_ListAgents_ResponseSyntax")**

The opaque string that indicates the position to begin the next list of results in the
response.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/ListAgents.md "../../../goto/cli2/datasync-2018-11-09/ListAgents.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/ListAgents.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/ListAgents.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ListAgents.md "../../../goto/SdkForCpp/datasync-2018-11-09/ListAgents.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/ListAgents.md "../../../goto/SdkForGoV2/datasync-2018-11-09/ListAgents.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ListAgents.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ListAgents.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListAgents.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListAgents.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/ListAgents.md "../../../goto/SdkForKotlin/datasync-2018-11-09/ListAgents.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/ListAgents.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/ListAgents.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/ListAgents.md "../../../goto/boto3/datasync-2018-11-09/ListAgents.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ListAgents.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ListAgents.md")
