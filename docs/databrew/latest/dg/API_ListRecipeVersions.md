# ListRecipeVersions

Lists the versions of a particular DataBrew recipe, except for
`LATEST_WORKING`.

## Request Syntax

```
GET /recipeVersions?maxResults=`MaxResults`&name=`Name`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListRecipeVersions_RequestSyntax "#API_ListRecipeVersions_RequestSyntax")**

The maximum number of results to return in this request.

Valid Range: Minimum value of 1. Maximum value of 100.

**[Name](#API_ListRecipeVersions_RequestSyntax "#API_ListRecipeVersions_RequestSyntax")**

The name of the recipe for which to return version information.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**[NextToken](#API_ListRecipeVersions_RequestSyntax "#API_ListRecipeVersions_RequestSyntax")**

The token returned by a previous call to retrieve the next set of results.

Length Constraints: Minimum length of 1. Maximum length of 2000.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Recipes": [
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
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Recipes](#API_ListRecipeVersions_ResponseSyntax "#API_ListRecipeVersions_ResponseSyntax")**

A list of versions for the specified recipe.

Type: Array of [Recipe](API_Recipe.md "API_Recipe.md") objects

**[NextToken](#API_ListRecipeVersions_ResponseSyntax "#API_ListRecipeVersions_ResponseSyntax")**

A token that you can use in a subsequent call to retrieve the next set of
results.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/cli2/databrew-2017-07-25/ListRecipeVersions.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/ListRecipeVersions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/SdkForCpp/databrew-2017-07-25/ListRecipeVersions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/SdkForGoV2/databrew-2017-07-25/ListRecipeVersions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ListRecipeVersions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListRecipeVersions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/SdkForKotlin/databrew-2017-07-25/ListRecipeVersions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/ListRecipeVersions.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/boto3/databrew-2017-07-25/ListRecipeVersions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ListRecipeVersions.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ListRecipeVersions.md")
