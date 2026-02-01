# CreateRecipe

Creates a new DataBrew recipe.

## Request Syntax

```
POST /recipes HTTP/1.1
Content-type: application/json

{
   "Description": "`string`",
   "Name": "`string`",
   "Steps": [
      {
         "Action": {
            "Operation": "`string`",
            "Parameters": {
               "`string`" : "`string`"
            }
         },
         "ConditionExpressions": [
            {
               "Condition": "`string`",
               "TargetColumn": "`string`",
               "Value": "`string`"
            }
         ]
      }
   ],
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[Name](#API_CreateRecipe_RequestSyntax "#API_CreateRecipe_RequestSyntax")**

A unique name for the recipe. Valid characters are alphanumeric (A-Z, a-z, 0-9),
hyphen (-), period (.), and space.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**[Steps](#API_CreateRecipe_RequestSyntax "#API_CreateRecipe_RequestSyntax")**

An array containing the steps to be performed by the recipe. Each recipe step consists
of one recipe action and (optionally) an array of condition expressions.

Type: Array of [RecipeStep](API_RecipeStep.md "API_RecipeStep.md") objects

Required: Yes

**[Description](#API_CreateRecipe_RequestSyntax "#API_CreateRecipe_RequestSyntax")**

A description for the recipe.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**[Tags](#API_CreateRecipe_RequestSyntax "#API_CreateRecipe_RequestSyntax")**

Metadata tags to apply to this recipe.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

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

**[Name](#API_CreateRecipe_ResponseSyntax "#API_CreateRecipe_ResponseSyntax")**

The name of the recipe that you created.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

HTTP Status Code: 409

**ServiceQuotaExceededException**

A service quota is exceeded.

HTTP Status Code: 402

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/CreateRecipe.md "../../../goto/cli2/databrew-2017-07-25/CreateRecipe.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/CreateRecipe.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/CreateRecipe.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/CreateRecipe.md "../../../goto/SdkForCpp/databrew-2017-07-25/CreateRecipe.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/CreateRecipe.md "../../../goto/SdkForGoV2/databrew-2017-07-25/CreateRecipe.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/CreateRecipe.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/CreateRecipe.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateRecipe.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateRecipe.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/CreateRecipe.md "../../../goto/SdkForKotlin/databrew-2017-07-25/CreateRecipe.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/CreateRecipe.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/CreateRecipe.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/CreateRecipe.md "../../../goto/boto3/databrew-2017-07-25/CreateRecipe.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/CreateRecipe.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/CreateRecipe.md")
