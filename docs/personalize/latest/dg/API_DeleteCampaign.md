# DeleteCampaign

Removes a campaign by deleting the solution deployment. The solution that
the campaign is based on is not deleted and can be redeployed when needed. A deleted campaign can no
longer be specified in a
[GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md")
request.
For information on creating campaigns, see [CreateCampaign](API_CreateCampaign.md "API_CreateCampaign.md").

## Request Syntax

```
{
   "campaignArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[campaignArn](#API_DeleteCampaign_RequestSyntax "#API_DeleteCampaign_RequestSyntax")**

The Amazon Resource Name (ARN) of the campaign to delete.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DeleteCampaign.md "../../../goto/cli2/personalize-2018-05-22/DeleteCampaign.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DeleteCampaign.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DeleteCampaign.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DeleteCampaign.md "../../../goto/SdkForCpp/personalize-2018-05-22/DeleteCampaign.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DeleteCampaign.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DeleteCampaign.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DeleteCampaign.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DeleteCampaign.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DeleteCampaign.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DeleteCampaign.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DeleteCampaign.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DeleteCampaign.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DeleteCampaign.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DeleteCampaign.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DeleteCampaign.md "../../../goto/boto3/personalize-2018-05-22/DeleteCampaign.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DeleteCampaign.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DeleteCampaign.md")
