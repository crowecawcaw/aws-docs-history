# DescribeFeatureTransformation

Describes the given feature transformation.

## Request Syntax

```
{
   "featureTransformationArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[featureTransformationArn](#API_DescribeFeatureTransformation_RequestSyntax "#API_DescribeFeatureTransformation_RequestSyntax")**

The Amazon Resource Name (ARN) of the feature transformation to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "featureTransformation": {
      "creationDateTime": ***number***,
      "defaultParameters": {
         "***string***" : "***string***"
      },
      "featureTransformationArn": "***string***",
      "lastUpdatedDateTime": ***number***,
      "name": "***string***",
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[featureTransformation](#API_DescribeFeatureTransformation_ResponseSyntax "#API_DescribeFeatureTransformation_ResponseSyntax")**

A listing of the FeatureTransformation properties.

Type: [FeatureTransformation](API_FeatureTransformation.md "API_FeatureTransformation.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/cli2/personalize-2018-05-22/DescribeFeatureTransformation.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeFeatureTransformation.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeFeatureTransformation.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeFeatureTransformation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeFeatureTransformation.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeFeatureTransformation.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeFeatureTransformation.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeFeatureTransformation.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/boto3/personalize-2018-05-22/DescribeFeatureTransformation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeFeatureTransformation.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeFeatureTransformation.md")
