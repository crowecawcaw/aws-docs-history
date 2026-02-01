# ListSolutionVersions

Returns a list of solution versions for the given solution. When a solution is not
specified, all the solution versions associated with the account are listed. The response
provides the properties for each solution version, including the Amazon Resource Name (ARN).

## Request Syntax

```
{
   "maxResults": `number`,
   "nextToken": "`string`",
   "solutionArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[maxResults](#API_ListSolutionVersions_RequestSyntax "#API_ListSolutionVersions_RequestSyntax")**

The maximum number of solution versions to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListSolutionVersions_RequestSyntax "#API_ListSolutionVersions_RequestSyntax")**

A token returned from the previous call to `ListSolutionVersions` for getting
the next set of solution versions (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

**[solutionArn](#API_ListSolutionVersions_RequestSyntax "#API_ListSolutionVersions_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

## Response Syntax

```
{
   "nextToken": "***string***",
   "solutionVersions": [
      {
         "creationDateTime": ***number***,
         "failureReason": "***string***",
         "lastUpdatedDateTime": ***number***,
         "solutionVersionArn": "***string***",
         "status": "***string***",
         "trainingMode": "***string***",
         "trainingType": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[nextToken](#API_ListSolutionVersions_ResponseSyntax "#API_ListSolutionVersions_ResponseSyntax")**

A token for getting the next set of solution versions (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

**[solutionVersions](#API_ListSolutionVersions_ResponseSyntax "#API_ListSolutionVersions_ResponseSyntax")**

A list of solution versions describing the version properties.

Type: Array of [SolutionVersionSummary](API_SolutionVersionSummary.md "API_SolutionVersionSummary.md") objects

Array Members: Maximum number of 100 items.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/cli2/personalize-2018-05-22/ListSolutionVersions.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/ListSolutionVersions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListSolutionVersions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListSolutionVersions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListSolutionVersions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListSolutionVersions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListSolutionVersions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListSolutionVersions.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/boto3/personalize-2018-05-22/ListSolutionVersions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListSolutionVersions.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListSolutionVersions.md")
