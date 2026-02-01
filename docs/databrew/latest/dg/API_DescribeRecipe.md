# DescribeRecipe

Returns the definition of a specific DataBrew recipe corresponding to a particular
version.

## Request Syntax

```
GET /recipes/`name`?recipeVersion=`RecipeVersion` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DescribeRecipe_RequestSyntax "#API_DescribeRecipe_RequestSyntax")**

The name of the recipe to be described.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**[RecipeVersion](#API_DescribeRecipe_RequestSyntax "#API_DescribeRecipe_RequestSyntax")**

The recipe version identifier. If this parameter isn't specified, then the latest
published version is returned.

Length Constraints: Minimum length of 1. Maximum length of 16.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateDate": ***number***,
   "CreatedBy": "***string***",
   "Description": "***string***",
   "LastModifiedBy": "***string***",
   "LastModifiedDate": ***number***,
   "Name": "***string***",
   "ProjectName": "***string***",
   "PublishedBy": "***string***",
   "PublishedDate": ***number***,
   "RecipeVersion": "***string***",
   "ResourceArn": "***string***",
   "Steps": [
      {
         "Action": {
            "Operation": "***string***",
            "Parameters": {
               "***string***" : "***string***"
            }
         },
         "ConditionExpressions": [
            {
               "Condition": "***string***",
               "TargetColumn": "***string***",
               "Value": "***string***"
            }
         ]
      }
   ],
   "Tags": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The name of the recipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[CreateDate](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The date and time that the recipe was created.

Type: Timestamp

**[CreatedBy](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The identifier (user name) of the user who created the recipe.

Type: String

**[Description](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The description of the recipe.

Type: String

Length Constraints: Maximum length of 1024.

**[LastModifiedBy](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The identifier (user name) of the user who last modified the recipe.

Type: String

**[LastModifiedDate](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The date and time that the recipe was last modified.

Type: Timestamp

**[ProjectName](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The name of the project associated with this recipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[PublishedBy](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The identifier (user name) of the user who last published the recipe.

Type: String

**[PublishedDate](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The date and time when the recipe was last published.

Type: Timestamp

**[RecipeVersion](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The recipe version identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 16.

**[ResourceArn](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

The ARN of the recipe.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

**[Steps](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

One or more steps to be performed by the recipe. Each step consists of an action, and
the conditions under which the action should succeed.

Type: Array of [RecipeStep](API_RecipeStep.md "API_RecipeStep.md") objects

**[Tags](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

Metadata tags associated with this project.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/DescribeRecipe.md "../../../goto/cli2/databrew-2017-07-25/DescribeRecipe.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/DescribeRecipe.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/DescribeRecipe.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DescribeRecipe.md "../../../goto/SdkForCpp/databrew-2017-07-25/DescribeRecipe.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeRecipe.md "../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeRecipe.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeRecipe.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeRecipe.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeRecipe.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeRecipe.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeRecipe.md "../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeRecipe.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeRecipe.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeRecipe.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/DescribeRecipe.md "../../../goto/boto3/databrew-2017-07-25/DescribeRecipe.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeRecipe.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeRecipe.md")
