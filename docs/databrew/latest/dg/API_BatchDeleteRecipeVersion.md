# BatchDeleteRecipeVersion

Deletes one or more versions of a recipe at a time.

The entire request will be rejected if:

- The recipe does not exist.
- There is an invalid version identifier in the list of versions.
- The version list is empty.
- The version list size exceeds 50.
- The version list contains duplicate entries.
  The request will complete successfully, but with partial failures, if:

- A version does not exist.
- A version is being used by a job.
- You specify `LATEST_WORKING`, but it's being used by a
  project.
- The version fails to be deleted.
  The `LATEST_WORKING` version will only be deleted if the recipe has no
  other versions. If you try to delete `LATEST_WORKING` while other versions
  exist (or if they can't be deleted), then `LATEST_WORKING` will be listed as
  partial failure in the response.

## Request Syntax

```
POST /recipes/`name`/batchDeleteRecipeVersion HTTP/1.1
Content-type: application/json

{
   "RecipeVersions": [ "`string`" ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_BatchDeleteRecipeVersion_RequestSyntax "#API_BatchDeleteRecipeVersion_RequestSyntax")**

The name of the recipe whose versions are to be deleted.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[RecipeVersions](#API_BatchDeleteRecipeVersion_RequestSyntax "#API_BatchDeleteRecipeVersion_RequestSyntax")**

An array of version identifiers, for the recipe versions to be deleted. You can
specify numeric versions (`X.Y`) or `LATEST_WORKING`.
`LATEST_PUBLISHED` is not supported.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 16.

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "ErrorCode": "***string***",
         "ErrorMessage": "***string***",
         "RecipeVersion": "***string***"
      }
   ],
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_BatchDeleteRecipeVersion_ResponseSyntax "#API_BatchDeleteRecipeVersion_ResponseSyntax")**

The name of the recipe that was modified.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[Errors](#API_BatchDeleteRecipeVersion_ResponseSyntax "#API_BatchDeleteRecipeVersion_ResponseSyntax")**

Errors, if any, that occurred while attempting to delete the recipe versions.

Type: Array of [RecipeVersionErrorDetail](API_RecipeVersionErrorDetail.md "API_RecipeVersionErrorDetail.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/cli2/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/SdkForCpp/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/SdkForGoV2/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/SdkForKotlin/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/boto3/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/BatchDeleteRecipeVersion.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/BatchDeleteRecipeVersion.md")
