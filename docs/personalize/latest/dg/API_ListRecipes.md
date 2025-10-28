# ListRecipes

Returns a list of available recipes. The response provides the properties
for each recipe, including the recipe's Amazon Resource Name (ARN).

## Request Syntax

```
{
   "domain": "`string`",
   "maxResults": `number`,
   "nextToken": "`string`",
   "recipeProvider": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[domain](#API_ListRecipes_RequestSyntax "#API_ListRecipes_RequestSyntax")**

Filters returned recipes by domain for a Domain dataset group. Only recipes (Domain dataset group use cases)
for this domain are included in the response. If you don't specify a domain, all recipes are returned.

Type: String

Valid Values: `ECOMMERCE | VIDEO_ON_DEMAND`

Required: No

**[maxResults](#API_ListRecipes_RequestSyntax "#API_ListRecipes_RequestSyntax")**

The maximum number of recipes to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListRecipes_RequestSyntax "#API_ListRecipes_RequestSyntax")**

A token returned from the previous call to `ListRecipes` for getting
the next set of recipes (if they exist).

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

**[recipeProvider](#API_ListRecipes_RequestSyntax "#API_ListRecipes_RequestSyntax")**

The default is `SERVICE`.

Type: String

Valid Values: `SERVICE`

Required: No

## Response Syntax

```
{
   "nextToken": "***string***",
   "recipes": [
      {
         "creationDateTime": ***number***,
         "domain": "***string***",
         "lastUpdatedDateTime": ***number***,
         "name": "***string***",
         "recipeArn": "***string***",
         "status": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[nextToken](#API_ListRecipes_ResponseSyntax "#API_ListRecipes_ResponseSyntax")**

A token for getting the next set of recipes.

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

**[recipes](#API_ListRecipes_ResponseSyntax "#API_ListRecipes_ResponseSyntax")**

The list of available recipes.

Type: Array of [RecipeSummary](API_RecipeSummary.md "API_RecipeSummary.md") objects

Array Members: Maximum number of 100 items.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListRecipes.md "../../../goto/cli2/personalize-2018-05-22/ListRecipes.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListRecipes.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListRecipes.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListRecipes.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListRecipes.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListRecipes.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListRecipes.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListRecipes.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListRecipes.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListRecipes.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListRecipes.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListRecipes.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListRecipes.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListRecipes.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListRecipes.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListRecipes.md "../../../goto/boto3/personalize-2018-05-22/ListRecipes.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListRecipes.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListRecipes.md")
