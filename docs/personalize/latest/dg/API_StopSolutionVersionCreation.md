# StopSolutionVersionCreation

Stops creating a solution version that is in a state of CREATE_PENDING or CREATE IN_PROGRESS.

Depending on the current state of the solution version, the solution version state changes as follows:

- CREATE_PENDING > CREATE_STOPPED

or

- CREATE_IN_PROGRESS > CREATE_STOPPING > CREATE_STOPPED
  You are billed for all of the training completed up
  until you stop the solution version creation. You cannot resume creating a solution version once it has been stopped.

## Request Syntax

```
{
   "solutionVersionArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[solutionVersionArn](#API_StopSolutionVersionCreation_RequestSyntax "#API_StopSolutionVersionCreation_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution version you want to stop creating.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/cli2/personalize-2018-05-22/StopSolutionVersionCreation.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/StopSolutionVersionCreation.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/SdkForCpp/personalize-2018-05-22/StopSolutionVersionCreation.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/SdkForGoV2/personalize-2018-05-22/StopSolutionVersionCreation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/StopSolutionVersionCreation.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/StopSolutionVersionCreation.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/SdkForKotlin/personalize-2018-05-22/StopSolutionVersionCreation.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/StopSolutionVersionCreation.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/boto3/personalize-2018-05-22/StopSolutionVersionCreation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/StopSolutionVersionCreation.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/StopSolutionVersionCreation.md")
