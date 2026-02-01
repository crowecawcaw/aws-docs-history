# PublishRecipe

Publishes a new version of a DataBrew recipe.

## Request Syntax

```
POST /recipes/`name`/publishRecipe HTTP/1.1
Content-type: application/json

{
   "Description": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_PublishRecipe_RequestSyntax "#API_PublishRecipe_RequestSyntax")**

The name of the recipe to be published.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Description](#API_PublishRecipe_RequestSyntax "#API_PublishRecipe_RequestSyntax")**

A description of the recipe to be published, for this version of the recipe.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_PublishRecipe_ResponseSyntax "#API_PublishRecipe_ResponseSyntax")**

The name of the recipe that you published.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ServiceQuotaExceededException**

A service quota is exceeded.

HTTP Status Code: 402

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/PublishRecipe.md "../../../goto/cli2/databrew-2017-07-25/PublishRecipe.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/PublishRecipe.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/PublishRecipe.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/PublishRecipe.md "../../../goto/SdkForCpp/databrew-2017-07-25/PublishRecipe.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/PublishRecipe.md "../../../goto/SdkForGoV2/databrew-2017-07-25/PublishRecipe.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/PublishRecipe.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/PublishRecipe.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/PublishRecipe.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/PublishRecipe.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/PublishRecipe.md "../../../goto/SdkForKotlin/databrew-2017-07-25/PublishRecipe.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/PublishRecipe.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/PublishRecipe.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/PublishRecipe.md "../../../goto/boto3/databrew-2017-07-25/PublishRecipe.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/PublishRecipe.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/PublishRecipe.md")
