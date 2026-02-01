# ListSolutions

Returns a list of solutions in a given dataset group.
When a dataset group is not specified, all the solutions associated with the account are listed.
The response provides the properties for each solution, including the Amazon Resource Name (ARN).
For more information on solutions, see [CreateSolution](API_CreateSolution.md "API_CreateSolution.md").

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "maxResults": `number`,
   "nextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_ListSolutions_RequestSyntax "#API_ListSolutions_RequestSyntax")**

The Amazon Resource Name (ARN) of the dataset group.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[maxResults](#API_ListSolutions_RequestSyntax "#API_ListSolutions_RequestSyntax")**

The maximum number of solutions to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListSolutions_RequestSyntax "#API_ListSolutions_RequestSyntax")**

A token returned from the previous call to `ListSolutions` for getting
the next set of solutions (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "nextToken": "***string***",
   "solutions": [
      {
         "creationDateTime": ***number***,
         "lastUpdatedDateTime": ***number***,
         "name": "***string***",
         "recipeArn": "***string***",
         "solutionArn": "***string***",
         "status": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[nextToken](#API_ListSolutions_ResponseSyntax "#API_ListSolutions_ResponseSyntax")**

A token for getting the next set of solutions (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

**[solutions](#API_ListSolutions_ResponseSyntax "#API_ListSolutions_ResponseSyntax")**

A list of the current solutions.

Type: Array of [SolutionSummary](API_SolutionSummary.md "API_SolutionSummary.md") objects

Array Members: Maximum number of 100 items.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListSolutions.md "../../../goto/cli2/personalize-2018-05-22/ListSolutions.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/ListSolutions.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/ListSolutions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListSolutions.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListSolutions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListSolutions.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListSolutions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListSolutions.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListSolutions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListSolutions.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListSolutions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListSolutions.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListSolutions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListSolutions.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListSolutions.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListSolutions.md "../../../goto/boto3/personalize-2018-05-22/ListSolutions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListSolutions.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListSolutions.md")
