# DescribeSolutionVersion

Describes a specific version of a solution. For more information on solutions, see [CreateSolution](API_CreateSolution.md "API_CreateSolution.md")

## Request Syntax

```
{
   "solutionVersionArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[solutionVersionArn](#API_DescribeSolutionVersion_RequestSyntax "#API_DescribeSolutionVersion_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution version.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "solutionVersion": {
      "creationDateTime": ***number***,
      "datasetGroupArn": "***string***",
      "eventType": "***string***",
      "failureReason": "***string***",
      "lastUpdatedDateTime": ***number***,
      "name": "***string***",
      "performAutoML": ***boolean***,
      "performHPO": ***boolean***,
      "performIncrementalUpdate": ***boolean***,
      "recipeArn": "***string***",
      "solutionArn": "***string***",
      "solutionConfig": {
         "algorithmHyperParameters": {
            "***string***" : "***string***"
         },
         "autoMLConfig": {
            "metricName": "***string***",
            "recipeList": [ "***string***" ]
         },
         "autoTrainingConfig": {
            "schedulingExpression": "***string***"
         },
         "eventsConfig": {
            "eventParametersList": [
               {
                  "eventType": "***string***",
                  "eventValueThreshold": ***number***,
                  "weight": ***number***
               }
            ]
         },
         "eventValueThreshold": "***string***",
         "featureTransformationParameters": {
            "***string***" : "***string***"
         },
         "hpoConfig": {
            "algorithmHyperParameterRanges": {
               "categoricalHyperParameterRanges": [
                  {
                     "name": "***string***",
                     "values": [ "***string***" ]
                  }
               ],
               "continuousHyperParameterRanges": [
                  {
                     "maxValue": ***number***,
                     "minValue": ***number***,
                     "name": "***string***"
                  }
               ],
               "integerHyperParameterRanges": [
                  {
                     "maxValue": ***number***,
                     "minValue": ***number***,
                     "name": "***string***"
                  }
               ]
            },
            "hpoObjective": {
               "metricName": "***string***",
               "metricRegex": "***string***",
               "type": "***string***"
            },
            "hpoResourceConfig": {
               "maxNumberOfTrainingJobs": "***string***",
               "maxParallelTrainingJobs": "***string***"
            }
         },
         "optimizationObjective": {
            "itemAttribute": "***string***",
            "objectiveSensitivity": "***string***"
         },
         "trainingDataConfig": {
            "excludedDatasetColumns": {
               "***string***" : [ "***string***" ]
            },
            "includedDatasetColumns": {
               "***string***" : [ "***string***" ]
            }
         }
      },
      "solutionVersionArn": "***string***",
      "status": "***string***",
      "trainingHours": ***number***,
      "trainingMode": "***string***",
      "trainingType": "***string***",
      "tunedHPOParams": {
         "algorithmHyperParameters": {
            "***string***" : "***string***"
         }
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[solutionVersion](#API_DescribeSolutionVersion_ResponseSyntax "#API_DescribeSolutionVersion_ResponseSyntax")**

The solution version.

Type: [SolutionVersion](API_SolutionVersion.md "API_SolutionVersion.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/cli2/personalize-2018-05-22/DescribeSolutionVersion.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/DescribeSolutionVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeSolutionVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeSolutionVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeSolutionVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeSolutionVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeSolutionVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeSolutionVersion.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/boto3/personalize-2018-05-22/DescribeSolutionVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeSolutionVersion.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeSolutionVersion.md")
