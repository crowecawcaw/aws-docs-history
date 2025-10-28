# UpdateRecipe

Modifies the definition of the `LATEST_WORKING` version of a DataBrew
recipe.

## Request Syntax

```
PUT /recipes/`name` HTTP/1.1
Content-type: application/json

{
   "Description": "`string`",
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
   ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_UpdateRecipe_RequestSyntax "#API_UpdateRecipe_RequestSyntax")**

The name of the recipe to be updated.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Description](#API_UpdateRecipe_RequestSyntax "#API_UpdateRecipe_RequestSyntax")**

A description of the recipe.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**[Steps](#API_UpdateRecipe_RequestSyntax "#API_UpdateRecipe_RequestSyntax")**

One or more steps to be performed by the recipe. Each step consists of an action, and
the conditions under which the action should succeed.

Type: Array of [RecipeStep](API_RecipeStep.md "API_RecipeStep.md") objects

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

**[Name](#API_UpdateRecipe_ResponseSyntax "#API_UpdateRecipe_ResponseSyntax")**

The name of the recipe that was updated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/UpdateRecipe.md "../../../goto/cli2/databrew-2017-07-25/UpdateRecipe.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/UpdateRecipe.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/UpdateRecipe.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/UpdateRecipe.md "../../../goto/SdkForCpp/databrew-2017-07-25/UpdateRecipe.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateRecipe.md "../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateRecipe.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateRecipe.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateRecipe.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateRecipe.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateRecipe.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateRecipe.md "../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateRecipe.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateRecipe.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateRecipe.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/UpdateRecipe.md "../../../goto/boto3/databrew-2017-07-25/UpdateRecipe.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateRecipe.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateRecipe.md")
