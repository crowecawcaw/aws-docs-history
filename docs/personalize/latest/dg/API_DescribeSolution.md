# DescribeSolution

Describes a solution.
For more information on solutions, see [CreateSolution](API_CreateSolution.md "API_CreateSolution.md").

## Request Syntax

```
{
   "solutionArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[solutionArn](#API_DescribeSolution_RequestSyntax "#API_DescribeSolution_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution to describe.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "solution": {
      "autoMLResult": {
         "bestRecipeArn": "***string***"
      },
      "creationDateTime": ***number***,
      "datasetGroupArn": "***string***",
      "eventType": "***string***",
      "lastUpdatedDateTime": ***number***,
      "latestSolutionUpdate": {
         "creationDateTime": ***number***,
         "failureReason": "***string***",
         "lastUpdatedDateTime": ***number***,
         "performAutoTraining": ***boolean***,
         "solutionUpdateConfig": {
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
            }
         },
         "status": "***string***"
      },
      "latestSolutionVersion": {
         "creationDateTime": ***number***,
         "failureReason": "***string***",
         "lastUpdatedDateTime": ***number***,
         "solutionVersionArn": "***string***",
         "status": "***string***",
         "trainingMode": "***string***",
         "trainingType": "***string***"
      },
      "name": "***string***",
      "performAutoML": ***boolean***,
      "performAutoTraining": ***boolean***,
      "performHPO": ***boolean***,
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
            }
         }
      },
      "status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[solution](#API_DescribeSolution_ResponseSyntax "#API_DescribeSolution_ResponseSyntax")**

An object that describes the solution.

Type: [Solution](API_Solution.md "API_Solution.md") object

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/DescribeSolution.md "../../../goto/cli2/personalize-2018-05-22/DescribeSolution.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeSolution.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/DescribeSolution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DescribeSolution.md "../../../goto/SdkForCpp/personalize-2018-05-22/DescribeSolution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeSolution.md "../../../goto/SdkForGoV2/personalize-2018-05-22/DescribeSolution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeSolution.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DescribeSolution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeSolution.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/DescribeSolution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeSolution.md "../../../goto/SdkForKotlin/personalize-2018-05-22/DescribeSolution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeSolution.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/DescribeSolution.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/DescribeSolution.md "../../../goto/boto3/personalize-2018-05-22/DescribeSolution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeSolution.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DescribeSolution.md")
