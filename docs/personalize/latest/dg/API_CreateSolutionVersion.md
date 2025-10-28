# CreateSolutionVersion

Trains or retrains an active solution in a Custom dataset group. A solution is created using the [CreateSolution](API_CreateSolution.md "API_CreateSolution.md")
operation and must be in the ACTIVE state before calling
`CreateSolutionVersion`. A new version of the solution is created every time you
call this operation.

**Status**

A solution version can be in one of the following states:

- CREATE PENDING
- CREATE IN_PROGRESS
- ACTIVE
- CREATE FAILED
- CREATE STOPPING
- CREATE STOPPED
  To get the status of the version, call [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md"). Wait
  until the status shows as ACTIVE before calling `CreateCampaign`.

If the status shows as CREATE FAILED, the response includes a `failureReason`
key, which describes why the job failed.

###### Related APIs

- [ListSolutionVersions](API_ListSolutionVersions.md "API_ListSolutionVersions.md")
- [DescribeSolutionVersion](API_DescribeSolutionVersion.md "API_DescribeSolutionVersion.md")
- [ListSolutions](API_ListSolutions.md "API_ListSolutions.md")
- [CreateSolution](API_CreateSolution.md "API_CreateSolution.md")
- [DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md")
- [DeleteSolution](API_DeleteSolution.md "API_DeleteSolution.md")

## Request Syntax

```
{
   "name": "`string`",
   "solutionArn": "`string`",
   "tags": [
      {
         "tagKey": "`string`",
         "tagValue": "`string`"
      }
   ],
   "trainingMode": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[name](#API_CreateSolutionVersion_RequestSyntax "#API_CreateSolutionVersion_RequestSyntax")**

The name of the solution version.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**[solutionArn](#API_CreateSolutionVersion_RequestSyntax "#API_CreateSolutionVersion_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution containing the training configuration
information.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[tags](#API_CreateSolutionVersion_RequestSyntax "#API_CreateSolutionVersion_RequestSyntax")**

A list of [tags](tagging-resources.md "tagging-resources.md") to apply to the solution version.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

**[trainingMode](#API_CreateSolutionVersion_RequestSyntax "#API_CreateSolutionVersion_RequestSyntax")**

The scope of training to be performed when creating the solution version.
The default is `FULL`. This creates a completely new model based on the entirety
of the training data from the datasets in your dataset group.

If you use
[User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md"),
you can specify a training mode of `UPDATE`. This updates the model to consider new items for recommendations. It is not a full
retraining. You should still complete a full retraining weekly.
If you specify `UPDATE`, Amazon Personalize will stop automatic updates for the solution version. To resume updates, create a new solution with training mode set to `FULL`
and deploy it in a campaign.
For more information about automatic updates, see
[Automatic updates](use-case-recipe-features.md#maintaining-with-automatic-updates "use-case-recipe-features.md#maintaining-with-automatic-updates").

The `UPDATE` option can only be used when you already have an active solution
version created from the input solution using the `FULL` option and the input
solution was trained with the
[User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
recipe or the legacy
[HRNN-Coldstart](native-recipe-hrnn-coldstart.md "native-recipe-hrnn-coldstart.md") recipe.

Type: String

Valid Values: `FULL | UPDATE | AUTOTRAIN`

Required: No

## Response Syntax

```
{
   "solutionVersionArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[solutionVersionArn](#API_CreateSolutionVersion_ResponseSyntax "#API_CreateSolutionVersion_ResponseSyntax")**

The ARN of the new solution version.

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

**ResourceAlreadyExistsException**

The specified resource already exists.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 400

**TooManyTagsException**

You have exceeded the maximum number of tags you can apply to this resource.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/cli2/personalize-2018-05-22/CreateSolutionVersion.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/CreateSolutionVersion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/SdkForCpp/personalize-2018-05-22/CreateSolutionVersion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/SdkForGoV2/personalize-2018-05-22/CreateSolutionVersion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/CreateSolutionVersion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateSolutionVersion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/SdkForKotlin/personalize-2018-05-22/CreateSolutionVersion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/CreateSolutionVersion.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/boto3/personalize-2018-05-22/CreateSolutionVersion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateSolutionVersion.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/CreateSolutionVersion.md")
