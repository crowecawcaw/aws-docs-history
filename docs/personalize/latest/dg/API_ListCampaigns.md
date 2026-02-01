# ListCampaigns

Returns a list of campaigns that use the given solution.
When a solution is not specified, all the campaigns associated with the account are listed.
The response provides the properties for each campaign, including the Amazon Resource Name (ARN).
For more information on campaigns, see [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md").

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

**[maxResults](#API_ListCampaigns_RequestSyntax "#API_ListCampaigns_RequestSyntax")**

The maximum number of campaigns to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListCampaigns_RequestSyntax "#API_ListCampaigns_RequestSyntax")**

A token returned from the previous call to [ListCampaigns](API_ListCampaigns.md "API_ListCampaigns.md") for getting
the next set of campaigns (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

**[solutionArn](#API_ListCampaigns_RequestSyntax "#API_ListCampaigns_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution to list the campaigns for. When
a solution is not specified, all the campaigns associated with the account are listed.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

## Response Syntax

```
{
   "campaigns": [
      {
         "campaignArn": "***string***",
         "creationDateTime": ***number***,
         "failureReason": "***string***",
         "lastUpdatedDateTime": ***number***,
         "name": "***string***",
         "status": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[campaigns](#API_ListCampaigns_ResponseSyntax "#API_ListCampaigns_ResponseSyntax")**

A list of the campaigns.

Type: Array of [CampaignSummary](API_CampaignSummary.md "API_CampaignSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListCampaigns_ResponseSyntax "#API_ListCampaigns_ResponseSyntax")**

A token for getting the next set of campaigns (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListCampaigns.md "../../../goto/cli2/personalize-2018-05-22/ListCampaigns.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/ListCampaigns.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/ListCampaigns.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListCampaigns.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListCampaigns.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListCampaigns.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListCampaigns.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListCampaigns.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListCampaigns.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListCampaigns.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListCampaigns.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListCampaigns.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListCampaigns.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListCampaigns.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListCampaigns.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListCampaigns.md "../../../goto/boto3/personalize-2018-05-22/ListCampaigns.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListCampaigns.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListCampaigns.md")
