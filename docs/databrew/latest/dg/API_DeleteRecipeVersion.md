# DeleteRecipeVersion

Deletes a single version of a DataBrew recipe.

## Request Syntax

```
DELETE /recipes/`name`/recipeVersion/`recipeVersion` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DeleteRecipeVersion_RequestSyntax "#API_DeleteRecipeVersion_RequestSyntax")**

The name of the recipe.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**[recipeVersion](#API_DeleteRecipeVersion_RequestSyntax "#API_DeleteRecipeVersion_RequestSyntax")**

The version of the recipe to be deleted. You can specify a numeric versions
(`X.Y`) or `LATEST_WORKING`. `LATEST_PUBLISHED` is
not supported.

Length Constraints: Minimum length of 1. Maximum length of 16.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "***string***",
   "RecipeVersion": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_DeleteRecipeVersion_ResponseSyntax "#API_DeleteRecipeVersion_ResponseSyntax")**

The name of the recipe that was deleted.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[RecipeVersion](#API_DeleteRecipeVersion_ResponseSyntax "#API_DeleteRecipeVersion_ResponseSyntax")**

The version of the recipe that was deleted.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 16.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

HTTP Status Code: 409

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/cli2/databrew-2017-07-25/DeleteRecipeVersion.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/DeleteRecipeVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/SdkForCpp/databrew-2017-07-25/DeleteRecipeVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/SdkForGoV2/databrew-2017-07-25/DeleteRecipeVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DeleteRecipeVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DeleteRecipeVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/SdkForKotlin/databrew-2017-07-25/DeleteRecipeVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/DeleteRecipeVersion.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/boto3/databrew-2017-07-25/DeleteRecipeVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DeleteRecipeVersion.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DeleteRecipeVersion.md")
