# StopRecommender

Stops a recommender that is ACTIVE. Stopping a recommender halts billing and automatic retraining for the recommender.

## Request Syntax

```
{
   "recommenderArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[recommenderArn](#API_StopRecommender_RequestSyntax "#API_StopRecommender_RequestSyntax")**

The Amazon Resource Name (ARN) of the recommender to stop.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "recommenderArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[recommenderArn](#API_StopRecommender_ResponseSyntax "#API_StopRecommender_ResponseSyntax")**

The Amazon Resource Name (ARN) of the recommender you stopped.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/StopRecommender.md "../../../goto/cli2/personalize-2018-05-22/StopRecommender.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/StopRecommender.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/StopRecommender.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/StopRecommender.md "../../../goto/SdkForCpp/personalize-2018-05-22/StopRecommender.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/StopRecommender.md "../../../goto/SdkForGoV2/personalize-2018-05-22/StopRecommender.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/StopRecommender.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/StopRecommender.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/StopRecommender.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/StopRecommender.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/StopRecommender.md "../../../goto/SdkForKotlin/personalize-2018-05-22/StopRecommender.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/StopRecommender.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/StopRecommender.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/StopRecommender.md "../../../goto/boto3/personalize-2018-05-22/StopRecommender.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/StopRecommender.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/StopRecommender.md")
