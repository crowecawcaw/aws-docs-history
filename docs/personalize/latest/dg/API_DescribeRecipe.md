# DescribeRecipe

Describes a recipe.

A recipe contains three items:

- An algorithm that trains a model.
- Hyperparameters that govern the training.
- Feature transformation information for modifying the input data before training.
  Amazon Personalize provides a set of predefined recipes. You specify a recipe when you create a
  solution with the [CreateSolution](API_CreateSolution.md "API_CreateSolution.md") API.
  `CreateSolution` trains a model by using the algorithm
  in the specified recipe and a training dataset. The solution, when deployed as a campaign,
  can provide recommendations using the
  [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") API.

## Request Syntax

```
{
   "recipeArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[recipeArn](#API_DescribeRecipe_RequestSyntax "#API_DescribeRecipe_RequestSyntax")**

The Amazon Resource Name (ARN) of the recipe to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "recipe": {
      "algorithmArn": "***string***",
      "creationDateTime": ***number***,
      "description": "***string***",
      "featureTransformationArn": "***string***",
      "lastUpdatedDateTime": ***number***,
      "name": "***string***",
      "recipeArn": "***string***",
      "recipeType": "***string***",
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[recipe](#API_DescribeRecipe_ResponseSyntax "#API_DescribeRecipe_ResponseSyntax")**

An object that describes the recipe.

Type: [Recipe](API_Recipe.md "API_Recipe.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeRecipe.md "../../../goto/cli2/personalize-2018-05-22/DescribeRecipe.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeRecipe.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeRecipe.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeRecipe.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeRecipe.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeRecipe.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeRecipe.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeRecipe.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeRecipe.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeRecipe.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeRecipe.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeRecipe.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeRecipe.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeRecipe.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeRecipe.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeRecipe.md "../../../goto/boto3/personalize-2018-05-22/DescribeRecipe.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeRecipe.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeRecipe.md")
