# DescribeAlgorithm

Describes the given algorithm.

## Request Syntax

```
{
   "algorithmArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[algorithmArn](#API_DescribeAlgorithm_RequestSyntax "#API_DescribeAlgorithm_RequestSyntax")**

The Amazon Resource Name (ARN) of the algorithm to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "algorithm": {
      "algorithmArn": "***string***",
      "algorithmImage": {
         "dockerURI": "***string***",
         "name": "***string***"
      },
      "creationDateTime": ***number***,
      "defaultHyperParameterRanges": {
         "categoricalHyperParameterRanges": [
            {
               "isTunable": ***boolean***,
               "name": "***string***",
               "values": [ "***string***" ]
            }
         ],
         "continuousHyperParameterRanges": [
            {
               "isTunable": ***boolean***,
               "maxValue": ***number***,
               "minValue": ***number***,
               "name": "***string***"
            }
         ],
         "integerHyperParameterRanges": [
            {
               "isTunable": ***boolean***,
               "maxValue": ***number***,
               "minValue": ***number***,
               "name": "***string***"
            }
         ]
      },
      "defaultHyperParameters": {
         "***string***" : "***string***"
      },
      "defaultResourceConfig": {
         "***string***" : "***string***"
      },
      "lastUpdatedDateTime": ***number***,
      "name": "***string***",
      "roleArn": "***string***",
      "trainingInputMode": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[algorithm](#API_DescribeAlgorithm_ResponseSyntax "#API_DescribeAlgorithm_ResponseSyntax")**

A listing of the properties of the algorithm.

Type: [Algorithm](API_Algorithm.md "API_Algorithm.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/cli2/personalize-2018-05-22/DescribeAlgorithm.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeAlgorithm.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeAlgorithm.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeAlgorithm.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeAlgorithm.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeAlgorithm.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeAlgorithm.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeAlgorithm.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/boto3/personalize-2018-05-22/DescribeAlgorithm.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeAlgorithm.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeAlgorithm.md")
