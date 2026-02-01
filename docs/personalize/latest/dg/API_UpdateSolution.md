# UpdateSolution

Updates an Amazon Personalize solution to use a different automatic training configuration. When you update a solution,
you can change whether the solution uses
automatic training, and you can change the training frequency. For more information about updating a solution, see
[Updating a solution](updating-solution.md "updating-solution.md").

A solution update can be in one of the
following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

To get the status of a solution update, call the
[DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md") API operation and find the status
in the `latestSolutionUpdate`.

## Request Syntax

```
{
   "performAutoTraining": `boolean`,
   "performIncrementalUpdate": `boolean`,
   "solutionArn": "`string`",
   "solutionUpdateConfig": {
      "autoTrainingConfig": {
         "schedulingExpression": "`string`"
      },
      "eventsConfig": {
         "eventParametersList": [
            {
               "eventType": "`string`",
               "eventValueThreshold": `number`,
               "weight": `number`
            }
         ]
      }
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[performAutoTraining](#API_UpdateSolution_RequestSyntax "#API_UpdateSolution_RequestSyntax")**

Whether the solution uses automatic training to create new solution versions (trained models). You can change the training
frequency by specifying a `schedulingExpression` in the `AutoTrainingConfig` as part of solution
configuration.

If you turn on automatic training, the first automatic training starts within one hour after the solution update
completes. If you manually create a solution version within the hour, the solution skips the first automatic training.
For more information about automatic training,
see [Configuring automatic training](solution-config-auto-training.md "solution-config-auto-training.md").

After training starts, you can
get the solution version's Amazon Resource Name (ARN) with the [ListSolutionVersions](API_ListSolutionVersions.md "API_ListSolutionVersions.md") API operation.
To get its status, use the [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md").

Type: Boolean

Required: No

**[performIncrementalUpdate](#API_UpdateSolution_RequestSyntax "#API_UpdateSolution_RequestSyntax")**

Whether to perform incremental training updates on your model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe.

Type: Boolean

Required: No

**[solutionArn](#API_UpdateSolution_RequestSyntax "#API_UpdateSolution_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution to update.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[solutionUpdateConfig](#API_UpdateSolution_RequestSyntax "#API_UpdateSolution_RequestSyntax")**

The new configuration details of the solution.

Type: [SolutionUpdateConfig](API_SolutionUpdateConfig.md "API_SolutionUpdateConfig.md") object

Required: No

## Response Syntax

```
{
   "solutionArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[solutionArn](#API_UpdateSolution_ResponseSyntax "#API_UpdateSolution_ResponseSyntax")**

The same solution Amazon Resource Name (ARN) as given in the request.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of requests per second has been exceeded.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/UpdateSolution.md "../../../goto/cli2/personalize-2018-05-22/UpdateSolution.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/UpdateSolution.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/UpdateSolution.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/UpdateSolution.md "../../../goto/SdkForCpp/personalize-2018-05-22/UpdateSolution.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateSolution.md "../../../goto/SdkForGoV2/personalize-2018-05-22/UpdateSolution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateSolution.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/UpdateSolution.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateSolution.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/UpdateSolution.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateSolution.md "../../../goto/SdkForKotlin/personalize-2018-05-22/UpdateSolution.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateSolution.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/UpdateSolution.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/UpdateSolution.md "../../../goto/boto3/personalize-2018-05-22/UpdateSolution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateSolution.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/UpdateSolution.md")
